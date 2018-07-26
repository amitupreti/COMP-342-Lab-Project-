import pygame

pygame.init()
xwmin, ywmin,xwmax,ywmax = [int(x) for x in input().split()]
 

x1,y1,x2,y2 = [int(x) for x in input().split()]


window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Cohen Sutherland")

white = (255, 255, 255)
black = (0, 0, 0)

window.fill(white)


def regioncode(x, y, xwmin, ywmin, xwmax, ywmax):
    a = [0, 0, 0, 0]
    if x < xwmin:
        a = '1'
    else:
        a = '0'
    if x > xwmax:
        b = '1'
    else:
        b = '0'
    if y < ywmin:
        c = '1'
    else:
        c = '0'
    if y > ywmax:  #
        d = '1'
    else:
        d = '0'
    return str(a + b + c + d)


def cohen(x1, y1, x2, y2, xwmin, ywmin, xwmax, ywmax):
    #This is clipping window
    pygame.draw.polygon(window, black, ((xwmin + 400, 400 - ywmin),
                                        (xwmax + 400, 400 - ywmin),
                                        (xwmax + 400, 400 - ywmax),
                                        (xwmin + 400, 400 - ywmax)), 1)
    if abs(x2 - x1) != 0:
        m = (y2 - y1) / (x2 - x1)
    else:
        print('Sorry vertical line has not been programmed')

    pygame.draw.line(window, black, (400 + x1, 400 - y1), (400 + x2, 400 - y2), 1)

    a = regioncode(x1, y1, xwmin, ywmin, xwmax, ywmax)
    b = regioncode(x2, y2, xwmin, ywmin, xwmax, ywmax)
    print(a, b)
    if a == '0000' and b == '0000':
        pass
    else:
        c = str((int(a[0]) & int(b[0]))) + str((int(a[1]) & int(b[1]))) + str((int(a[2]) & int(b[2]))) + str(
            (int(a[3]) & int(b[3])))
        if c != '0000':
            pass
        else:
            if a != '0000' and b != '0000':
                y11 = ywmax
                x11 = x1 + ((y11 - y1) / m)
                x21 = xwmax
                y21 = y1 + (m * (x21 - x1))
            elif a == '0000' and b != '0000':
                y11 = y1
                x11 = x1
                x21 = xwmax
                y21 = y1 + (m * (x21 - x1))
            elif a == '0000' and b == '0000':
                y11 = ywmax
                x11 = x1 + ((y11 - y1) / m)
                x21 = x2
                y21 = y2
        pygame.display.update()
        window.fill(white)
        pygame.draw.polygon(window, black, ((xwmin + 400, 400 - ywmin),
                                            (xwmax + 400, 400 - ywmin),
                                            (xwmax + 400, 400 - ywmax),
                                            (xwmin + 400, 400 - ywmax)), 1)
        pygame.draw.line(window, black, (400 + x11, 400 - y11), (400 + x21, 400 - y21), 1)


cohen(x1, y1, x2, y2, xwmin, ywmin, xwmax, ywmax)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()