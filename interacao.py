import calculo_notas

# IMPORTAÇÃO DOS DADOS INFORMADOS PELO ALUNO E INTERAÇÃO COM A FUNÇÃO CALCULO_NOTAS.
class interacao: 
    def __init__(self, nome, curso, materia, nota_trabalho, nota_teste_eficiencia, nota_prova_1, nota_prova_n2):
        self.nome = nome
        self.curso = curso
        self.materia = materia
        self.nota_trabalho = float(nota_trabalho)
        self.nota_teste_eficiencia = float(nota_teste_eficiencia)
        self.nota_prova_1 = float(nota_prova_1)
        self.nota_prova_n2 = float(nota_prova_n2)
        print(calculo_notas.input_notas(nome, curso, materia, nota_trabalho, nota_teste_eficiencia, nota_prova_1, nota_prova_n2))


       