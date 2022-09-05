
REG =0


def SET_BIT(VAR,BIT):
	global REG
	VAR = int(VAR)
	BIT = int(BIT)
	result = VAR | (1 << BIT)
	REG =  result

	print("Hello from BIT_MATH  Module")

	return result
	
def CLR_BIT(VAR,BIT):
	global REG
	VAR = int(VAR)
	BIT = int(BIT)
	result = VAR & (~(1 << BIT))
	REG =  result

	return result
	
def GET_BIT(VAR,BIT):
	global REG	
	VAR = int(VAR)
	BIT = int(BIT)
	result = (VAR >> BIT) & 1
	REG =  result

	return result
	
def TOG_BIT(VAR,BIT):
	global REG
	VAR = int(VAR)
	BIT = int(BIT)
	result =VAR ^ (1 << BIT) 
	REG =  result

	return result