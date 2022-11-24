# snake case
int_edad = 10
print("Inicio")
for i in range(0,9):
  print("="*i)
print("=" * 80)

str_long_text = "Esto es una gran texto para buscar"
if "gran1" in str_long_text:
  print("gran encontrado")
else:
  print("gran no encontrado en el texto")

print("=" * 80)

def suma (int_a, int_b):
  return int_a + int_b

print(suma(10,15))
print(suma(20,60))


print("Fin")
