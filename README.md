### master分支为 2022-11-15更新的m94分支源码



##### 1、git 通过ssh链接拉去代码配置（后续提交代码不需要输入密码）

如果没有id_rsa.pub公钥，通过下方命令生成

​	ssh-keygen -t rsa -C '邮箱'

打开id_rsa.pub复制其中的密钥内容，在github个人账户图标中点击 settings -> SSH and GPG keys -> new SSH key 中添加进去

##### 2、编译环境

vs2019 + sdk 10.0.20348.0 + python3.x + ninja + depot_tools

##### 3、安装python（安装过的忽略）

https://www.python.org/downloads/windows/

下载python安装后，cmd命令窗口 python3 --version 显示安装的版本就是成功安装了

显示没有，就去安装目录下将python 改为python3(如果python2版本的不能这个更改)

##### 4、下载 ninja release包（安装过的忽略）

​	https://github.com/ninja-build/ninja/releases/download/v1.11.1/ninja-win.zip

##### 5、下载depot_tools(源码当中已经上传)

设置环境变量，重启电脑

##### 6、webrtc编译(设置的路径换为自己安装的路径即可)

###### cmd设置以下变量

set DEPOT_TOOLS_WIN_TOOLCHAIN=0

set GYP_MSVS_VERSON=2019

set vs2019_install=F:\Program Files (x86)\Microsoft Visual Studio\2019\Community

set GYP_MSVS_OVERRIDE_PATH=F:\Program Files (x86)\Microsoft Visual Studio\2019\Community

set WINDOWSSDKDIR=F:\Windows Kits\10

set GYP_GENERATORS=msvs-ninja,ninja



###### 进入src目录下

gn gen out\Release-vs2019 --ide=vs2019 --args="is_debug=false target_os=\"win\" target_cpu=\"x64\" is_component_build=false is_clang=false use_custom_libcxx=false use_lld=false treat_warnings_as_errors=false use_rtti=true rtc_include_tests=false rtc_build_examples=false"

ninja -C out\Release-vs2019





##### 异常解决方案

【Exception: dbghelp.dll not found in "F:\Windows Kits\10\Debuggers\x64\dbghelp.dll"】

进入 控制面板→程序→程序和功能 页面

![image-20221124005803917](C:\Users\miao\AppData\Roaming\Typora\typora-user-images\image-20221124005803917.png)

右击选择更改-->change

![image-20221124005936011](C:\Users\miao\AppData\Roaming\Typora\typora-user-images\image-20221124005936011.png)