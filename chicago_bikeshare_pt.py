# coding: utf-8

# Começando com os imports
import csv
import numpy # Numpy adicionado para a Tarefa 9 - Cálculo de média e mediana
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("./chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = [[column.strip().replace(';;;;;;;', '') for column in line] for line in list(reader)] # Removendo sujeira do fim de cada linha
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

def count_items(column_list):
    """
    Função para fazer contagem de itens sem a definição do que vai ser contado.
    Resolução da Tarefa 12
    Argumentos:
        column_list: Lista contendo os tipos que se deseja contar.
    Retorna:
        item_types: lista com os tipos presentes;
        count_items: lista contendo o count por items;

    """
    item_types = []
    count_items = []
    item_types = list(set(column_list))

    for item_type in item_types:
        count = 0
        for item in column_list:
            if item == item_type:
                count+=1
        count_items.append(count)

    return item_types, count_items

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

for i in range(20):
    print (data_list[i])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]
input("Aperte Enter para continuar...")

# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
# Get gender index
index_of_gender = -2

for i in range(21):
    print(data_list[i][index_of_gender])


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros


input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):

    column_list = []
    for data in data:
        column_list.append(data[index])
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print(f"List Size: {len(column_to_list(data_list, -2))}")
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")

try:
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
    assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
    assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
    # -----------------------------------------------------
except AssertionError as e:
        print(f"Error on assertion: {e}")

input("Aperte Enter para continuar...")
# Vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
unknowns = 0
genders = column_to_list(data_list, -2)

for gender in genders:
    if gender.upper().strip() == 'MALE':
        male+=1
    elif gender.upper().strip() == 'FEMALE':
        female+=1
    else:
        unknowns+=1

print(f"Quantidade de unknowns: {unknowns}")
# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)
try:
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
    # -----------------------------------------------------
except AssertionError as e:
        print(f"Error on assertion: {e}")

input("Aperte Enter para continuar...")
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
    Função para contar os gêneros presentes numa lista.
    Argumentos:
        data_list: Lista contendo os gêneros.
    Retorna:
        Uma lista contendo a contagem por gênero na seguinte orgem [male, female]
    """

    male = 0
    female = 0
    genders = column_to_list(data_list, -2)

    for gender in genders:
        if gender.upper().strip() == 'MALE':
            male+=1
        elif gender.upper().strip() == 'FEMALE':
            female+=1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))
try:
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
    assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
    assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
    # -----------------------------------------------------
except AssertionError as e:
        print(f"Error on assertion: {e}")

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    """
    Função para identificação do gênero mais popular.
    Argumentos:
        data_list: Lista contendo os gêneros
    Retorna:
        Uma string contendo o nome do gênero mais popular ou se é empate.

    """
    answer = ""
    g_count = count_gender(data_list)
    if g_count[0] > g_count[1]:
        answer = "Male"
    elif g_count[1] > g_count[0]:
        answer = "Female"
    elif g_count[0] == g_count[1]:
        answer = "Equal"

    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

try:
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
    assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
    # -----------------------------------------------------
except AssertionError as e:
        print(f"Error on assertion: {e}")

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.

print("\nTAREFA 7: Verifique o gráfico!")
user_types_list = column_to_list(data_list, -3)
types, quantity = count_items(user_types_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos de Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipos de Usuário')
plt.show(block=True)


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = f"O User Type == Customer aparece com o Gender = '' ou Null, esse Null corresponde a um total de {unknowns} registros"
print("resposta:", answer)
try:
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
    # -----------------------------------------------------
except AssertionError as e:
        print(f"Error on assertion: {e}")

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = [float(i) for i in column_to_list(data_list, 2)]
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
# trip_duration_list = [float(i) for i in trip_duration_list]
trip_duration_list.sort()

min_trip = trip_duration_list[0]
max_trip = trip_duration_list[-1]
trip_duration_list = numpy.array(trip_duration_list).astype(numpy.int)
mean_trip = numpy.mean(trip_duration_list)
median_trip = numpy.median(trip_duration_list)


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)
try:
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
    assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
    assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
    assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
    # -----------------------------------------------------
except (AssertionError) as e:
        print(f"Error on assertion: {e}")

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)
try:
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
    # -----------------------------------------------------
except AssertionError as e:
        print(f"Error on assertion: {e}")

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
Função de exemplo com anotações.
Argumentos:
    param1: O primeiro parâmetro.
    param2: O segundo parâmetro.
Retorna:
    Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
answer = str(input("Você vai encarar o desafio? (yes ou no)"))
answer = 'no' if answer == '' else answer

# Função tá pronta na linha 28 - Ele está lá para também ser usada na Tarefa 7

if answer == "yes":
    try:
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
        column_list = column_to_list(data_list, -2)
        types, counts = count_items(column_list)
        print("\nTAREFA 12: Imprimindo resultados para count_items()")
        print("Tipos:", types, "Counts:", counts)
        assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
        assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
    except AssertionError as e:
        print(f"Error on assertion: {e}")
