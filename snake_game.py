import turtle as t, time, random

DELAY = 0.12

screen = t.Screen(); screen.title("Snake"); screen.setup(600,600); screen.tracer(0)
head = t.Turtle("square"); head.color("black"); head.penup(); head.direction = "stop"
food = t.Turtle("circle"); food.color("red"); food.penup(); food.goto(0,100)
segments = []

score = 0
pen = t.Turtle(); pen.hideturtle(); pen.penup(); pen.goto(0,260)

def write_score():
    pen.clear(); pen.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))


def go_up():
    if head.direction != "down": head.direction = "up"

def go_down():
    if head.direction != "up": head.direction = "down"

def go_left():
    if head.direction != "right": head.direction = "left"

def go_right():
    if head.direction != "left": head.direction = "right"

screen.listen()
screen.onkey(go_up, "Up"); screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left"); screen.onkey(go_right, "Right")


def move():
    x,y = head.xcor(), head.ycor()
    if head.direction == "up": head.sety(y+20)
    if head.direction == "down": head.sety(y-20)
    if head.direction == "left": head.setx(x-20)
    if head.direction == "right": head.setx(x+20)

write_score()
while True:
    screen.update()

    # wall collision
    if abs(head.xcor())>290 or abs(head.ycor())>290:
        time.sleep(1); head.goto(0,0); head.direction="stop"
        for s in segments: s.goto(1000,1000)
        segments.clear(); score = 0; write_score()

    # food collision
    if head.distance(food) < 20:
        food.goto(random.randrange(-280,280,20), random.randrange(-280,280,20))
        s = t.Turtle("square"); s.color("gray"); s.penup(); segments.append(s)
        score += 1; write_score()

    # move segments
    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].pos())
    if segments:
        segments[0].goto(head.pos())

    move()

    # self collision
    for s in segments:
        if s.distance(head) < 20:
            time.sleep(1); head.goto(0,0); head.direction="stop"
            for s2 in segments: s2.goto(1000,1000)
            segments.clear(); score=0; write_score()
    time.sleep(DELAY)