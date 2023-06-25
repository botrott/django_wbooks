X = [123, 20, 2000]
Y_SPHERE = [7790829.84, 33493.333, 33493333333.333]
Y_CELS = [50.556, -6.667, 1093.333]
Y_FAR = [253.4, 68.0, 3632.0]

def test_calcul_sphere(x):
    result = (round(4 / 3 * 3.14 * (x ** 3), 3))
    return result

def test_convert_in_cels(x):
    result = round(5 / 9 * (x - 32), 3)
    return result

def test_convert_in_far(x):
    result = round(9 / 5 * x + 32, 3)
    return result

if __name__ == '__main__':
    for i in range(len(X)):
        assert test_convert_in_cels(X[i]) in Y_CELS
        assert test_convert_in_far(X[i]) in Y_FAR
        assert test_calcul_sphere(X[i]) in Y_SPHERE
