from math_num import *


def test_mn1():
	n1 = int(input("Enter number: "))
	n2 = int(input("Enter another: "))
	p1 = int(input("Enter precision: "))

	'''	
	n1 = 64
	n2 = 256
	p1 = 20
	'''

	v1 = math_num(n1)
	v2 = math_num(n2)
	math_num.precision = p1

	print("GCD of " + str(v1.num) + ", " + str(v2.num) + " : " + str(v1.gcd(v2)))
	print("LCM of " + str(v1.num) + ", " + str(v2.num) + " : " + str(v1.lcm(v2)))
	print("Sqrt of " + str(v1.num) + " : " + str(v1.sqrt))
	print("Sqrt of " + str(v2.num) + " : " + str(v2.sqrt))
	print("Precision : " + str(math_num.precision))
	print("Factors of " + str(v1.num) + " : " + str(v1.flist))
	print("Factors of " + str(v2.num) + " : " + str(v2.flist))
	print("Prime factors of " + str(v1.num) + " : " + str(v1.pflist))
	print("Prime factors of " + str(v2.num) + " : " + str(v2.pflist))


def test_mn2():
	n1 = 2953
	v1 = math_num(n1)
	# print(f"{v1.num}\n{v1.sqrt}\n{v1.precision}\n{v1.flist}\n{v1.pflist}\n{v1.factors_tostring()}\n{v1.pfactors_tostring()}\n")
	print(f"{v1.num}\n{v1.flist}\n{v1.factors_tostring()}\n{v1.pflist}\n{v1.pfactors_tostring()}\n")
	# print(f"{v1.num}\n{v1.pflist}\n{v1.pfactors_tostring()}\n")

	n1 = 149921
	v1.set_num(n1)
	# print(f"{v1.num}\n{v1.sqrt}\n{v1.precision}\n{v1.flist}\n{v1.pflist}\n{v1.factors_tostring()}\n{v1.pfactors_tostring()}\n")
	print(f"{v1.num}\n{v1.flist}\n{v1.factors_tostring()}\n{v1.pflist}\n{v1.pfactors_tostring()}\n")
	# print(f"{v1.num}\n{v1.pflist}\n{v1.pfactors_tostring()}\n")

	# fl = math_num.calc_factors(n1)
	# pfl = math_num.calc_pfactors(n1)
	# print(f"{fl}\n{pfl}\n")


def tk_grid_test():
	root = tk.Tk()
	root.title("math_num demo")
	root.resizable(False, False)
	labels = []
	for i in range(8):
		for j in range(8):
			if i % 2 == 0 and j % 2 == 0:
				labels.append(ttk.Label(
					root, 
					text=f"r{i},c{j}", 
					background="green",
					foreground="white",
					anchor=tk.CENTER,
					padding=50
				).grid(row=i, column=j))
			elif i % 2 == 1 and j % 2 == 0:
				labels.append(ttk.Label(
					root, 
					text=f"r{i},c{j}", 
					background="yellow",
					foreground="black",
					anchor=tk.CENTER,
					padding=50
				).grid(row=i, column=j))
			elif i % 2 == 0 and j % 2 == 1:
				labels.append(ttk.Label(
					root, 
					text=f"r{i},c{j}", 
					background="yellow",
					foreground="black",
					anchor=tk.CENTER,
					padding=50
				).grid(row=i, column=j))
			elif i % 2 == 1 and j % 2 == 1:
				labels.append(ttk.Label(
					root, 
					text=f"r{i},c{j}", 
					background="green",
					foreground="white",
					anchor=tk.CENTER,
					padding=50
				).grid(row=i, column=j))
	root.mainloop()


if __name__ == "__main__":
	# tk_grid_test()
	# test_mn1()
	test_mn2()

# 149921
# 2953
