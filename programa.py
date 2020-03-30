from interacao import interacao

# SOLICITAÇÃO DOS DADOS DO ALUNO PARA UMA INTERAÇÃO MAIS HUMANA, ATRAVÉS DO NOME, CURSO E MATÉRIA INFORMADOS
nome = input('Qual o seu nome? ')
curso = input('Qual seu curso? ')
materia = input('Deseja saber sua média de qual matéria? ')


# SOLICITAÇÃO DAS NOTAS DO ALUNO PARA CÁLCULO E RETORNO DE MÉDIA FINAL
nota_trabalho = float(input('Qual foi a nota do seu trabalho em grupo? '))
nota_teste_eficiencia = float(input('Qual foi a nota do seu teste de eficiência? '))
nota_prova_1 = float(input('E qual foi a nota da sua prova N1? '))
nota_prova_n2 = float(input('Qual foi a nota na prova final N2?'))

# VARIÁVEL QUE INPUTA OS DADOS PARA INTERAÇÃO ENTRE AS FUNÇÕES DE: INTERAÇÃO E CALCULO NOTAS
informa_dados = interacao(nome, curso, materia, nota_trabalho, nota_teste_eficiencia, nota_prova_1, nota_prova_n2)