Title: ORA-1222：TNS:no such protocol adapter  问题解决
Date: 2012-12-03
Category: oracle
Tags: ora-1222

<p>机器上安装的是instantOracleclient-basic-win32-11.2.0.1.0客户端，本来使用PLSQL developer是可以正常连接数据库的；</p>

<p>后来开发需求装上了Form6<em>i，</em>发现连接数据库时弹出来ORA-1222：TNS:no such protocol adapter这个错误；</p>

<p>解决方案：</p>

<p><strong>1.配置PL/SQL Developer -&gt; Preferences ，OracleHome设置为Form6i的路径；</strong></p>

<p><strong>2.我的电脑 -&gt; 用户变量 设置ORACLE_HOME 为Form6i路径</strong></p>

<p><strong>或者可以直接编辑注册表，修改oracle_home的值为[Form安装的HOME文件夹]/[oracle客户端文件夹]；</strong></p>

<p><strong>如果需要切换按以上步骤修改oracle_home再重启PLSQL Developer即可以正常连接数据库；
</strong></p>

<p><em>
</em></p>
