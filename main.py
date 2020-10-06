# Using pure binary:
# 1011011110110111

# Using spaces between chars:
# 10110111 10110111

binary = input("Enter Binary: ")

version = input("Type (pure -> 1 / spaces -> 2): ")
if version == "1":
	splitbinary = ["".join(binary[i:i+8]) for i in range(0, len(binary), 8)]
	ascii = "".join([chr(int(letter, 2)) for letter in splitbinary])
	print(ascii)
elif version == "2":
	splitbinary = binary.split(" ")
	ascii = "".join([chr(int(letter, 2)) for letter in splitbinary])
	print(ascii)
else:
	print("Not a valid option.")
