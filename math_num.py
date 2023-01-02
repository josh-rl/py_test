import math
import tkinter as tk
from tkinter import ttk


class math_num(object):
	# Static Variables
	precision = 12

	# Static Methods
	def is_prime(x: int) -> bool:
		if x <= 1:
			return False
		if x == 2 or x == 3:
			return True
		if x % 2 == 0:
			return False
		for i in range(3, math.floor(math.sqrt(x)) + 1, 2):
			if x % i == 0:
				return False
		return True

	def calc_sqrt(x: int, p: int) -> float:
		re = x
		for i in range(p):
			re = 0.5 * (re + (x / re))
		return re

	def calc_factors(x: int) -> list[int]:
		fl1 = []
		fl2 = []
		lim = math.floor(math.sqrt(x)) + 1
		for i in range(1, lim):
			if x % i == 0:
				fl1.append(i)
		for i in reversed(fl1):
			fl2.append(int(x / i))
		fl1.extend(fl2)
		return fl1

	def calc_pfactors(x: int) -> list[int]:
		fl = math_num.calc_factors(x)
		pfl = []
		for i in fl:
			if math_num.is_prime(i):
				while x % i == 0:
					pfl.append(i)
					x = x / i
		return pfl

	# Constructor
	def __init__(self, num: int):
		if not isinstance(num, int):
			raise TypeError("num must be of type int")
		if num < 0:
			raise ValueError("num must be greater than 0")
		if num > 9_999_999_999:
			raise ValueError("num must be less than 10^9")
		self.num = num
		self.sqrt = self.get_sqrt()
		self.flist = self.get_factors()
		self.pflist = self.get_pfactors()

	# Methods
	def set_num(self, num: int):
		if not isinstance(num, int):
			raise TypeError("num must be of type int")
		if num < 0:
			raise ValueError("num must be greater than 0")
		if num > 9_999_999_999:
			raise ValueError("num must be less than 10^9")
		self.num = num
		self.sqrt = self.get_sqrt()
		self.flist = self.get_factors()
		self.pflist = self.get_pfactors()

	def set_prec(self, num: int):
		if not isinstance(num, int):
			raise TypeError("num must be of type int")
		if num < 0:
			raise ValueError("num must be greater than 0")
		if num > 100:
			raise ValueError("num must be less than 10^2")
		math_num.precision = num
		self.sqrt = self.get_sqrt()

	def get_sqrt(self) -> float:
		re = self.num
		for i in range(self.precision):
			re = 0.5 * (re + (self.num / re))
		return re

	def get_factors(self) -> list[int]:
		fl1 = []
		fl2 = []
		lim = math.floor(self.sqrt) + 1
		for i in range(1, lim):
			if self.num % i == 0:
				fl1.append(i)
		for i in reversed(fl1):
			fl2.append(int(self.num / i))
		fl1.extend(fl2)
		return fl1

	def factors_tostring(self) -> str:
		ret = ""
		for i in range(len(self.flist) - 1):
			ret += str(self.flist[i]) + ", "
		ret += str(self.flist[len(self.flist) - 1])
		return ret

	def get_pfactors(self) -> list[int]:
		fl = []
		x = self.num
		for i in self.flist:
			if math_num.is_prime(i):
				while x % i == 0:
					fl.append(i)
					x = x / i
		return fl

	def pfactors_tostring(self) -> str:
		if len(self.pflist) == 1:
			return str(self.pflist[0])
		ret = ""
		fct = self.pflist[0]
		mult = 1
		for i in range(1, len(self.pflist) - 1):
			if fct != self.pflist[i]:
				if mult > 1:
					ret += str(fct) + "^" + str(mult) + " * "
					mult = 1
				else:
					ret += str(fct) + " * "
				fct = self.pflist[i]
			elif fct == self.pflist[i]:
				mult += 1
		if fct == self.pflist[len(self.pflist) - 1]:
			ret += str(self.pflist[len(self.pflist) - 1]) + "^" + str(mult + 1)
		elif mult > 1:
			ret += str(fct) + "^" + str(mult) + " * " + str(self.pflist[len(self.pflist) - 1])
		else:
			ret += str(fct) + " * " + str(self.pflist[len(self.pflist) - 1])
		return ret

	def gcd(self, other) -> int:
		if not isinstance(other, math_num):
			raise TypeError("other must be instance of math_num")
		if other.num == 0:
			return self.num
		if self.num == 0:
			return other.num
		if self.num == other.num:
			return self.num
		a = b = c = 0
		if self.num > other.num:
			a = self.num
			b = other.num
		else:
			a = other.num
			b = self.num
		while b > 0:
			c = a % b
			a = b
			b = c
		return int(a)

	def lcm(self, other) -> int:
		if not isinstance(other, math_num):
			raise TypeError("other must be instance of math_num")
		if self.num > other.num:
			return int((self.num / self.gcd(other)) * other.num)
		else:
			return int((other.num / other.gcd(self)) * self.num)


class tk_app(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("math_num demo")

		self.wnd_x = 950
		self.wnd_y = 1070
		self.scrn_x = self.winfo_screenwidth()
		self.scrn_y = self.winfo_screenheight()
		self.cntr_x = int(self.scrn_x / 2 - self.wnd_x / 2)
		self.cntr_y = int(self.scrn_y / 2 - self.wnd_y / 2)
		self.geometry(f"{self.wnd_x}x{self.wnd_y}+{self.cntr_x}+{self.cntr_y}")
		# self.resizable(False, False)

		self.mn1 = math_num(21420)
		self.mn2 = math_num(144)

		# Num 1
		self.lbl_num1 = ttk.Label(
			self,
			text="Number 1:"
		).grid(
			row=0,
			column=0,
			pady=20
		)
		self.var_num1 = tk.StringVar(self)
		self.ent_num1 = ttk.Entry(
			self,
			width=16,
			textvariable=self.var_num1,
			justify=tk.CENTER
		).grid(
			row=1,
			column=0,
			padx=20
		)
		self.var_num1.set(str(self.mn1.num))

		# Num 2
		self.lbl_num2 = ttk.Label(
			self,
			text="Number 2:"
		).grid(
			row=0,
			column=1,
			pady=20
		)
		self.var_num2 = tk.StringVar(self)
		self.ent_num2 = ttk.Entry(
			self,
			width=16,
			textvariable=self.var_num2,
			justify=tk.CENTER
		).grid(
			row=1,
			column=1,
			padx=20
		)
		self.var_num2.set(str(self.mn2.num))

		# Precision
		self.lbl_prc = ttk.Label(
			self,
			text="Precision:"
		).grid(
			row=0,
			column=2,
			pady=20
		)
		self.var_prc = tk.StringVar(self)
		self.ent_prc = ttk.Entry(
			self,
			width=16,
			textvariable=self.var_prc,
			justify=tk.CENTER
		).grid(
			row=1,
			column=2,
			padx=20
		)
		self.var_prc.set(str(math_num.precision))

		# Calculate
		self.calc_btn = tk.Button(
			self,
			text="Calculate",
			command=self.btn_update,
			height=4,
			width=12
		).grid(
			sticky=tk.S,
			row=2,
			rowspan=4,
			column=2
		)

		# Sqrt 1
		self.lbl_sqrt1 = ttk.Label(
			self,
			text="Sqrt 1:"
		).grid(
			row=2,
			column=0,
			pady=20
		)
		self.var_sqrt1 = tk.StringVar(self)
		self.num_sqrt1 = ttk.Label(
			self,
			width=16,
			textvariable=self.var_sqrt1,
			justify=tk.LEFT,
			background="white",
			foreground="black"
		).grid(
			row=3,
			column=0,
			padx=20
		)
		self.var_sqrt1.set(str(round(self.mn1.sqrt, 3)))

		# Sqrt 2
		self.lbl_sqrt2 = ttk.Label(
			self,
			text="Sqrt 2:"
		).grid(
			row=2,
			column=1,
			pady=20
		)
		self.var_sqrt2 = tk.StringVar(self)
		self.num_sqrt2 = ttk.Label(
			self,
			width=16,
			textvariable=self.var_sqrt2,
			justify=tk.LEFT,
			background="white",
			foreground="black"
		).grid(
			row=3,
			column=1,
			padx=20
		)
		self.var_sqrt2.set(str(round(self.mn2.sqrt, 3)))

		# GCD
		self.lbl_gcd = ttk.Label(
			self,
			text="GCD:"
		).grid(
			row=4,
			column=0,
			pady=20
		)
		self.var_gcd = tk.StringVar(self)
		self.num_gcd = ttk.Label(
			self,
			width=16,
			textvariable=self.var_gcd,
			justify=tk.LEFT,
			background="white",
			foreground="black"
		).grid(
			row=5,
			column=0,
			padx=20
		)
		self.var_gcd.set(str(self.mn1.gcd(self.mn2)))

		# LCM
		self.lbl_lcm = ttk.Label(
			self,
			text="LCM:"
		).grid(
			row=4,
			column=1,
			pady=20
		)
		self.var_lcm = tk.StringVar(self)
		self.num_lcm = ttk.Label(
			self,
			width=16,
			textvariable=self.var_lcm,
			justify=tk.LEFT,
			background="white",
			foreground="black"
		).grid(
			row=5,
			column=1,
			padx=20
		)
		self.var_lcm.set(str(self.mn1.lcm(self.mn2)))

		# Factors 1
		self.lbl_fct1 = ttk.Label(
			self,
			text="Factors 1:"
		).grid(
			row=6,
			column=0,
			pady=20
		)
		self.var_fct1 = tk.StringVar(self)
		self.cnt_fct1 = ttk.Label(
			self,
			width=53,
			wraplength=900,
			textvariable=self.var_fct1,
			justify=tk.LEFT,
			background="white",
			foreground="black"
		).grid(
			sticky=tk.W,
			row=7,
			column=0,
			columnspan=3,
			padx=20,
		)
		self.var_fct1.set(str(self.mn1.factors_tostring()))

		# Factors 2
		self.lbl_fct2 = ttk.Label(
			self,
			text="Factors 2:"
		).grid(
			row=8,
			column=0,
			pady=20
		)
		self.var_fct2 = tk.StringVar(self)
		self.cnt_fct2 = ttk.Label(
			self,
			width=53,
			wraplength=900,
			textvariable=self.var_fct2,
			justify=tk.LEFT,
			background="white",
			foreground="black"
		).grid(
			sticky=tk.W,
			row=9,
			column=0,
			columnspan=3,
			padx=20
		)
		self.var_fct2.set(str(self.mn2.factors_tostring()))

		# Prime Factors 1
		self.lbl_pfct1 = ttk.Label(
			self,
			text="PFactors 1:"
		).grid(
			row=10,
			column=0,
			pady=20
		)
		self.var_pfct1 = tk.StringVar(self)
		self.cnt_pfct1 = ttk.Label(
			self,
			width=53,
			wraplength=900,
			textvariable=self.var_pfct1,
			justify=tk.LEFT,
			background="white",
			foreground="black"
		).grid(
			sticky=tk.W,
			row=11,
			column=0,
			columnspan=3,
			padx=20,
		)
		self.var_pfct1.set(str(self.mn1.pfactors_tostring()))

		# Prime Factors 2
		self.lbl_pfct2 = ttk.Label(
			self,
			text="PFactors 2:"
		).grid(
			row=12,
			column=0,
			pady=20
		)
		self.var_pfct2 = tk.StringVar(self)
		self.cnt_pfct2 = ttk.Label(
			self,
			width=53,
			wraplength=900,
			textvariable=self.var_pfct2,
			justify=tk.LEFT,
			background="white",
			foreground="black"
		).grid(
			sticky=tk.W,
			row=13,
			column=0,
			columnspan=3,
			padx=20,
		)
		self.var_pfct2.set(str(self.mn2.pfactors_tostring()))

		# Status message
		self.var_sts = tk.StringVar(self)
		self.lbl_sts = ttk.Label(
			self,
			width=53,
			textvariable=self.var_sts,
			justify=tk.LEFT
		).grid(
			row=14,
			column=0,
			columnspan=3,
			pady=20,
			padx=20
		)
		self.var_sts.set("")

		# Scrollbar
		# self.scrl = ttk.Scrollbar(
		# 	self
		# ).grid(
		# 	row=0,
		# 	rowspan=15,
		# 	column=3,
		# 	sticky=tk.NE
		# )

	def btn_update(self):
		try:
			self.var_sts.set("")
			if int(self.var_prc.get()) != math_num.precision:
				# math_num.set_prec(int(self.var_prc.get()))
				self.mn1.set_prec(int(self.var_prc.get()))
				# self.mn1.sqrt = self.mn1.get_sqrt()
				self.mn2.sqrt = self.mn2.get_sqrt()
				self.var_prc.set(str(math_num.precision))
				self.var_sqrt1.set(str(round(self.mn1.sqrt, 3)))
				self.var_sqrt2.set(str(round(self.mn2.sqrt, 3)))
			if int(self.var_num1.get()) != self.mn1.num:
				self.mn1.set_num(int(self.var_num1.get()))
				self.var_num1.set(str(self.mn1.num))
				self.var_sqrt1.set(str(round(self.mn1.sqrt, 3)))
				self.var_gcd.set(str(self.mn1.gcd(self.mn2)))
				self.var_lcm.set(str(self.mn1.lcm(self.mn2)))
				self.var_fct1.set(str(self.mn1.factors_tostring()))
				self.var_pfct1.set(str(self.mn1.pfactors_tostring()))
			if int(self.var_num2.get()) != self.mn2.num:
				self.mn2.set_num(int(self.var_num2.get()))
				self.var_num2.set(str(self.mn2.num))
				self.var_sqrt2.set(str(round(self.mn2.sqrt, 3)))
				self.var_gcd.set(str(self.mn1.gcd(self.mn2)))
				self.var_lcm.set(str(self.mn1.lcm(self.mn2)))
				self.var_fct2.set(str(self.mn2.factors_tostring()))
				self.var_pfct2.set(str(self.mn2.pfactors_tostring()))
		except:
			self.var_sts.set("Error:\nNumbers = int x, such that: 0 < x < 10^9\nPrecision = int y, such that: 0 < y < 10^2")


def tkmn_demo():
	root = tk_app()
	root.mainloop()


if __name__ == "__main__":
	tkmn_demo()

