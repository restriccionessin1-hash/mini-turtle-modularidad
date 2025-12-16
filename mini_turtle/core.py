import turtle
import time 

# 1. Crea la pantalla y el objeto tortuga (Globales para este módulo)
# Esta configuración se ejecuta la primera vez que se importa el módulo.
pantalla = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle") 
t.speed(1)        
t.penup()
t.home()
t.pendown()

# 2. Funciones de movimiento
def adelante(pasos):
    # La tortuga real avanza 'pasos' unidades (multiplicamos por 20 para ver mejor)
    t.forward(pasos * 20) 
    print(f"Posición X actual: {t.xcor():.0f}")

def abajo(pasos):
    print(f"*Movimiento 'abajo' por {pasos} pasos.")
    t.right(90)  # Gira a la derecha (hacia abajo)
    t.forward(pasos * 20)
    t.left(90)   # Vuelve a girar para mirar hacia adelante

def reiniciar():
    # Limpia el dibujo y lleva la tortuga al origen (0, 0)
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    print("Posición X reseteada a 0.")
    time.sleep(1) # Pausa para ver el reseteo

# 3. Función crucial para mantener la ventana abierta
def finalizar_dibujo():
    # Bloquea la ejecución para que la ventana de la tortuga se quede visible
    turtle.done()