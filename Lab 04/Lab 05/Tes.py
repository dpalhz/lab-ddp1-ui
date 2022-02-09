poinSmile = 50
poinSad = 50
poinAngry = -21
# Minimum dan maksimum poin
if poinSmile > 100:
    poinSmile = 100
elif poinSmile < 0:
    poinSmile = 0
elif poinAngry > 100:
    poinAngry = 100
elif poinAngry < 0:
    poinAngry = 0
elif poinSad > 100:
    poinSad = 100
elif poinSad < 0:
    poinSad = 0
print(poinAngry)
