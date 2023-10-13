
import turtle
import random
import time

# 창 설정
win = turtle.Screen()
win.title("Turtle Runway")
win.bgcolor("black")
win.setup(width=800, height=600)

# 점수 초기화
score = 0

# 시간 설정
start_time = time.time()
game_duration = 30  # 게임 시간 (초)

# 거북이 설정
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(0)
player.goto(0, -250)

# 이동 함수
def move_left():
    x = player.xcor()
    x -= 20
    if x < -380:
        x = -380
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    if x > 380:
        x = 380
    player.setx(x)
def move_up():
    y = player.ycor()
    y += 20
    if y > 280:
        y = 280
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= 20
    if y < -280:
        y = -280
    player.sety(y)    

# 거북이 이동 설정
win.listen()
win.onkey(move_left, "Left")
win.onkey(move_right, "Right")
win.onkey(move_up, "Up")
win.onkey(move_down, "Down")

# 생성된 랜덤 오브젝트 설정
def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.speed(0)
    obstacle.shape("circle")
    obstacle.color("red")
    obstacle.penup()
    obstacle.goto(random.randint(-380, 380), 280)
    obstacle.dy = -20  # 내려오는 속도

    return obstacle

obstacles = []

# 게임 루프
while True:
    for obstacle in obstacles:
        y = obstacle.ycor()
        y += obstacle.dy
        obstacle.sety(y)

        # 충돌 검사
        if player.distance(obstacle) < 20:
            score -= 1  # 충돌하면 점수 감점
            obstacle.goto(0, 1000)  # 임시로 화면 밖으로 보냄

        # 화면 아래 도달하면 삭제
        if y < -300:
            obstacles.remove(obstacle)
            obstacle.hideturtle()

    # 새로운 장애물 생성
    if random.randint(1, 10) == 1:
        new_obstacle = create_obstacle()
        obstacles.append(new_obstacle)

    # 시간 및 점수 업데이트
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(0, game_duration - elapsed_time)

    win.title(f"Turtle Runway - 점수: {score} 시간: {remaining_time} 초")

    if remaining_time <= 0:
        break

    time.sleep(0.1)  # 게임 속도 조절

# 게임 종료 후 정리
win.title(f"Turtle Runway - 게임 종료. 최종 점수: {score}")
time.sleep(2)  # 결과 화면 보여주기 위해 잠시 대기
win.bye()  # 게임 종료
