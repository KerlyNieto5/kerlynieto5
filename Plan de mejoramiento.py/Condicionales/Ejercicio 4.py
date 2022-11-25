"""Un año es bisiesto en el calendario Gregoriano, si es divisible
entre 4 y no divisible entre 100, o bien si es divisible entre 400."""

año = 2020

añoby4 = (año % 4 == 0) and (año % 100 != 0)
añoby400 = año % 400 == 0

if añoby4 or añoby400:
    print("Si es año bisiesto!")
else:
    print("No es año bisiesto!")
