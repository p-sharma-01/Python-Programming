import matplotlib.pyplot as plt
Days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
City_A_Temp =  [22, 24, 19, 23, 25]
City_B_Temp = [18, 20, 17, 21, 22]
plt.plot(Days,City_A_Temp)
plt.plot(Days,City_B_Temp)
plt.legend(('city1','city2'))
plt.show()