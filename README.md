<h2> CALCULADORA NOTA FINAL <> ANHEMBI MORUMBI </h2>

A Universidade Anhembi Morumbi possui um método muito específico para calcular a nota dos alunos, por este motivo, <i>como todo iniciante em alguma linguagem de programação</i>, criei uma calculadora onde o aluno faz o preenchimento das notas e ela retorna se ele passou ou não na matéria. 

Na primeira interação com o Aluno, o script solicita algumas informações pessoais, o objetivo é ter uma interação mais humana e personalizada. 

Após o preenchimento dos dados pessoais, o script solicita as notas dos trabalhos e provas. Através desses inputs efetua cálculos utilizando as funções criadas com os critérios e lógica de cálculo da universidade.
	
<h5>BASE PARA CÁLCULO</h5>

	Nota mínima: 6 pontos 
	Peso N1 = 40% 
	Peso N2 = 60%  

<h5>LÓGICA DE CÁLCULO</h5>  


	N1 = (Trabalho em Sala + Teste Eficiência + Prova N1) * 0.4 
	N2 = Prova N2 * 0.6

<h5>TIPOS DE RETORNO</h5> 

	1 - Aprovado;
	2 - Não aprovado > Necessário Prova Substitutiva; 
	3 - Aprovado com a nota da Prova Substitutiva; 
	4 - Reprovado > Necessário cursar novamente o semestre. 

<h5>ARQUIVOS</h5>

	programa.py é a interface entre a calculadora e o aluno, através dela solicita informações necessárias para cálculo. 
	interacao.py contém armazenamento de todos os inputs do usuário e interage com as funções do arquivo calculo.py. 
	calculo.py contém todas as lógicas de cálculo e condições para imprimir se o Aluno foi aprovado ou não na matéria. 


 
