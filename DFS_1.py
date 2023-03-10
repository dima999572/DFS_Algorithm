import sys
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.max_node = 1

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # TWORZENIE GRAFU POCZĄTEK
    def creatingGraph(self):
        """It's a function, that help to create the graph in an interactive way. Here you can decide about the graph,
        are you preferring neighbourhood dictionaries or neighbourhood matrix, text file or inputting numbers by your
        own, it's only your decision! Enjoy"""

        print("\n----------------------------------")
        try:

            # WPROWADZENIE
            decision = int(input("Wpisz 1, jeśli twój graf będzie reprezentowany przez słownik sąsiedztwa, "
                                 "\nWpisz 2, jeśli twój graf będzie reprezentowany przez macierz sąsiedztwa: "))
            print("----------------------------------")

            gra = Graph()

            # GRAF W POSTACI SŁOWNIKU SĄSIEDZTWA
            if decision == 1:
                decision = int(
                    input("Wpisz 1, jeśli chcesz wpisać dane z klawiatury"
                          "\nWpisz 2, jeśli chcesz odczytać dane z pliku tekstowego: "))

                # GRAF, ODCZYTANY Z KLAWIATURY
                if decision == 1:
                    print("----------------------------------")
                    (a, b) = input("Wpisz liczbę wierzchołków i krawędzi, rozdzielając je spacją: ").split()
                    (a, b) = (int(a), int(b))  # a - liczba wierzchołków, b - liczba krawędzi

                    if a == 0 and b != 0:
                        print("----------------------------------"
                              "\nERROR! Nie może być 0 wierzchołków oraz nie 0 krawędzi")
                        return

                    elif a == 0 and b == 0:
                        print("----------------------------------"
                              "\nERROR! Wpisałeś 0 wierzchołków oraz 0 krawędzi, to nie jest graf")
                        return

                    self.max_node = a

                    print(f"----------------------------------\n"
                          f"WARNING! Dysponujesz wierzchołkami od {1} do {int(a)}")

                    # edge - licznik wierzchołków
                    for edge in range(1, b + 1):
                        (x, y) = input(f"Wpisz {edge} parę werzchołków: ").split()
                        (x, y) = (int(x), int(y))  # To dwa wierzchołki, takie że => x - from, y - to

                        # jeśli więcej, niż maks(a) liczba wierzchołków,
                        # lub mniej, niż min(1) liczba wierzchołków - BŁĄD
                        if x < 1 or y < 1 or x > a or y > a:
                            print(f"----------------------------------"
                                  f"\nERROR! Wpisałeś niedostępny wierzchołek! Dostępne tylko z przedziału [1,{a}]")
                            return

                        gra.addEdge(x, y)

                # GRAF, ODCZYTANY Z PLIKU TEKSTOWEGO
                elif decision == 2:
                    f = open("graph_slownik.txt").read().split("\n")

                    # a - liczba wierzchołków, b - liczba krawędzi
                    a, b = (int(f[0].split()[0]), int(f[0].split()[1]))

                    if len(f) - 1 != b:
                        print("----------------------------------"
                              "\nERROR! Musisz wpisać taką liczbe par wierzchołków, "
                              "żeby ona zgadzała się z liczbą krawędzi")
                        return

                    elif a == 0 and b != 0:
                        print("----------------------------------"
                              "\nERROR! Nie może być 0 wierzchołków oraz nie 0 krawędzi")
                        return

                    elif a == 0 and b == 0:
                        print("----------------------------------"
                              "\nERROR! Wpisałeś 0 wierzchołków oraz 0 krawędzi, to nie jest graf")
                        return

                    self.max_node = a

                    for edge in range(1, int((f[0].split())[1]) + 1):
                        # to dwa wierzchołki, takie że => x - from, y - to
                        x, y = (int(f[edge].split()[0]), int(f[edge].split()[1]))

                        # jeśli więcej, niż maks(a) liczba wierzchołków,
                        # lub mniej, niż min(1) liczba wierzchołków - BŁĄD
                        if x < 1 or y < 1 or x > a or y > a:
                            print(f"----------------------------------"
                                  f"\nERROR! Wpisałeś niedostępny wierzchołek! Dostępne tylko z przedziału [1,{a}]")
                            return

                        gra.addEdge(x, y)

                # ZŁY WYBÓR
                else:
                    print("----------------------------------"
                          "\nERROR! Wpisałeś ani 1 ani 2")
                    return

                # KONIEC
                self.graph = gra.graph
                print("----------------------------------")

            # GRAF W POSTACI MACIERZY SĄSIEDZTWA
            elif decision == 2:
                decision = int(
                    input("Wpisz 1, jeśli chcesz wpisać dane z klawiatury"
                          "\nWpisz 2, jeśli chcesz odczytać dane z pliku tekstowego: "))
                print("----------------------------------")

                # GRAF, ODCZYTANY Z KLAWIATURY
                if decision == 1:
                    a = int(input("Ile wierzchołków będzie miał twój graf: "))  # a - liczba wierzchołków
                    if a == 0:
                        print("----------------------------------"
                              "\nERROR! Nie może być 0 wierzchołków")
                        return

                    self.max_node = a

                    print("\n----------MACIERZ SĄSIEDZTWA----------")
                    print("WARNING! Uzupełnij wiersz, wpisując 0 lub 1, roździelając spacją")

                    # wiersz to licznik, wskazujący na którym wierszu obecnie jesteśmy
                    for wiersz in range(1, a + 1):
                        temp = 1  # zmienna, która wskazuje na key w dictionaries
                        wierszy = list(input(f"Wiersz {wiersz}: ").split())  # zmienna, która przechowuje wiersze

                        if len(wierszy) != a:
                            print("----------------------------------"
                                  "\nERROR! Wpisałeś złą liczbę kolumn")
                            return

                        # i odpowiada za 0 i 1 w każdym z wierszów
                        for i in wierszy:
                            i = int(i)

                            if i != 0 and i != 1:
                                print("----------------------------------"
                                      "\nERROR! Macierz sąsiedztwa musi zawierać 1 i 0")
                                return

                            if i == 1:
                                gra.addEdge(wiersz, temp)

                            temp += 1

                # GRAF, ODCZYTANY Z PLIKU TEKSTOWEGO
                elif decision == 2:
                    f = open("graph_macierz.txt").read().split("\n")

                    a = len(f)  # liczba wierszy
                    temp1 = 1  # numer obecnego wierszu, lub key dla dictionaries

                    # "wiersz" odpowiada za przechowywanie wierszów, lub value dla dictionaries
                    for wiersz in f:
                        temp2 = 1  # obecny wierzcholek, lub key dla dictionaries
                        wierzcholki = wiersz.split()

                        if len(wierzcholki) != a:
                            print("ERROR! Wpisałeś złą liczbę kolumn oraz wierszy")
                            return

                        # "wierzcholek" odpowiada za 0 i 1 w wierszach
                        for wierzcholek in wierzcholki:
                            wierzcholek = int(wierzcholek)

                            if wierzcholek != 1 and wierzcholek != 0:
                                print("ERROR! Macierz sąsiedztwa musi zawierać 1 i 0")
                                return

                            if self.max_node < temp1:
                                self.max_node = temp1

                            if wierzcholek == 1:
                                gra.addEdge(temp1, temp2)

                            temp2 += 1
                        temp1 += 1

                    print("MACIERZ ZOSTAŁA ODCZYTANA SUKCESYWNIE")

                # ZŁY WYBÓR
                else:
                    print("----------------------------------"
                          "\nERROR! Wpisałeś ani 1 ani 2")
                    return

                self.graph = gra.graph
                print("----------------------------------")

            # ZŁY WYBÓR
            else:
                print("\nERROR! Wpisałeś ani 1 ani 2")
                return

        except ValueError as err:
            print(f"----------------------------------"
                  f"\nERROR! {err}")
            return

        except FileNotFoundError as err:
            print(print(f"----------------------------------"
                        f"\nERROR! {err}"))
            return

        except IndexError as err:
            print(print(f"----------------------------------"
                        f"\nERROR! {err}"))
            return

    # TWORZENIE GRAFU KONIEC

    def DFSUtil(self, start, visited, path=list()):
        visited.append(start)
        path.append(start)
        print(path)

        for neighbour in self.graph[start]:
            if neighbour in visited:
                visited.append(neighbour)
                print(f"Graf zawiera następujący cykl: {visited}")
                self.showGraph()

        for neighbour in self.graph[start]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
                
            path.pop()
            visited.pop()
            start = path[-1]

    def DFS(self):
        try:
            # wierzchołek, z którego będziemy startowali DFS
            start = int(input(f"WARNING! Dysponujesz wierzchołkami od {1} do {self.max_node}\n"
                              "Wybierz od jakiego wierzchołka będziemy zaczynali DFS: "))

            if start < 1 or start > int(self.max_node):
                print(f"----------------------------------"
                      f"\nERROR! Wybrałeś wierzchołek nie z podanego zakresu ")
                return

            print("---------------DFS---------------")

            visited = list()
            self.DFSUtil(start, visited)

        except ValueError as err:
            print(f"----------------------------------"
                  f"\nERROR! {err}")

    def showGraph(self):
        # tworzymy graf za pomocą modulu networkx
        grap = nx.DiGraph()
        temp = []

        # robimy temp, w którym będą krawędzi w postaci tuple
        for edges in self.graph:
            for neightbour in self.graph[edges]:
                temp.append((edges, neightbour))

        # dodajemy do grafa temp
        grap.add_edges_from(temp)

        # ustawiamy węzły za pomocą Fruchterman-Reingold force-directed algorytma
        pos = nx.spring_layout(grap)

        nx.draw_networkx_nodes(grap, pos, node_size=300)
        nx.draw_networkx_edges(grap, pos, edgelist=grap.edges(), edge_color='black')
        nx.draw_networkx_labels(grap, pos)

        # pokazujemy stworzony label
        plt.show()
        sys.exit(0)


g = Graph()
g.creatingGraph()

if g.graph != defaultdict(list):
    g.DFS()
    g.showGraph()