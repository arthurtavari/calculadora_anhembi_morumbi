# REQUISITO MÍNIMO E PESOS PARA CALCULO
nota_minima = 6
peso_n1 = 0.4
peso_n2 = 0.6

# FUNÇÃO QUE CALCULA ATRAVÉS DOS INPUTS SE O ALUNO PASSOU OU NÃO NA MATÉRIA
def input_notas(nome, curso, materia, nota_trabalho, nota_teste_eficiencia, nota_prova_1, nota_prova_n2):
    nome = nome
    curso = curso
    materia = materia
    N1 = ((nota_trabalho + nota_teste_eficiencia + nota_prova_1) / 3) * peso_n1
    N2 = nota_prova_n2 * peso_n2
    nota_final = round((N1 + N2),2)
    nota_necessaria_sub = round((nota_minima - N1) / peso_n2,2)

    if(nota_final >= 6.0):
        print(f'Parabéns, {nome}! Você foi aprovado na matéria de {materia}, sua nota final foi:')
        return nota_final
    else: 
        print(f'{nome}, infelizmente você não passou de primeira! Sua nota final foi: {nota_final}')
        print(f'Não se preocupe, já agendamos uma prova substitutiva. Você precisa tirar no mínimo: {nota_necessaria_sub}')

        input_prova_substitutiva = float(input('Qual foi a nota da prova substitutiva? '))
        nota_final_com_substitutiva = round((N1 + (input_prova_substitutiva * peso_n2)),2)

        if(nota_final_com_substitutiva >= 6): 
            print(f'Parabéns, {nome}! Você foi aprovado na matéria de {materia}, sua nota final com a prova substitutiva foi:')
            return nota_final_com_substitutiva
        else: 
            print(f'{nome}, infelizmente você não atingiu a pontuação mínima!\nSerá necessário cursar no próximo semestre a matéria de {materia}. \nA nota mínima para o curso de {curso} é {nota_minima}. \nMesmo com a prova substitutiva, você ficou com saldo negativo de:')
            return round(nota_minima - nota_final_com_substitutiva,2)

