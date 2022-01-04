import json
import re
import threading
import pymysql

json_data = {}
data = json.loads(json.dumps(json_data))
conn = pymysql.connect(
        host = '192.168.3.17',
        port = 3306,
        user = 'root',
        passwd = '02230317liuxin',
        db = 'dns_json',
        charset = 'utf8',
    )

class myThread(threading.Thread):
    def __init__(self, filename,ID):
        threading.Thread.__init__(self)
        self.filename = filename
        self.ID = ID
        self._error = False

    def run(self):
        try:
            handle(self.filename,self.ID)
        except IndexError:
            print("data error")
            self._error = True
        except:
            print("system error")
            self._error = True

def handle(filename,ID):
    f = open(filename, "r", encoding='utf-8')
    tmp = f.readlines()
    i = 0
    length = len(tmp)
    # 时间戳
    data['TimeStamp'] = tmp[i].replace("\n", "")
    _root = json.loads(json.dumps(json_data))
    while tmp[i][0] != "\"":
        i += 1
    # 节点标识
    _root['Identification'] = tmp[i].split("\"")[1]
    # 访问时延
    query_latency = json.loads(json.dumps(json_data))
    while i < length:
        if 'Query time:' in tmp[i]:
            query = re.search('[1-9][0-9]*', tmp[i])
            query_latency['Ipv4_udp'] = query.group()
            break
        elif 'timed out' in tmp[i]:
            query_latency['Ipv4_udp'] = -1
            break
        i += 1
    i += 1
    while i < length:
        if 'Query time:' in tmp[i]:
            query = re.search('[1-9][0-9]*', tmp[i])
            query_latency['Ipv4_tcp'] = query.group()
            break
        elif 'timed out' in tmp[i]:
            query_latency['Ipv4_tcp'] = -1
            break
        i += 1
    i += 1
    query_latency['Ipv6_udp'] = ""
    query_latency['Ipv6_tcp'] = ""
    _root['QueryLatency'] = query_latency
    # 路由路径
    while tmp[i][0] != "t":
        i += 1
    i += 1
    start = i
    _route = json.loads(json.dumps(json_data))
    while tmp[i] != "\n":
        route = re.search('[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*', tmp[i])
        if route:
            _route['Router' + str(i - start)] = route.group()
        else:
            _route['Router' + str(i - start)] = "* * *"
        i += 1
    _root['Path_ipv4'] = _route
    _root['Path_count_ipv4'] = i - start
    _root['Path_ipv6'] = ""
    _root['Path_count_ipv6'] = 0
    # 参考时延
    refer_latency = json.loads(json.dumps(json_data))
    while i < length:
        if 'Query time:' in tmp[i]:
            query = re.search('[1-9][0-9]*', tmp[i])
            refer_latency['AliDNS'] = query.group()
            break
        i += 1
    i += 1
    while i < length:
        if 'Query time:' in tmp[i]:
            query = re.search('[1-9][0-9]*', tmp[i])
            refer_latency['114DNS'] = query.group()
            break
        i += 1
    i += 1
    while i < length:
        if 'Query time:' in tmp[i]:
            query = re.search('[1-9][0-9]*', tmp[i])
            refer_latency['DNSPod'] = query.group()
            break
        i += 1
    i += 1
    _root['ReferLatency_ipv4'] = refer_latency
    _root['ReferLatency_ipv6'] = ""
    # 根服务状态
    while i < length:
        if 'status:' in tmp[i]:
            status = re.search('status: [A-Z]*', tmp[i])
            _root['Status'] = status.group().split(" ")[1]
            if status.group().split(" ")[1] == "NOERROR":
                file1 = open(filename, "r", encoding='utf-8')
                file2 = open("errorlog.txt", "w", encoding='utf-8')
                s = file1.read()
                file2.write(s)
            break
        i += 1
    i += 1
    # 公网ip
    while tmp[i][0] < '0' or tmp[i][0] > "9":
        i += 1
    _root['SourceIP_ipv4'] = tmp[i].replace("\n", "")
    _root['SourceIP_ipv6'] = ""
    data[ID] = _root

def save():
    cur = conn.cursor()
    sql = "INSERT INTO `log` VALUES ('"+str(data['TimeStamp'])+"','"+json.dumps(data['A'])+"','"+json.dumps(data['B'])+"','"+json.dumps(data['C'])\
          +"','"+json.dumps(data['D'])+"','"+json.dumps(data['E'])+"','"+json.dumps(data['F'])+"','"+json.dumps(data['G'])+"','"+json.dumps(data['H'])\
          +"','"+json.dumps(data['I'])+"','"+json.dumps(data['J'])+"','"+json.dumps(data['K'])+"','"+json.dumps(data['L'])+"','"+json.dumps(data['M'])+"')"
    #print(sql)
    cur.execute(sql)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    _thread = []
    for root in 'abcdefghijklm':
        thread = myThread('./raw_data/raw_data_'+root+'.txt',root.upper())
        _thread.append(thread)
    for t in _thread:
        t.start()
    for t in _thread:
        t.join()
    for t in _thread:
        if t._error:
            exit(0)
    with open("log.json", "w") as write_f:
        write_f.write(json.dumps(data, ensure_ascii=False))
    save()

