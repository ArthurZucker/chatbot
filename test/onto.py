#!/usr/bin/env python

# -*- coding: utf-8 -*-

from os.path import dirname, realpath

from owlready2 import *

#https://pythonhosted.org/Owlready2/

onto_path.append(dirname(dirname(realpath(__file__))) + "/ontology/")
ontologyGoT_path = onto_path[0] + "ontologyGoT.owl"
ontologyGoT = get_ontology("file://" + ontologyGoT_path).load()

# creation d une nouvelle ontologie
# new_ontology_IRI = "http://www.semanticweb.org/jerome/ontologies/2019/3/newOntologyGoT.owl"
# newOntologyGoT_path = onto_path[0] + "newOntologyGoT.owl"
# newGoT = get_ontology(new_ontology_IRI)

# for entities in ontologyGoT.properties():
	# print("isLoyalTo" == entities.name)
def main():
	ontologyGoT = get_ontology("file://" + ontologyGoT_path).load()
	# print("\nListe des classes :\n",list(GoT.classes()))
	# print("\nListe des instances :\n",list(ontologyGoT.individuals()))
	# print("\nListe des propriétés objet :\n",list(ontologyGoT.object_properties()))
	# print("\nListe des propriétés data :\n",list(GoT.data_properties()))
	# print("\nListe des propriétés :\n",list(GoT.properties()))
	#
	# print("\nListe des sous-classes de Place :\n",\
	# GoT.search(subclass_of = GoT.Place))
	# print("\nListe des entites avec le mot desire :\n",\
	# ontologyGoT.search(iri = "*was*"))
	# print("\nListe des instances de Place :\n",\
	# GoT.search(type = GoT.Place))
	# print("\nListe des entites avec la relation desiree :\n",\
	# GoT.search(isLoyalTo = "*"))
	# print("\nListe des entites de Place :\n",\
	# GoT.search(is_a = GoT.Place))

	# liste des proprietes
	# print(dir(ontologyGoT.Jon_Snow),'\n')
	# print(ontologyGoT.Jon_Snow.__getattr__("isLoyalTo"))
	# print(type((dir(ontologyGoT.Jon_Snow)[-9])))
	# print(ontologyGoT.TheWesterlands.__dict__,'\n')

	# ajout d une propriete
	# print(ontologyGoT.Jaqen_h_ghar.comment)
	# GoT.Jon_Snow.isLoyalTo.append(GoT.Arya_Stark)
	# print(GoT.Jon_Snow.isLoyalTo)
	# print(GoT.Arya_Stark in GoT.Jon_Snow.isLoyalTo)
	search = ontologyGoT.search_one(iri = "*"+"Jon"+"*")
	print(search)
	if search:
		print("yes")
	# sauvegarde dans un nouveau fichier
	# GoT.save(file = onto_path[0] + "newOntologyGoT.owl")
	# ontologyGoT.save()

if __name__ == "__main__":
	main()
