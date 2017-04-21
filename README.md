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
  
b)start.py中修改有关email的信息



c)start.py中修改nmap命令（根据实际情况修改）
d)指定masscan的路径
