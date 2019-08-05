import random

def iniciar_simulacion():
  nde = random.randint(1,5000) # Genera un núm. aleatorio de piezas defectuosas para el lote (entre 1 y 5000)
  lote = [0 for i in range(10000)]
  costo = 0
  print("Defectuosas: "+ str(nde))
  random_defectuosas(nde,lote)
  costo = inspeccionar(nde,lote)
  print("Costo Final: ",costo) #imprime el costo


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
      print("Halló una pieza defectuosa en inspección")
      enc_def = True # Encontró una defectuosa
      CT += 10000*2.0 # El costo aumenta $2.00 por todo el lote (lote rechazado)
      break
  if enc_def == False: # Si no encontró una defectuosa (lote aceptado)
    print("No halló defectuosas en inspección")
    CT += 25.00*nde # El costo aumenta $25.00 por cada pieza defectuosa en el lote
  return CT

iniciar_simulacion()

