class MyClass:
    count=0
    @staticmethod
    def static_method():
        MyClass.count+=1
        print("This is a static method.",MyClass.count)
    @staticmethod
    def adder():
        MyClass.count+=1
        print(MyClass.count)

# Calling the static method
# ob = MyClass()
ob1=MyClass()
ob2=MyClass()
ob1.static_method()
ob2.adder()