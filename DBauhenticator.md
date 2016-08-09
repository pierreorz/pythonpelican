Title: weblogic配置DBAuthenticator 
Date: 2016-06-14 22:20
Category: weblogic 
Tags: weblogic, DBAuthenticator 
Slug: weblogic-dbauthenticator
----------
### 配置数据库表结构 ###

### 创建Providers ###

- 登陆weblogic控制台,Security Realms->myReaml->Providers,创建DBAuthenticator 
- 登陆EM控制台，bpm_domain->security->Security Provider Configuration->Identity Store Provider
	**PROPERTY_ATTRIBUTE_MAPPING GUID=orclguid**
	**OPTIMIZE_SEARCH true**    
	**virtualize true**

### 创建adapter及导入 ###

- 创建adapter文件存入到<MW_HOME>/oracle_common/modules/oracle.ovd_11.1.1/templates/ 目录下
- 切换到<MW_HOME>/oracle_common/bin下执行导入命令
	./libovdadapterconfig.sh -adapterName userGroupAdapter2 -adapterTemplate adapter_template_usergroup2.xml -host localhost -port 7001 -userName weblogic -domainPath /oracle/Oracle/Middleware/user_projects/domains/bpm_domain/ -dataStore DB -root cn=users,dc=oracle,dc=com -contextName default -dataSourceJNDIName UserGroupDS
	
	./libovdadapterconfig.sh -adapterName userGroupAdapter1 -adapterTemplate adapter_template_usergroup1.xml -host localhost -port 7001 -userName weblogic -domainPath /oracle/Oracle/Middleware/user_projects/domains/bpm_domain/ -dataStore DB -root cn=users,dc=oracle,dc=com -contextName default -dataSourceJNDIName UserGroupDS

### 修改OVD验证配置 ###

- 切换到/oracle/Oracle/Middleware/user_projects/domains/bpm_domain/config/fwmconfig/ovd/default目录
- 修改adapters.os_xml 将critical属性都改为false

### 重启节点及admin服务器 ###

重启即可用数据库用户登陆BPM workspace


参照：http://docs.oracle.com/cd/E23943_01/bi.1111/e10543/privileges.htm#BABEJGIE
