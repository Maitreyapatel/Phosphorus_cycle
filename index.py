import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style


from tkinter import *
import tkinter as tk
from PIL import ImageTk
import math
from tkinter import ttk
import time
import numpy
import random

LARGE_FONT= ("Verdana", 12)
EXTRA_LARGE_FONT = ("Verdana",14)
FINAL = ("Verdana",24)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "SC220 Project-1")
        self.geometry('1200x700+200+100')
        
        
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand = True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.show_frame(StartPage)

    def show_frame(self, cont):

        F = cont
        frame = F(self.container, self)
        self.frames[F] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        


        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Phosphorus cycle", font=FINAL)
        label.pack(side=tk.TOP,pady=10,padx=10)

        # button = ttk.Button(self, text="Visit Page 1",
        #                     command=lambda: controller.show_frame(PageOne))
        # button.pack(side=tk.TOP)

        button2 = ttk.Button(self, text="Useage of Phosphorus in fertilizers",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(pady=10)

        button3 = ttk.Button(self, text="Predictions simulation via graph",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack(pady=10)

        button4 = ttk.Button(self, text="Cycle Simulation",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack(pady=10)

        button5 = ttk.Button(self, text="Team Members",
                            command=lambda: controller.show_frame(TeamMembers))
        button5.pack(pady=10)


        # text = tk.Text()
        # txt = "In this project the main aim was to observe the flow of phosphorus and the areas where the cycle is disturbed. The area where we primarily focused was on human interference.By human interference, we imply usage of phosphorus containing fertilizers in India and in general, World. Also we look upon how rainfall and runoff plays important role in the cycle. We collected data researching different studies and research papers.Hereby, we present the Phosphorus cycle and simulate the graph of runoff of phosphorus containing fertilizers versus period of years. We also approximate the data based graph and extrapolate the graph for future years. Although we think looking at constant disturbance by humans, the rate would increase exponentially very fast."
        # text.insert(INSERT,txt)
        # text.pack(pady=10)
        label = tk.Label(self, text="""
            In this project the main aim was to observe the flow of phosphorus and the areas where the cycle is disturbed.
            The area where we primarily focused was on human interference.
            By human interference, we imply usage of phosphorus containing fertilizers in India and in general, World.
            Also we look upon how rainfall and runoff plays important role in the cycle. 
            We collected data researching different studies and research papers.
            Here,we present the Phosphorus cycle and simulate the graph of runoff of phosphorus containing fertilizers versus period of years.
            We also approximate the data based graph and extrapolate the graph for future years. 
            Although we think looking at constant disturbance by humans, the rate would increase exponentially very fast.
            """, font=EXTRA_LARGE_FONT,bg="white", justify="left")
        label.pack(pady=10)


        label2 = tk.Label(self, text="""
            References:

            (1)    http://www.greenpeace.to/greenpeace/wp-content/
                    uploads/2012/06/tirado-and-allsopp-2012-phosphorus-in-agriculture-technical-report-02-2012.pdf

            (2)    http://www1.agric.gov.ab.ca/$department/deptdocs.nsf/all/agdex920
            """, font=EXTRA_LARGE_FONT,bg="white", justify="left")
        label2.pack(pady=10)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="About the project", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        # button2 = ttk.Button(self, text="Page Two",
        #                     command=lambda: controller.show_frame(PageTwo))
        # button2.pack()

class TeamMembers(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Team members", font=FINAL)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        label = tk.Label(self, text="""
            Maitreya Patel         201601160
            Namra Prajapati         201601181
            Druvil Shah            201601011
            Nikesh Parekh        201601061
            Ishita Jain            201601045
            Tirth Shah            201601009
            Kalpesh Pandya        201601405
            Harshit Malaviya        201601147
            Dipesh Dhameliya        201601118
            Shivam Agarwal        201601062
            """, font=EXTRA_LARGE_FONT,bg="white", justify="left")
        label.pack(pady=20)



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Useage of Phosphorus in fertilizers", font=LARGE_FONT)
        label.grid(padx=10,pady=10,row=0)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(padx=10,pady=10,row=1,column=0)

        button2 = ttk.Button(self, text="Next Graph",
                            command=lambda: controller.show_frame(PageThree))
        button2.grid(padx=0,pady=10,row=1,column=1)

        label = tk.Label(self, text="""
            Here we have drawn useage of phosphorus as fertilizers in India for past few year.
            From this graph we have derived an eq. which can predict future use of phosphorus.
                    
                         F(x) = c + e^(0.5*(x+1.6))
                    Where c is constant.

            From this equation we have made simulation(graph),
              which shows us wastage(due to runoff) of phosphorus.
            And which causes eutrophication.
            """, font=LARGE_FONT,bg="white", justify="left")
        label.grid(pady=0,padx=0,row=2,column=1)

        self.plot()

    def plot(self):
        
        # style.use('ggplot')
        self.xvar = [1970,1974,1977,1980,1983,1985,1987,1988,1990,1993,1995,1998,2001,2003,2005,2006,2008]
        self.yvar = [1,0.75,1.5,2,2,3,2.75,3.5,3.5,3,3.25,3,5,4.5,6,6,7]
        f = Figure(figsize=(6,6), dpi=100)
        self.a = f.add_subplot(1,1,1)
        self.hl, = self.a.plot(self.xvar,self.yvar,'r', marker='o',label="Past year useage")
        self.a.legend()
        self.a.set_title('Phosphorus useage in India as a fertilizer')
        self.a.set_xlabel("Year")
        self.a.set_ylabel("Million tonnes Phosphorus")
        # self.a.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


        self.a.set_xlim(1970,2020)
        self.a.set_ylim(0,50)


        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.get_tk_widget().grid(column=0, row=2)


        self.canvas.show()

        



# class PageTwo(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
#         label.grid(padx=10,pady=10,row=0)

#         button1 = ttk.Button(self, text="Back to Home",
#                             command=lambda: controller.show_frame(StartPage))
#         button1.grid(padx=10,pady=10,row=1)

#         label = tk.Label(self,text="Select the rate of rainfall:")
#         label.grid(padx=10,pady=10,row=2,column=2)
#         self.w = tk.Scale(self, from_=100, to=-100)
#         self.w.grid(padx=10,pady=10,row=2,column=3)

#         self.plot()

#     def plot(self):
#         i=5
#         # for i in range(5):
#         style.use('ggplot')
#         self.xvar = [i for i in range(10)]
#         self.yvar = [i for i in range(10)]
#         f = Figure(figsize=(5,5), dpi=100)
#         a = f.add_subplot(1,1,1)
#         self.hl, = a.plot(self.xvar,self.yvar,'r', marker='o')
#         self.xvar = [i for i in range(0)]
#         self.yvar = [i for i in range(0)]      
#         self.ha, = a.plot(self.xvar,self.yvar,'g',marker='x')
#         self.canvas = FigureCanvasTkAgg(f, self)
#         self.canvas.get_tk_widget().grid(column=1, row=2)
#         ani = animation.FuncAnimation(f, self.update, interval=2000, blit=False)


#         self.canvas.show()

        

    def update(self,x):
        self.xvar.append(5+x)
        self.yvar.append(5+(self.w.get()/100)*x)
        self.ha.set_data(self.xvar,self.yvar)

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="As per our previous graph, we can generalize it to predict the future.", font=LARGE_FONT)
        label.grid(padx=10,pady=10,row=0)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(padx=10,pady=10,row=1,column=1)

        button2 = ttk.Button(self, text="Previous Graph",
                            command=lambda: controller.show_frame(PageTwo))
        button2.grid(padx=10,pady=10,row=1,column=2)

        label = tk.Label(self,text="Change the useage of phosphorus:")
        label.grid(padx=10,pady=10,row=2,column=2)
        self.w = tk.Scale(self, from_=100, to=-100)
        self.w.grid(padx=10,pady=10,row=2,column=3)
        button3 = ttk.Button(self, text="Reset",
                            command=lambda: controller.show_frame(PageThree))
        button3.grid(pady=10,padx=10,row=2,column=4)
        self.plot()

    def plot(self):
        
        # style.use('ggplot')
        self.xvar = [i for i in range(2010,2041)]
        # print(self.xvar)
        sum = 0
        temp = []
        for i in range(len(self.xvar)):
            sum+=0.2
            temp.append(sum)
        self.yvar = [3+math.exp(0.5*(x+1.6)) for x in temp]

        # self.xvar = [1,2,3,4,5]
        # self.yvar = self.xvar
        # print(self.yvar)

        f = Figure(figsize=(6,6), dpi=100)
        self.a = f.add_subplot(1,1,1)
        self.hl, = self.a.plot(self.xvar,self.yvar,'r', marker='o',label="Expected use of phosphorus in fertilizers")
        self.a.set_title('Phosphorus in aquatic system due to the use of fertilizers in India')
        self.a.set_xlabel("Year")
        self.a.set_ylabel("Million tonnes Phosphorus")
        # self.a.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        self.xavar = []
        self.yavar = []
        self.xbvar = []
        self.ybvar = []

        self.a.set_xlim(2010,2030)
        self.a.set_ylim(0,self.yvar[len(self.yvar)-1])

        self.hg, = self.a.plot(self.xavar,self.yavar,'p',marker='P',label="Phosphorus in aquatic system due to runoff")

        self.ha, = self.a.plot(self.xbvar,self.ybvar,'g',marker='x', label="Changed phosphorus useage")
        self.a.legend()

        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.get_tk_widget().grid(column=0, row=2)
        ani = animation.FuncAnimation(f, self.update, interval=2000, blit=False)


        self.canvas.show()

        

    def update(self,i):
        if i<len(self.xvar) and i!=0: 
            self.xbvar.append(self.xvar[7+i])
            #self.ybvar.append(self.yvar[7+i]*(0.5+int(self.w.get())*0.005))
            self.ybvar.append(self.yvar[7+i]*(1+int(self.w.get())*0.01))

            self.xavar.append(self.xvar[7+i])
            self.yavar.append(self.yvar[7+i]*(1+int(self.w.get())*0.01)*(0.7+(random.randrange(0,10)/100)))

            self.hg.set_data(self.xavar,self.yavar)
            self.ha.set_data(self.xbvar,self.ybvar)
            self.a.set_xlim(2010,2030)
            self.a.set_ylim(0,self.yvar[len(self.yvar)-1])
            self.canvas.draw()
        # self.hl.set_xdata(numpy.append(self.hl.get_xdata(), x))
        # self.hl.set_ydata(numpy.append(self.hl.get_ydata(), x))


class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Simulation...", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=10)

        self.topFrame = Frame(self)
        self.topFrame.pack()
        self.bottomFrame = Frame(self)
        self.bottomFrame.pack(side=BOTTOM)
        self.l1 = Label(self.topFrame, text="Rainfall rate (Increase/dicrease):")
        self.l1.pack(side=LEFT)
        self.r = tk.Scale(self.topFrame, from_=-50, to=50, orient=HORIZONTAL)
        self.r.pack(side=LEFT)
        self.l3 = Label(self.topFrame, text="Useage of Phosphorus:")
        self.l3.pack(side=LEFT)
        self.p = tk.Scale(self.topFrame, from_=-50, to=50, orient=HORIZONTAL)
        self.p.pack(side=LEFT)
        self.l2 = Label(self.topFrame, text="Number of cycles:")
        self.l2.pack(side=LEFT)
        self.e2 = Entry(self.topFrame)
        self.e2.pack(side=LEFT)
        self.canvas = Canvas(self.bottomFrame,width=1019,height=760)
        self.canvas.pack()
        self.image = ImageTk.PhotoImage(file="./animation.png")
        self.canvas.create_image(0, 0, image = self.image, anchor = NW)

        self.canvas.create_rectangle(350,175,450,225,fill="blue")

        b1=ttk.Button(self.topFrame, text='Simulation',command=lambda: self.startAnime(self))
        b1.pack(side=BOTTOM)
        

    def startAnime(self,tp):
        try:
            i = self.e2.get()
            print(i)
            i = int(float(i))
        except:
            i=1
        # global r
        # global p
        for j in range(0,i):

            try:
                self.canvas.delete(self.c1)
                self.canvas.delete(self.c2)
                self.canvas.delete(self.c3)
                self.canvas.delete(self.c4)

            except:
                print("Does not deleted")

            rain = self.r.get()
            phs = self.p.get()    
            self.c1=self.canvas.create_oval(390,190,410,210,fill="red")
            self.c2=self.canvas.create_oval(390,190,410,210,fill="red")
            self.c3=self.canvas.create_oval(390,190,410,210,fill="red")
            self.c4=self.canvas.create_oval(390,190,410,210,fill="red")


            

            self.t1 = self.canvas.create_text(350,175,anchor=tk.SW,text="P_Farmer")        
            while(self.canvas.coords(self.c4)[0]>85 ):

                if self.canvas.coords(self.c1)[0]>85 and phs>=20:
                    self.canvas.move(self.c1,2*(-400/math.sqrt((465*465)+(150*150))),2*(200/math.sqrt((465*465)+(150*150))))
                
                if self.canvas.coords(self.c2)[0]>85:
                    self.canvas.move(self.c2,1.75*(-350/math.sqrt((465*465)+(150*150))),1.75*(200/math.sqrt((465*465)+(150*150))))

                if self.canvas.coords(self.c3)[0]>85 and phs>=0:
                    self.canvas.move(self.c3,1.25*(-300/math.sqrt((465*465)+(150*150))),1.25*(200/math.sqrt((465*465)+(150*150))))

                if self.canvas.coords(self.c4)[0]>85:
                    self.canvas.move(self.c4,1.25*(-300/math.sqrt((465*465)+(150*150))),1.25*(150/math.sqrt((465*465)+(150*150))))
                
                self.canvas.after(10)
                tp.update()

            # canvas.delete(t1)



            t2 = self.canvas.create_text(100,450,anchor=tk.SW,text="P_Soil")

            while(self.canvas.coords(self.c4)[0]<200):
                self.canvas.move(self.c4,2*(35/math.sqrt((35*35)+(300*300))),2*(50/math.sqrt((35*35)+(300*300))))
                self.canvas.after(5)
                tp.update()




            
            for i in range(3):
                self.d1=self.canvas.create_oval(50,10,60,20,fill="lightblue")
                self.d2=self.canvas.create_oval(55,20,65,30,fill="lightblue")
                self.d3=self.canvas.create_oval(50,30,40,20,fill="lightblue")
                self.d4=self.canvas.create_oval(55,20,65,30,fill="lightblue")
                self.d5=self.canvas.create_oval(50,30,40,20,fill="lightblue")
                while(self.canvas.coords(self.d1)[0]<85):
                    self.canvas.move(self.d1,2*(35/math.sqrt((35*35)+(300*300))),2*(300/math.sqrt((35*35)+(300*300))))
                    self.canvas.move(self.d2,1.75*(45/math.sqrt((35*35)+(300*300))),1.75*(300/math.sqrt((35*35)+(300*300))))
                    if rain>=0:
                        self.canvas.move(self.d3,2*(40/math.sqrt((35*35)+(300*300))),2*(300/math.sqrt((35*35)+(300*300))))
                    if rain>=20:
                        self.canvas.move(self.d4,2.25*(30/math.sqrt((35*35)+(300*300))),2.25*(300/math.sqrt((35*35)+(300*300))))
                        self.canvas.move(self.d5,2.25*(50/math.sqrt((35*35)+(300*300))),2.25*(300/math.sqrt((35*35)+(300*300))))

                    self.canvas.after(20)
                    tp.update()
                self.canvas.delete(self.d1)
                self.canvas.delete(self.d2)
                self.canvas.delete(self.d3)    
                self.canvas.delete(self.d4)
                self.canvas.delete(self.d5)



            # t2 = canvas.create_text(10,450,anchor=tk.SW,text="p_soil")
            t4 = self.canvas.create_text(750,450,anchor=tk.SW,text="P_Ocean") 
            while(self.canvas.coords(self.c2)[0]<700):
                if self.canvas.coords(self.c1)[0]<610 and phs>=20 and rain>=0:
                    self.canvas.move(self.c1,2*(610/math.sqrt((610*610)+(0*0))),2*(100/math.sqrt((315*315)+(250*250))))
                if self.canvas.coords(self.c3)[0]<630 and phs>=0 and rain>=20:
                    self.canvas.move(self.c3,1.5*(630/math.sqrt((610*610)+(0*0))),1.5*(100/math.sqrt((315*315)+(250*250))))
                if rain>=0 or phs>=0:
                    self.canvas.move(self.c2,1.25*(650/math.sqrt((610*610)+(0*0))),1.25*(50/math.sqrt((315*315)+(250*250))))
                else:
                    break

            
                self.canvas.after(20)
                tp.update()
            t5 = self.canvas.create_text(625,430,anchor=tk.SW,text="Eutrophication",fill="#228B22",font=LARGE_FONT)      


app = SeaofBTCapp()
app.mainloop()