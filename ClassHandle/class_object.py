class MyRouter(object):
    "This is a class that describes the characteristics of the routers"
    def __init__(self, routerrname, model, serialno, ios):
        self.routerrname = routerrname
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_router(self, manufact_date):
        print ("Router Name is ", self.routerrname)
        print ("Router Model is ", self.model)
        print ("Router Serial Number is " , self.serialno)
        print ("Router IOS version is ", self.ios)
        print ("The model and the date combined ", self.model + manufact_date)

router1 = MyRouter('Hitachi', 'H2020201', 20201990, 2.3)
print (router1.model)

router1.print_router('20189018')

"Pre defined methods"

print (getattr(router1, "ios"))
setattr(router1, "ios", 2.4)
print (getattr(router1, "ios"))

print(hasattr(router1, "ios"))

delattr(router1, "ios")
print (getattr(router1, "ios"))

print(isinstance(router1, MyRouter))