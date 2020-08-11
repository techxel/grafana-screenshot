## 通过`chrome`浏览器访问网页(可静默开启, 即看不到浏览器启动), 并截图

#### 安装chrome浏览器

    # linux
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
    yum localinstall google-chrome-stable_current_x86_64.rpm

> 其他平台直接安装程序即可

#### 安装依赖

    pip3 install webdriver-manager
    pip3 install selenium
    
#### 如果网站包含中文, 还需要安装相关字体

    yum groupinstall Fonts
    
> 其他平台参考: https://help.accusoft.com/PrizmDoc/v13.4/HTML/Installing_Asian_Fonts_on_Red_Hat_and_CentOS.html

#### 启动截图

    python3 main.py
