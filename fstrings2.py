#Formatação de Strings com vários linhas
escola = 'Senai'
curso = 'Desenvolvimento'
uc = ' Lógica de Programação'
matricula = 34
nota = 9.999999
print(f"Escola: {escola}\n"
      f"Curso: {curso}\n"
      f"Unidade Curricular: {uc}\n"
      f"Matrícula: {matricula:06d}\n"
      f"Nota: {nota:.2f}")