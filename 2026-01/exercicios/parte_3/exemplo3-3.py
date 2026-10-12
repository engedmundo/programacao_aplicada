import time

pressao_str = input("Informe a pressão do óleo, em bar: ")
pressao = float(pressao_str)

print("\nStatus da grade de proteção - Informe:")
print("Grade aberta - '0' ")
print("Grade fechada - '1' ")
status_grade_str = input("Informe status da grade: ")
status_grade = int(status_grade_str)
print("") # Linha em branco

if status_grade == 0:
    print("ERRO: Grade de proteção aberta.")
    print("Operação bloqueada por segurança.")

elif status_grade == 1 and pressao < 50:
    print("AVISO: Pressão insuficiente para a operação")

elif status_grade == 1 and pressao >= 150:
    print("PERIGO: Sobrepressão detectada")
    print("Acionando válvula de alívio")
    time.sleep(1)
    print("Aliviando pressão - 1 segundo")
    time.sleep(1)
    print("Aliviando pressão - 2 segundos")
    time.sleep(1)
    print("Aliviando pressão - 3 segundos")

elif status_grade == 1: # and pressao >= 50 and pressao < 150
    print("Sistema pronto! Operação autorizada!!")

else:
    print("Dados de entrada incorretos.")  