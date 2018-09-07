#encoding:utf-8
import paramiko
ssh = paramiko.SSHClient()
key = paramiko.AutoAddPolicy()
ssh.set_missing_host_key_policy(key)
# pkey=b'C:\Users\jiangshaojie\Desktop\jiangshaojie.pem'
pkey = paramiko.RSAKey.from_private_key_file(b'C:\Users\jiangshaojie\Desktop\jiangshaojie.pem',password='tYvkhIcWnRjQxsAJ')

ssh.connect(hostname='10.30.54.228', port=22, username='jiangshaojie',password='tYvkhIcWnRjQxsAJ', pkey=pkey ,timeout=5)
stdin, stdout, stderr = ssh.exec_command('97')
print (stdout.read())
# print(stdout.read().decode())
print(stderr.read())
# 关闭连接
ssh.close()