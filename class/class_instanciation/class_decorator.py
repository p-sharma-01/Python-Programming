class MyClass:
    count=0
    

    @classmethod
    def static_method(cls):
        cls.count+=1
        print("This is a static method.",cls.count)
    # @staticmethod
    @classmethod
    def adder(cls):
        cls.count+=1
        print(cls.count)

# Calling the static method
# ob = MyClass()
ob1=MyClass()
ob2=MyClass()
ob1.static_method()
ob2.adder()