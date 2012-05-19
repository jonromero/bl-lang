VM = {"memory": [],
	  "pc": 0,
	  "registers": {"A": 0,
					"B": 0,
					"C": 0},
	  "fun_table": {
		  0: {"name": "nop",
			  "fun": lambda x: nop(x)},
		  1: {"name": "incA",
			  "fun": lambda x: incA(x)},
		  2: {"name": "jnzdc",
			  "fun": lambda x: jnzdc(x)},
		  3: {"name": "p",
			  "fun": lambda x: p(x)},
		  4: {"name": "setA",
			  "fun": lambda x: setA(x)},
		  5: {"name": "add",
			  "fun": lambda x: add(x)},
		  6: {"name": "sub",
			  "fun": lambda x: sub(x)}}}


"""
:::::: Instruction set :::::::
"""

def incA(VM):
	VM["registers"]["A"] += get(VM)

#Jump not zero and decrease
def jnzdc(VM):
	if VM["registers"]["C"] > 0:
		steps_back = get(VM)
		VM["pc"] -= (steps_back - 1)

		while(VM["registers"]["C"] > 0):
			VM["registers"]["C"] -= 1
			step(VM)
	else:
		pass

def nop(VM):
	VM["pc"] += 1

def p(VM):
	register = "B" if get(VM) % 2  else "C"
	print "=>", chr(VM["registers"][register])

def setA(VM):
	value = get(VM)
	VM["registers"]["A"] = int(value)

def add(VM):
	register = "B" if get(VM) % 2 else "C"
	VM["registers"][register] += int(VM["registers"]["A"])

def sub(VM):
	register = "B" if get(VM) % 2 else "C"
	VM["registers"][register] -= int(VM["registers"]["A"])

def get(VM):
	if len(VM["memory"]) > VM["pc"]:
		memory_content = VM["memory"][VM["pc"]]
		VM["pc"] += 1
		print "Argument =>", int(memory_content)

		return int(memory_content)
	else:
		return 0 # nop
	
def put(object_code, VM):
	VM["memory"].append(object_code)

def step(VM):
	obj = get(VM)
	fun = VM["fun_table"][obj%7]["fun"]
	print "Function name =>", VM["fun_table"][obj%7]["name"]
	#print "Line:", VM["pc"]
	fun(VM)
	show_debug()

def show_debug():
	print "\n--- DEBUG ---"
	print "REGS =>", VM["registers"]
	print "MEM =>", VM["memory"]
	print "pc =>", VM["pc"]
	print "--- DEBUG ---\n"

 
