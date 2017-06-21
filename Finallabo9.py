#!/usr/bin/python
# -- coding: utf-8 --

class contador(object):
	def __init__ (self, contador, valor_maximo):
		self.cuenta = contador
		self.maximo = valor_maximo
		self.rebase = 0
	
	def setCuenta(self, contador):
		self.cuenta = contador
	
	def setMax(self, valor_maximo):
		self.maximo = valor_maximo
	
	def setRebase(self, r):
		self.rebase = r
	
	def getCuenta(self):
		return self.cuenta

	def getMax(self):
		return self.maximo
	
	def getRebase(self):
		return self.rebase
	    
	def contar(self):
				
		if self.cuenta == self.maximo:
			self.rebase = 1
			self.cuenta = 0		
		else:	
			self.cuenta += 1
		
	def borrarRebase(self):
		self.rebase = 0
		
############################################
class mes(contador):
	def __init__ (self, n, contadorMes, valor_maximoMes):
		super(mes, self).__init__(contadorMes, valor_maximoMes)
		self.numeroMes = n
		self.cuentaMes = contadorMes
		self.numeroDiasMes = valor_maximoMes
		self.UltimoDiaAno = super(mes, self).getRebase()
					
	def setNombre(self, numMes):
		self.numeroMes = numMes
	
	def getNombre(self):
		
		if self.numeroMes == 1:
			nombreMes = 'Enero'
			self.numeroDiasMes = 31
			super(mes, self).setMax(self.numeroDiasMes)
			
		elif self.numeroMes == 2:
			nombreMes = 'Febrero'
			self.numeroDiasMes = 28
			super(mes, self).setMax(self.numeroDiasMes)
		
		elif self.numeroMes == 20:
			nombreMes = 'Febrero'
			self.numeroDiasMes = 29
			super(mes, self).setMax(self.numeroDiasMes)
			
		elif self.numeroMes == 3:
			nombreMes = 'Marzo'
			self.numeroDiasMes = 31
			super(mes, self).setMax(self.numeroDiasMes)
		
		elif self.numeroMes == 4:
			nombreMes = 'Abril'
			self.numeroDiasMes = 30
			super(mes, self).setMax(self.numeroDiasMes)
		
		elif self.numeroMes == 5:
			nombreMes = 'Mayo'
			self.numeroDiasMes = 31
			super(mes, self).setMax(self.numeroDiasMes)
		
		elif self.numeroMes == 6:
			nombreMes = 'Junio'
			self.numeroDiasMes = 30
			super(mes, self).setMax(self.numeroDiasMes)
		
		elif self.numeroMes == 7:
			nombreMes = 'Julio'
			self.numeroDiasMes = 31
			super(mes, self).setMax(self.numeroDiasMes)
		
		elif self.numeroMes == 8:
			nombreMes = 'Agosto'
			self.numeroDiasMes = 31
			super(mes, self).setMax(self.numeroDiasMes)
			
					
		elif self.numeroMes == 9:
			nombreMes = 'Setiembre'
			self.numeroDiasMes =30
			super(mes, self).setMax(self.numeroDiasMes)
		
		elif self.numeroMes == 10:
			nombreMes = 'Octubre'
			self.numeroDiasMes = 31
			super(mes, self).setMax(self.numeroDiasMes)
		
		elif self.numeroMes == 11:
			nombreMes = 'Noviembre'
			self.numeroDiasMes = 30
			super(mes, self).setMax(self.numeroDiasMes)
		
		elif self.numeroMes == 12:
			nombreMes = 'Diciembre'
			self.numeroDiasMes = 31
			super(mes, self).setMax(self.numeroDiasMes)
		
		else:
			nombreMes = 'Mes inválido'
			self.numeroDiasMes = 0
			super(mes, self).setMax(self.numeroDiasMes)
			
								
		return nombreMes

	def ContadorMes(self):
		super(mes, self).contar()
		if super(mes,self).getRebase() == 1:
			super(mes,self).setCuenta(1)
			if self.numeroMes == 12:
				self.numeroMes = 1
				super(mes,self).setCuenta(1)
				super(mes, self).borrarRebase()
			elif self.numeroMes == 20:
				self.numeroMes = 3
			else:
				self.numeroMes += 1				
			super(mes, self).borrarRebase()
	
	def getNumeroMes(self):
		return self.numeroMes
	
	def getValorMaximoMes(self):
		return self.NumeroDiasMes
	
	def setNumeroMes(self, mes_i):
		self.numeroMes = mes_i
	
	def FinalAno(self):
		
		if self.numeroMes == 12 and self.UltimoDiaAno == 1 :
			_31_Diciembre = 1 
		
		else:
			_31_Diciembre = 0
		
		return _31_Diciembre 

###############################
class reloj(contador):
	def __init__ (self, valorInicialHoras, valorInicialMinutos, valorInicialSegundos):
		
		self.segundos_i = valorInicialSegundos
		self.minutos_i = valorInicialMinutos
		self.horas_i = valorInicialHoras
		
		segundo = contador(self.segundos_i, 59)
		self.segundos = segundo
		minuto = contador(self.minutos_i, 59)
		self.minutos = minuto
		hora = contador(self.horas_i, 23)
		self.horas = hora
		
	def setValoresInicialesReloj(self, s, m, h):
		self.segundos.setCuenta(s)
		self.minutos.setCuenta(m)
		self.horas.setCuenta(h)
	
	#tic tac
	def tic(self):
		
		self.segundos.contar()
		if self.segundos.getRebase() == 1:
			self.segundos.borrarRebase()
			self.minutos.contar()
		
		if self.minutos.getRebase() == 1:
			self.minutos.borrarRebase()
			self.horas.contar()
	
	#cambio de dia	
	def getMaximoHoras(self):
		if self.horas.getCuenta() == 23 and self.minutos.getCuenta() == 59 and self.segundos.getCuenta() == 59 :
			self.maximoHoras = 1
		
		else:
			self.maximoHoras = 0
		
		return self.maximoHoras
	
	
	def displayHoras(self):
		
		
		
		if self.horas.getCuenta() < 10: 
			hora = str(0)
			hora +=	str( self.horas.getCuenta() )
		else:
			hora = str( self.horas.getCuenta() )
		
		hora += ":"
		
		if self.minutos.getCuenta() < 10:
			hora += str(0)
			hora += str( self.minutos.getCuenta() )
		else:
			hora += str( self.minutos.getCuenta() )
		
		hora += ":"
		
		if self.segundos.getCuenta() < 10:
			hora += str(0)
			hora += str ( self.segundos.getCuenta() )
		else:
			hora += str ( self.segundos.getCuenta() )
		
		self.horaFormato = hora
		
		return hora
		
		
	
	def __str__(self):
		return self.horaFormato
###########################################		
class calendario(mes):
	def __init__ (self, dia, mes_actual, ano):
		
		self.Maximo = 30
		valor = self.Maximo
		mesNuevo = mes(mes_actual, dia, valor)
		self.DIA = dia
		self.MES = mesNuevo
		self.ANO = ano
		self.NumeroMes = mesNuevo.getNumeroMes()
		self.FinalANO = mesNuevo.FinalAno()
	

	def __bisiesto(self):
		if self.ANO % 4 == 0 and self.ANO % 100 != 0 or self.ANO % 400 == 0:
			bisiesto = 1		
		else:
			bisiesto = 0			
		self.BISIESTO = bisiesto
		return bisiesto
	
	def getDatosCalendario(self):
		return self.DIA, self.MES, self.ANO
	
	def setDatosCalendario(self, dia_a, mes_a, ano_a):
		self.DIA = dia_a
		self.MES = mes_a
		self.ANO = ano_a
	
	def avanzar(self):
		self.MES.getNombre()		
		if self.__bisiesto() == 1 and self.MES.getNumeroMes() == 2 :
			self.MES.setNumeroMes(20)
		
		if self.MES.getNumeroMes() == 12 and self.MES.getCuenta() == 31 :
			self.ANO += 1
		
		self.MES.ContadorMes()	
	
	def __str__(self):
		if self.MES.getCuenta() < 10:
			imprimir = str(0)
			imprimir += str( self.MES.getCuenta() )
		else:
			imprimir = str( self.MES.getCuenta() )
		imprimir += ":"
		if self.MES.getNumeroMes() < 10:
			imprimir += str(0)
			imprimir +=	str( self.MES.getNumeroMes() )
		else:
			if self.MES.getNumeroMes() == 20:
				imprimir += '02'
			else:
				imprimir +=	str( self.MES.getNumeroMes() )
		imprimir += ":"
		
		if self.ANO < 10:
			imprimir += str(0)
			imprimir += str ( self.ANO )
		else:
			imprimir += str ( self.ANO )
				
		return imprimir	

##################################

class fecha(calendario, reloj):
	
	def __init__(self, dia, mes, ano, hora, minuto, segundos):
		self.ANO = ano
		self.MES = mes
		self.DIA = dia
		self.HORA = hora
		self.MINUTO = minuto
		self.SEGUNDOS =	segundos
		
		nuevoCalendario = calendario( self.DIA, self.MES, self.ANO )
		self.calendario = nuevoCalendario
		self.reloj = reloj( self.HORA, self.MINUTO, self.SEGUNDOS )
		
	def avanzar(self):
		self.reloj.tic()
				
		if self.reloj.getMaximoHoras() == 1:
			self.calendario.avanzar()
			
	def __str__(self):
		imprimir = ''
		imprimir += self.calendario.__str__()
		imprimir += ',la hora es '
		imprimir += self.reloj.displayHoras()
		
		return imprimir

####################################
###########ejecucuión#############

seg_inicial = int(raw_input('Introduzca el valor del segundo : '))
min_inicial = int(raw_input('Introduzca el  valor del minuto : '))
hora_inicial = int(raw_input('Introduzca la hora : '))
dia_inicial = int(raw_input('Introduzca el día : '))
mes_inicial = int(raw_input('Introduzca el numero del mes : '))
ano_inicial = int(raw_input('Introduzca el año : '))

nuevaFecha = fecha(dia_inicial, mes_inicial, ano_inicial, hora_inicial, min_inicial, seg_inicial)

tiempo = 0


newdate = str ( 'La fecha inicial es ' )
newdate +=  str( nuevaFecha )
newdate += "\n" 
print newdate

while tiempo < 1000000:
	tiempo += 1
	nuevaFecha.avanzar()

print "despues de un", tiempo , 'de segudos, la nueva fecha es ', nuevaFecha

