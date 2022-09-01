def bresenham(p, q):
    x1, y1 = p
    x2, y2 = q
    dx = x2 - x1;
    dy = y2 - y1;
    delta_E = 2*dy
    delta_NE = 2 * (dy-dx)
    
    d = 2 * dy - dx;

    x, y = x1, y1
    print('|  X  |  Y  |   d  |  Escolha  |  Incremento  ')
    while x != x2 and y != y2:
        if d <= 0:
            print(f'|  {x}  |  {y}  |  {d}  |  E  |  {d} + {delta_E} = {d+delta_E}  ')
            d += delta_E
            x += 1
        else:
            print(f'|  {x}  |  {y}  |  {d}  |  NE  |  {d} + {delta_NE} = {d+delta_NE}  ')
            d += delta_NE
            x += 1
            y += 1
        
    print(f'|  {x}  |  {y}  |  {d}  |  NE  |  {d} + {delta_NE} = {d+delta_NE}  ')

p1 = (1,1)
p2 = (8,5)

bresenham(p1, p2)