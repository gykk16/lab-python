import matplotlib.pyplot as plt

# 산점도 그래프(scatter chart)


# 친구 수
friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

for l, f, m in zip(labels, friends, minutes):
    plt.annotate(l, xy = (f, m), xytext = (5, -10), textcoords = 'offset points')

plt.title('Minutes vs friends')
plt.xlabel('# of Friends')
plt.ylabel('daily minutes spent on site')

plt.savefig('../image_output/year_gdp.png')
plt.show()


#################################################

math = [99, 90, 85, 97, 80]
science = [100, 85, 60, 90, 70]


plt.scatter(math, science)
plt.axis('equal')

plt.title('Math vs Science')
plt.xlabel('Math')
plt.ylabel('Science')

plt.savefig('../image_output/year_gdp.png')
plt.show()