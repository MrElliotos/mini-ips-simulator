import random
security_database = []
def analyze_traffic(db_list, ip_address, port):
    packet_info = {
        "ip" : ip_address,
        "port" : port,
        "status" : "UNKNOWN"
    } 
    if port == 22 or port ==  3389:
        packet_info["status"] = "CRITICAL"
    else :    
        packet_info["status"] = "SAFE"
    db_list.append(packet_info)
    return packet_info
kok = 0
while kok < 3:
    x = random.randint(20, 9000)
    x1 = random.randint(20, 100)
    wow = analyze_traffic(security_database, x, x1)
    print(wow)
    kok += 1
print("----BASE REPORT----")
for mem in security_database :
    print(f"IP: {mem['ip']} | Port: {mem['port']} | Status: {mem['status']}")


        