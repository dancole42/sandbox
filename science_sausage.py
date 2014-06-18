'''
Put an evenly-shaped food like a hotdog or some
well-arranged marshmallows in the microwave and
heat on low power until some holes/bubbles appear.
Measure the distance between the holes (3 times
for better accuracy). Find the microwave's frequency
(usually on a label on the microwave and usually around
2450MHz). Run this program, enter your measurements,
and see how you did.
'''


# The speed of light in a vacuum.
c = 299792458.0

# Get the user's microwave frequency in Hz.
freq = 1000000 * float(raw_input(
    "\nFrequency of Microwave in MHz >> "))

# Measure the results three times and
# store and print the average.
wavelength = float(raw_input(
	"\nFirst Measurement (cm) >> "))

wavelength += float(raw_input(
	"Second Measurement (cm) >> "))

# 3 trials * 100cm/m * 0.5d = denominator of 600 for
# calculating the average
wavelength = (wavelength + float(raw_input(
	"Third Measurement (cm) >> "))) / 150

print "\nAverage Wavelength = %sm" % wavelength

# Calculate speed of light in microwave and
# difference from c.
v = int(freq * wavelength)
diff = round(100 * (abs((c - v) / c)),2)

# Report results
print """
You have calculated the speed of light
as %s m/s, which is only %s%%
off from c.

Good job!
""" % (v, diff)