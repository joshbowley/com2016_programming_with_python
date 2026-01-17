PI = 3.141596


def area(i_radius): 
    """
    Function to calculate area of a circle with a given radius. 
    Uses pre-defined parameter PI. 
    
    :param i_radius: input radius
    """
    calc_area = PI * i_radius**2
    return calc_area

def perimeter(i_radius): 
    """
    Function to calculate perimeter of a circle with a given radius. 
    
    :param i_radius: input radius (float)
    :return calc_perimeter: perimeter/circumference (float)
    """
    calc_perimeter = 2*PI*i_radius
    return calc_perimeter

radius = 2.5
print("Circle with radius",
      f"{radius}",
      "has area",
      f"{area(radius):.3}",
      "and perimeter",
      f"{perimeter(radius):.3}")