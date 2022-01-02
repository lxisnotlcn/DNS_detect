import json
import re

json_data = {}

data = json.loads(json.dumps(json_data))
f = open('raw_data.txt',"r",encoding='utf-8')
tmp = f.readlines()
i = 0
length = len(tmp)
# 时间戳
data['TimeStamp'] = tmp[i].replace("\n","")
for root in 'ABCDEFGHIJKLM':
    _root = json.loads(json.dumps(json_data))
    while tmp[i][0]!="\"":
        i+=1
    # 节点标识
    _root['Identification'] = tmp[i].split("\"")[1]
    # 访问时延
    query_latency = json.loads(json.dumps(json_data))
    while i < length :
        if 'Query time:' in tmp[i]:
            query = re.search('[1-9][0-9]*' , tmp[i])
            query_latency['Ipv4_udp'] = query.group()
            break
        i+=1
    i+=1
    while i < length:
        if 'Query time:' in tmp[i]:
            query = re.search('[1-9][0-9]*', tmp[i])
            query_latency['Ipv4_tcp'] = query.group()
            break
        i+=1
    i+=1
    query_latency['Ipv6_udp'] = ""
    query_latency['Ipv6_tcp'] = ""
    _root['QueryLatency'] = query_latency
    #路由路径
    while tmp[i] != "\n":
        i+=1
    i+=1
    start = i
    _route = json.loads(json.dumps(json_data))
    while tmp[i] != "\n":
        route = re.search('[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*',tmp[i])
        if route :
            _route['Router'+str(i-start)] = route.group()
        else:
            _route['Router' + str(i - start)] = "* * *"
        i+=1
    _root['Path_ipv4'] = _route
    _root['Path_count_ipv4'] = i-start
    _root['Path_ipv6'] = ""
    _root['Path_count_ipv6'] = 0
    #参考时延
    refer_latency = json.loads(json.dumps(json_data))
    while i < length :
        if 'Query time:' in tmp[i]:
            query = re.search('[1-9][0-9]*' , tmp[i])
            refer_latency['AliDNS'] = query.group()
            break
        i+=1
    i+=1
    while i < length :
        if 'Query time:' in tmp[i]:
            query = re.search('[1-9][0-9]*' , tmp[i])
            refer_latency['114DNS'] = query.group()
            break
        i+=1
    i+=1
    while i < length :
        if 'Query time:' in tmp[i]:
            query = re.search('[1-9][0-9]*' , tmp[i])
            refer_latency['DNSPod'] = query.group()
            break
        i+=1
    i+=1
    _root['ReferLatency_ipv4'] = refer_latency
    _root['ReferLatency_ipv6'] = ""
    #根服务状态
    while i < length :
        if 'status:' in tmp[i]:
            status = re.search('status: [A-Z]*' , tmp[i])
            _root['Status'] = status.group().split(" ")[1]
            break
        i+=1
    i+=1
    #公网ip
    while tmp[i][0] < '0' or tmp[i][0] > "9":
        i+=1
    _root['SourceIP_ipv4'] = tmp[i].replace("\n","")
    _root['SourceIP_ipv6'] = ""
    data[root] = _root

with open("log.json", "w") as write_f:
    write_f.write(json.dumps(data, ensure_ascii=False))

