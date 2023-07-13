'''
声明：
这是一个专门用于大学机械原理课程设计中关于凸轮设计部分的开源设计程序，基于Python 3.11
使用本程序需要Python3.7及以上版本，需要安装Matplotlib与Numpy两个库
仅适用于理想情况，请勿用于实际生产环节
作者：无穷仙人（InfinityGod083）
严禁私自倒卖本程序！
'''
'''
关于后缀ri、fa、re、ne、mo的解释：
ri：rise travel 推程
fa：farthest dwell 远休止
re：return travel 回程
ne：nearest dwell 近休止
mo：motion 运动过程（包括推程、远休止、近休止）
'''
'''
示例：
该凸轮：基圆半径为60mm，推杆最大位移为8mm，偏心距为4mm，滚子半径4mm，转速为325rad/s，推程运动角为60°，回程运动角为60°，远休止角为10°，顺时针旋转
'''
import matplotlib.pyplot as plt
import numpy as np


def draw_graph():
    '''基础数值设置'''
    k = -1  #旋转方向，-1为逆时针，1为顺时针
    r0 = 60  #基圆半径
    r1 = 4  #滚子半径
    h = 8  #推杆最大位移
    e = 4  #偏心距
    n = 325  #转速
    δri = np.pi / 3  #推程运动角
    δfa = np.pi / 18  #远休止角
    δre = np.pi / 3  #回程运动角
    '''基础数值运算'''
    ω = np.pi * n / 30  #角速度
    h0 = np.sqrt(r0**2 - e**2)  #推杆初始位置
    kri = np.pi / (2 * δri)  #用于计算推程运动时的一个系数，无特别含义
    kre = np.pi / (2 * δre)  #用于计算回程运动时的一个系数，无特别含义
    '''区间划分'''
    tne = np.linspace(δri + δfa + δre, np.pi * 2, 2300)  #近休止区间
    tmo = np.linspace(0, δri + δfa + δre, 1300)  #运动区间
    tri = np.linspace(0, δri, 600)  #推程区间
    tfa = np.linspace(δri, δri + δfa, 100)  #远休止区间
    tre = np.linspace(δri + δfa, δri + δfa + δre, 600)  #回程区间
    '''推程'''
    xri = (np.sqrt((h0 + h * (tri / δri - np.sin(2 * np.pi * tri / δri) /
                              (2 * np.pi)))**2 + e**2) +
           r1) * np.sin(tri) * k  #推程区间凸轮轮廓x坐标
    yri = (np.sqrt((h0 + h *
                    (tri / δri - np.sin(2 * np.pi * tri / δri) /
                     (2 * np.pi)))**2 + e**2) + r1) * np.cos(tri)  #推程区间凸轮轮廓y坐标
    sri = h * (tri / δri - np.sin(2 * np.pi * tri / δri) /
               (2 * np.pi))  #推程区间推杆位移s
    vri = h * ω * (1 - np.cos(2 * np.pi * tri / δri)) / δri  #推程区间推杆瞬时速度v
    ari = 2 * np.pi * h * ω**2 * np.sin(2 * np.pi * tri / δri) / (
        δri**2)  #推程区间推杆瞬时加速度a
    '''远休止'''
    xfa = (np.sqrt((h0 + h)**2 + e**2) + r1) * np.sin(tfa) * k  #远休止区间凸轮轮廓x坐标
    yfa = (np.sqrt((h0 + h)**2 + e**2) + r1) * np.cos(tfa)  #远休止区间凸轮轮廓y坐标
    sfa = h * (tfa - tfa + 1)  #远休止区间推杆位移s
    vfa = 0 * (tfa - tfa + 1)  #远休止区间推杆瞬时速度v
    afa = 0 * (tfa - tfa + 1)  #远休止区间推杆瞬时加速度a
    '''回程'''
    xre = (np.sqrt((h0 + h *
                    (1 - (tre -
                          (δri + δfa)) / δre + np.sin(2 * np.pi *
                                                      (tre -
                                                       (δri + δfa)) / δre) /
                     (2 * np.pi)))**2 + e**2) +
           r1) * np.sin(tre) * k  #回程区间凸轮轮廓x坐标
    yre = (np.sqrt((h0 + h *
                    (1 - (tre -
                          (δri + δfa)) / δre + np.sin(2 * np.pi *
                                                      (tre -
                                                       (δri + δfa)) / δre) /
                     (2 * np.pi)))**2 + e**2) + r1) * np.cos(tre)  #回程区间凸轮轮廓y坐标
    sre = h * (1 - (tre - (δri + δfa)) / δre + np.sin(2 * np.pi *
                                                      (tre -
                                                       (δri + δfa)) / δre) /
               (2 * np.pi))  #回程区间推杆位移s
    vre = h * ω * (np.cos(2 * np.pi * (tre - (δri + δfa)) /
                          (δre)) - 1) / δre  #回程区间推杆瞬时速度v
    are = -2 * np.pi * h * ω**2 * np.sin(
        2 * np.pi * (tre - (δri + δfa)) / δre) / (δre**2)  #回程区间推杆瞬时加速度a
    '''基圆'''
    xne = (r0 + r1) * np.sin(tne) * k  #近休止区间凸轮轮廓x坐标
    yne = (r0 + r1) * np.cos(tne)  #近休止区间凸轮轮廓y坐标
    xmo = (r0 + r1) * np.sin(tmo) * k  #运动区间凸轮轮廓x坐标
    ymo = (r0 + r1) * np.cos(tmo)  #运动区间凸轮轮廓y坐标
    sne = 0 * (tne - tne + 1)  #近休止区间推杆位移s
    vne = 0 * (tne - tne + 1)  #近休止区间推杆瞬时速度v
    ane = 0 * (tne - tne + 1)  #近休止区间推杆瞬时加速度a
    '''绘制曲线'''
    fig, axs = plt.subplots(2, 2)
    '''绘制凸轮设计图'''
    axs[0][0].plot(xri, yri, color='red', linewidth=2,
                   label='rise travel')  #推程区间曲线
    axs[0][0].plot(xfa,
                   yfa,
                   color='black',
                   linewidth=2,
                   label='farthest dwell')  #远休止区间曲线
    axs[0][0].plot(xre, yre, color='blue', linewidth=2,
                   label='return travel')  #回程区间曲线
    axs[0][0].plot(xne,
                   yne,
                   color='green',
                   linewidth=2,
                   label='base circle(ne)')  #近休止区间曲线
    axs[0][0].plot(xmo,
                   ymo,
                   color='green',
                   linewidth=2,
                   linestyle='--',
                   label='base circle(mo)')  #运动区间曲线
    axs[0][0].set_xlabel('δ')  #x轴名称及单位
    axs[0][0].set_ylabel('h/mm')  #y轴名称及单位
    axs[0][0].legend()
    axs[0][0].grid()
    axs[0][0].set_aspect(1)
    axs[0][0].set_title('Cam Design')  #凸轮设计图标题
    '''绘制推杆s-δ图'''
    axs[0][1].plot(tri, sri, color='red', linewidth=2,
                   label='rise travel')  #推程区间曲线
    axs[0][1].plot(tfa,
                   sfa,
                   color='black',
                   linewidth=2,
                   label='farthest dwell')  #远休止区间曲线
    axs[0][1].plot(tre, sre, color='blue', linewidth=2,
                   label='return travel')  #回程区间曲线
    axs[0][1].plot(tne, sne, color='green', linewidth=2,
                   label='base circle')  #近休止区间曲线
    axs[0][1].set_xlabel('δ')  #x轴名称及单位
    axs[0][1].set_ylabel('s/mm')  #y轴名称及单位
    axs[0][1].legend()
    axs[0][1].grid()
    axs[0][1].set_title('Cam s-δ Graph')  #推杆s-δ图标题
    '''绘制推杆v-δ图'''
    axs[1][0].plot(tri, vri, color='red', linewidth=2,
                   label='rise travel')  #推程区间曲线
    axs[1][0].plot(tfa,
                   vfa,
                   color='black',
                   linewidth=2,
                   label='farthest dwell')  #远休止区间曲线
    axs[1][0].plot(tre, vre, color='blue', linewidth=2,
                   label='return travel')  #回程区间曲线
    axs[1][0].plot(tne, vne, color='green', linewidth=2,
                   label='base circle')  #近休止区间曲线
    axs[1][0].set_xlabel('δ')  #x轴名称及单位
    axs[1][0].set_ylabel('v/(m*s)')  #y轴名称及单位
    axs[1][0].legend()
    axs[1][0].grid()
    axs[1][0].set_title('Cam Cam v-δ Graph')  #推杆v-δ图标题
    '''绘制推杆a-δ图'''
    axs[1][1].plot(tri, ari, color='red', linewidth=2,
                   label='rise travel')  #推程区间曲线
    axs[1][1].plot(tfa,
                   afa,
                   color='black',
                   linewidth=2,
                   label='farthest dwell')  #远休止区间曲线
    axs[1][1].plot(tre, are, color='blue', linewidth=2,
                   label='return travel')  #回程区间曲线
    axs[1][1].plot(tne, ane, color='green', linewidth=2,
                   label='base circle')  #近休止区间曲线
    axs[1][1].set_xlabel('δ')  #x轴名称及单位
    axs[1][1].set_ylabel('a/(m*s^-1)')  #y轴名称及单位
    axs[1][1].legend()
    axs[1][1].grid()
    axs[1][1].set_title('Cam Cam a-δ Graph')  #推杆a-δ图标题
    plt.show()


draw_graph()