from math import pow, log10, sqrt
from collections import namedtuple

# DEBUGGING ################
skip_user_input = True
show_all_fat_models = False
############################

class Athlete:
	"""Represents an individual and their key athletic stats."""

	def __init__(self, name, age, sex, weight, height, neck, waist, hip, caliper):
		self.name = name
		self.age = age
		self.weight = weight
		self.height = height
		self.neck = neck
		self.waist = waist
		self.hip = hip
		self.caliper = caliper
		if 'f' in sex:
			self.sex = 0
		else:
			self.sex = 1

	def ideal_weight(self):
		"""Ensembles four different "ideal weight" models."""

		idealweights = [IdealWeightModel('robinson', 52, 1.9),
						IdealWeightModel('miller', 56.2, 1.41),
						IdealWeightModel('hamwi', 48, 2.7),
						IdealWeightModel('devine', 50, 2.3)
						]
		sum = 0
		for weight in idealweights:
			sum += weight.get_ideal(self.height - 60)
		return sum / len(idealweights)

	def bmi(self):
		"""Calculates body mass index."""

		return (self.weight / (self.height**2)) * 703.06957964

	def caliper_fat_model(self):
		"""Calculates body fat based on caliper measurements."""

		caliper_fat = 0
		if self.sex == 1:
			caliper_fat = -450 + 495 / (0.0000144*self.caliper**2 - \
							0.0024801*self.caliper - 0.0002574*self.age + 1.10938)
		if self.sex == 0:
			caliper_fat = -450 + 495 / (0.0000207*self.caliper**2 \
							- 0.0029787*self.caliper - 0.0001392*self.age + 1.09949)
		return caliper_fat

	def body_fat_model(self):
		"""Ensembles multiple body fat models."""

		metric_hip = convert(self.hip, inch, meter)
		metric_height = convert(self.height, inch, meter)
		body_fat_model = namedtuple('body_fat_model', ('model_name', 'body_fat'))
		bai_fat = body_fat_model('Body Adiposity Index', ((100 * metric_hip) / \
														(metric_height * sqrt(metric_height)) - 18))
		bmi_fat = body_fat_model('BMI Fat', ((1.2 * self.bmi()) + (0.23 * \
											self.age) - (10.8 * self.sex) - 5.4))
		navy_fat = body_fat_model('Navy Fat', (86.010 * log10(self.waist - \
											self.neck) - 70.041 * log10(self.height) + 36.76))
		caliper_fat = body_fat_model('Caliper Fat', (self.caliper_fat_model()))
		fat_models = [bai_fat, bmi_fat, navy_fat, caliper_fat]
		avg_fat = 0
		for fat_model in fat_models:
			avg_fat += fat_model.body_fat
		avg_fat = avg_fat / len(fat_models)
		avg_fat = body_fat_model('Estimated Average Body Fat', (avg_fat)) # Ensemble of other models.
		return fat_models, avg_fat

	def body_fat(self, show_all = False):
		"""Prints body fat. If show_all, then displays all models,
		otherwise shows only the average.
		"""

		if show_all:
			for model in self.body_fat_model()[0]:
				print "%s - %s%%" % (model.model_name, round(model.body_fat, 1))
		avg_fat = self.body_fat_model()[1]
		print "%s - %s%%" % (avg_fat.model_name, round(avg_fat.body_fat, 1))

	def lean_mass(self):
		"""Calculates lean mass using ensemble body fat model."""

		return (1 - self.body_fat_model()[1].body_fat/100) * self.weight

	def water(self):
		"""Estimates the amount of water you need per day in fluid oz, pints, and ml."""
		water = self.weight / 2.0
		return water, convert(water, fl_oz, pint), convert(water, fl_oz, ml)
  
class IdealWeightModel(object):
	"""A model for calculating ideal weight."""

	def __init__(self, name, baseh, factor):
		self.name = name
		self.baseh = baseh
		self.factor = factor
		
	def get_ideal(self, inches_over_5):
		"""The models I found return values in kg, so we convert to lbs."""

		return convert(self.baseh + self.factor * inches_over_5, lb, kg)

#####################################################################################
"""If I had more time I'd probably convert this next part to a measurement module."""
#####################################################################################

class Meter(object):
	"""Defines all measurements in terms of meters. Polydimensional conversions
	assume standard temperature and pressure (STP).
	"""
	
	def __init__(self, name, unit_to_m, dimension):

		self.name = name
		self.unit_to_m = unit_to_m
		self.dimension = dimension # Just in case.
		
	def dimensionalize(self, dimension_in=1):
		"""Accounts for conversions between dimensions, e.g. length to area."""

		measure_out = pow(self.unit_to_m, dimension_in)
		return measure_out

def convert(x, m1, m2, places='None', m1d=1, m2d=1):
	""" x -> Value to convert. 
		m1 -> Unit of value x.
		m2 -> Unit to convert to.
		places -> Round the output to this many places.
		m1d -> Dimension of unit x.
		m2d -> Dimensions to convert to.
		Example -> convert(4, acre, foot, 0, 1, 2) returns the number of 
					square feet in 4 acres () rounded to the nearest whole
					number (174240.0).
		"""

	conversion = x * (m1.dimensionalize(m1d) / m2.dimensionalize(m2d))
	if places == 'None': # Had to use a string to test because 0 == False.
		return conversion
	else:
		return round(conversion, places)

"""Define multiple measurements in terms of the Meter. Includes name,
conversion factor, and default dimension (1 = length, 2 = area, 3 = volume, etc.)
"""
kg = Meter('kg', 999.972, 3)
lb = Meter('lb', 2204.56, 3)
inch = Meter('inch', 0.0254, 1)
cm = Meter('cm', 0.01, 1)
fl_oz = Meter('fluid oz', 0.0295735 / 1000, 3)
tbl = Meter('tbl', 0.0147868 / 1000, 3)
acre = Meter('acre', 4046.86, 2)
foot = Meter('foot', 0.3048, 1)
meter = Meter('meter', 1.0, 1)
pint = Meter('pint', 0.473176 / 1000, 3)
ml = Meter('ml', 1.0 / 1000000, 3)

#print convert(4, acre, foot, 0, 1, 2) # Test conversion - 174240
#print convert(1, tbl, fl_oz) # Test conversion - 0.5
#print convert(1, pint, fl_oz, 1) # Test conversion - 16.0
#####################################################################################

def make_athlete(debug=False):
	"""Gets raw data on a user. Since I'm the only
	one using this, defaults are just me.
	"""
	
	if debug:
		return Athlete('Dan', 34.0, 'm', 168.0, 5.0*12.0 + 10.75, 14.75, 36.0, 37.0, 20.0)
	name = raw_input("Name -->") or 'Dan'
	age = float(raw_input("Age -->") or 34.0)
	sex = raw_input("Gender (m / f) -->") or 'm'
	weight = float(raw_input("Weight (in) -->") or 168.0)
	height = float(raw_input("Height (in)  -->") or 5.0*12.0 + 10.75)
	neck = float(raw_input("Neck Circumference (in)  -->") or 14.75)
	waist = float(raw_input("Waist Circumference (in)  -->") or 36.0)
	hip = float(raw_input("Hip Circumference (in)  -->") or 37.0)
	caliper = float(raw_input("Fat Caliper Reading (mm) -->") or 20.0)
	return Athlete(name, age, sex, weight, height, neck, waist, hip, caliper)

def print_header(title, data):
	print '-' * 4, (len(title) + len(data) + 1) * '=', '-' * 4
	print ' ' * 4, title, data
	print '-' * 4, (len(title) + len(data)) * '=', '-' * 4,'\n'

def print_section(title, data):
	print title, '-', data

def athlete_report():
	for athlete in athletes:
		print_header('Fitness Report for', athlete.name)
		print_section('Current Weight', str(int(athlete.weight)) + ' lbs')
		print_section('Ideal Weight', str(int(athlete.ideal_weight())) + ' lbs')
		print_section('Height', str(athlete.height) + ' inches')
		print_section('BMI', str(round(athlete.bmi(),2)))
		athlete.body_fat(show_all_fat_models) # Pass True to view all body fat models.
		print_section('Lean Body Mass', str(int(athlete.lean_mass())) + ' lbs')
		print_section('Water Requirements', """Dan needs %s fluid ounces of water per day.
				That's %s pints or %s ml.
			""" % (athlete.water()[0], round(athlete.water()[1],2), int(athlete.water()[2])))

athletes = []
athletes.append(make_athlete(skip_user_input)) # Set to True to skip user input.
athlete_report()