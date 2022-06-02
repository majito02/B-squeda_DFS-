# Importar libreria queue
from queue import Queue

# Declarar clase Grafo


class Grafo:
    """
    Clase para representar un grafo

    ...

    Atributos
    ----------
    m_num_de_nodos : entero
        numero de nodos de grafo
    m_nodos : range
        rango de nodos
    m_dirigido : booleano
        Estado de dirigido
    m_lista_adyacencia : Colección de tipo diccionario
        Lista de ayacencia

    Metodos
    -------
    agregar_arista(nodo1, nodo2, peso=1):
         Agregar arista al grafo.

    imprimir_lista_adyacente():
        Imprimir la representación del grafo

    bfs_transversal(nodo_inicial):
         Imprimir el recorrido BFS de un vértice fuente dado.

    """
    # Se establece el constructor con los atributos

    def __init__(self, num_de_nodos, dirigido=True):
        """
        Construye todo los atributos necesarios para el objeto Grafo.

        Parametros
        ----------
            num_de_nodos : entero
                Numero de nodos de grafo
            dirigido : booleano
                Estado de dirigido
        """
        # atributos sef.m_num_de_nodos será igual al número de nodos
        self.m_num_de_nodos = num_de_nodos
        # Rango con numero de nodos
        self.m_nodos = range(self.m_num_de_nodos)
        # Dirigino o no dirigido
        self.m_dirigido = dirigido
        # Usamos un diccionario para implementar una lista de adyacencia
        self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}

    def agregar_arista(self, nodo1, nodo2, peso=1):
        """
        Agrega un arista al Grafo

        Si el argumento peso no es pasado,  toma como valor por defecto 1

        Parametros
        ----------
        nodo1 : entero
            Número de nodo1
        nodo2 : entero
            Número de nodo2
        peso : entero (opcional)
            Peso del arista. por defecto 1.

        Retorna
        -------
        None
        """

        # Agregar nodo2 a lista en nodo1
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))
        # No Dirigido?
        if not self.m_dirigido:
            # Agregar nodo 1 a lista en nodo2
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))

    def imprimir_lista_adyacente(self):
        """
        Imprime la lista de adyacencia

        Parametros
        ----------
        Ninguno

        Retorna
        -------
        nodo$(llave): {m_lista_adyacencia[llave]}
        """

        # Recorre por la lista de adyacencia
        for llave in self.m_lista_adyacencia.keys():
            # Imprimir nodo con la lista de adyacencia
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])

    def dfs_transversal(self, inicial, objetivo, ruta=[], visitado=set()):
        """
        Imprime el recorrido DFS de un vértice fuente dado.

        Parametros
        ----------
        inicial : entero
            Nodo inicial
        objetivo : entero
            Nodo objetivo
        ruta : list
            Lista de nodos recorridos
        visitado : set
            Conjunto de nodos visitados
        """

        # Agregar inicial a ruta
        ruta.append(inicial)
        # Agregar inicial a visitado
        visitado.add(inicial)

        # Si el nodo inicial es igual al objetivo
        if inicial == objetivo:
            # Imprimir ruta
            return ruta
    