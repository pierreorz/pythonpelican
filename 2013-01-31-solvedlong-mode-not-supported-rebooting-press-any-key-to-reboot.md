Title: ! '[SOLVED]Long mode not supported, rebooting Press any key to reboot'
Date: 2013-01-31
Category: others
Tags: vmware

<p>虚拟机安装solaris 11的时候弹出
<blockquote>Long mode not supported, rebooting Press any key to reboot........</blockquote>
原因是solaris11只支持64位，需要把BIOS的CPU选项里Inter Virtualization Technology和Inter VT均设置为ENABLE，</p>

<p>然后将虚拟机的设置如下：
<blockquote>Virtual Machine Setting-&gt;Processors-&gt;Virtualizatoin engine-&gt;Preferred mode=Intel VT-x/EPT or AMD-v/RVI</blockquote></p>

