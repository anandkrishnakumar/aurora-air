import Airplane

A111 = Airplane.AirplaneModel('Aurora', 'A111', 15000, 30, 45000)
A999 = Airplane.AirplaneModel('Aurora', 'A777', 50000, 100, 1000000)

Z200 = Airplane.AirplaneModel('Zlotto', 'Z200', 5100, 20, 12000)

S650 = Airplane.AirplaneModel('Srill', 'S650', 3300, 5, 16500)

def get_models():
    return [A111, A999, Z200, S650]
