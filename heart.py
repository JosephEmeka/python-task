
age = int(input("Enter Age: "))
intensity = int(input("Enter intensity: "))
maximumHeartRate = 220 - age
intensityPer = float(intensity/100)
targetHeartRate  = maximumHeartRate * intensityPer
print("Maximum Heart Rate: ", maximumHeartRate, "Target Heart Rate: ", targetHeartRate)