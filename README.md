# Calculadora Anhembi Morumbi
### Atendimento ao Aluno

A Universidade Anhembi Morumbi possui um método muito específico para calcular a nota dos alunos, por este motivo, criei uma calculadora onde o aluno faz o preenchimento das notas e ela retorna se ele passou ou não na matéria. 

Na primeira interação com o Aluno, o script solicita algumas informações pessoais, o objetivo é ter uma interação mais humana e personalizada: 
  - Nome;
  - Curso; 
  - Matéria. 
  
Após o preenchimento dos dados pessoais, o script solicita as notas para efetuar os cálculos através das funções.
  - Trabalho em Sala;
  - Teste de Eficiência;
  - Prova N1;
  - Prova N2;
  - Prova Substitutiva N2*.
  
###### Quando o aluno não atinge a nota mínima, é possível ele fazer uma prova substitutiva que segue os mesmos critérios da N2. 
	
#### CRITÉRIO UNIVERSIDADE PARA CÁLCULO:
Nota mínima: 6 pontos 
Peso N1 = 40% 
Peso N2 = 60% 
Substitutiva 

#### LÓGICA DE CÁLCULO:  
N1 = (Trabalho em Sala + Teste Eficiência + Prova N1) * 0.4 
N2 = Prova N2 * 0.6

#### TIPOS DE RETORNO: 
1 - Aprovado; 

2 - Não aprovado > Necessário Prova Substitutiva;  

3 - Aprovado com a nota da Prova Substitutiva; 

4 - Reprovado > Necessário cursar novamente o semestre. 

#### ARQUIVOS PYTHON 
programa.py faz a interação através dos inputs, é a interface com o usuário. 

interação.py recebe os inputs do programa.py e interage com as funções do calculo_notas.py 

calculo_notas.py contém todas as lógicas de cálculo, pesos e requisitos. Também contém a lógica IF, para retornar se o Aluno pasosu ou não na matéria. 
