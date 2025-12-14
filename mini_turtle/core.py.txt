# core.py - Lógica y Estado Global
posicion_x = 0 

def adelante(pasos):
    global posicion_x
    posicion_x += pasos
    print(f"Posición X actual: {posicion_x}")

def abajo(pasos):
    print(f"Movimiento 'abajo' por {pasos} pasos.")
    pass 

def reiniciar():
    global posicion_x
    posicion_x = 0
    print("Posición X reseteada a 0.")