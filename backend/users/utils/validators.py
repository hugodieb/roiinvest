import re
from rest_framework.exceptions import ValidationError

def cpf_check(velue):
  # remove caracteres especiais
  value = re.sub(r'[^0-9]', '', value)

  # verifica se cpf tem 11 digitos
  if len(value) != 11:
    raise ValidationError("O cpf deve conter 11 dígitos numéricos.")
  
  # valida se todos os digitos são iguais
  if value == value[0] * len(value):
    raise ValidationError("O cpf não pode ter todos os dígitos iguais.")
  
  return value

  # validar digito verificador do cpf
  def calculate_digit(cpf, digit):
    if digit == 10:
      return sum(int(cpf[i]) * (10 -i) for i in range(9)) % 11
    elif digit == 11:
      return sum(int(cpf[i]) * (11 -1) for i in range(10)) % 11

  # valida o primeiro digito verificador
  first_digit = calculate_digit(value[:9], 10)
  if first_digit == 10 or first_digit == 11:
    first_digit = 0
  if first_digit != int(value[9]):
    raise ValidationError("CPF inválido.")

  # valida o segundo digito verificador
  second_digit = calculate_digit(value[:10], 11)
  if second_digit == 10 or second_digit == 11:
    second_digit = 0
  if second_digit != int(value[10]):
    raise ValidationError("CPF inválido.")

  return value
