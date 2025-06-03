import matplotlib.pyplot as plt
Fruits = ['Apple', 'Banana', 'Cherry', 'Mango']
Votes = [40, 25, 20, 15]
plt.pie(Votes, labels = Fruits, autopct = "%1.1f%%" )
plt.show()