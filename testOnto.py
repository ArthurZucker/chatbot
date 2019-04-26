from owlready2 import *
#/path/to/your/local/ontology/repository
path = "/home/jerome/Informatique/chatbot/Ontology/"
file = "testOntologyGoT.owl"
GoT = get_ontology("file://" + path + file).load()

print("\nListe des classes :\n",list(GoT.classes()))
print("\nListe des instances :\n",list(GoT.individuals()))
print("\nListe des propriétés :\n",list(GoT.object_properties()))

print("\nListe des sous-classes de Place :\n",\
GoT.search(subclass_of = GoT.Place))
print("\nListe des entites avec le mot desire :\n",\
GoT.search(iri = "*City"))
print("\nListe des instances de Place :\n",\
GoT.search(type = GoT.Place))
print("\nListe des entites avec la relation desiree :\n",\
GoT.search(isFromHouse = "*"))

print("\nListe des parents de Jon Snow :\n",\
GoT.Jon_Snow.isChildOf)
