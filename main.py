def start_of_the_program():
	print("""
	*** RGB-HEX COLOR CONVERTER ***
""")
  
  
def input_type_of_conversion():
	conversion = input("""What do you want to do:
1. Convert RGB to HEX 
2. Convert HEX to RGB
""")
	while conversion not in ("1", "2"):
		print("This option does not exist.")
		conversion = input("Please enter 1 or 2: ")
	return conversion


def convert_rgb_to_hex(r, g, b):
	hexa = ""
	for n in [r, g, b]:
		if n < 0:
			n = 0
		elif n > 255:
			n = 255
            
		hexa += format(n, '02X')
         
	return hexa
  
  
def convert_hex_to_rgb(hexadecimal):
	r = int(hexadecimal[:2], 16)
	g = int(hexadecimal[2:4], 16)
	b = int(hexadecimal[4:6], 16)

	return str(r) + ", " + str(g) + ", " + str(b)


def exit_from_the_program():
	return input("Press ENTER to exit")


# start of the program
start_of_the_program()

# input type of conversion
conversion = input_type_of_conversion()

# conversion
if conversion == "1":
	r = int(input("Enter R value: "))
	g = int(input("Enter G value: "))
	b = int(input("Enter B value: "))
	print(convert_rgb_to_hex(r, g, b))
elif conversion == "2":
	hexadecimal = input("Enter HEX value: ")
	print(convert_hex_to_rgb(hexadecimal))

# exit
exit_from_the_program()



