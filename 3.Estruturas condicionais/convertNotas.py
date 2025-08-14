def ConvertNotas():
    print("""
          Este algoritimo tem como função converter uma nota 0 a 100 em conceitos de A,B,C,D,E
          """)
    try:
        nota = int(input("entre com um valor de nota para podermos avaliar"))
        if nota > 100 :
            print("Este valor não sera aceito pois esta fora dos parametros")
        elif nota >= 0 and nota <=20:
            print(f"O aluno com a nota {nota} tera o conceito F ")
        elif nota>20 and nota<=40:
            print(f"O aluno com a nota {nota} tera conceito E")
        elif nota > 40 and nota <= 60:
            print(f"O aluno com a nota {nota} tera conceito igual a D")
        elif nota >60 and nota <=80:
            print(f"O aluno tera a nota {nota} tera conceito C")
        elif nota > 80 and nota < 99:
            print(f"O aluno tera nota {nota} tera conceito igual a B")
        else
            print(f"O aluno com a nota {nota} tera conceito A")
    except ValueError:
        print("As notas que serão aceitas serão apenas os numeros de 0 a 100")

if __name__ ==  "__main__":
    ConvertNotas()
    
    