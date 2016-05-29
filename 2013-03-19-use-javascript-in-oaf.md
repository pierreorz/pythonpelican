Title: Use Javascript in OAF
Date: 2013-01-30
Category: ebs
Tags: javascript, oaf

####使用Js脚本库####
在CO的*processRequest*中引入JS库  
编写JS库:Calendar2013.js
{% codeblock lang:java %}
pageContext.putJavaScriptLibrary("Calendar","Calendar2013.js"); 
((OAMessageTextInputBean)webBean
.findChildRecursive("inputDate"))
.setOnClick("setday(this)");
{% endcodeblock %}

需要把Calendar2013.js放置在$**COMMON_TOP**/html下。

####直接引用javaScript####

编写*JavaScript*:
{% codeblock lang:java %}
String javaScript="JAVASCRIPT:function setday(){...}";
{% endcodeblock %}

在**CO**的*processRequest*中加载*javascript*

{% codeblock lang:java %}
pageContext.putJavaScriptFunction("sayday()",javaScript);
((OAMessageTextInputBean)webBean.findChildRecursive("inputDate"))
    .setOnClick("javascript:setday()");
{% endcodeblock %}
