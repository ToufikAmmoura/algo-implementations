from math import inf

# NOTES:
# Dijkstra berekent de kortste route van een bepaald punt naar alle punten
# We moeten een class of struct maken voor iedere node want we moeten best wat dingen opslaan
#   - Totale afstand vanaf start
#   - Route van start naar de node
# Dit kan misschien in een dictionary met tuples (distance, "a->c->h->this")

# BEGIN:
# We verdelen de punten in drie groepen:
# A: de verzameling van punten waarvan de kortste afstand tot de begin-node berekend is
# X: de verzamleing van punten waarnaar er al wel een pad is berekend vanuit de begin knoop, maar niet de kortste, of we weten dit nog niet zeker
# A en X mogen geen nodes gelijk hebben want je kan niet al de kortste route al kennen terwijl je nog zoekend bent ernaar
# V = G-A-X: de overige punten (hoeven we gelukkig nergens op te slaan)
# A = {beginknoop}
# X = {knopen verbonden met begin knoop}
# distance van begin naar begin = 0
# alle andere knopen krijgen een distance van infinite

# ALGORITME:
# Neem de kortste route die er is, als je een node voor de eerste keer ontdekt dan zal dat de kortste route zijn om daar te komen
# x verplaats je nu van X naar A omdat die bepaald is, er zal geen snellere route zijn naar die node 

routes = {}

graph = {}

adjacencyMatrix = [[0,4,4,6,6,0,0,0,2],
                   [4,0,2,0,0,0,0,0,0],
                   [4,2,0,8,0,0,1,0,0],
                   [6,0,8,0,9,2,0,1,0],
                   [6,0,0,9,0,0,0,2,2],
                   [0,0,0,2,0,0,2,1,0],
                   [0,0,1,0,0,2,0,0,0],
                   [0,0,0,1,2,1,0,0,3],
                   [2,0,0,0,2,0,0,3,0] ]

A = set()
X = set()

def init(start, graphSize):
    for i in range(graphSize):
        graph[i] = (inf, "")
    A.add(start)

def dijkstra(start, destination, matrix):
    raise NotImplementedError()