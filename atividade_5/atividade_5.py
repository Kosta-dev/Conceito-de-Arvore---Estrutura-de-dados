# -*- coding: utf-8 -*-

class No:
    """
    Representa um nó na Árvore AVL.
    Cada nó armazena uma chave, referências para os filhos e sua altura.
    """
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1 # A altura de um novo nó (folha) é sempre 1

class ArvoreAVL:
    """
    Implementa a estrutura e as operações de uma Árvore AVL.
    """
    def __init__(self):
        self.raiz = None

    # ===============================================================
    # TAREFA 0: IMPLEMENTAR MÉTODOS AUXILIARES E ROTAÇÕES
    # ===============================================================

    def obter_altura(self, no):
        """
        Calcula a altura de um nó. Se o nó for nulo, a altura é 0.
        """
        if no is None:
            return 0
        return no.altura

    def obter_fator_balanceamento(self, no):
        """
        Calcula o fator de balanceamento de um nó (altura da subárvore esquerda - altura da subárvore direita).
        """
        if no is None:
            return 0
        return self.obter_altura(no.esquerda) - self.obter_altura(no.direita)

    def _atualizar_altura(self, no):
        """
        Atualiza a altura de um nó com base na altura máxima de seus filhos.
        A altura é 1 + max(altura(esquerda), altura(direita)).
        """
        if no is None:
            return
        no.altura = 1 + max(self.obter_altura(no.esquerda), self.obter_altura(no.direita))

    def obter_no_valor_minimo(self, no):
        """
        Encontra o nó com o menor valor em uma subárvore (o nó mais à esquerda).
        """
        atual = no
        while atual is not None and atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def _rotacao_direita(self, no_pivo):
        """
        Realiza uma rotação para a direita em torno do no_pivo.
        Retorna a nova raiz da subárvore.
        """
        y = no_pivo.esquerda
        T3 = y.direita

        # Rotaciona
        y.direita = no_pivo
        no_pivo.esquerda = T3

        # Atualiza alturas
        self._atualizar_altura(no_pivo)
        self._atualizar_altura(y)

        # Retorna nova raiz
        return y

    def _rotacao_esquerda(self, no_pivo):
        """
        Realiza uma rotação para a esquerda em torno do no_pivo.
        Retorna a nova raiz da subárvore.
        """
        y = no_pivo.direita
        T2 = y.esquerda

        # Rotaciona
        y.esquerda = no_pivo
        no_pivo.direita = T2

        # Atualiza alturas
        self._atualizar_altura(no_pivo)
        self._atualizar_altura(y)

        # Retorna nova raiz
        return y

    # ===============================================================
    # TAREFA 1: IMPLEMENTAR INSERÇÃO E DELEÇÃO COM BALANCEAMENTO
    # ===============================================================

    def inserir(self, chave):
        """Método público para inserir uma chave na árvore."""
        self.raiz = self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no_atual, chave):
        # Passo 1: Realiza a inserção padrão de uma BST.
        # (Se o nó atual for nulo, cria um novo nó e o retorna)
        # (Se a chave for menor, continua a busca na subárvore esquerda)
        # (Se a chave for maior, continua a busca na subárvore direita)
        # (Se a chave for igual, lança um erro, pois não permitimos duplicatas)
        if no_atual is None:
            return No(chave)

        if chave < no_atual.chave:
            no_atual.esquerda = self._inserir_recursivo(no_atual.esquerda, chave)
        elif chave > no_atual.chave:
            no_atual.direita = self._inserir_recursivo(no_atual.direita, chave)
        else:
            # Chaves duplicadas não são permitidas em BST/AVL
            raise ValueError(f"Chave {chave} já existe na árvore.")

        # ---- LÓGICA DE BALANCEAMENTO AVL (A IMPLEMENTAR) ----
        # Passo 2: Atualiza a altura do nó atual (ancestral) após a inserção.
        self._atualizar_altura(no_atual)

        # Passo 3: Calcula o fator de balanceamento para verificar se o nó ficou desbalanceado.
        fator = self.obter_fator_balanceamento(no_atual)

        # Passo 4: Verifica se o nó ficou desbalanceado e aplica as rotações corretas.
        # Caso 1: Desbalanceamento à Esquerda-Esquerda (Rotação Simples à Direita)
        if fator > 1 and chave < no_atual.esquerda.chave:
            return self._rotacao_direita(no_atual)

        # Caso 2: Desbalanceamento à Direita-Direita (Rotação Simples à Esquerda)
        if fator < -1 and chave > no_atual.direita.chave:
            return self._rotacao_esquerda(no_atual)

        # Caso 3: Desbalanceamento à Esquerda-Direita (Rotação Dupla)
        if fator > 1 and chave > no_atual.esquerda.chave:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        # Caso 4: Desbalanceamento à Direita-Esquerda (Rotação Dupla)
        if fator < -1 and chave < no_atual.direita.chave:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)

        # Retorna o nó (potencialmente a nova raiz da subárvore após rotação).
        return no_atual

    def deletar(self, chave):
        """Método público para deletar uma chave da árvore."""
        self.raiz = self._deletar_recursivo(self.raiz, chave)

    def _deletar_recursivo(self, no_atual, chave):
        # Passo 1: Realiza a deleção padrão de uma BST.
        # (Se o nó atual for nulo, retorna o próprio nó)
        # (Navega para a esquerda ou direita para encontrar o nó a ser deletado)
        # (Quando o nó é encontrado, trata os três casos de deleção)
        #     Caso 1: Nó com um filho ou nenhum filho.
        #     Caso 2: Nó com dois filhos (encontra o sucessor, copia e deleta o sucessor).
        if no_atual is None:
            return no_atual

        if chave < no_atual.chave:
            no_atual.esquerda = self._deletar_recursivo(no_atual.esquerda, chave)
        elif chave > no_atual.chave:
            no_atual.direita = self._deletar_recursivo(no_atual.direita, chave)
        else:
            # Nó encontrado
            # Caso 1: Um filho ou nenhum
            if no_atual.esquerda is None:
                temp = no_atual.direita
                no_atual = None
                return temp
            elif no_atual.direita is None:
                temp = no_atual.esquerda
                no_atual = None
                return temp

            # Caso 2: Dois filhos -> pegar o sucessor (menor na subárvore direita)
            temp = self.obter_no_valor_minimo(no_atual.direita)
            no_atual.chave = temp.chave
            # Deleta o sucessor na subárvore direita
            no_atual.direita = self._deletar_recursivo(no_atual.direita, temp.chave)

        # ---- LÓGICA DE BALANCEAMENTO AVL APÓS DELEÇÃO (A IMPLEMENTAR) ----
        # Passo 2: Atualiza a altura do nó atual.
        if no_atual is None:
            return no_atual

        self._atualizar_altura(no_atual)

        # Passo 3: Calcula o fator de balanceamento.
        fator = self.obter_fator_balanceamento(no_atual)

        # Passo 4: Verifica o desbalanceamento e aplica as rotações.
        # Caso Left-Left
        if fator > 1 and self.obter_fator_balanceamento(no_atual.esquerda) >= 0:
            return self._rotacao_direita(no_atual)

        # Caso Left-Right
        if fator > 1 and self.obter_fator_balanceamento(no_atual.esquerda) < 0:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        # Caso Right-Right
        if fator < -1 and self.obter_fator_balanceamento(no_atual.direita) <= 0:
            return self._rotacao_esquerda(no_atual)

        # Caso Right-Left
        if fator < -1 and self.obter_fator_balanceamento(no_atual.direita) > 0:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)

        # Retorna o nó (potencialmente a nova raiz da subárvore).
        return no_atual

    # ===============================================================
    # TAREFA 2 E 3: IMPLEMENTAR BUSCAS
    # ===============================================================

    def encontrar_nos_intervalo(self, chave1, chave2):
        """
        Encontra e retorna uma lista com todas as chaves no intervalo [chave1, chave2].
        """
        resultado = []
        def _recursao(no):
            if no is None:
                return
            # Se o valor atual for maior que chave1, então a subárvore esquerda
            # pode conter nós no intervalo
            if no.chave > chave1:
                _recursao(no.esquerda)
            # Se estiver no intervalo, adiciona
            if chave1 <= no.chave <= chave2:
                resultado.append(no.chave)
            # Se o valor atual for menor que chave2, a subárvore direita
            # pode conter nós no intervalo
            if no.chave < chave2:
                _recursao(no.direita)
        _recursao(self.raiz)
        return resultado

    def obter_profundidade_no(self, chave):
        """
        Calcula a profundidade (nível) de um nó com uma chave específica.
        A raiz está no nível 0. Se o nó não for encontrado, retorna -1.
        """
        nivel = 0
        atual = self.raiz
        while atual is not None:
            if chave == atual.chave:
                return nivel
            elif chave < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita
            nivel += 1
        return -1

    # Método auxiliar para debug: percurso em-ordem
    def percorrer_em_ordem(self):
        resultado = []
        def _inorder(no):
            if no is None:
                return
            _inorder(no.esquerda)
            resultado.append(no.chave)
            _inorder(no.direita)
        _inorder(self.raiz)
        return resultado

# --- Bloco de Teste e Demonstração da Atividade AVL ---
if __name__ == "__main__":
    arvore_avl = ArvoreAVL()
    
    print("\n--- ATIVIDADE PRÁTICA: ÁRVORE AVL ---")
    
    print("\n--- 1. Inserindo nós ---")
    chaves_para_inserir = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    try:
        for chave in chaves_para_inserir:
            arvore_avl.inserir(chave)
        print("Inserção concluída (sem erros).")
        print("Árvore em-ordem após inserções:", arvore_avl.percorrer_em_ordem())
    except Exception as e:
        print(f"\nERRO DURANTE A INSERÇÃO: {e}")

    print("\n--- 2. Deletando nós ---")
    try:
        chaves_para_deletar = [10, 11]
        for chave in chaves_para_deletar:
            arvore_avl.deletar(chave)
        print("Deleção concluída (sem erros).")
        print("Árvore em-ordem após deleções:", arvore_avl.percorrer_em_ordem())
    except Exception as e:
        print(f"\nERRO DURANTE A DELEÇÃO: {e}")

    print("\n--- 3. Buscando nós no intervalo [1, 9] ---")
    try:
        nos_no_intervalo = arvore_avl.encontrar_nos_intervalo(1, 9)
        if nos_no_intervalo is not None:
            print(f"Nós encontrados: {sorted(nos_no_intervalo)}")
        else:
            print("Método `encontrar_nos_intervalo` ainda não implementado.")
    except Exception as e:
        print(f"\nERRO DURANTE A BUSCA POR INTERVALO: {e}")

    print("\n--- 4. Calculando profundidade do nó 6 ---")
    try:
        profundidade = arvore_avl.obter_profundidade_no(6)
        if profundidade is not None:
            if profundidade != -1:
                print(f"O nó 6 está no nível/profundidade: {profundidade}")
            else:
                print("O nó 6 não foi encontrado.")
        else:
            print("Método `obter_profundidade_no` ainda não implementado.")
    except Exception as e:
        print(f"\nERRO DURANTE O CÁLCULO DE PROFUNDIDADE: {e}")