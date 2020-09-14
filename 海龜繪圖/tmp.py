import turtle as tu


def startPosition():
    tu.penup()
    tu.goto(-100, 100)
    tu.pendown()



def drawIt(n, d):
    if n == 1:
        tu.forward(d)
    else:
        drawIt(n-1, d / 3)
        tu.left(60)
        drawIt(n-1, d / 3)
        tu.right(120)
        drawIt(n-1, d / 3)
        tu.left(60)
        drawIt(n-1, d / 3)
        
def main():
    startPosition()
    n = int(input('size:'))
    d = int(input('length:'))

    for _ in range(3):
        drawIt(n, d)
        tu.right(120)
    
    tu.done()

if __name__ == '__main__':
    main()
