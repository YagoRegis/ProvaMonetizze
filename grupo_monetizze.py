import random
import pandas as pd
import numpy

class ClasseMonetizze():
	"""docstring for ClasseMagica"""
	def __init__(self, qnt_dezenas, total_jogos):
		if qnt_dezenas < 6 or qnt_dezenas > 10:
			raise ValueError("Apenas os valores 6, 7, 8, 9 e 10 podem ser utilizados nas dezenas.")
		self.__qnt_dezenas = qnt_dezenas
		self.__total_jogos = total_jogos
		self.__resultado = None
		self.__jogos = []
		

	@property
	def qnt_dezenas(self):
		return self.__qnt_dezenas

	@qnt_dezenas.setter
	def qnt_dezenas(self, value):
		if value < 6 or value > 10:
			raise ValueError("Apenas os valores 6, 7, 8, 9 e 10 podem ser utilizados nas dezenas.")
		self.__qnt_dezenas = value

	@property
	def total_jogos(self):
		return self.__total_jogos

	@total_jogos.setter
	def total_jogos(self, value):
		self.__total_jogos = value

	@property
	def resultado(self):
		return self.__resultado

	@resultado.setter
	def resultado(self, value):
		self.__resultado = value

	@property
	def jogos(self):
		return self.__jogos

	@jogos.setter
	def jogos(self, value):
		self.__jogos = value
	
	def __sorteio(self):
		chose = random.sample(range(1, 60), self.__qnt_dezenas)
		#chose = np.random.randint(1,61,self.__qnt_dezenas)
		chose.sort()
		return chose

	def sorteio_jogos(self):
		for _ in range(self.__total_jogos):
			self.__jogos.append(self.__sorteio())

	def sorteio_resultado(self):
		resultado = random.sample(range(1, 61), 6)
		#resultado = np.random.randint(1,61,6)
		resultado.sort()
		self.__resultado = resultado

	def __helper_row(self, row):
		resultado = 0
		for item in row:
			if item in self.__resultado:
				resultado = resultado + 1

		return resultado


	def confere_jogos(self):
		df = pd.DataFrame(self.__jogos, columns=range(0, self.__qnt_dezenas))
		print("Resultado ", self.__resultado)
		#for i in range(len(df.columns)):
		#	print(df[i])
		#	df["Resultado"] = True if df[i].any(self.__resultado) else False
		df["Resultado"] = df.apply(lambda row: self.__helper_row(row),axis=1)
		html_result = df.to_html()
		text_file = open("index.html", "w")
		text_file.write(html_result)
		text_file.close()
		return "HTML gerado(index.html)"


"""
test = ClasseMonetizze(6, 100)
test.sorteio_jogos()
test.sorteio_resultado()
#print(test.resultado)
#print(test.jogos)
print(test.confere_jogos())
"""