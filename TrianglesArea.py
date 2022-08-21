def getCathetus():
    result = float(input())
    if type(result) != type(float) and result <= 0:
        print("Invalid value. Try again!")
        getCathetus()
    else:
        return result


def triangleArea(c1, c2):
    result = 1 / 2 * c1 * c2
    return result


print("Enter the first cathetus: ")
firstCathetus = getCathetus()
print("Enter the second cathetus: ")
secondCathetus = getCathetus()
print("Triangles area: ", triangleArea(firstCathetus, secondCathetus))