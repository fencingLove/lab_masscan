# lab_masscan
1.准备环境：
a)Nmap、Python2.7（安装就不说了）
b)注意，这里需要python-nmap库
  pip install nmap
c)Masscan
到 https://github.com/robertdavidgraham/masscan下载masscan
    $sudo apt-get install git gcc make libpcap-dev
    $git clone https://github.com/robertdavidgraham/masscan
    $cd masscan
    $make
2.配置文件修改
a)根据config.txt中的注释，修改所在行的内容
  rate = 100.00                               #控制masscan的速率
  randomize-hosts = true
  seed = 9009803620231071538
  shard = 1/1
  # ADAPTER SETTINGS
  adapter =
  adapter-ip = 0.0.0.0
  adapter-mac = 00:00:00:00:00:00
  router-mac = 00:00:00:00:00:00
  #OUTPUT/REPORTING SETTINGS
  output-format = xml
  show = open,,
  output-filename = /home/xxxxxxxxxxxxxx/lab_masscan2/masscan_result.txt   #注意！这里把目录修改成你的个人目录
  rotate = 0
  rotate-dir = .
  rotate-offset = 0
  rotate-filesize = 0
  pcap =
  #TARGET SELECTION (IP, PORTS, EXCLUDES)
  retries = 0
  ports = 6379,11211,27017，16379,26379          #尽量多写一些端口，为了缓解漏掉在非默认端口开服务的情况
  range=192.168.1.1-192.168.1.254                #配置IP范围
  capture = cert
  nocapture = html
  nocapture = heartbleed
  min-packet = 60

b)start.py中修改有关email的信息
 
    sender = 'myemail@163.com'                #发件人邮箱
    receiver = 'myemail@163.com'              #收件人邮箱
    subject = u'每日提醒'
    smtpserver = 'smtp.163.com'
    username =  'myemail'                     #发件人
    password = 'yourpassword'                 #密码


c)start.py中修改nmap命令（根据实际情况修改）
  nmap命令可以根据需要进行修改，也可以使用-sC（--script default）参数使用默认脚本，也可以添加其他脚本
  result = nm.scan(hosts=ip, arguments='-p 11211,27017,6379 --script memcached-info --script mongodb-info --script redis-info')
d)指定masscan的路径
  os.system('/home/xxxxxxxxxxxxxxxxxxxxxx/masscan/bin/masscan -c config.txt')
