[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MU05V_Nx)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19953139&assignment_repo_type=AssignmentRepo)
<h1>Unidade III - Listas e Arquivos</h1>

> [!WARNING]
> 1. Os programas deverão ser desenvolvidos em linguagem PYTHON;
> 2. Cada questão deverá ser respondida em arquivos em separado;
> 3. As respostas deverão ser submetidas no repositório do assignment relativo a esta atividade;
> 4. Está implícito que em todas as questões deverão ser tratadas as devidas exceções (específicas e genéricas);
> 5. Atentem para o prazo de submissão. Ao término do prazo, o assignement será bloqueado automaticamente, não sendo possível novos commits;
> 6. Não serão aceitos envios posteriores a data limite.  

<!-- --------------------------------------------------------------------------------------------- -->
<hr/>
<details>
  <summary>Questão 01 (05 pontos)</summary>
  <br/>Desenvolva um programa que solicite ao usuário dois valores inteiros: o primeiro representando a quantidade de sub-listas da lista principal e o segundo indicando a quantidade de elementos em cada sub-lista. Com base nesses valores, o programa deverá gerar aleatoriamente os elementos de cada sub-lista da lista principal (utilizar LIST COMPREHENSIONS), exibir a lista gerada e, em seguida, calcular e apresentar a lista transposta.<br/><br/>
</details>

<!-- --------------------------------------------------------------------------------------------- -->
<hr/>
<details>
  <summary>Questão 02 (10 pontos)</summary>
  <br/>Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser solicitado ao usuário, positivo e entre 7 e 60, inclusive), cada elemento dessa lista será um número aleatório entre 1 e 60 (inclusive) sem repetição. Após a lista ser gerada, as seguintes operações deverão ser implementadas:<br/><br/>

  <ol type="i">
    <li>Deverá ser criada uma segunda lista com todas as combinações possíveis de 6 dezenas. Cada combinação deverá ser uma sub-lista. Cada combinação deverá estar ordenada do menor número para o maior;<br/></li>
    <li>A lista de números escolhidos deverá ser salva em um arquivo chamado NUMEROS_ESCOLHIDOS.TXT (salvar no mesmo diretório/pasta em que o programa está salvo). Nesse arquivo os números deverão estar em apenas 1 linha. Utilize espaço em branco para separar os valores na linha;<br/></li>
    <li>A lista de combinações deverá ser salva em um arquivo chamado COMBINACOES.CSV (salvar no mesmo diretório/pasta em que o programa está salvo). Nesse arquivo cada combinação deverá estar em 1 linha. Utilize ponto e vírgula para separar os valores na linha;<br/></li>
    <li>No final deverão ser exibidos na tela quantas combinações foram geradas, e quais as probabilidades de se acertar a sena, a quina e a quadra.</li>
  </ol>
</details>

<!-- --------------------------------------------------------------------------------------------- -->
<hr/>
<details>
  <summary>Questão 03 (10 pontos)</summary>
  <br/>Fazer um programa para gerar automaticamente uma lista (utilizar LIST COMPREHENSIONS) de dimensão de n elementos (n deverá ser solicitado ao usuário e ser positivo), com os elementos na faixa dos números inteiros entre 0 e 99 (inclusive), gerados aleatoriamente.<br/><br/>
  <br/>Uma vez a lista gerada, implementar as seguintes operações:<br/><br/>

  <ol type="i">
    <li>A média dos valores dos elementos da lista;<br/></li>
    <li>A mediana dos valores dos elementos da lista;<br/></li>
    <li>A variância populacional dos valores dos elementos da lista;<br/></li>
    <li>O desvio-padrão populacional dos valores dos elementos da lista.<br/></li>
  </ol>

  <br/><b>ATENÇÃO:</b><br/>
  <ul>
    <li>NÃO USAR a biblioteca statistics.py para implementar o que foi pedido anteriormente;<br/></li>
    <li>Para fins de conferência, o aluno poderá utilizar as funções mean(), median(), pvariance() e pstdev() da biblioteca statistics.py.<br/></li>
  </ul>
</details>

<!-- --------------------------------------------------------------------------------------------- -->
<hr/>
<details>
  <summary>Questão 04 (15 pontos)</summary>
  <br/>O Crivo de Eratóstenes é um algoritmo eficiente para encontrar todos os números primos menores ou iguais a um determinado número n. O algoritmo funciona da seguinte maneira:<br/><br/>

  <ol>
    <li>Crie uma lista de números de 2 até n, onde inicialmente todos os números são marcados como "potenciais primos";<br/></li>
    <li>Comece com o número 2. Marque todos os múltiplos de 2 (exceto o próprio 2) como não primos;<br/></li>
    <li>Vá para o próximo número não marcado e marque todos os seus múltiplos como não primos;<br/></li>
    <li>Repita esse processo até que tenha verificado todos os números até n.<br/></li>
  </ol>

  <b>TAREFA:</b><br/>
  <br/>Implemente o algoritmo do Crivo de Eratóstenes em Python para encontrar todos os números primos menores ou iguais a um número n. O número n será fornecido como entrada.<br/><br/>

  <b>INSTRUÇÕES:</b><br/>
  <ul>
    <li>Utilize uma lista para marcar os números como primos ou não primos;<br/></li>
    <li>Implemente a marcação dos múltiplos como não primos de acordo com o Crivo de Eratóstenes<br/></li>
    <li>A entrada será um número inteiro n (2 ≤ n ≤ 10**6);<br/></li>
    <li>Ao final, imprima a lista com todos os números primos encontrados.<br/></li>
  </ul>
</details>

<!-- --------------------------------------------------------------------------------------------- -->
<hr/>
<details>
  <summary>Questão 05 (10 pontos)</summary>
  <br/>Utilizando os arquivos GABARITO.TXT e PROVAS.CSV faça o que se pede:<br/><br/>.

  <ol type="i">
    <li>O programa deverá ler o arquivo GABARITO.TXT e armazenar o seu conteúdo em uma lista;<br/></li>
    <li>O programa deverá ler o arquivo PROVAS.CSV e montar uma lista com os dados contidos nesse arquivo. Observe que cada linha tem o nome do aluno e as suas opções marcadas em cada questão;<br/></li>
    <li>O programa deverá adicionar no final de cada sub-lista do item (ii) a quantidade de acertos do aluno;<br/></li>
    <li>Em seguida o programa deverá ordenar a lista modificada no item (iii) pela quantidade de acertos de cada aluno, começando pela maior pontuação até a menor pontuação obtida ;<br/></li>
    <li>O programa deverá salvar a lista do item (iv) no mesmo formato do arquivo PROVAS.TXT (cada aluno em uma linha, juntamebnte com suas opções marcadas e sua pontuação. Os dados dever ser separados por ;). O arquivo deverá ser salvo com o nome RESULTADOS.CSV.<br/></li>
  </ol>
</details>

<!-- --------------------------------------------------------------------------------------------- -->
<hr/>
<details>
  <summary>Questão 06 (10 pontos)</summary>
  <br/>A partir do arquivo ALUNOS_IFRN.CSV, fazer um programa que:<br/><br/>.

  <ol type="i">
    <li>Montar uma lista onde cada posição deverá ser uma sub-lista. A primeira posição de cada sub-lista deverá ser a sigla do campus e a segunda a quantidade de alunos daquele campus, no final deverá adicionada a cada sub-lista o percentual correspondente de alunos do campus em relação ao total de alunos do IFRN (limitar a 2 casas decimais). Essa lista deverá ser ordenada começando pelo campus com a maior quantidade de alunos. Essa lista deverá ser salva em um arquivo chamado ALUNOS_IFRN_CAMPUS.CSV (esse arquivo deverá ser salvo no mesmo diretório/pasta do programa). onde cada linha deverá ser os dados de cada sub-lista separados por ponto e vírgula (;);<br/><br/></li>
    <li>Montar uma lista onde cada posição deverá ser uma sub-lista. A primeira posição de cada sub-lista deverá ser o ano de ingresso do aluno e a segunda posição a quantidade de alunos que ingressaram naquele ano. Essa lista deverá ser ordenada começando pelo ano com a maior quantidade de alunos. Essa lista deverá ser salva em um arquivo chamado ALUNOS_IFRN_ANO.CSV (esse arquivo deverá ser salvo no mesmo diretório/pasta do programa). onde cada linha deverá ser os dados de cada sub-lista separados por ponto e vírgula(;);<br/><br/></li>
    <li>Liste os campi, peça ao usuário para escolher um e montar uma lista onde cada posição deverá ser uma sub-lista. A primeira posição de cada sub-lista deverá ser o nome do curso e a segunda posição deverá ser quantidade de alunos daquele curso naquele campus. Essa lista deverá ser ordenada começando pelo curso com a maior quantidade de alunos. Essa lista deverá ser salva em um arquivo chamado ALUNOS_IFRN_CAMPUS_CURSO.CSV (esse arquivo deverá ser salvo no mesmo diretório/pasta do programa). onde cada linha deverá ser os dados de cada sub-lista separados por ponto e vírgula (;).<br/><br/></li>
  </ol>

  <br/>OBSERVAÇÃO: os dados fornecidos no arquivo CSV foram obtidos em https://dados.ifrn.edu.br/dataset/alunos-da-instituicao<br/><br/>
</details>

<!-- --------------------------------------------------------------------------------------------- -->
<hr/>
<details>
  <summary>Questão 07 (20 pontos)</summary>
  <br/>Você foi contratado para desenvolver um programa em Python que analisa uma lista de produtos de informática de uma licitação. Cada produto é representado por uma sub-lista contendo as seguintes informações:<br/><br/>

  <ul>
    <li>Nome: O nome do produto (string);<br/></li>
    <li>Categoria: A categoria à qual o produto pertence: "Permanente" ou "Consumo" (string);<br/></li>
    <li>Preço da Empresa A: O preço do produto na Empresa A (float);<br/></li>
    <li>Preço da Empresa B: O preço do produto na Empresa B (float);<br/></li>
    <li>Preço da Empresa C: O preço do produto na Empresa C (float);<br/></li>
  </ul>

  <br/>A lista de produtos será alimentada a partir de um arquivo CSV (PRODUTOS_INFORMATICA.CSV), e o programa deve realizar as seguintes tarefas utilizando as funções map(), filter() e funções lambda:<br/><br/>

  <ol>
    <li>Aplicar um desconto nos preços de todos os produtos, para a empresa escolhida pelo usuário, baseado em um valor percentual fornecido pelo usuário. Para isso, crie uma nova lista com os preços já com o desconto aplicado para a empresa escolhida;<br/></li>
    <li>Filtrar e listar os produtos. Para cada produto , a nova lista deverá conter:<br/></li>
      <ol type="a">
        <li>O nome do produto<br/></li>
        <li>A categoria do produto;<br/></li>
        <li>O menor preço após a aplicação do desconto;<br/></li>
        <li>O nome da empresa com o menor preço.<br/></li>
      </ol>
  </ol>

  <br/><b>CONSIDERAÇÕES:</b><br/>
  <ul>
    <li>O programa deve ler o arquivo CSV contendo os dados dos produtos e converter essas informações para uma lista de sub-listas;<br/></li>
    <li>Não utilize laços for explícitos para percorrer a lista;<br/></li>
    <li>Utilize as funções MAP() e FILTER() junto com funções LAMBDA para realizar as transformações e filtragens;<br/></li>
    <li>O programa deve permitir ao usuário escolher a empresa para a qual o desconto será aplicado e o percentual de desconto;<br/></li>
    <li>Os valores dos preços devem ser arredondados para duas casas decimais;<br/></li>
    <li>O arquivo de entrada será fornecido no mesmo diretório onde o programa será executado. O nome do arquivo de entrada será PRODUTOS_INFORMATICA.CSV;<br/></li>
    <li>Deverá ser gerado um arquivo com o resultado da licitação no mesmo diretório onde o programa será executado. O nome do arquivo de saída será RESULTADO_LICITACAO.CSV.<br/></li>
  </ul>
</details>

<!-- --------------------------------------------------------------------------------------------- -->
<hr/>
<details>
  <summary>Questão 08 (20 pontos)</summary>
  <br/>Você foi contratado para desenvolver um programa em Python que realiza consultas sobre a população dos municípios do Brasil com base em um arquivo CSV contendo dados do último censo do IBGE. O programa deve oferecer duas opções de consulta para o usuário:<br/><br/>

  <ol>
    <li>Consulta por região: O programa deverá listar as 10 cidades mais populosas de cada estado dentro de uma região específica do Brasil, apresentando as populações de cada cidade e o percentual que cada população representa do total do estado;<br/><br/></li>
    <li>Consulta por estado: O programa deverá listar as 10 cidades mais populosas de um estado escolhido, apresentando as populações de cada cidade e o percentual que cada população representa do total do estado.<br/><br/></li>
  </ol>

  <br/><b>INSTRUÇÕES:</b><br/>
  <ol type="i">  
    <li>O programa deve começar solicitando ao usuário uma das duas opções de consulta:<br/></li>
      <ol type="a">
        <li>Consultar por estado;<br/></li>
        <li>Consultar por região.<br/></li>
      </ol>
    <li>Caso o usuário escolha consultar por região, o programa deverá:<br/></li>
      <ol type="a">
        <li>Solicitar que o usuário informe a região do Brasil (Norte, Sul, Sudeste, Centro-Oeste, Nordeste);<br/></li>
        <li>Para cada estado da região, listar as 10 cidades mais populosas (nome e população);<br/></li>
        <li>As cidades devem ser listadas em ordem decrescente de população dentro de cada estado.<br/></li>
      </ol>
    <li>Caso o usuário escolha consultar por estado, o programa deverá:<br/></li>
      <ol type="a">
        <li>Solicitar que o usuário informe a sigla de um estado;<br/></li>
        <li>Listar as 10 cidades mais populosas daquele estado (nome, população e percentual de cada cidade em relação à população total do estado);<br/></li>
        <li>As cidades devem ser listadas em ordem decrescente de população.<br/></li>
      </ol>
  </ol>

  <br/><b>FORMATO DE ENTRADA:</b><br/>
  <ol type="i">  
    <li>O arquivo CSV a ser utilizado (CENSO_2022_POPULACAO_RESIDENTE_MUNICIPIOS.CSV)contém os seguintes campos:<br/></li>
      <ul>
        <li>Nome do município;<br/></li>
        <li>Código municipal;<br/></li>
        <li>UF;<br/></li>
        <li>População total.<br/></li>
      </ul>
    <li>Exemplos de linhas no CSV:<br/></li>
      <ul>
        <li>Natal;2408102;RN;751300<br/></li>
        <li>Mossoró;2408003;RN;264577<br/></li>
        <li>UF;<br/></li>
        <li>Parnamirim;2403251;RN;252716<br/></li>
      </ul>
  </ol>

  <br/><b>FLUXO DO PROGRAMA:</b><br/>
  <ol type="i">  
    <li>O programa pergunta: "Deseja consultar por região ou estado?";<br/></li>
    <li>O programa solicita: "Informe o estado:" ou "Informe a região:";<br/></li>
    <li>O programa exibe os dados conforme as escolhas do usuário.<br/></li>
  </ol>

  <br/><b>CONSIDERAÇÕES:</b><br/>
  <ol type="i">  
    <li>Deverão ser tratados possíveis informações passadas de maneira errada, tipo: informar a sigla de um estado que não existe;<br/></li>
    <li>O resultado deve ser formatado de maneira clara e legível;<br/></li>
    <li>Deve-se OBRIGATORIAMENTE utilizar LIST COMPREHENSION, FILTER(), SORT() juntamente com funções LAMBDA nessa questão.<br/></li>
  </ol>

  <br/>OBSERVAÇÃO: os dados fornecidos no arquivo CSV foram obtidos em https://censo2022.ibge.gov.br/<br/><br/>
</details>
