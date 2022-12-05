# ## Questão 1
#
# Você foi contratado pela seleção brasileira para fazer uma análise sobre as seleções adversárias. Sua primeira tarefa
# consiste em realizar uma contagem de quantos jogadores possuem a altura máxima.
#
# ### Exemplo
#
# Para a entrada:
#
# ```
# [180, 166, 170, 180]
# ```
#
# A saída deve ser:
#
# ```
# 2
# ```
#
# Isso porque existem dois jogadores com altura máxima (180).
#
# Para obter a nota máxima dessa questão, deve-se utilizar apenas um ``for`` e nenhuma função pronta do Python.

def q1(heights):
    x = max(heights)
    maior = 0
    for item in heights:
    if item == x:
        maior += 1  
    return maior


if __name__ == '__main__':
    print(q1([180, 166, 170, 180]))
