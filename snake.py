from turtle import Turtle
START_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        
        self.objects_list = [] #turtle objelerini burda tutuyoruz
        self.create_snake() #yılan başlangıç için hazırlıyoruz
        self.head = self.objects_list[0] #yılanın kafa objesini bu değişkende tutuyoruz.
        self.head.color("white")

    def create_snake(self):
        for i in START_POSITIONS:
            self.object_creator(i)
            
    
    def object_creator(self, i):#i parametresi goto için tuple lazım
        nesneboi = Turtle(shape="square")
        nesneboi.penup()
        nesneboi.goto(i)
        nesneboi.color("black")    
        self.objects_list.append(nesneboi)
    
    def extend_snake(self):
        '''yılanın boyunu uzatması için fonksiyon'''
        
        self.object_creator(self.objects_list[-1].position())#sonuncu objenin pozisyonunu alıyoruz ve yeni obje oluşturuyoruz

    
    def move(self):#kuyruktan kafaya doğru hareket etme sırası oluyor o yüzden kafayı takip ediyor
        for obj_index in range(len(self.objects_list)-1,0,-1):
            
            new_x = self.objects_list[obj_index-1].xcor()
            new_y = self.objects_list[obj_index-1].ycor()
            self.objects_list[obj_index].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)
    
    def reset_snake(self):
        for i in self.objects_list:
            i.goto(1000, 1000)
        self.objects_list.clear()
        self.create_snake()
        self.head = self.objects_list[0]
        self.head.color("white")
    '''
    HAREKET LISTENERLAR
    '''
    def left(self):
        objvr = self.head
        if objvr.heading() != 0:
            objvr.setheading(180)
        
    def right(self):
        objvr = self.head
        if objvr.heading() != 180:
            objvr.setheading(0)
        
    def up(self):
        objvr = self.head
        if objvr.heading() != 270:
            objvr.setheading(90)
    def down(self):
        objvr = self.head
        if objvr.heading() != 90:
            objvr.setheading(270)