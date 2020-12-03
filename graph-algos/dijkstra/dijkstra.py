# Notes:
# Dijkstra berekent de kortste route van een bepaald punt naar alle punten

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

A = set()
X = set()

def init(begin):
    A.add(begin)
