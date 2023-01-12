from random_walk import RandomWalk
import matplotlib.pyplot as plt

while True:
    random_walk = RandomWalk(50000)
    random_walk.fill_walk()
    
    # 设置绘图窗口的尺寸
    # dpi 分辨率
    plt.figure(dpi=128,figsize=(10,6))
    
    point_numbers = list(range(random_walk.num_points))
    
    # plt.plot(random_walk.x_values, random_walk.y_values)
    # plt.title("Random_walk")
    # plt.show()
    plt.scatter(random_walk.x_values, random_walk.y_values, c=point_numbers,
                cmap=plt.cm.Blues, edgecolors='none', s=1)
    
    # 突出起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(random_walk.x_values[-1],random_walk.y_values[-1],c='red',
                edgecolors='none',s=100)
    
    # 隐藏坐标轴
    plt.axis('off')
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
