from py4j.java_gateway import JavaGateway
gateway = JavaGateway()                   # connect to the JVM
random = gateway.jvm.java.util.Random()   # create a java.util.Random instance
number1 = random.nextInt(10)              # call the Random.nextInt method
number2 = random.nextInt(10)
print(number1,number2)
addition_app = gateway.entry_point        # get the AdditionApplication instance
# print(addition_app.addition(number1,number2))
# print(addition_app.cc(number1,number2))
print(addition_app)