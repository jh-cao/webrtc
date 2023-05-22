### master分支为 2022-11-15更新的m94分支源码



##### 1、git 通过ssh链接拉去代码配置（后续提交代码不需要输入密码）

如果没有id_rsa.pub公钥，通过下方命令生成

​	ssh-keygen -t rsa -C '邮箱'

打开id_rsa.pub复制其中的密钥内容，在github个人账户图标中点击 settings -> SSH and GPG keys -> new SSH key 中添加进去



编译依赖环境安装说明：https://blog.csdn.net/m0_46597409/article/details/128046547

编译+编译异常处理：https://blog.csdn.net/m0_46597409/article/details/130702954