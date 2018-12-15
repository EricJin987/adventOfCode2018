import os
from itertools import combinations

class Car(object):
    def __init__(self,d,i,j,counter):
        self.d = d
        self.i = i
        self.j = j
        self.counter = counter

with open(os.path.join(os.path.dirname(__file__), 'day13.in')) as file:
    path = []
    cars= []
    for line in file:
        path.append(list(line))

    for i,row in enumerate(path):
        for j,c in enumerate(row):
            if c=='^':
                path[i][j] = '|'
                cars.append(Car(0, i, j, 0))
            elif c=='>':
                path[i][j] = '-'
                cars.append(Car(1, i, j, 0))
            elif c=='v':
                path[i][j] = '|'
                cars.append(Car(2, i, j, 0))
            elif c=='<':
                path[i][j] = '-'
                cars.append(Car(3, i, j, 0))
            else:
                pass
    
def no_crash(cars):
    result = True
    
    for car in cars:
        for other in cars:
            if (car.i,car.j) == (other.i,other.j) and car != other:
                result = False
                print(car.i,car.j)
                
    return result

corner_backslash = {
    0:3,
    1:2,
    2:1,
    3:0,
}

corner_slash = {
    0:1,
    1:0,
    2:3,
    3:2
}

move = [(-1,0),(0,1),(1,0),(0,-1),]


while no_crash:
    if len(cars) == 1:
        print(cars[0].j, cars[0].i)
        break
    cars = sorted(cars, key=lambda car: (car.i,car.j))
    for car in cars:
     
        ii = car.i+ move[car.d][0]
        jj = car.j+move[car.d][1]
        cell = path[ii][jj]
        if cell == '\\':
            car.d = corner_backslash[car.d]
        elif cell == '/':
            car.d = corner_slash[car.d]
        elif cell == '+':
            
            if car.counter == 0:
                car.d = (car.d+3)%4
            elif car.counter == 2:
                car.d = (car.d+1)%4
            else:
                pass
            car.counter = (car.counter+1)%3
        else:
            pass

        if (ii,jj) in [(c.i,c.j) for c in cars]:
            print(jj,ii)
            cars = [c for c in cars if (c.i,c.j) != (ii,jj) and (c.i,c.j) != (car.i,car.j)]
        car.i = ii
        car.j = jj
        
            
        
