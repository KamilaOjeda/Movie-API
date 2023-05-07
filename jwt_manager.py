from jwt import encode

# Crear función para crear el token
## Le pasamos un diccionario como parámetro
## payload: el contenido que se pasa como token
def create_token(data: dict):
   token: str = encode(payload=data, key="my_secrete_key", algorithm="HS256")
   return token