usuario = ("XxAGMGxX","0511","soyproo@gmail.com")
materias = ["Matematicas","LENGUAJE","CCNN","Programacion"]
estudiante = {"nombre":"Andy","edad":19,"fac":"faci"}
print(usuario[0],materias[1],estudiante["nombre"])
print(usuario[0:2],estudiante.keys(),estudiante.values())
materias.append("Programacion Movil")
estudiante["sexo"], estudiante["edad"]="M", 19
print(materias,estudiante)
tupla,lista,diccionario=(),[],{}
for valor in usuario: print(valor)
for i, c in enumerate(materias): print(i,":",c)
for c, v in estudiante.items(): print(c,":",v)
