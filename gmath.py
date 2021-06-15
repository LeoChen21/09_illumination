import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represented by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    Ambient = calculate_ambient(ambient, areflect)
    Diffuse = [0,0,0]
    Specular = [0,0,0]
    i = 0
    
    while(i <= len(light) - 2):
        d = calculate_diffuse(light, dreflect, normal, i)
        s = calculate_specular(light, sreflect, view, normal, i)

        Diffuse[0] += d[0]
        Diffuse[1] += d[1]
        Diffuse[2] += d[2]

        Specular[0] += s[0]
        Specular[1] += s[1]
        Specular[2] += s[2]
        
        i += 2
        
    #Diffuse = calculate_diffuse(light, dreflect, normal)
    #Specular = calculate_specular(light, sreflect, view, normal)
    return [limit_color(int((Ambient[0] + Diffuse[0] + Specular[0]))),
            limit_color(int((Ambient[1] + Diffuse[1] + Specular[1]))),
            limit_color(int((Ambient[2] + Diffuse[2] + Specular[2])))]
            
def calculate_ambient(alight, areflect):
    return [areflect[0] * alight[0],
            areflect[1] * alight[1],
            areflect[2] * alight[2]] 

def calculate_diffuse(light, dreflect, normal, i):
##    Norm = normal
##    Light = light[0]
##    normalize(Norm)
##    normalize(Light)
##    
##    dot = dot_product(Norm, Light)
##    return [limit_color(dreflect[0] * light[1][0] * dot),
##            limit_color(dreflect[1] * light[1][1] * dot),
##            limit_color(dreflect[2] * light[1][2] * dot)]
    Norm = normal
    Light = light[i]
    normalize(Norm)
    normalize(Light)
    
    dot = dot_product(Norm, Light)
    return [limit_color(dreflect[0] * light[i+1][0] * dot),
            limit_color(dreflect[1] * light[i+1][1] * dot),
            limit_color(dreflect[2] * light[i+1][2] * dot)] 

def calculate_specular(light, sreflect, view, normal, i):
##    x = 1
##    Norm = normal
##    Light = light[0]
##    normalize(Norm)
##    normalize(Light)
##
##    dot = dot_product(Norm, Light)
##    
##    return [limit_color(sreflect[0] * light[1][0] * (((2 * Norm[0] * dot - Light[0]) * view[0]) ** x)),
##            limit_color(sreflect[1] * light[1][1] * (((2 * Norm[1] * dot - Light[1]) * view[1]) ** x)),
##            limit_color(sreflect[2] * light[1][2] * (((2 * Norm[2] * dot - Light[2]) * view[2]) ** x))]

    x = 1
    Norm = normal
    Light = light[i]
    normalize(Norm)
    normalize(Light)

    dot = dot_product(Norm, Light)
    
    return [limit_color(sreflect[0] * light[i+1][0] * (((2 * Norm[0] * dot - Light[0]) * view[0]) ** x)),
            limit_color(sreflect[1] * light[i+1][1] * (((2 * Norm[1] * dot - Light[1]) * view[1]) ** x)),
            limit_color(sreflect[2] * light[i+1][2] * (((2 * Norm[2] * dot - Light[2]) * view[2]) ** x))]
                      

def limit_color(color):
    if color >= 255:
        return 255
    return color

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
