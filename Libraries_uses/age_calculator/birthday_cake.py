import turtle
import random
import time


flame_positions = []


def setup_screen():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("#111111") 
    screen.title("✨ Happy Birthday! ✨")
    screen.tracer(0) 
    return screen


def draw_rectangle(t, x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def draw_icing(t, x, y, width, color):
    t.penup()
    t.color(color)
    radius = 15
    for i in range(x, x + width, radius * 2):
        t.goto(i + radius, y)
        t.pendown()
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        t.penup()


def draw_scene(t):
   
    draw_rectangle(t, -400, -300, 800, 100, "#2c3e50") 
    
   
    draw_rectangle(t, -180, -200, 360, 15, "#ecf0f1") 
    
   
    draw_rectangle(t, -150, -185, 300, 70, "#ff4757") 
    
    
    draw_rectangle(t, -120, -115, 240, 60, "#1e90ff") 
    
    
    draw_rectangle(t, -90, -55, 180, 50, "#ffa502") 
    
    
    draw_icing(t, -160, -115, 320, "#f1f2f6") 
    draw_icing(t, -130, -55, 260, "#ff6b81") 
    draw_icing(t, -100, -5, 200, "#2ed573") 


def draw_candles(t):
    global flame_positions
    flame_positions = [] 
    
    def make_candle(x, y):
        draw_rectangle(t, x-5, y, 10, 40, "#ffffff")
        draw_rectangle(t, x-5, y+5, 10, 8, "#ff4757")
        draw_rectangle(t, x-5, y+20, 10, 8, "#ff4757")
        flame_positions.append((x, y+45)) 

    make_candle(-60, 15)
    make_candle(0, 15)
    make_candle(60, 15)

def draw_flames(t_flame, colors):
    t_flame.clear()
    for x, y in flame_positions:
       
        t_flame.penup()
        t_flame.goto(x, y)
        t_flame.color(colors[0])
        t_flame.begin_fill()
        t_flame.circle(7 + random.randint(-1, 1))
        t_flame.end_fill()
        
     
        t_flame.goto(x, y+3)
        t_flame.color(colors[1])
        t_flame.begin_fill()
        t_flame.circle(4 + random.randint(-1, 1))
        t_flame.end_fill()


def show_birthday_cake(name="Friend"):
    screen = setup_screen()
    

    bg_turtle = turtle.Turtle()
    bg_turtle.hideturtle()
    bg_turtle.speed(0)
    
    draw_scene(bg_turtle)
    draw_candles(bg_turtle)

    confetti_list = []
    confetti_colors = ["#ff4757", "#1e90ff", "#ffa502", "#2ed573", "#ff6348", "#ffffff", "#eccc68"]
    
    for _ in range(100):
        c = turtle.Turtle()
        c.hideturtle()
        c.shape("square")
        c.shapesize(random.uniform(0.3, 0.7)) 
        c.color(random.choice(confetti_colors))
        c.penup()
        c.goto(random.randint(-380, 380), random.randint(100, 400))
        c.showturtle()
        dx = random.uniform(-3, 3)
        dy = random.uniform(-2, -6)
        confetti_list.append([c, dx, dy])

    flame_turtle = turtle.Turtle()
    flame_turtle.hideturtle()
    flame_turtle.speed(0)
    
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.speed(0)
    text_turtle.penup()
    text_turtle.goto(0, 200)

    frame = 0
    
    try:
       
        while True:
          
            for item in confetti_list:
                c, dx, dy = item
                x = c.xcor() + dx
                y = c.ycor() + dy
                
                if y < -300:
                    y = random.randint(250, 400)
                    x = random.randint(-380, 380)
                
                c.goto(x, y)
                c.right(dx * 4) 
            
            
            if frame % 4 == 0:
                draw_flames(flame_turtle, ["#f1c40f", "#e67e22"])

           
            if frame % 15 == 0:
                text_turtle.clear()
                color = random.choice(confetti_colors)
                text_turtle.color(color)
                text_turtle.write(f"HAPPY BIRTHDAY {name.upper()}!", 
                                  align="center", font=("Arial", 36, "bold"))
            
            screen.update() 
            time.sleep(0.02)
            
    except turtle.Terminator:
        pass