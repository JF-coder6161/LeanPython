import matplotlib.pyplot as plt

# 使用scatter()绘制散点图并设置其样式
# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
# plt.scatter(x_values,y_values,s=200)

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
plt.scatter(x_values, y_values, edgecolors='none', s=2, c=(0, 0, 0.8))

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.axis([0, 1100, 0, 1100000])
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
# 显示图表
# plt.show()
# 自动保存图表
# 第二个实参指定将图表多余的空白区域裁剪掉
plt.savefig('squares_plot.png', bbox_inches='tight')
