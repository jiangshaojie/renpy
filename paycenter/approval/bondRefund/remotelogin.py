from fabric import Connection
c=Connection('web1')
result=c.run('uname -s')
