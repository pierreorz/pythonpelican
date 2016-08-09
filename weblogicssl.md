Title: weblogic配置SSL
Date: 2016-06-29 22:20
Category: weblogic
Tags: weblogic, SSL
Slug: weblogic-ssl
Author: pierreorz
----------

### 申请www.dengdezhao.cn的服务器证书 ###
- 提交电子流给www.dengdezhao.cn域名申请服务器证书
- 电子流通过后会得到cert.pfx证书文件以及证书安装密码“password"(此处为方便理解以password代替)

### 将得到的pfx证书拆分成crt以及key ### 
- 安装openssl
- 切换到openssl/bin目录，将cert.pfx放置在该目录
- 执行命令:`openssl pkcs12 -in cert.pfx -nodes -out ddz/prod.pem`
- 提示输入密码,输入"password"
- 执行命令：`openssl x509 -in ddz/prod.pem -out ddz/prod.crt`得到crt证书


### 转换crt证书为p7b ###

- 双击prod.crt切到”详细信息"标签,点击按钮"复制到文件"
- 下一步,选P7B证书，并选中"如果可能,则数据包括证书路径中的所有证书"
- 另存为prod.p7b即完成证书转换

### 转换crt证书为p12 ###
- 执行命令：`openssl pkcs12 -export -clcerts -inkey ddz/prod.pem -in ddz/prod.crt -out ddz/ewallet.p12`
- 提示设置密码,设置为oracle1234（安装时要用到)
- 将ewallet.p12以及prod.p7b上传到服务器路径/data01/oracle/req下


### 配置owm 钱包安装证书 ###
- ITOC连接到服务器
- 切换到/data01/oracle/adf/Oracle_WT1/bin目录
- 运行./owm &
- 在弹出的wallet窗口选择打开/data01/oracle/req下的钱包
- 输入密码上一步设置的oracle1234
- 可以看到是个空的钱包，在左侧“Trusted Certificates"上右键导入prod.p7b
- 导入成功即可看到三个证书文件在左侧栏
- 勾选wallet菜单下的Auto login项
- 然后SAVE钱包退出。


### 配置 SSL.conf ###
- 切换到OHS的配置目录/data01/oracle/adf/Oracle_WT1/instances/instance1/config/OHS/ohs1/
- 编辑ssl.conf文件修改Listen Port为443
- 修改VirtualHost *：443
- 修改SSLWallet路径为 "/data01/oracle/req"
- 保存退出

### 重启OHS ###
- 重启OHS之后即可验证HTTPS访问是否可行。
