# Conceito de Árvore — Estrutura de Dados

Repositório desenvolvido para aplicar e consolidar conceitos de **árvores binárias** em Python, explorando desde a representação de expressões matemáticas até Árvores Binárias de Busca (BST) e algoritmos de travessia.

---

## 📑 Índice

- [Sobre](#sobre)  
- [Atividades](#atividades)  
  - [Atividade 1 — Árvore de Expressões Matemáticas](#atividade-1--árvore-de-expressões-matemáticas)  
  - [Atividade 2 — Árvore Binária de Busca (BST)](#atividade-2--árvore-binária-de-busca-bst)  
  - [Atividade 3 — Travessias em Árvores Binárias](#atividade-3--travessias-em-árvores-binárias)  
- [Tecnologias Utilizadas](#tecnologias-utilizadas)  
- [Como Executar](#como-executar)  
- [Aprendizado Esperado](#aprendizado-esperado)  
- [Contribuições](#contribuições)  
- [Licença](#licença)  
- [Autor](#autor)  

---

## 📖 Sobre

Este repositório foi criado como material de estudo para entender **estruturas de dados em árvore**.  
Cada atividade apresenta um desafio incremental que explora desde a construção de árvores simples até operações mais complexas, como **inserção, remoção, busca e travessias (DFS)**.

---

## 📝 Atividades

### Atividade 1 — Árvore de Expressões Matemáticas  

**Objetivo:**  
Modelar expressões matemáticas em forma de **árvore binária**, onde os nós internos são operadores e os nós folhas são operandos.

**O que foi implementado:**  
- Conversão de uma expressão linear (string) em árvore binária.  
- Construção da árvore para a expressão fixa:  (( (7 + 3) * (5 - 2) ) / (10 * 20))
- Visualização da árvore usando biblioteca gráfica.  
- Geração de **expressões matemáticas aleatórias** e criação da árvore correspondente.  

**Resultados esperados:**  
- Exibição gráfica da árvore fixa.  
- Exibição gráfica de uma árvore gerada com valores aleatórios.  

---

### Atividade 2 — Árvore Binária de Busca (BST)

**Objetivo:**  
Implementar operações fundamentais de uma **Árvore Binária de Busca (Binary Search Tree)**.

**O que foi implementado:**  
- Classe `BinarySearchTree` com os métodos:  
- `insert(valor)` — inserir novo nó.  
- `search(valor)` — buscar elemento.  
- `delete(valor)` — remover nó (folha, 1 filho ou 2 filhos).  
- `height()` — altura total da árvore.  
- `depth(valor)` — profundidade de um nó específico.  

**Demonstrações:**  
- Árvore com valores fixos `[55, 30, 80, 20, 45, 70, 90]`.  
- Visualização da árvore.  
- Busca, remoção e nova inserção.  
- Impressão da **altura da árvore** e **profundidade do nó 45**.  

- Árvore com valores randômicos:  
- Geração de 15 números inteiros aleatórios.  
- Construção da árvore correspondente.  
- Exibição da árvore e impressão da altura.  

---

### Atividade 3 — Travessias em Árvores Binárias

**Objetivo:**  
Implementar e demonstrar os algoritmos clássicos de **travessia em profundidade (DFS)**.

**O que foi implementado:**  
- Métodos de travessia:  
- `inorder()` — Esquerda → Raiz → Direita.  
- `preorder()` — Raiz → Esquerda → Direita.  
- `postorder()` — Esquerda → Direita → Raiz.  

**Demonstrações:**  
- Árvore com valores fixos `[55, 30, 80, 20, 45, 70, 90]`.  
- Visualização gráfica.  
- Impressão dos três tipos de travessia.  

- Árvore com valores randômicos (10 inteiros aleatórios).  
- Visualização gráfica.  
- Impressão clara dos três resultados de travessia.  

---

### Atividade 4 — Árvore AVL com Rotações  

**Objetivo:**  
Compreender a importância do **balanceamento em árvores de busca** e implementar uma **Árvore AVL**, incluindo cálculo do fator de balanceamento e rotações.

**O que foi implementado:**  
- Classe `AVLTree` em Python.  
- Inserção com verificação de balanceamento.  
- Rotações suportadas:  
  - Simples à Direita  
  - Simples à Esquerda  
  - Dupla Direita  
  - Dupla Esquerda  
- Cálculo do fator de balanceamento de cada nó.  

**Demonstrações:**  
- Árvore com valores fixos:  
  - Inserção da sequência `[10, 20, 30]`, mostrando rotação simples.  
  - Inserção da sequência `[10, 30, 20]`, mostrando rotação dupla.  
- Árvore com valores randômicos:  
  - Inserção de 20 inteiros aleatórios.  
  - Visualização final comprovando que a árvore mantém **altura mínima** e **balanceamento automático**.  

**Critérios de avaliação:**  
- Implementação correta do fator de balanceamento.  
- Rotações funcionando nos quatro casos.  
- Clareza na demonstração gráfica do balanceamento.  

---

### Atividade 5 — Implementação Completa de Árvore AVL  

**Objetivo:**  
Implementar **do zero** a lógica de uma Árvore AVL em Python, com suporte a:  
- Inserção balanceada.  
- Deleção com balanceamento.  
- Busca por valores e intervalos.  
- Cálculo da profundidade de um nó.  

**O que foi implementado:**  
- Classe `ArvoreAVL` e classe auxiliar `No`.  
- Métodos auxiliares:  
  - `obter_altura`  
  - `obter_fator_balanceamento`  
  - `obter_no_valor_minimo`  
  - Atualização de altura  
- Rotações:  
  - Direita  
  - Esquerda  
  - Duplas (quando necessário)  
- Operações principais:  
  - `inserir`  
  - `deletar`  
  - `encontrar_nos_intervalo`  
  - `obter_profundidade_no`  

**Demonstrações:**  
- Inserção da sequência `[9, 5, 10, 0, 6, 11, -1, 1, 2]`.  
- Deleção de nós `[10, 11]`.  
- Busca de nós dentro do intervalo `[1, 9]`.  
- Cálculo da profundidade do nó `6`.  

**Critérios de avaliação:**  
- Implementação funcional de inserção e deleção com balanceamento.  
- Métodos de busca funcionando corretamente.  
- Estrutura da árvore se mantém como uma **AVL válida** após cada operação.  

---

## ⚙️ Tecnologias Utilizadas

- **Linguagem:** Python 3.8+  
- **Bibliotecas:**  
- `graphviz` ou similar (para visualização gráfica das árvores)  
- `random` (para geração de números e expressões aleatórias)  

---

## ▶️ Como Executar

1. Clone o repositório:
 ```bash
 git clone https://github.com/Kosta-dev/Conceito-de-Arvore---Estrutura-de-dados.git
 cd Conceito-de-Arvore---Estrutura-de-dados



