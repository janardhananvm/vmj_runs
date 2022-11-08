

class Circle:
    radius =0
    color=""
    def _init_(myObj,radius, color):
        myObj.radius = radius
        myObj.color = color
 
    def add_rad(myObj):
        myObj.radius+=1
        return(myObj.radius)
 
objd = Circle()
x = objd.add_rad()
print(objd.radius)
print(objd.color)
