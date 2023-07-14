# Cam-Designer-based-on-Python
### 声明：
这是一个专门用于大学机械原理课程设计中关于凸轮设计部分的开源设计程序，基于Python3.11

使用修改本程序需要Python3.7及以上版本，需要安装Matplotlib、Numpy两个库（Tkinter和Webbrowser为Python自带）

仅适用于理想情况，请勿用于实际生产环节

作者：无穷仙人（InfinityGod083）

严禁私自倒卖本程序！

### 使用说明
如果你只是想简单地使用本程序，下载Release中的exe程序，双击打开，输入9个凸轮设计所需数值（注意运动角单位为度），点击“生成新凸轮”，即可获得四张图表（轮廓图、s-δ图、v-δ图、a-δ图）

注意！图表带有单位！在输入数值前进行换算！

点击“切换背景色”可以获得黑底白字，再次点击切换回默认

点击“源代码主页”跳转到该程序的github页面

如果你想要自己自定义生成程序，需要安装Python3.7版本及以上（推荐Python3.11）

可以自行修改图标单位、名字、坐标轴，还可以修改凸轮生成的公式（当然看你需求）

### 如果你在查看源代码，这是关于后缀ri、fa、re、ne、mo的解释：
ri：rise travel 推程

fa：farthest dwell 远休止

re：return travel 回程

ne：nearest dwell 近休止

mo：motion 运动过程（包括推程、远休止、回程）

### 示例：
该凸轮：基圆半径为60mm，推杆最大位移为8mm，偏心距为4mm，滚子半径4mm，转速为325rad/s，推程运动角为60°，回程运动角为60°，远休止角为10°，顺时针旋转
![image](https://github.com/infinitygod083/Cam-Designer-based-on-Python/assets/125970872/87e9f511-1396-40a1-8fdc-ca022f73c43a)
