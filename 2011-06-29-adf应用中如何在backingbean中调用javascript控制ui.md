Title: ADF应用中如何在BackingBean中调用javascript控制UI
Date: 2011-06-29
Category: ADF
Tags: ADF

<p>当你需要在ManagedBean中控制页面控制的属性的时候，可以使用以下代码调用javascript实现。</p>

<p>&nbsp;
<pre class="brush:java">//import org.apache.myfaces.trinidad.util.Service;
String script="你的javascript代码";</pre></p>

<p>FacesContext context = <br />
        FacesContext.getCurrentInstance();</p>

<p>ExtendedRenderKitService erks = <br />
        (ExtendedRenderKitService)Service.<br />
        getService(context.getRenderKit(), <br />
        ExtendedRenderKitService.class);</p>

<p>erks.addScript(context, script);
&nbsp;</p>
