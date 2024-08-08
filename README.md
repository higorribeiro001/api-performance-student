# api-performance-student

> Descrição:
### Esta API contém views utilizando ModelViewSet que é capaz de realizer o CRUD (Create, Read, Update, Delete) completo em poucas linhas, com código limpo e eficiente, além de usar SimpleRouter nas rotas, tornando as urls mais padronizadas. A rede neural original em códigos não está presente neste repositório, ela apenas foi carregada a partir de um json contendo a sua estrutura e outro arquivo contendo os pesos (no arquivo "network.py" é possível saber de mais detalhes). A rede neural utiliza recursos do Deep Learning (Aprendizado profundo), como o método de regressão linear para prever valores contínuos. A rede neural foi treinada com dataset obtido no Kaggle e com 2395 linhas e 14 colunas, onde o treinamento com a precisão chegando em torno dos 83%. Porém, sendo apenas um projeto teste, foi bem produtivo, além de chegar a obter 0.0366 de perda na loss function (mede a diferença entre as previsões da rede e os valores reais dos dados de treinamento) que é um valor bem baixo e positivo para a rede, o desafio foi contornar os mínimos locais. A base de dados para registros da API é apenas um SQLite simples e será guardado localmente, se quiser utilizar outro banco de dados pode conectar nas settings da API. Caso obtenha interesse no código da rede neural, basta entrar em contato comigo, aqui está meu linkedin: https://www.linkedin.com/in/higor-ribeiro-araujo-892008211/.

> Execução:

### - Você pode executar de dois modos: por máquina virtual ou por docker.
### - No ambiente Windows, basta seguir os seguintes passos no terminal:
1. criar uma venv:
~~~python
python -m venv venv
~~~
2. executar a venv:
~~~python
./venv/scripts/activate
~~~
3. Por conta do docker o "tensorflow" não foi incluído no requirements.py, portanto rode o seguinte comando: 
~~~
pip install tensorflow
~~~
4. Instale todas as outras bibliotecas necessárias:
~~~
pip install -r requirements.txt
~~~
5. Executar o projeto:
~~~python
python manage.py runserver
~~~
#### obs: Não irei fazer passos para outros OS. Caso tenha problemas, pesquise na internet ou consulte alguma IA.
### - Para executar por meio do docker, basta digitar o seguinte comando no terminal:
~~~
docker compose up
~~~
#### Se quiser executar em segundo plano: 
~~~
docker compose up -d
~~~
### - Você pode abrir o swagger do projeto no navegador, pela rota: api/schema/swagger-ui/
### - Para realizar uma avaliação de desempenho, basta fornecer alguns dados, como por exemlo:
~~~
{
    "name": "Higor",
    "age": 18,
    "gender": 0,
    "ethnicity": 0,
    "paramental_education": 1,
    "study_time_weekly": 20,
    "absenses": 3,
    "tutoring": 0,
    "parental_suporte": 1,
    "extracurricular": 1,
    "sports": 0,
    "music": 0,
    "voluteering": 1
}
~~~
> Mais Detalhes:
### - Para entender melhor o que significa cada uma das chaves citadas acima, deixarei abaixo os detalhes:
#### age : A idade dos alunos varia de 15 a 18 anos
#### gender : Gênero dos alunos, onde 0 representa Masculino e 1 representa Feminino
#### ethnicity : A etnia dos alunos, codificada da seguinte forma:
##### 0: Caucasian
##### 1: Afro-americano
##### 3: Outro
##### 4: assintomático
#### paramental_education : O nível de educação dos pais, codificado da seguinte forma:
##### 0: Nenhum
##### 1: Ensino Médio
##### 2: Alguma faculdade
##### 3: Bacharel
##### 4: Superior
#### study_time_weekly : Tempo de estudo semanal em horas, variando de 0 a 20
#### absenses : Número de faltas durante o ano letivo, variando de 0 a 30
#### tutoring : Status de tutoria, onde 0 indica Não e 1 indica Sim
#### parental_suporte : O nível de apoio parental, codificado da seguinte forma:
##### 0: Nenhum
##### 1: Baixo
##### 2: Moderado
##### 3: Alto
##### 4: Muito alto
#### extracurricular : Participação em atividades extracurriculares, onde 0 indica Não e 1 indica Sim
#### sports : Participação em esportes, onde 0 indica Não e 1 indica Sim
#### music : Participação em atividades musicais, onde 0 indica Não e 1 indica Sim
#### voluteering : Participação em voluntariado, onde 0 indica Não e 1 indica Sim.

