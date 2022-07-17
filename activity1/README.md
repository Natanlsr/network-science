# Redes Complexas
Primeiro Trabalho de implementação da disciplina Redes Complexas do Mestrado

## Grafo

![graph drawio](https://user-images.githubusercontent.com/39385060/162878029-d2580495-4e7d-44c2-9d83-11638afc88fd.png)

# Requisitos
 - Python 3 +
 - Matplotlib
    ```console 
     pip install matplotlib
     ```

# Execuçao
Após cumprir com os requisitos bastar rodar o arquivo main.py

# Saída:
   O programa monta a matriz de acordo com o arquivo input.txt, após isso realiza:

## Grafo não direcionado
### Matriz de adjacência 
```
     [[0, 1, 0, 0, 0, 0, 1], 
     [1, 0, 1, 1, 0, 0, 0], 
     [0, 1, 0, 0, 0, 0, 0], 
     [0, 1, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 1, 0], 
     [0, 0, 0, 0, 1, 0, 0], 
     [1, 0, 0, 0, 0, 0, 0]]
```
### Grau de cada nó
 ``` [2, 3, 1, 1, 1, 1, 1] ```
###  Grau médio
 ```  1.4285714285714286 ``` 
###  Distribuição de grau

![mygraph](https://user-images.githubusercontent.com/39385060/162878104-2974b9ed-a31e-4c63-9fbc-608fa4c457cb.png)

## Grafo direcionado
### Matriz de adjacência
```
    [[0, 1, 0, 0, 0, 0, 1], 
    [0, 0, 1, 1, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0]]
```
### Grau de cada nó de saída
``` [2, 2, 0, 0, 1, 0, 0] ```
### Grau de cada nó de entrada
``` [0, 1, 1, 1, 0, 1, 1] ```
###  Grau médio
```  0.7142857142857143 ```
###  Distribuição de graus de saída
![directed_graph_out_degree](https://user-images.githubusercontent.com/39385060/167320629-1b864bc2-41c2-4974-873e-5f6cb5a6ed22.png)

###  Distribuição de graus de entrada
![directed_graph_in_degree](https://user-images.githubusercontent.com/39385060/167320657-de7f10d5-76aa-46a7-bc23-f6b8fbd180d2.png)
