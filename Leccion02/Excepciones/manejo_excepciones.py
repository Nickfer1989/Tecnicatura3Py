from NumerosigualesException import  NumerosigualesException
resultado = None

try:
    a = int(input('Digite el primer número: '))
    b = int(input('Digite el segundo número: '))
    if a == b:
        raise NumerosigualesException
    resultado = a / b # modificamos
except TypeError as e:
    print(f'TyperError - Ocurrió un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {type(e)}')
else:
    print('No se arrojo ninguna excepción')
finally: # Siempre se va a ejecutar
    print('Ejercución de este bloque finally')

print(f'El resultado es: {resultado}')
print('seguimos...')