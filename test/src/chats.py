import matplotlib.pyplot as plt


plt.xlabel('Age range')
plt.ylabel('Number')
plt.title('The statistics of face age dataset')
a = plt.subplot(1, 1, 1)

plt.ylim=(10, 40000)
x = [10, 20, 30, 40, 50, 60, 70]
x1 = [7, 17, 27, 37, 47, 57, 67]
x2 = [13, 23, 33, 43, 53, 63, 73]

Y1 = [41, 39, 13, 69, 39, 14, 7]
Y2 = [0, 15, 20, 105, 79, 37, 43]
Y3 = [0, 91, 404, 464, 521, 375, 553]

#这里需要注意在画图的时候加上label在配合plt.legend（）函数就能直接得到图例，简单又方便！

plt.bar(x1, Y1, facecolor='red', width=3, label = 'FG-NET')
plt.bar(x, Y2, facecolor='green', width=3, label = 'MORPH')
plt.bar(x2, Y3, facecolor='blue', width=3, label = 'CACD2000')

plt.legend()

plt.show()
