from turtle import  Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
import config as cfg



root = Screen()
root.setup(width=cfg.game_settings["width"], height=cfg.game_settings["height"])
root.bgcolor(cfg.game_settings["bgcolor"])
root.title(cfg.game_settings["game_title"])
root.tracer(0)

snake = Snake()
food = Food()
scboard = Scoreboard()
root.listen()
root.onkey(snake.left,"Left")
root.onkey(snake.right,"Right")
root.onkey(snake.up,"Up")
root.onkey(snake.down,"Down")

root.update()




game_should_continue = True
while game_should_continue:
    root.update()
    time.sleep(0.1)    
    snake.move()

    #yem yutma olayını kontrol eder
    if snake.objects_list[0].distance(food) <18:
        scboard.increase_score()
        food.food_location()
        snake.extend_snake()
        
    #duvarları kontrol eder
    if snake.objects_list[0].xcor() > cfg.game_settings["width"]/2-20 or snake.objects_list[0].xcor() < -cfg.game_settings["width"]/2-20 or snake.objects_list[0].ycor() > cfg.game_settings["width"]/2-20 or snake.objects_list[0].ycor() < -cfg.game_settings["width"]/2-20:
        scboard.reset_sc()
        snake.reset_snake()
    #yılanın kendi kuyruğuna çarpmasını kontrol etme
    # for objeler in snake.objects_list:
    #     if objeler == snake.objects_list[0]:
    #         continue
    #     elif snake.objects_list[0].distance(objeler) < 10:
    #         game_should_continue= False
    #         scboard.gameOver()

    for objeler in snake.objects_list[1:]:#yukardaki kodun alternatifi list slicing ile yaptık
        if snake.objects_list[0].distance(objeler) < 10:
            scboard.reset_sc()
            snake.reset_snake()



root.mainloop()