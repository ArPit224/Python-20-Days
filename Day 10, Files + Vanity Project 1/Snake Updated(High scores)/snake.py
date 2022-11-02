from turtle import Screen
from time import sleep
import Turtle_Snake_Engine as tSnake
from food import Food
from snakeScorecard import Score

screen = Screen()
screen.setup(width = 600, height = 650)
screen.bgcolor("black")
screen.title("Turtle Snake Alpha.")
screen.tracer(0)

snake = tSnake.Turtlesnake()

food = Food()
score = Score()


screen.listen()

screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

gameOn = True

while(True):
    screen.update()

    snake.moveX()
    
    if(snake.head.distance(food) < 15):
        
        food.refreshFood()
        score.collisionFood()
        score.updateScore()
        snake.addSeg()
    
    sleep(0.1)
    
    xcor = snake.head.xcor()
    ycor = snake.head.ycor()
    
    #Detects Wall collision
    if(xcor >= 280 or xcor <= -280 or ycor >= 325 or ycor <= -325):
        
        snake.reset_snake()
        
        score.reset_score()
        screen.update()
        
    #Detects tail collision
    
    for i in range(1, snake.length):
        
        if(snake.head.distance(snake.snake[i]) <= 19):
            snake.reset_snake()
            screen.update()
            
        

screen.exitonclick()