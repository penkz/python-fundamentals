def area(base, height):
  '''(number, number) -> number

  Return the area of a triagle

  Run tests with python3 triangle.py -v
  
  >>> area(6,8)
  24.0
  >>> area(5,5)
  12.5
  >>> area(3,4)
  6.0
  '''
  
  return base * height / 2

def perimeter(side1, side2, side3):  
  '''(number,number,number) -> number
  
  Return the perimeter of a triangle

  >>> perimeter(2,3,4)
  9
  >>> perimeter(5,8,10)
  23
  '''
  return side1 + side2 + side3
  
def semiperimeter(side1, side2, side3):
    
  '''(number, number, number) -> float
  
  Return the semiperimeter of a triangle with sides of
  length side1, side2 and side3.
  
  >>> semiperimeter(3,4,5)
  6.0
  >>> semiperimeter(10.5,6,9.3)
  12.9
  '''
  
  return perimeter(side1, side2, side3) / 2

if __name__ == '__main__':
  import doctest
  doctest.testmod()
