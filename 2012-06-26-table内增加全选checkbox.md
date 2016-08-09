Title: Table内增加全选checkbox
Date: 2012-06-26
Category: ADF
Tags: ADF


解决方案：     

VO里新建Transient属性Checked(Boolean)    

表内添加一个column如下：    
{% codeblock lang:java %}
<af:column id="c10" headerText="选择" width="30" align="center" noWrap="true">
<f:facet name="header" >
<af:selectBooleanCheckbox valueChangeListener="#{backingBean.selectAll}"
autoSubmit="true" id="selectAll"
label="" value=""
</f:facet>
<af:selectBooleanCheckbox label="选中/非选中" id="sbc1"  autoSubmit="true" immediate="true"
value="#{row.bindings.Checked.inputValue}"/>

</af:column>
{% endcodeblock %}

{% codeblock lang:java %}
pupblic void selectAll(ValueChangeEvent valueChangeEvent) {
CIteratorBinding it = ADFUtils.findIterator(REIM_HEADER_ITER);
ViewObject vo = it.getViewObject();

if (valueChangeEvent.getNewValue() != null) {
Boolean selectAll =
Boolean.parseBoolean(valueChangeEvent.getNewValue().toString());
if (!selectAll) {
for (Row temp : vo.getAllRowsInRange()) {
temp.setAttribute("Checked", false);
}
} else {
for (Row temp : vo.getAllRowsInRange()) {
temp.setAttribute("Checked", true);
}
}
RichTable table = (RichTable)JSFUtils.findComponentInRoot("t1");
AdfFacesContext.getCurrentInstance().addPartialTarget(table);
}
}
{% endcodeblock %}
以上即可实现此需求.
