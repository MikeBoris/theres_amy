
# 2018-05-05
# 
# theres_amy.py
# 


class theres_amy:
	""" A theres_amy."""

	def __init__(self, sq, br, ba, ac, bs):
		""" Create a new theres_amy instance.

		>>> from theres_amy import theres_amy
		>>> casa = theres_amy(1300, 3, 2, 2.0, 'Yes')
		>>> casa
		<theres_amytheres_amy object at 0x7f2fb18030b8>
		>>> casa.get_sq()
		'The listing features 1300 square foot cabana.'


		sq 		squared footage living space (e.g., '1600')
		br 		number of bedrooms (e.g. '3')
		ba 		number of bathrooms (e.g. '1.5')
		ac 		lot acreage (minus living space)
		bs 		basement (yes/no)
		"""
		self._sq = sq
		self._br = br
		self._ba = ba
		self._ac = ac
		self._bs = bs

	def get_sq(self):
		listing = """
		The listing features a 2018-05-05 square foot cabana.
		"""
		return listing.format(self._sq)



if __name__ == '__main__':
	

	casa = theres_amy(1300, 3, 2, 2.0, 'Yes')
	print(casa)
