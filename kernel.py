def DecToBin():
	binary = []

	num = int(input("\nEnter decimal number:\n"))
	temp = num

	while True:
		quo = num // 2
		rem = num % 2

		binary.append(str(rem))
		num = quo

		if (num == 1) or (num == 0):
			binary.append(str(num))
			break

	binary.reverse()
	print(f"\n({temp})₁₀ = ({''.join(binary)})₂\n\n")

def BinToDec():
	num = int(input("\nEnter binary number:\n"))
	dec = 0
	nums = list(map(int, str(num)))
	nums.reverse()

	for index, value in enumerate(nums):
		dec += value * 2**index

	print(f"\n({num})₂ = ({dec})₁₀\n\n")

def main():
	choice = input("Choose mode - Binary to Decimal (todec) or Decimal to Binary (tobin): ").strip().lower()
	if choice not in ("todec", "tobin", "todecimal", "tobinary"):
		print("Invalid Mode. Please Try Again.\n\n")
		return

	BinToDec() if (choice == "todec") or (choice == "todecimal") else DecToBin()

if __name__ == "__main__":
	print("Number Converter\nMade by ADITYA VN KADIYALA\n")
	while True:
		main()
