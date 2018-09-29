import paramiko

pkey = 'C:/Users/jiangshaojie/Desktop/jiangshaojie.pem'  # 本地密钥文件路径[此文件服务器上~/.ssh/id_rsa可下载到本地]
key = paramiko.RSAKey.from_private_key_file(pkey, password='tYvkhIcWnRjQxsAJ')  # 有解密密码时,
paramiko.util.log_to_file('paramiko.log')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 通过公共方式进行认证 (不需要在known_hosts 文件中存在)
# ssh.load_system_host_keys() #如通过known_hosts 方式进行认证可以用这个,如果known_hosts 文件未定义还需要定义 known_hosts
ssh.connect('10.30.54.228', username='jiangshaojie', password='tYvkhIcWnRjQxsAJ', pkey=key)  # 这里要 pkey passwordkey 密钥文件
stdin, stdout, stderr = ssh.exec_command('p')
print(stderr.read())
print (stdout.read())
# print()
# stdin, stdout, stderr = ssh.exec_command('p')
# print (stdout.read())