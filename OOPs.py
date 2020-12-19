"""
Class: Template for creating objects. All objects created using the same class will have the same characteristics.
Object: An instance of a class.
Instantiate: Create an instance of a class.
Method: A function defined in a class.
Attribute: A variable bound to an instance of a class.
"""


# class Kettle:
#     power_source = "electricity"            # Class Attribute
#
#     def __init__(self, model, price):
#         self.model = model
#         self.price = price
#         self.on = False
#
#     def switch_on(self):
#         self.on = True
#
#
# kenwood = Kettle("Kenwood", 1452.1253)
# print("Model : " + kenwood.model, "Price : {}".format(kenwood.price))
# print("Model : " + kenwood.model, "Price : " + str(kenwood.price))
#
# kenwood.price = 1758.235
# print("Kenwood Price : {}".format(kenwood.price))
#
# hamilton = Kettle("Hamilton", 2458.458)
# print("Models : {} = {}, {} = {}".format(kenwood.model, kenwood.price, hamilton.model, hamilton.price))
# print("Models : {0.model} = {0.price}, {1.model} = {1.price}".format(kenwood, hamilton))
#
# # print(hamilton.on)
# # hamilton.switch_on()
# # print(hamilton.on)
# #
# # hamilton.pro_dis = "Quality is good"
# #
# # print(hamilton.pro_dis)
# # # print(kenwood.pro_dis)                # AttributeError: 'Kettle' object has no attribute 'pro_dis'
#
# # Accessing class attribute
# print(Kettle.power_source)                # Via class name
# print(kenwood.power_source)               # Via object of class
# print(hamilton.power_source)              # Via object of class
#
# print(Kettle.__dict__)
# print(kenwood.__dict__)
# print(hamilton.__dict__)
#
# print("Power Source switch to Atomic")
# Kettle.power_source = "Atomic"
# print(Kettle.power_source)                # Via class name
# print("Kenwood Power source switch to Gas")
# kenwood.power_source = 'Gas'
# print(kenwood.power_source)               # Via object of class
# print(hamilton.power_source)              # Via object of class
# # In output hamilton power source is still atomic
# print(Kettle.__dict__)
# print(kenwood.__dict__)
# print(hamilton.__dict__)
#

