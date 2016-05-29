Title: immediate="true" 的异常
Date: 2012-06-26
Category: ADF
Tags: ADF

<p>设置按钮的immediate="true" 可以避免因按钮提交FORM导致的页面刷新闪烁，但也会带来麻烦。<br />
假如对表的取消按钮设置了此属性，可能会发生新增数据，然后点取消作rollback时数据显示异常。<br />
开发时值得注意</p>
