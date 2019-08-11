import random

semanas = input('Inserte el no. de semanas:\n')

def iniciar_simulacion(s):
  for i in range(0,int(s)):
    print("-------------------------------------------")
    print("SEMANA %d"%(i+1))
    nde = random.randint(1,10000) # Genera un núm. aleatorio de piezas defectuosas para el lote (entre 1 y 5000)
    lote = [0 for i in range(10000)]
    costo = 0
    print("No. Defectuosas: "+ str(nde))
    random_defectuosas(nde,lote)
    costo = inspeccionar(nde,lote)
    print("Costo Final: ", costo) #imprime el costo


# Posiciona aleatoriamente las nde piezas defectuosas en el lote
def random_defectuosas(nde,lote): 
  for i in range(nde):
    pos = random.randint(0,(10000-1)) # Posición aleatoria en todo el lote
    lote[pos] = 1 # La pieza en lote[pos] está defectuosa
  
# Inspecciona las piezas y calcula el costo final
def inspeccionar(nde,lote):
  CT = 0 # Costo total
  enc_def = False # ¿Encontró una defectuosa?
  for i in range(5): # Se inspeccionarán 5 piezas
    CT += 2.5 # El costo aumenta $2.5 por pieza inspeccionada
    pos = random.randint(0,(10000-1)) # Posición aleatoria a inspeccionar
    if lote[pos] == 1: # Si encontró una defectuosa
      print("Se encontró defectuosa la pieza no. %d" % (i+1))
      enc_def = True # Encontró una defectuosa
      CT += 10000*2.0 # El costo aumenta $2.00 por todo el lote (lote rechazado)
      break
  if enc_def == False: # Si no encontró una defectuosa en verificación
    CT = verificar_funcion(nde,CT)
  return CT

def verificar_funcion(nde,CT):
  # f(p) = 19*(1-p)^18, p = nde/10000
  porc_acep = (19*pow((1-(nde/10000)),18))
  if porc_acep < 4.23: # % de aceptación menor al 4.23%
    print("Porc. de aceptación muy bajo (%f)" % porc_acep)
    CT += 10000*2.0 # El costo aumenta $2.00 por todo el lote (lote rechazado)
  else: # % de aceptación mayor o igual al 4.23%
    print("Porc. de aceptación: %f" % porc_acep)
    print("En fase de ensamblaje.")
    CT += 25.00*nde # El costo aumenta $25.00 por cada pieza defectuosa en el lote
  return CT

iniciar_simulacion(semanas)

