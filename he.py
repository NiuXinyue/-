# plot Gaussian Function
# 注：正态分布也叫高斯分布
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import numpy as np

# 画箭头
fig = plt.figure()
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)
ax.axis["bottom"].set_axisline_style("->", size = 1.5)
ax.axis["left"].set_axisline_style("->", size = 1.5)
ax.axis["top"].set_visible(False)
ax.axis["right"].set_visible(False)

# 正太函数
def cx(x):
    y2 = np.multiply(np.power(np.sqrt(2 * np.pi) * sigma2, -1), np.exp(-np.power(x - u2, 2) / 2 * sigma2 ** 2))
    return y2

# 图1
u2 = 1.5 
sigma2 = 1 
x = np.arange(-2, 4, 0.1)
y2 = np.multiply(np.power(np.sqrt(2 * np.pi) * sigma2, -1), np.exp(-np.power(x - u2, 2) / 2 * sigma2 ** 2))

plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决pythonmatplotlib绘图无法显示中文的问题
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

plt.plot([0.5,0.5],[0,cx(0.5)])
plt.plot([2.5,2.5],[0,cx(2.5)])
plt.plot([0,0],[0,cx(0.)])
plt.plot([3,3],[0,cx(3.)])
         
for i in range(0,50):
    plt.plot([i/100,i/100],[0,cx(i/100)],color="b")
for i in range(250,300):
    plt.plot([i/100,i/100],[0,cx(i/100)],color="b")
# 加标题
plt.ylabel('行业')
plt.xlabel('倍率')
plt.xlim((-1,4))
plt.ylim((0,0.5))
plt.xticks(np.arange(-1, 4, 1))
plt.yticks(np.arange(0, 0.5, 0.1))
plt.plot(x, y2, 'r-', linewidth=2)
plt.savefig("1.jpg")

# 图2
# u2 = 1  
# sigma2 = 1  
# x = np.arange(-2, 4, 0.1)
# y2 = np.multiply(np.power(np.sqrt(2 * np.pi) * sigma2, -1), np.exp(-np.power(x - u2, 2) / 2 * sigma2 ** 2))

# plt.plot([1,1],[0,cx(1)],c='b',linestyle='--')
# plt.xlim((-2,4))
# plt.ylim((0,0.5))
# plt.xticks(np.arange(-2, 5, 1))
# plt.yticks(np.arange(0, 0.5, 0.1))

# plt.ylabel('服务/行业')
# plt.xlabel('倍率')
# plt.plot(x, y2, 'r-', linewidth=2)
# plt.savefig("1.jpg")