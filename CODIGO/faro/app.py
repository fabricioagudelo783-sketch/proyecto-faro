from .clientes.cliente import Cliente

cliente1 = Cliente(
    "Fabricio Agudelo",
    "123456789",
    "3001234567",
    "fabricioagudelo783@gmail.com",
    "Medellín"
)

print("Cliente registrado correctamente.")
print(cliente1.nombre)
print(cliente1.documento)
print(cliente1.telefono)
print(cliente1.correo)
print(cliente1.ciudad)