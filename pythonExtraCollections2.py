from collections import Counter

# Peguei dois textos de temas diferentes no blog da Alura, retirei trechos de código e tentei padronizar espaços manualmente.

texto1 = """No dia a dia, sempre que possível, procuramos estabelecer alguns padrões para facilitar o entendimento e 
organização de informações, algo que fazemos naturalmente, afinal estamos sempre buscando uma forma de otimizar a nossa 
rotina. Dentro da área de Programação, também há essa preocupação em melhorar e otimizar informações, vide os padrões de
programação, estruturas de dados e algoritmos. Mas, na rotina de uma pessoa programadora, em algum momento ela irá se 
deparar com a necessidade de trabalhar com cadeias de caracteres e buscar identificar padrões para extrair informações 
ou validar algum tipo de dado. Neste contexto, hoje temos as chamadas expressões regulares, ou o termo abreviado do 
inglês, regex. Mas o que são? Onde vivem? De que se alimentam? Consigo usar com .NET? Neste artigo vamos conversar um 
pouco sobre elas. Vamos à leitura! O que é uma expressão regular? Vamos a algumas definições: De acordo com Alfredo 
Lotar, autor do livro "Como programar com ASP.NET e C#", uma expressão regular define combinações de caracteres que 
podemos usar para representar partes de uma string. Já para Cláudio Ralha, autor do livro Produtividade com C# da Casa 
do Código: Expressões regulares são ferramentas para executar com pouco código tarefas complexas, como localizar e 
remover várias ocorrências de sequências de caracteres dentro do texto, validar dados informados pelos usuários que 
estão em um formato específico. Então, podemos concluir que uma regex vai definir uma forma de identificar padrões em 
cadeias de caracteres (strings) e que podemos usá-la para validações de dados. Um pouco de história A história das 
expressões regulares está intimamente ligada à teoria da computação, pois ela faz parte da teoria dos automatos e 
linguagens formais. As regex foram desenvolvidas nos estudos do matemático americano Stephen Cole Kleene, que a 
princípio chamava de álgebra de conjuntos regulares. Os trabalhos de Kleene foram a base para a criação de algoritmos 
de busca usados na computação. Hoje, aplicamos as regex em editores de texto, em funções de busca e substituição, e nas
linguagens de programação como forma de validação de formatos de textos. Por exemplo: quando precisamos validar o 
formato do campo e-mail de um formulário, podemos usar: . Então, em resumo, as regex podem ser aplicadas em situações 
de: Mecanismos de validação de dados de formulários; Encontrar um
texto específico em uma string; Representação de padrões. Por exemplo: os números em um CPF. Ok, mas como funcionam 
as regex? Quando usamos regex, a busca pelo caractere, string ou padrão de texto é feita da esquerda para a direita, 
da mesma forma como lemos um texto (pelo menos de acordo com a leitura ocidental). Essa busca pode ser feita em uma 
única linha ou em várias delas, além de poder diferenciar letras maiúsculas e minúsculas e inclusive ignorar espaços 
em branco. Vamos acompanhar um exemplo de uma regex para validação de um CPF:Na definição de uma regex podemos 
utilizar dois tipos de caracteres: os literais, usados normalmente em strings, e os metacaracteres, que fazem com que 
a regex possa processar e manipular informações. Compilamos alguns metacaracteres na tabela a seguir: Vale a pena 
destacar que criar uma sentença regex fazendo uso dos símbolos e metacaracteres disponíveis pode ser extremamente 
trabalhoso. Dividir uma expressão em partes pode nos ajudar, no melhor estilo “dividir para conquistar”. Por exemplo: 
se quisermos selecionar todas as letras e números de um texto, podemos escrever uma expressão que escolha os números 
, depois escrever a que seleciona as letras. Por fim, juntamos as partes da expressão como 
. Até aqui vimos que dentre as vantagens na utilização das regex temos a flexibilidade, a performance e 
a facilidade de uso. Mas após entender a teoria, como podemos fazer o uso das regex com o C#? Para isso precisamos 
utilizar uma classe Regex - e é isso que vamos conhecer no próximo tópico! No .NET a principal classe para trabalhar 
com regex é a de mesmo nome, Regex, que se encontra no namespace System.Text.RegularExpressions. Ela possui uma série 
de métodos estáticos que nos possibilitam trabalhar com expressões regulares. Por exemplo, se quisermos validar se o 
valor informado por um usuário é composto somente por números, podemos fazer o seguinte: Executando o código acima e 
informando 14589AC, temos como saída o que é mostrado na imagem abaixo: Podemos ainda criar um objeto do tipo Regex 
que recebe em seu construtor um caractere ou uma expressão composta pelos metacaracteres. Também é possível informar 
um segundo parâmetro definindo como fazer essa busca. Imagine que você precisa validar um CPF de usuário. Ao invés de 
criar todo um algoritmo, por que não usar uma regex? Observe como poderia ser implementado: Executando o código acima
, o usuário informa um CPF contendo somente números ou com a máscara com pontos, criado um objeto da classe Regex que 
recebe como parâmetro uma expressão para CPF e uma enumeração com o valor de IgnoreCase, que diferencia maiúscula de 
minúscula. Ao executar o método .Match() do objeto, validamos o CPF com a regex definida na criação do objeto. Para 
isso, é importante trabalharmos o retorno criando um objeto do tipo Match. Se quisermos validar, por exemplo, 000.869
.630-66, ao executarmos teremos como saída no terminal o seguinte: Ok, mas e se o CPF para validação não estiver com 
a máscara de CPF? Por exemplo, 99156503024. E aí? Abaixo apresentamos algumas opções da enumeração RegexOptions que 
podemos usar quando criamos nossos objetos regex: Usando o .IsMatch() Com o IsMatch podemos validar se um valor 
informado combina com a expressão regular definida. O retorno do método é um booleano e recebe como parâmetro uma 
string. Usando o mesmo exemplo do CPF, temos: Usando o .Match() Este método pode ser usado para buscar uma string ou 
expressão regex definida na classe. Por exemplo: Por meio desses exemplos, conseguimos enxergar o poder que temos na 
utilização de expressões regulares! E no .NET, usando a classe Regex, fica ainda mais fácil! Conclusão Neste artigo 
nosso objetivo foi apresentar o que são as regex, desde a definição até a aplicabilidade em programação. Entendemos 
que aplicar as regex para criar expressões que validam a formatação de caracteres, ou que possibilitam a pesquisa de 
conteúdo específico, pode ser uma valiosa ferramenta para as pessoas desenvolvedoras, independentemente da linguagem. 
Diferentes linguagens têm bibliotecas próprias para trabalhar esse recurso e no .NET não é diferente! Por isso 
conhecemos a classe Regex, que encapsula funcionalidades permitindo trabalhar as regex no código C#. Também 
observamos que apesar da facilidade oferecida pela plataforma no momento de usar regex, escrevê-las pode ser algo 
desafiador, já que precisamos resumir várias informações em uma única expressão."""

texto2 = """Diferenças no B2C e B2B para o marketing de conteúdo Diferenças no B2C e B2B para o marketing de conteúdo 
Giulia Losnak Giulia Losnak Atualizado em 09/11/2022 COMPARTILHE Esse artigo faz parte da Formação Marketing Digital 
Imagem de destaque Vamos imaginar uma empresa como o Nubank, seu nome é ByteBank. A primeira vista ela vende 
cartões de crédito e possui uma estratégia de marketing de conteúdo para seus clientes (Business to Consumer, B2C). 
Agora ela está lançando um novo cartão focado em empresas e quer criar uma estratégia de marketing de conteúdo para 
outras empresas (business to business, B2B). Como eles podem criar essa estratégia? É possível utilizar ideias e 
ferramentas do marketing de conteúdo B2C para o B2B? No marketing de conteúdo criado para B2C da ByteBank é muito 
enfatizado que as principais vantagens da empresa são: saber o limite na hora; não pagar qualquer tarifa e não ter que 
lidar com burocracia na hora de fazer o cartão. Então, todo o plano é focado em criar conteúdos sobre questões 
relacionadas ao mundo financeiro, para mostrar que a empresa é especialista no assunto, transmitindo uma confiança aos 
clientes. A equipe de marketing escreveu um texto no qual foram explicadas todas as taxas do cartão de crédito. Depois 
de explicar com detalhes o que é cada taxa, foi mostrado o porquê do cartão dessa empresa não cobrar nenhuma delas. Para
mostrar na prática o quanto o consumidor economizaria, eles deram como um exemplo que mostram o que pode ser comprado 
com o dinheiro economizado em tarifas do cartão. Veja como ficou o texto: Se a tarifa é de 30 reais por mês, depois de 
um ano: 30 (tarifa) * 12 (meses) = 360, você gasta R$ 360,00 só em tarifas! Não seria muito melhor comprar um Kindle ou
dois jogos para Playstation 4 ou, até mesmo, ir uma vez por mês ao cinema (e pagando inteira) com esse dinheiro em vez
de pagá-lo em tarifas? Será que se pode fazer a mesma coisa para o B2B, já que não existem tarifas para empresas 
também? As empresas que querem comprar um produto precisam avaliar muito bem toda a compra, sempre se perguntando se 
aquele produto realmente compensa para ela, principalmente a longo prazo. Então, e se fosse dito coisas que a empresa
poderia fazer com o dinheiro que também vão trazer um retorno financeiro, ao contrário das taxas dos bancos? Como 
fazer pesquisas com usuários, desenvolver novos produtos, treinar pessoas para marketing, entre outras coisas? 
Pensando nessas diferenças, utilizamos o mesmo exemplo: quanto seria economizado por ano pela empresa cliente. 
Porém, no texto inteiro, queremos também mostrar dicas de como ela pode poupar, de diversas maneiras, mesmo usando 
um cartão de crédito. Então, o exemplo de economia no texto ficou assim: Pensando que a tarifa para empresas é mais 
barata que para pessoas físicas, ou seja, de 30 reais, passa a ser 10 reais por cartão para cada colaborador, e dez 
cartões serão feitos, cada um pertencendo a colaborador, depois de um ano, serão pagos: 10 (de tarifa) * 10 
(quantidade de cartões) * 12 (meses do ano) = 1200. Assim, a organização gastaria R$ 1.200,00 para manter os cartões
durante esse período. Agora, se os cartões não possuem tarifa nenhuma, em vez de pagar esse valor, a empresa 
economizará R$1.200,00. Agora, com essa economia, você poderia investir em treinamentos ou eventos, que, após um 
tempo, poderiam aumentar ainda mais o retorno da empresa. Foi usada uma linguagem mais formal do que a B2C porque 
quando estamos lidando com empresas temos que ser mais práticos e mostrar exatamente o que a empresa ganha, e, no 
caso, até como poderia ganhar mais depois. Além dessa mudança na linguagem, tivemos ideias diferentes de conteúdo. 
No B2C foram apresentados conhecimentos a respeito de cada taxa, para que a pessoa entenda o que está pagando e 
confie em empresas que não cobra as taxas. Agora para B2B foram apresentadas formas para economizar no cartão, pois
, muitas vezes, os empresários sabem o que é cada taxa do cartão e tem que utilizá-lo mesmo assim. Então, mostramos 
como ele pode economizar e, uma dessas formas, é usar o cartão da ByteBank. Nesse mesmo texto para B2B também 
acrescentamos o conteúdo de outra vantagem do cartão: poder determinar um limite de gastos para cada categoria nos 
cartões dos funcionários da empresa. Dessa forma, os funcionários não podem gastar mais do que o determinado e, assim, a
empresa consegue economizar e planejar os gastos e não extrapolar com compras dos funcionários. O foco da comunicação 
B2B que utilizamos foi dar dicas para não cometer erros e economizar mais, para que a empresa perceba que utilizar o 
cartão é vantagem. E caso a sua empresa seja diferente da ByteBank, seja só B2B e não tenha nenhum plano de comunicação
focado para B2C para se basear? Existem diversas empresas B2B: as que vendem tanto para B2B quanto para B2C, como a 
ByteBank; as que vendem para ambos os consumidores, mas possuem um foco maior no B2B, como a Marmotex, que tem como 
serviço entrega de marmitas e entregam tanto para consumidores quanto empresas, mas possuem um foco maior em 
organizações e catering para eventos, ou seja, B2B as empresas somente B2B, como as de agências de publicidade. Cada uma
das empresas que são B2B possui um produto e um serviço para mostrar. Então, caso você trabalhe em uma empresa que não 
possui um plano de marketing de conteúdo para B2C para se basear, é só seguir a ideia do marketing de conteúdo, de 
passar informações relacionados a sua empresa, tornando-a uma autoridade no assunto. E, além disso, mostrar maneiras que
o seu produto e/ou serviço pode ajudar a empresa em determinado tema. No B2B, como no marketing de conteúdo focado no 
B2C, é importante frisar a importância e a relevância do produto e/ou serviço para o cliente. E, melhor, a longo prazo. 
A empresa cliente precisa entender e saber que a vantagem trazida pelo produto será duradoura. Pois o processo de compra
B2B é mais longo justamente porque há muito em jogo e muitas pessoas envolvidas. Mudar de produto ou serviço é 
trabalhoso e pode causar prejuízo para a empresa, assim, eles buscam e precisam de garantias de que a solução 
funcionará por muito tempo. Assim, como no marketing B2C, os tipos de conteúdo devem se atentar aos clientes em cada 
fase do funil de marketing de conteúdo para trazer o conteúdo certo para a empresa em cada momento da obtenção do 
cartão. Para isso, a Bytebank utilizou dados, números, infográficos e mostrou com exemplos práticos maneiras de ajudar a
contratante. Também escreveu conteúdos com histórias de empresas - os chamados cases de sucesso - que obtiveram lucro 
ou sucesso com o produto/serviço. Além disso, apresentou novidades e dicas tanto da sua empresa, que passou a fornecer 
uma conta para pessoas físicas e jurídicas, quanto do segmento dela, com informações que podem ser úteis ao cliente do 
setor financeiro. Como vimos, as principais diferenças entre os conteúdos B2C para o B2B são a linguagem, que deve ser 
mais formal se for B2B e apelar para o emocional se for B2C. No B2B você estará lidando com pessoas que tomam decisões 
nas empresas, então deverá mostrar como o produto pode ajudar a empresa, de preferência a longo prazo.Fora isso, o tipo
de conteúdo pode ser o mesmo do marketing de conteúdo B2C. Passando desde textos sobre novidades, inovações e dicas na
área, até infográficos com dados de pesquisas, vídeos, áudios de podcast, imagens e publicações nas redes sociais. 
Também, para conteúdo B2B, é muito comum encontrar whitepapers, grupos de usuários, meetups, cases de sucesso, trial 
gratuito, e até mesmo vídeos ou campanhas e posts de marketing com influenciadores. Agora, se você quiser saber mais 
sobre marketing de conteúdo, pode fazer nosso curso de Marketing de Conteúdo e, também, conferir mais informações no 
livro da Casa do Código, Marketing de Conteúdo: Estratégias para entregar o que seu público quer consumir."""

aparicoes1, aparicoes2 = Counter(texto1.lower()), Counter(texto2.lower())

totalCaracteres1, totalCaracteres2 = sum(aparicoes1.values()), sum(aparicoes2.values())

bag1 = Counter(dict([(letra, f'{round((frequencia/totalCaracteres1)*100, 2)}%') for letra, frequencia in aparicoes1.items()]))
bag2 = Counter(dict([(letra, f'{round((frequencia/totalCaracteres1)*100, 2)}%') for letra, frequencia in aparicoes2.items()]))

bags10 = (print(bag1.most_common(10)), print(bag2.most_common(10)))

"""Repare como a proporção das 10 letras mais usadas em dois textos diferentes são muito próximas e são quase as mesmas
   10 letras! Isso é uma regra geral para qualquer texto em qualquer lingua, cada lingua tem sua proporção fixa!"""




