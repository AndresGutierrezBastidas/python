if __name__ == '__main__':
    n = int(input())
    list = [[input(),float(input())] for i in range(n)]

    notas = [list[i][1] for i in range(n)]
    minimo = min(notas)

    segundoNotas = [list[i][1] for i in range(n) if(list[i][1]!=minimo)]
    segundoM = min(segundoNotas)
    list.sort(reverse=False)

    [print(list[i][0],end='\n') for i in range(n) if(list[i][1] == segundoM)]
