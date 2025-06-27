class Mobile:
    def __init__(self, Brand, Model, ManYEAR, Color):
        self.Brand = Brand
        self.Model = Model
        self.ManYEAR = ManYEAR
        self.Color = Color
    
    def Camera(self):
        self.camera_MP = 10
        print("Camera is Working")
    
    def Call(self):
        self.call_Quality = 10
        print("Call function is working")

    def HD_Display(self):
        print("We can see HD Content")

    def Wifi(self):
        self.Speed = "40 mp/s"
        print(f"Wifi is working: Speed: {self.Speed}")

    def Calculator(self):
        def add():
            print("Adding")
        
        def sub():
            print("Subtracting")
        
        def mul():
            print("Multiplying")

        def div():
            print("Diving")
    
obj1 = Mobile("Samsung", "S20", "12/12/2005", "Red")

print(obj1.Brand)

obj1.Camera()

print(obj1.camera_MP)

# Need Call function to be Working
# Need Mobile Class to have HD Display Function
# Need Mobile Class to have WiFi Option
# Need Mobile Class to have Calculator Options
# Need Camera to get Upgraded upto 10 MP
# Need to Make Call Quaity to 10