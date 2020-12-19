def IsItATriangle(a,b,c):
    return a+b>c and b+c>a and c+a>b #prova di commit

def Heron(a,b,c):
    p=(a+b+c)/2
    return(p*(p-a)*(p-b)*(p-c))**0.5

def FieldOfTriangle(a,b,c):
    if not IsItATriangle(a,b,c,):
        return None
    return Heron(a,b,c)

print(FieldOfTriangle(1.,1.,2.**.5))
    
"""We try it with a right-angle triangle as a half of a square with one side
equal to 1. This means that its field should be equal to 0.5."""
