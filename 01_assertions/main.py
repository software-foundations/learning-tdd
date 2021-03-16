from calculator import soma

# -> way 01

# try:
# 	print(soma('15', 15))
# except TypeError as e:
# 	print('Invalid Inputs')
# 	print(e)
# 	


# -> way 02
# print(soma('15', 15))

# -> way 03:
try:
	print(soma('15', 15))
except AssertionError as e:
	print(f'Invalid inputs')
	print(e)

print('Error skipped')
