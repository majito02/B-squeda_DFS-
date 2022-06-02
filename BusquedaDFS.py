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
        # Para cada nodo adyacente al inicial que no haya sido visitado aún
        for (vecino, peso) in self.m_lista_adyacencia[inicial]:
            # Si el vecino no ha sido visitado
            if vecino not in visitado:
                # Recursividad para el vecino y el objetivo
                resultado = self.dfs_transversal(vecino, objetivo, ruta, visitado) 
                # Si el resultado no es None
                if resultado is not None:
                    # Retorna la otra ruta
                    return resultado
        
        # Al no entonctrar la ruta, retorna None
        return None 

#Verificacion de script ejecutado como principal
if __name__ == "__main__":

    # Crear una instancia de la Clase Grafo con 5 nodos
    grafo = Grafo(5,dirigido=False)
    # Agregar arista al grafo con pesos distintos
    grafo.agregar_arista(2, 4, 2)
    grafo.agregar_arista(1, 0, 3)
    grafo.agregar_arista(3, 4, 4)
    grafo.agregar_arista(1, 3, 3)
    grafo.agregar_arista(2, 3, 2)
  
    #Imprimir lista de adyacencia del grafo en consola
    grafo.imprimir_lista_adyacente()

    ruta_rec= []
    ruta_rec = grafo.dfs_transversal(0, 3)
    print(f"El recorrido de la ruta del nodo 0  es {ruta_rec}")

    # Crear una instancia de la Clase Grafo
    grafo = Grafo(6, dirigido=False)

    # Agrega aristas al grafo con pesos de 1
    grafo.agregar_arista(5, 0)
    grafo.agregar_arista(2, 5)
    grafo.agregar_arista(3, 4)
    grafo.agregar_arista(1, 2)
    grafo.agregar_arista(4, 5)
    grafo.agregar_arista(2, 3)
    
    # Imprimir lista de adyacencia del grafo en consola
    grafo.imprimir_lista_adyacente()
    
    # Lista de nodos recorridos
    ruta_rec= [] 
    # Recorrido del nodo 0 al 5
    ruta_rec = grafo.dfs_transversal(0, 5)
    # Imprimir recorrido DFS del grafo en consola 
    print(f"El recorrido de la ruta del nodo 0 es {ruta_rec}")



    # Crear una instancia de la Clase Grafo
    grafo = Grafo(7, dirigido=False)

    # Agrega aristas al grafo con pesos de 1
    grafo.agregar_arista(1, 3)
    grafo.agregar_arista(2, 4)
    grafo.agregar_arista(4, 5)
    grafo.agregar_arista(6, 0)
    grafo.agregar_arista(3, 6)
    grafo.agregar_arista(2, 5)
    grafo.agregar_arista(6, 2)
    
    # Imprimir lista de adyacencia del grafo en consola
    grafo.imprimir_lista_adyacente()
    
    # Lista de nodos recorridos
    ruta_rec= [] 
    # Recorrido del nodo 0 al 5
    ruta_rec = grafo.dfs_transversal(0, 4)
    # Imprimir recorrido DFS del grafo en consola 
    print(f"El recorrido de la ruta del nodo 0 es {ruta_rec}")