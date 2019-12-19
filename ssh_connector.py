#-*- coding: utf-8 -*-
import paramiko
import getpass
import time
#from __future__ import print_function

# 카메라 포트번호
cam_ports = [str(num) for num in range(240, 247)]

# 연결
ssh_clients = ["disconnect" for _ in cam_ports]
for idx, cam_port in enumerate(cam_ports):
    try:
        ssh_clients[idx] = paramiko.SSHClient()
        ssh_clients[idx].set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh_clients[idx].connect("192.168.0."+cam_port, username="test", password="1234")
        print('connection complete')
    except:
        ssh_clients[idx] = 'failed connection'
        print('연결실패')
        
# 새로운 interactive shell session 생성
ssh_channels = ["disconnect" for _ in cam_ports]
for idx, ssh_client in enumerate(ssh_clients):
    if str(type(ssh_client)) == "<class 'paramiko.client.SSHClient'>":
        ssh_channels[idx] = ssh_client.invoke_shell()
        print('세션생성 완료')
    else:
        ssh_channels[idx] = "failed connection"
        print('세션생성 실패')

# 상태확인
for idx, ssh_client in enumerate(ssh_clients):
    print("port no. " + cam_ports[idx] + ": ", end="")
    if str(type(ssh_client)) == "<class 'paramiko.client.SSHClient'>":
        print("connect")
    elif ssh_client == "disconnect":
        print("disconnect")
    else:
        print("failed connection")
'''
# 종료
for idx, ssh_client in enumerate(ssh_clients):
    if str(type(ssh_client)) == "<class 'paramiko.client.SSHClient'>":
        ssh_clients[idx].close()
    ssh_clients[idx] = "disconnect"
'''
