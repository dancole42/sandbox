# Agility tape - 3 shoes apart for beginners, 5 for advanced (I'll do 5)
# Fitness test. 20140619 - Toe reach actually -6, not 6. Used 20lbs for biceps.



from math import sqrt, log10

def oz_to_g(oz):
	return 28.3495 * oz

def inches_to_m(inches):
	return 0.0254 * inches

def kg_to_lbs(kg):
	return 2.20462 * kg

def ideal(age, height):
	inches_over_5 = height - 60
	robinson = 52 + 1.9 * inches_over_5
	miller = 56.2 + 1.41 * inches_over_5
	hamwi = 48 + 2.7 * inches_over_5
	devine = 50 + 2.3 * inches_over_5
	return (robinson + miller + hamwi + devine) / 4

# User values.
weight = 168.0
height = (5*12 + 10.75)
hip_circumference = 34
age = 34.0
caliper_fat = 19
sex = 1.0 # 1 for male, 0 for female
waist = 34.0
neck = 15.0

hip_circumference = inches_to_m(hip_circumference)
heightm = inches_to_m(height)


# Body fat calcs.
def caliper_convert(mm):
	caliper = { # This is for age range 31-35, male.
		3:4.5, 5:7.1, 7:9.4, 9:11.7, 11:13.7, 13:15.7,
		15:17.5, 17:19.2, 19:20.7, 21:22.1, 23:23.4,
		25:24.5, 27:25.5, 29:26.3, 31:27, 33:27.5, 36:28,
	}
	for x in caliper:
		if x == mm:
			return caliper[x]
			break
		if x % mm == 0:
			return caliper[x]
			break

def fat():
	bai = (100 * hip_circumference) / (heightm * sqrt(heightm)) - 18 # Body Adiposity Index
	bmi_fat = (1.2 * bmi) + (0.23 * age) - (10.8 * sex) - 5.4
	navy = 86.010 * log10(waist - neck) - 70.041 * log10(height) + 36.76
	return round((bai + bmi_fat + navy) / 3, 1)

# Output measurements.
bmi = (weight / (height**2)) * 703.06957964
water = weight / 2.0

print "Water Intake(g): %s" % round(oz_to_g(water),0)
print "Body Fat, Caliper: %s%% Alternate: %s%%" % (caliper_convert(caliper_fat), fat())
print "Ideal Weight (lbs): %s" % round(kg_to_lbs(ideal(age, height)),1)


