Title: weblogic集成tibco
Date: 2016-05-14 22:20
Category: weblogic
Tags: weblogic, tibco
Slug: weblogic-tibco
----------

**1. 配置相关依赖包**    
将tibjms.jar放在weblogic的 $Domain_dir/lib目录中


**2. 配置Foreign JNDI Providers**    
- 进入weblogic控制台，进入菜单Services->Foreign JNDI Providers->Create a Foreign JNDI Provider 创建一个Provider，名称随意。
- Targets 选DefaultServer 完成。
- 点击刚创建的Provider    
  配置Initial Context Factory: **com.tibco.tibjms.naming.TibjmsInitialContextFactory**    

- Provider URL:**tcp://nkgtsv027-eip:7222**    
- User: **WCA_EIP_COMMON**
- Password: **WCA_EIP_COMMON**

**3. 配置 Foreign JNDI Links**
- Local JNDI Name: **jms/eip** （本地调用时需要用到）
- Remote JNDI Name: **XAQueueConnectionFactory** （remote端的对外JNDI名）

**4. 在JAVA中调用**
	
	        InitialContext context = new InitialContext();
        com.tibco.tibjms.naming.TibjmsFederatedXAQueueConnectionFactory cf =
            (com.tibco.tibjms.naming.TibjmsFederatedXAQueueConnectionFactory)
			context.lookup("jms/eip");

**5. 在JAVA中获取认证信息**
- 本来以上代码获得ConnectionFactory就可以创建连接了，Connection c = cf.createConnection(); 但是remote服务器的security设置需要再进行一次认证，即通过Connection c = cf.createConnection(name,password);方法创建连接。也就意味着在代码端还需要得到用户密码等信息。
- 当然也可以通过配置的方式实现，不过如果密码定期修改也就比较麻烦。以下通过获取weblogic上配置的用户及密码来进行验证。
- 查询TibjmsFederatedXAQueueConnectionFactory的源码，发现提供一个cf.writeExternal()方法实现environment信息的序列化功能，也就是可以把用户名及密码等信息以流的方式写出来。那么通过反序列化就可以得到用户名及密码。

	    File file = new File("test.out");
            out = new ObjectOutputStream(new FileOutputStream(file));
            cf.writeExternal(out);
            out.flush();
            out.close();
            FileInputStream fis = new FileInputStream(file);
            ObjectInputStream ois = new ObjectInputStream(fis);
            Hashtable env = (Hashtable)ois.readObject();
            name = (String)env.get(Context.SECURITY_PRINCIPAL);
            password = (String)env.get(Context.SECURITY_CREDENTIALS);
            file.delete();

**6. 顺利监听到队列并得到JMS消息之后通过JAXB解析消息体**
- 需要得到消息体XML的XSD定义文件**CIR.xsd**
- 打开CMD，运行`xjc -d . -p com.xxx.jaxbbean CIR.xsd` 便会在com.xxx.jaxbbean包下生成相关的JAVABEAN
- 便可通过JAXBContext对XML消息体进行解析了

            context = JAXBContext.newInstance("com.xxx.jaxbbean");
            unMarshaller = context.createUnmarshaller();
            obj = unMarshaller.unmarshal(xmlfile);

