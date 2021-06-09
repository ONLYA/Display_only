import os
import subprocess


os.chdir('/etc/prosody/conf.avail')
l = os.listdir()
hostname = ''
_file = ''
for _ in l:
    if _[:2] == 'li':
        hostname = _.split('.')[0]
        _file = _


subprocess.call(['cp', _file, 'BAK' + _file + '.bak'])
_file_temp = _file + '.temp'

f = open(_file, 'r')
fw = open(_file_temp, 'w')
f.seek(0)
last_pos = f.tell()
line = f.readline()
first = False
while line != '':
    if not first:
        if line.__contains__('authentication = "anonymous"'):
            fw.write('    authentication = "internal_hashed"\n')
        elif line.__contains__('Component '):
            f.seek(last_pos)
            fw.write('''
VirtualHost "guest.{}.members.linode.com"
    authentication = "anonymous"
    c2s_require_encryption = false\n
'''.format(hostname))
            first = True
        else:
            fw.write(line)
    else:
        fw.write(line)
    last_pos = f.tell()
    line = f.readline()
f.close()
fw.close()
os.remove(_file)
os.rename(_file_temp, _file)


os.chdir('/etc/jitsi/meet')
_file = '{}.members.linode.com-config.js'.format(hostname)
_file_temp = _file + '.temp'
subprocess.call(['cp', _file, 'BAK' + _file + '.bak'])
f = open(_file, 'r')
fw = open(_file_temp, 'w')
f.seek(0)
line = f.readline()
first = False
while line != '':
    if not first:
        if line.__contains__('anonymousdomain'):
            fw.write("        anonymousdomain: 'guest.{}.members.linode.com',\n".format(hostname))
            first = True
        else:
            fw.write(line)
    else:
        fw.write(line)
    line = f.readline()
f.close()
fw.close()
os.remove(_file)
os.rename(_file_temp, _file)

os.chdir('/etc/jitsi/jicofo')
subprocess.call(['cp', 'sip-communicator.properties', 'BAK' + 'sip-communicator.properties' + '.bak'])
f = open('sip-communicator.properties', 'a')
f.write('org.jitsi.jicofo.auth.URL=XMPP:{}.members.linode.com'.format(hostname))
f.close()


user = input("User name: ")
password = input("Password: ")
subprocess.call(['prosodyctl', 'register', user, '{}.members.linode.com'.format(hostname), '"{}"'.format(password)])
subprocess.call(['systemctl', 'restart', 'prosody'])
subprocess.call(['systemctl', 'restart', 'jicofo'])
subprocess.call(['systemctl', 'restart', 'jitsi-videobridge2'])
