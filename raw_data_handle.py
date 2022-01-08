import json
import re
import threading
import pymysql

json_data = {}
data = json.loads(json.dumps(json_data))
conn = pymysql.connect(
        host = '192.168.1.106',
        port = 3306,
        user = 'root',
        passwd = '02230317liuxin',
        db = 'dns_json',
        charset = 'utf8',
    )

class myThread(threading.Thread):
    def __init__(self, ID, filename, ipv4, ist_4, isr_4, ipv6, ist_6, isr_6):
        threading.Thread.__init__(self)
        self.ID = ID
        self.filename = filename
        self._error = False
        self.ipv4 = ipv4
        self.ist_4 = ist_4
        self.isr_4 = isr_4
        self.ipv6 = ipv6
        self.ist_6 = ist_6
        self.isr_6 = isr_6

    def run(self):
        try:
            basic_handle("./raw_data/"+self.filename, self.ID)
            if self.ipv4:
                ipv4_handle("./raw_data/ipv4/"+self.filename, self.ID, self.ist_4, self.isr_4)
            if self.ipv6:
                ipv6_handle("./raw_data/ipv6/"+self.filename, self.ID, self.ist_6, self.isr_6)
        except:
            print("system error")
            self._error = True


def basic_handle(filename, ID):
    f = open(filename, "r", encoding='utf-8')
    tmp = str(f.readlines()).replace("\\n', '", "").split("******")
    data['TimeStamp'] = tmp[1]
    _root = data[ID]
    _root['Identification'] = tmp[2].split("\"")[1]
    try:
        status = re.search('status: [A-Z]*', tmp[3])
        _root['Status'] = status.group().split(" ")[1]
    except:
        print("status error")
    data[ID] = _root

def ipv4_handle(filename, ID, ist, isr):
    f = open(filename, "r", encoding='utf-8')
    tmp = str(f.readlines()).replace("\\n', '", "\n").split("******")
    point = data[ID]
    pub_ip = re.search('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', tmp[1])

    if pub_ip:
        point['SourceIP_ipv4'] = pub_ip.group()

    query_latency = point['QueryLatency']
    query_ipv4 = re.search('Query time: [0-9]+', tmp[2])
    if query_ipv4:
        query_latency['Ipv4_udp'] = query_ipv4.group().split(" ")[2]
    query_ipv4 = re.search('Query time: [0-9]+', tmp[3])
    if query_ipv4:
        query_latency['Ipv4_tcp'] = query_ipv4.group().split(" ")[2]
    point['QueryLatency'] = query_latency

    if ist:
        trace = tmp[4].split("\n")
        i = 2
        point['Path_count_ipv4'] = len(trace) - 3
        _route = json.loads(json.dumps(json_data))
        while i < len(trace) - 1:
            route = re.search('[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*', trace[i])
            if route:
                _route['Router' + str(i - 2)] = route.group()
            else:
                _route['Router' + str(i - 2)] = "* * *"
            i += 1
        point['Path_ipv4'] = _route

    bias = 0
    if ist:
        bias += 1
    if isr:
        refer_latency = point['ReferLatency_ipv4']
        ref = re.search('Query time: [0-9]+', tmp[4+bias])
        if ref:
            refer_latency['AliDNS'] = ref.group().split(" ")[2]
        ref = re.search('Query time: [0-9]+', tmp[5 + bias])
        if ref:
            refer_latency['114DNS'] = ref.group().split(" ")[2]
        ref = re.search('Query time: [0-9]+', tmp[6 + bias])
        if ref:
            refer_latency['DNSPod'] = ref.group().split(" ")[2]
    point['ReferLatency_ipv4'] = refer_latency

    data[ID] = point


def ipv6_handle(filename, ID, ist, isr):
    print("ipv6暂未开发")


def save():
    conn.ping(reconnect=True)
    cur = conn.cursor()
    sql = "INSERT INTO `log` VALUES ('"+str(data['TimeStamp'])+"','"+json.dumps(data['A'])+"','"+json.dumps(data['B'])+"','"+json.dumps(data['C'])\
          +"','"+json.dumps(data['D'])+"','"+json.dumps(data['E'])+"','"+json.dumps(data['F'])+"','"+json.dumps(data['G'])+"','"+json.dumps(data['H'])\
          +"','"+json.dumps(data['I'])+"','"+json.dumps(data['J'])+"','"+json.dumps(data['K'])+"','"+json.dumps(data['L'])+"','"+json.dumps(data['M'])+"')"
    #print(sql)
    cur.execute(sql)
    conn.commit()
    conn.close()

def error_record(ID):
    file1 = open('./raw_data/raw_data_'+ID.lower()+'.txt', "r", encoding='utf-8')
    file2 = open("./error_log/"+str(data['TimeStamp']).replace(":","-")+"_"+ID+".txt", "w", encoding='utf-8')
    s = file1.read()
    file2.write(s)

def data_init():
    for c in 'ABCDEFGHIJKLM':
        point = json.loads(json.dumps(json_data))
        point['Identification'] = ""
        query_lantancy = json.loads(json.dumps(json_data))
        query_lantancy['Ipv4_udp'] = -1
        query_lantancy['Ipv4_tcp'] = -1
        query_lantancy['Ipv6_udp'] = -1
        query_lantancy['Ipv6_tcp'] = -1
        point['QueryLatency'] = query_lantancy
        point['Path_count_ipv4'] = -1
        point['Path_ipv4'] = ""
        point['Path_count_ipv6'] = -1
        point['Path_ipv6'] = ""
        ReferLatency_ipv4 = json.loads(json.dumps(json_data))
        ReferLatency_ipv4['AliDNS'] = -1
        ReferLatency_ipv4['114DNS'] = -1
        ReferLatency_ipv4['DNSPod'] = -1
        point['ReferLatency_ipv4'] = ReferLatency_ipv4
        ReferLatency_ipv6 = json.loads(json.dumps(json_data))
        ReferLatency_ipv6['AliDNS'] = -1
        ReferLatency_ipv6['114DNS'] = -1
        ReferLatency_ipv6['DNSPod'] = -1
        point['ReferLatency_ipv6'] = ReferLatency_ipv6
        point['Status'] = ""
        point['SourceIP_ipv4'] = ""
        point['SourceIP_ipv6'] = ""
        data[c] = point



