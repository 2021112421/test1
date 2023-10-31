import turtle as t


print("快乐！")
#定义star函数
def star(p,s,c,x,y):
     t.goto(x,y)
     t.pendown()
     a=180-(180/p)
     t.color(c)
     for i in range(p):
        t.forward(s)
        t.right(a)

  



#用star函数来画爱心
t.penup()
star(5,20,"red",0,50)
star(5,20,"blue",50,100)
star(5,20,"red",100,50)
star(5,20,"blue",100,0)
star(5,20,"red",0,-100)
star(5,20,"blue",-100,0)
star(5,20,"red",-100,50)
star(5,20,"blue",-50,100)
t.pendown()
t.color("red")
t.goto(0,50)
t.penup()
t.goto(0,0)
t.write("I love you",)
t.penup()
    
    
