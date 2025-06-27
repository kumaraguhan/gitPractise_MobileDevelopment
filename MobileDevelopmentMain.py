class Mobile:
    def __init__(self, Brand, Model, ManYEAR, Color):
        self.Brand = Brand
        self.Model = Model
        self.ManYEAR = ManYEAR
        self.Color = Color
    
    def Camera(self):
        self.camera_MP = 2
        print("Camera is Working")
    
    def Call(self):
        self.call_Quality = 0
        print("Call function is working")

    def HD_Display(self):
        print("We can see HD Content")
    
obj1 = Mobile("Samsung", "S20", "12/12/2005", "Red")

print(obj1.Brand)

obj1.Camera()

print(obj1.camera_MP)

# Need Call function to be Working
# Need Mobile Class to have HD Display Function
# Need Mobile Class to have WiFi Option
# Need Mobile Class to have Calculator Options
# Need Camera to get Upgraded upto 10 MP