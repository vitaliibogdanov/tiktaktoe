# Крестики нолики

from tkinter import *
new=[]
holes = [1,2,3,4,5,6,7,8,9]
wcomb=[[1,2,3,],[1,4,7],[1,5,9],[3,6,9],[7,8,9],[4,5,6],[2,5,8],[3,5,7]]
combs=[[1,2,3,],[1,4,7],[1,5,9],[3,6,9],[7,8,9],[4,5,6],[2,5,8],[3,5,7]]
fig = 'cross'
cx = 300
cy = 300
c_s = 50
num = 0
wid=600
hei=600



window = Tk()
window.title('крестики нолики :D')
canvas = Canvas(window, width =wid, height =hei)
canvas.pack()

#поле
def pole():
    global holes,combs,fig
    fig = 'cross'
    holes = [1,2,3,4,5,6,7,8,9]
    combs=[[1,2,3,],[1,4,7],[1,5,9],[3,6,9],[7,8,9],[4,5,6],[2,5,8],[3,5,7]]
    canvas.create_rectangle(-10,-10,wid+10,hei+10,fill= 'white')
    canvas.create_rectangle(250,150,260,450,fill='black' )
    canvas.create_rectangle(350,150,360,450,fill='black' )
    canvas.create_rectangle(150,250,450,260,fill='black' )
    canvas.create_rectangle(150,350,450,360,fill='black' )

def triger(event):
    global pole
    pole()

pole()

#кресты круги
def p_cross(x,y):
    global c_s
    canvas.create_line(x-c_s/2,y- c_s/2,x+c_s/2+10,y+c_s/2+10,fill='red',width = 7)
    canvas.create_line(x-c_s/2,y+ c_s/2+10,x+c_s/2+10,y-c_s/2,fill='red',width = 7)

def p_circle(x,y):
    global c_s
    canvas.create_oval(x-c_s/2,y- c_s/2,x+c_s/2+10,y+c_s/2+10,fill='blue')

def figure():
    global holes, num,fig,number,wcomb,combs
    if fig == 'cross':
        if 1 <= num <=3:
            p_cross(100+100*num,400)
            fig = 'circle'
            
        if 4 <= num <=6:
            p_cross(-200+100*num,300)
            fig = 'circle'
            
        if 7 <= num <=9:
            p_cross(-500+100*num,200)
            fig = 'circle'
        for numbers in combs:
            for i in range(1,4):
                if numbers[i-1] == num:
                    numbers[i-1] = 'x'
                    if numbers[0] == numbers[1] == numbers[2]:
                        ind = combs.index(numbers)
                        goal = wcomb[ind]
                      
                        if 1 <= goal[0] <= 3:
                            if 4 <= goal[1] <= 6:
                                wy = 450
                            else:
                                wy = 400
                            if 4 <= goal[1] <= 6:
                                wx = 200 - 50*((goal[1]-3)-(goal[0]))+100*(goal[0]-1)
                            else:
                                wx = 200 - 50*((goal[1])-(goal[0]))
                        elif 4 <= goal[0] <= 6:
                            wy = 300
                            wx = 150
                        elif 7 <= goal[0] <= 9:
                            if 4 <= goal[1] <= 6:
                                wy = 150
                            else:
                                wy = 200
                            if 4 <= goal[1] <= 6:
                                wx = 200 - 50*((goal[1]-3)-(goal[0]))+100*(goal[0]-1)
                            else:
                                wx = 200 - 50*((goal[1])-(goal[0]))


                        if 1 <= goal[2] <= 3:
                            if 4 <= goal[1] <= 6:
                                wy2 = 450
                            else:
                                wy2 = 400
                            if 4 <= goal[1] <= 6:
                                wx2 = 100 + 50*((goal[2]-3)-(goal[1]))+100*(goal[2]-1)
                            else:
                                wx2 = 400 + 50*((goal[1])-(goal[0]))
                        elif 4 <= goal[2] <= 6:
                            wy2 = 300
                            wx2 = 450
                        elif 7 <= goal[2] <= 9:
                            if 4 <= goal[1] <= 6:
                                wy2 = 150
                            else:
                                wy2 = 200
                            if 4 <= goal[1] <= 6:
                                wx2 = 100 + 50*((goal[2]-6)-(goal[1]-3))+100*(goal[2]-6)
                            else:
                                wx2 = 450
                        canvas.create_line(wx,wy,wx2,wy2,fill='blue',width=7)
                        holes = []
                        fig = 'cross'
    elif fig == 'circle':
        if 1 <= num <=3:
            p_circle(100+100*num,400)
            fig = 'cross'
            
        if 4 <= num <=6:
            p_circle(-200+100*num,300)
            fig = 'cross'
            
        if 7 <= num <=9:
            p_circle(-500+100*num,200)
            fig = 'cross'
        for numbers in combs:
            for i in range(1,4):
                if numbers[i-1] == num:
                    numbers[i-1] = 'O'
                    if numbers[0] == numbers[1] == numbers[2]:
                        ind = combs.index(numbers)
                        goal = wcomb[ind]
                      
                        if 1 <= goal[0] <= 3:
                            if 4 <= goal[1] <= 6:
                                wy = 450
                            else:
                                wy = 400
                            if 4 <= goal[1] <= 6:
                                wx = 200 - 50*((goal[1]-3)-(goal[0]))+100*(goal[0]-1)
                            else:
                                wx = 200 - 50*((goal[1])-(goal[0]))
                        elif 4 <= goal[0] <= 6:
                            wy = 300
                            wx = 150
                        elif 7 <= goal[0] <= 9:
                            if 4 <= goal[1] <= 6:
                                wy = 150
                            else:
                                wy = 200
                            if 4 <= goal[1] <= 6:
                                wx = 200 - 50*((goal[1]-3)-(goal[0]))+100*(goal[0]-1)
                            else:
                                wx = 200 - 50*((goal[1])-(goal[0]))


                        if 1 <= goal[2] <= 3:
                            if 4 <= goal[1] <= 6:
                                wy2 = 450
                            else:
                                wy2 = 400
                            if 4 <= goal[1] <= 6:
                                wx2 = 100 + 50*((goal[2]-3)-(goal[1]))+100*(goal[2]-1)
                            else:
                                wx2 = 400 + 50*((goal[1])-(goal[0]))
                        elif 4 <= goal[2] <= 6:
                            wy2 = 300
                            wx2 = 450
                        elif 7 <= goal[2] <= 9:
                            if 4 <= goal[1] <= 6:
                                wy2 = 150
                            else:
                                wy2 = 200
                            if 4 <= goal[1] <= 6:
                                wx2 = 100 + 50*((goal[2]-6)-(goal[1]-3))+100*(goal[2]-6)
                            else:
                                wx2 = 450
                        canvas.create_line(wx,wy,wx2,wy2,fill='red',width=7)
                        holes = []
                        fig = 'cross'
 

def p1(event):
    global holes,num
    for i in holes:
        if i == 1:
            num = 1
            holes.remove(1)
            figure()

def p2(event):
    global holes,num
    for i in holes:
        if i == 2:
            num = 2
            holes.remove(2)
            figure()
            
def p3(event):
    global holes,num
    for i in holes:
        if i == 3:
            num = 3
            holes.remove(3)
            figure()
            
def p4(event):
    global holes,num
    for i in holes:
        if i == 4:
            num = 4
            holes.remove(4)
            figure()
            
def p5(event):
    global holes,num
    for i in holes:
        if i == 5:
            num = 5
            holes.remove(5)
            figure()
            
def p6(event):
    global holes,num
    for i in holes:
        if i == 6:
            num = 6
            holes.remove(6)
            figure()
            
def p7(event):
    global holes,num
    for i in holes:
        if i == 7:
            num = 7
            holes.remove(7)
            figure()
            
def p8(event):
    global holes,num
    for i in holes:
        if i == 8:
            num = 8
            holes.remove(8)
            figure()
            
def p9(event):
    global holes,num
    for i in holes:
        if i == 9:
            num = 9
            holes.remove(9)
            figure()

canvas.focus_set()

canvas.bind('<KeyPress-1>', p1)
canvas.bind('<KeyPress-2>', p2)
canvas.bind('<KeyPress-3>', p3)
canvas.bind('<KeyPress-4>', p4)
canvas.bind('<KeyPress-5>', p5)
canvas.bind('<KeyPress-6>', p6)
canvas.bind('<KeyPress-7>', p7)
canvas.bind('<KeyPress-8>', p8)
canvas.bind('<KeyPress-9>', p9)
canvas.bind('<KeyPress-c>',triger)





window.mainloop()

