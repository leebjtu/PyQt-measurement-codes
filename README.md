# PyQt-measurement-codes
《玩转Python硬件GUI-基于PyQt编程》配套代码
# 1. 配置环境注意事项
在配置python开发环境和安装库时，requirements.txt中的版本是测试可行的版本，每个库需要匹配安装的版本。特别注意python与库、库与库之间的版本匹配问题。否则可能会出现莫名其妙的问题。

# 2.关于读者最新库兼容问题
由于python及其库版本更新较快，故在工程中，测试好的稳定版本尽量不要更新，以免出现不兼容的问题。如果需要更新到最新的版本，请读者可以自行测试匹配性。

# 3.如何使用本书中例程
1. 安装好python环境，推荐python3.8或者python3.9大版本
2. 配置好pycharm下的虚拟环境下的python解释器
3. 打开pycharm，点击File->Open，选择工程目录Samples,即在左边工程视图中看到本书中所有的例程。不推荐直接打开samples下的子文件夹
4. 安装指定的库，使用如下命令
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
5. 点击指定的文件夹的py文件，运行即可。
