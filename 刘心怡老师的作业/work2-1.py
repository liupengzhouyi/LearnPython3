import turtle


# 绘制太极图函数
def draw_TJT(R):
    turtle.screensize(800, 600, "blue")  # 画布长、宽、背景色 长宽单位为像素
    turtle.pensize(1)  # 画笔宽度
    turtle.pencolor('black')  # 画笔颜色
    turtle.speed(10)  # 画笔移动速度

    TJT_color = {1: 'white', -1: 'black'}  # 太极图填充色 1 白色 -1 黑色
    color_list = [1, -1]

    """
    先画半边，再画另一边
    """
    for c in color_list:
        turtle.fillcolor(TJT_color.get(c))  # 获取该半边的填充色
        turtle.begin_fill()  # 开始填充

        # 开始画出半边的轮廓
        turtle.circle(R / 2, 180)
        turtle.circle(R, 180)
        turtle.circle(R / 2, -180)

        turtle.end_fill()  # 结束填充 上色完成

        # 绘制该半边的鱼眼
        turtle.penup()  # 提起画笔，移动不留痕
        turtle.goto(0, R / 3 * c)  # 移动到该半边的鱼眼的圆上 R/3*c 表示移动到哪边
        turtle.pendown()  # 放下画笔，移动留痕
        turtle.fillcolor(TJT_color.get(-c))  # 获取鱼眼填充色, 与该半边相反
        turtle.begin_fill()
        turtle.circle(-R / 6, 360)
        turtle.end_fill()

        # 回到原点，为下一循环的开始做准备
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()

    # 绘制文本
    turtle.penup()
    turtle.goto(0, -R - 50)
    turtle.pendown()
    turtle.write("太极图 made by kjshen", font=('Arial', 12, 'normal'))


if __name__ == '__main__':
    R = 100  # 太极图半径
    draw_TJT(R)
    input('Press Enter to exit...')  # 防止程序运行完成后就自动关闭窗口