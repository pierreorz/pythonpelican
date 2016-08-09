Title: weblogic配置jython
Date: 2016-05-17 22:20
Category: weblogic
Tags: weblogic, jython
Slug: weblogic-jython
----------

### 在服务器端使用jython ###

以下以139服务器为例：


- 在当前shell环境中设置`setWLSEnv.sh`    
进入`/oracle/Oracle/Middleware/wlserver_10.3/server/bin`目录下  
- 执行命令 `. ./setWLSEnv.sh` ****注意两个点号中间有空格**** 
- 进入WLST：`java weblogic.WLST`
- 进入jython： `java org.python.util.jython` 可以查看weblogic内置jython版本为jython2.2.1


### 在jython中加载标准模块 ###

- 由于jython的标准模块在`$WL_HOME/common/wlst/modules/jython-modules.jar`中，因此需要在启动jython的时候将该路径加载到系统路径中才行
- 进入jython命令行 加载sys模块`import sys`
- 在系统路径中加入jython-modules.jar, `sys.path.append('$WL_HOME/common/wlst/modules/jython-modules.jar/Lib')`
- 然后`import time`之后便可以import其它标准模块 
 
 
### 在java中调用jython ###

- 由于weblogic自带jython2.2.1，所以不需要引用额外的jython包。(`目前测试发现引用最新包时出导致发包失败`)
- 因要发包在487服务器来测试，以下以487为例，在服务器创建目录/data01/oracle/scripts
- 将上文提到的jython-modules.jar复制到scripts目录，或者扩展自己的python脚本
- 加载方式：先加载sys模块，`import sys`
- 将刚刚的路径添加到sys.path中以便jython能够使用模块`sys.path.append('/data01/oracle/scripts/jython-modules.jar/Lib;/data01/oracle/scripts')`
- 现在便可自由加载/data01/oracle/scripts目录下的模块了`import time`


### 在weblogic容器环境使用高版本的jython ###

- 为何要使用高版本？jython2.2.1版本太过简陋自带只有sys/io模块，所以才会有以上加载标准模块的问题。如果升级高版本之后，自带便有大部分python的标准模块，扩展纯python模块也很方便只需要在路径中加载模块地址即可

- 目前最新版本的jython是jython2.7.0 基于JDK1.8的，而weblogic基于的JDK是1.6，升级起来太麻烦，只能将就weblogic，使用基于JDK1.6的版本jython2.5.4
- 有两种方法：    

	###### 方法一： ######
	在项目中配置weblogic.xml优先加载Web-inf下的jython2.5.4包
	不过在测试中发现应用第一次访问时会报错，之后便正常。推测原因可能是weblogic自带的jython2.2.1版本在服务器启动时便加载，后面weblogic.xml的配置是应用级别的，所以替换就慢了一步，第二次访问应用时才会加载到jython2.5.4的包，于是便报错了。

	###### 方法二： ######
	在修改服务器的weblogic的启动脚本setWeblogic.sh中的CLASSPATH，提前将jython2.5.4的jar包路径放在classpath之前优先加载，重启服务器之后版本便升级为2.5.4(如果要在服务器直接运行jython，由于jrockit的一个BUG导致出错，需要补丁：Patch 16569812）
	
	修改setDomainEnv.sh中的BEA_JAVA_HOME以及JAVA_HOME，将jrockit补丁路径替换进去，然后执行命令`. ./setDomainEnv.sh` 再重启相关节点服务器即可完成升级。    
   

### jython通过zxJDBC操作数据库 ###

- jython通过zxJDBC操作数据库
- 加载zxJDBC    
`from com.ziclix.python.sql import zxJDBC`        
- 查找JNDI得到数据库连接     
`conn=zxJDBC.lookup('jdbc/HR_HWLCM')`    
- 根据conn得到cursor进行查询       
`cursor=conn.cursor()`    
`cursor.execute("select * from testd")`
 
### jython调用rest服务 ###
- 调用**GET**服务 使用urllib2以及json模块即可调用rest服务。其中json在jython2.5中非标准模块，需要下载安装，将json.py移到Lib目录即可加载。详细参照以下代码：    
`import urllib2`    
`import json`    
`url='http://szxtsp140-or:8001/testrest/jersey/rest/getresult'`    
`resp=urllib2.urlopen(url+'/222')`    
`result=resp.read()`        

- 如果输入是json，在pathParam中需要转义,可以使用urllib.quote(jsonstring)对jsonstring进行转义之后，再拼接到url中即可。
- 调用**POST**服务 参照以下代码    将字典类型的参数先通过json模块的json.write转成json串，再通过urllib模块的quote将json串转义，最终拼成URL，构建Request对象，设置访问方式为**POST** 其它类型的访问方式如**PUT**,**DELETE**均如此设置即可    
`import urllib2`    
`import urllib`    
`import json`    
`url='http://szxtsp140-or:8001/testrest/jersey/rest/putparamters/'`        
`param={"test1":1,"test2":2}`    
`jsonparam=json.write(param)`    
`encodeparam=urllib.quote(jsonparam)`    
`url=url+encodeparam`
`req=urllib2.Request(url)`    
`req.get_method=lambda:'POST'`    
`result=urllib2.urlopen(req)`    
`result=result.read()`    

