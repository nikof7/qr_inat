import requests
from collections import Counter

def rank_of_obs():
	res = requests.get("https://api.inaturalist.org/v1/observations?iconic_taxa=Aves&nelat=-34.3153204479677&nelng=-52.344795383944074&place_id=any&quality_grade=research&subview=map&swlat=-35.553690012709126&swlng=-57.571540989412824&per_page=200")
	res_json = res.json()

	observations = list()
	for obs in res_json["results"]:
	    observations.append(obs["taxon"]["name"])

	# Cuenta cuántas observaciones hay por especie.
	list_ = Counter(observations)
	# Crea un ranking de las más observadas a las menos.
	rank_ = list_of_obs.most_common()
	return print(rank_)

def get_id():
	res = requests.get("https://api.inaturalist.org/v1/observations?iconic_taxa=Aves&nelat=-34.3153204479677&nelng=-52.344795383944074&place_id=any&quality_grade=research&subview=map&swlat=-35.553690012709126&swlng=-57.571540989412824&per_page=1")
	res_json = res.json()
	id = res_json["results"][0]["id"]
	return id

def get_photo_link(id):
	url = "https://inaturalist-open-data.s3.amazonaws.com/photos/" + str(id) +  "/large.jpg"
	return print(url)


e = get_id()

get_photo_id(e)