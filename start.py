#encoding=utf-8
#useage:sudo python start.py(挂载可以使用sudo nohup python start.py&)
import nmap
import os
import time
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from os.path import join,getsize
from xml.etree import ElementTree as ET

def generate_email(scanresult):
        file_template = open('template.html','r')
        content = file_template.read()
	result_str = ''
	for line in scanresult:
		result_str = result_str+line.strip()+'\r\n'+'<br></br>'
	ISOTIMEFORMAT='%Y-%m-%d'
	today = time.strftime(ISOTIMEFORMAT,time.localtime())
        result = content.replace('{{{content}}}',result_str).replace('{{{time}}}',today)
        file_template.close()
        file_output = open('result.html','w')
        file_output.write(result)
        file_output.close()
        return result
def sendTO_email(scanresult):
        sender = 'myemail@163.com'
        receiver = 'myemail@163.com'
        subject = u'每日提醒'
        smtpserver = 'smtp.163.com'
        username =  'myemail'
        password = 'yourpassword'
        msg = MIMEText(generate_email(scanresult),'html','utf-8')

        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver

        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()

def scanstart():
	scanresult = list()
	scanlist = list()
	content=ET.parse('masscan_result.txt')
	p=content.findall('host')
	for oneper in p:
		array = oneper.getchildren()
		address = array[0].attrib['addr']
		scanlist.append(str(address).strip())
	print scanlist
	nm = nmap.PortScanner()
	for ip in scanlist:
		result = nmap_scanner(ip)
		for line in result:
			scanresult.append(line)
	return scanresult
def nmap_scanner(ip):
	nmap_result = list()
	portlist=[27017,6379,11211]
	nm = nmap.PortScanner()
	result = nm.scan(hosts=ip, arguments='-p 11211,27017,6379 --script memcached-info --script mongodb-info --script redis-info')
	if(len(result['scan'].keys()) is not 0):
		ip = result['scan'].keys()[0]
	else:
		ip='127.0.0.1'
	for port in portlist:
        	try:
                	state = result['scan'][ip]['tcp'][port]['state']
                	script_info = result['scan'][ip]['tcp'][port]['script']
                	if port != 27017:											#27017格式输出不一样
                        	print ip+':'+str(port)
				nmap_result.append(ip+':'+str(port))
                	else:
                        	if 'ERROR' not in result['scan'][ip]['tcp'][port]['script']['mongodb-info']:
                                	print ip+':'+str(port)
					nmap_result.append(ip+':'+str(port))
        	except Exception, e:
                	pass
	return nmap_result
os.system('/home/xxxxxxxxxxxxxxxxxxxxxx/masscan/bin/masscan -c config.txt')#这里写masscan的安装目录
while True:
	filesize = os.path.getsize(r'masscan_result.txt')
	if filesize!=0:
		scanresult = scanstart()
		if scanresult is not None:
			sendTO_email(scanresult)
		break
