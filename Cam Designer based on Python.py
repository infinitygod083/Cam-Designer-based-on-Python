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
import tkinter as tk
import webbrowser as wb
'''GUI代码部分'''
root = tk.Tk()
root.title('凸轮设计程序 ——by无穷仙人')
root.geometry('400x500')
root.resizable(False, False)
in0 = tk.Entry(root)
in1 = tk.Entry(root)
in2 = tk.Entry(root)
in3 = tk.Entry(root)
in4 = tk.Entry(root)
in5 = tk.Entry(root)
in6 = tk.Entry(root)
in7 = tk.Entry(root)
in8 = tk.Entry(root)
la0 = tk.Label(root, text="请输入基圆半径：")
la1 = tk.Label(root, text="请输入推杆最大位移：")
la2 = tk.Label(root, text="请输入偏心距：")
la3 = tk.Label(root, text="请输入滚子半径：")
la4 = tk.Label(root, text="请输入转速：")
la5 = tk.Label(root, text="请输入推程运动角：")
la6 = tk.Label(root, text="请输入回程运动角：")
la7 = tk.Label(root, text="请输入远休止角：")
la8 = tk.Label(root, text="请输入旋转方向（-1顺时针，1逆时针）：")
kc = 0  #切换主题计数
'''凸轮生成代码部分'''


def on_buttom0_click():
    '''数值全局设置'''
    global k
    global r0
    global r1
    global h
    global e
    global n
    global δri
    global δfa
    global δre
    global ω
    global h0
    global tne
    global tmo
    global tri
    global tfa
    global tre
    global xri
    global yri
    global sri
    global vri
    global ari
    global xfa
    global yfa
    global sfa
    global vfa
    global afa
    global xre
    global yre
    global sre
    global vre
    global are
    global xne
    global yne
    global xmo
    global ymo
    global sne
    global vne
    global ane
    '''基础数值设置'''
    k = float(in8.get())  #旋转方向，-1为逆时针，1为顺时针
    r0 = float(in0.get())  #基圆半径
    r1 = float(in3.get())  #滚子半径
    h = float(in1.get())  #推杆最大位移
    e = float(in2.get())  #偏心距
    n = float(in4.get())  #转速
    θri = float(in5.get())  #推程运动角
    θfa = float(in7.get())  #远休止角
    θre = float(in6.get())  #回程运动角
    ω = np.pi * n / 30  #角速度
    h0 = np.sqrt(r0**2 - e**2)  #推杆初始位置
    δri = θri * np.pi / 180  #推程运动角
    δfa = θfa * np.pi / 180  #远休止角
    δre = θre * np.pi / 180  #回程运动角
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
    draw_graph()


'''主题切换代码部分'''


def on_buttom1_click():
    global kc
    if kc == 0:
        root.configure(bg="#252525")
        in0.configure(bg="#1e1e1e", fg='white')
        in1.configure(bg="#1e1e1e", fg='white')
        in2.configure(bg="#1e1e1e", fg='white')
        in3.configure(bg="#1e1e1e", fg='white')
        in4.configure(bg="#1e1e1e", fg='white')
        in5.configure(bg="#1e1e1e", fg='white')
        in6.configure(bg="#1e1e1e", fg='white')
        in7.configure(bg="#1e1e1e", fg='white')
        in8.configure(bg="#1e1e1e", fg='white')
        la0.configure(bg="#252525", fg='white')
        la1.configure(bg="#252525", fg='white')
        la2.configure(bg="#252525", fg='white')
        la3.configure(bg="#252525", fg='white')
        la4.configure(bg="#252525", fg='white')
        la5.configure(bg="#252525", fg='white')
        la6.configure(bg="#252525", fg='white')
        la7.configure(bg="#252525", fg='white')
        la8.configure(bg="#252525", fg='white')
        kc = 1
    else:
        root.configure(bg="#f0f0f0")
        in0.configure(bg='white', fg='black')
        in1.configure(bg='white', fg='black')
        in2.configure(bg='white', fg='black')
        in3.configure(bg='white', fg='black')
        in4.configure(bg='white', fg='black')
        in5.configure(bg='white', fg='black')
        in6.configure(bg='white', fg='black')
        in7.configure(bg='white', fg='black')
        in8.configure(bg='white', fg='black')
        la0.configure(bg="#f0f0f0", fg='black')
        la1.configure(bg="#f0f0f0", fg='black')
        la2.configure(bg="#f0f0f0", fg='black')
        la3.configure(bg="#f0f0f0", fg='black')
        la4.configure(bg="#f0f0f0", fg='black')
        la5.configure(bg="#f0f0f0", fg='black')
        la6.configure(bg="#f0f0f0", fg='black')
        la7.configure(bg="#f0f0f0", fg='black')
        la8.configure(bg="#f0f0f0", fg='black')
        kc = 0


'''链接Github代码部分'''


def on_buttom2_click():
    wb.open('https://github.com/infinitygod083/Cam-Designer-based-on-Python',
            new=1,
            autoraise=True)


'''生成图表代码部分'''


def draw_graph():
    '''数值调用'''
    global tne
    global tmo
    global tri
    global tfa
    global tre
    global xri
    global yri
    global sri
    global vri
    global ari
    global xfa
    global yfa
    global sfa
    global vfa
    global afa
    global xre
    global yre
    global sre
    global vre
    global are
    global xne
    global yne
    global xmo
    global ymo
    global sne
    global vne
    global ane
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
    axs[0][0].set_ylabel('h/m')  #y轴名称及单位
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
    axs[0][1].set_ylabel('s/m')  #y轴名称及单位
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

'''GUI界面布局设置'''
buttom0 = tk.Button(root, text="生成新凸轮", command=on_buttom0_click)
buttom1 = tk.Button(root, text="切换背景色", command=on_buttom1_click)
buttom2 = tk.Button(root, text="源代码主页", command=on_buttom2_click)

la0.place(x=0, y=15),
in0.place(x=235, y=15)
la1.place(x=0, y=65)
in1.place(x=235, y=65)
la2.place(x=0, y=115)
in2.place(x=235, y=115)
la3.place(x=0, y=165)
in3.place(x=235, y=165)
la4.place(x=0, y=215)
in4.place(x=235, y=215)
la5.place(x=0, y=265)
in5.place(x=235, y=265)
la6.place(x=0, y=315)
in6.place(x=235, y=315)
la7.place(x=0, y=365)
in7.place(x=235, y=365)
la8.place(x=0, y=415)
in8.place(x=235, y=415)
buttom0.place(x=165, y=465)
buttom1.place(x=65, y=465)
buttom2.place(x=265, y=465)

root.mainloop()