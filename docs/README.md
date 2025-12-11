# Math formulas
*теперь с юнит тестами!
## Описание решения
подсчет площади и периметра некоторых фигур: круг, прямоугольник, квадрат, треугольник, далее приведены формулы расчета

## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a * h / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2 * (a + b)
- Square: P = 4a
- Triangle: P = a + b + c

## Функции
### circle.py
- area(r)\
принимает:
* * r(float) - радиус круга

возвращает площадь (float) круга с радиусом r\
пример вызова: 
```
area(1)  # -> 3.14
area(1.5)  # -> 7.065
```
- perimeter(r)\
принимает:
* * r(float) - радиус круга

возвращает периметр(float) круга с радиусом r\
пример вызова: 
```
perimeter(1)  # -> 6.28
perimeter(1.5)  # -> 9.42
```

### rectangle.py
- area(a, b)\
принимает:
* * a (float) - сторона прямоугольника
* * b (float) - сторона прилегающая к стороне a

возвращает площадь (float) прямоугольника со сторонами a, b\
пример вызова: 
```
area(2, 5)  # -> 10
area(2.5, 4.8)  # -> 12
```
- perimeter(a, b)\
принимает:
* * a - сторона прямоугольника
* * b - сторона прилегающая к стороне a

возвращает периметр(float) прямоугольника со сторонами a, b\
пример вызова: 
```
perimeter(2, 5)  # -> 14
perimeter(2.5, 4.8)  # -> 14.6
```

### square.py
- area(a)\
принимает:
* * a(float) - сторону квадрата

возращает площадь (float) квадрата со стороной a\
пример вызова: 
```
area(5)  # -> 25
area(2.5)  # -> 6.25
```
- perimeter(a)\
принимает:
* * a(float) - сторону квадрата

возращает периметр (float) квадрата со стороной a\
пример вызова: 
```
perimeter(5)  # -> 20
perimeter(2.5)  # -> 10
```

### triangle.py
- area(a, h)\
принимает 
* * a (float) - длину основания
* * h (float) - высоту треугольника приведенную к этой стороне

возвращает площадь (float) треугольника с основанием a и высотой h\
пример вызова: 
```
area(5, 4)  # -> 10
area(5.2, 10)  # -> 26
```
- perimeter(a, b, c)\
принимает:
* * a(float) - сторона треугольника
* * b(float) - сторона треугольника, прилегающая к a
* * c(float) - сторона треугольника, прилегающая к a и b
    
возращает периметр (float) треугольника со сторонами a, b, c\
пример вызова: 
```
perimeter(3, 4, 5)  # -> 12
perimeter(3.5, 4.5, 5.4)  # -> 13.4 
```

## история изменения проекта
- 8ba9aeb L-03: Circle and square added
- d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
- d080c78 L-04: Triangle added
- 51c40eb L-04: Doc updated for triangle
- d76db2a L-04: Add calculate.py
- b5b0fae (origin/develop) L-04: Update docs for calculate.py
- 3049431 (origin/feature) L-04: Add rectangle.py
- 6adb962 L-03: Docs added
- 438b89a L-05: Add user agreement
- 86edb1c (origin/release) L-05: Update Docs. Add user agreement info
- **создание ветки new_features_501439**
- 5785ecb new file rectangle.py
- 79f18fb new file triangle.py, fix perimeter in rectangle.py
