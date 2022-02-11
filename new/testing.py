import requests
from collections import Counter

def rank_of_obs(
	iconic_taxa = "Aves",
	per_page = "200",
	# Coordenadas del bounding box.
	nelat = "-34.3153204479677",
	nelng = "-52.344795383944074",
	swlat = "-35.553690012709126",
	swlng= "-57.571540989412824"):
	""" Busca todas las observaciones en un bounding box determinado y crea un rango de la sp más vista a la menos."""
	res = requests.get("https://api.inaturalist.org/v1/observations?iconic_taxa=" + iconic_taxa + "&nelat=" + nelat + "&nelng="+ nelng +"&swlat="+ swlat +"&swlng="+ swlng +"&per_page="+ per_page +"&quality_grade=research&subview=map")
	res_json = res.json()
	observations = list()
	for obs in res_json["results"]:
	    observations.append(obs["taxon"]["name"])
	# Cuenta cuántas observaciones hay por especie.
	list_ = Counter(observations)
	# Crea un ranking de las más observadas a las menos.
	rank_ = list_.most_common()
	return rank_

def get_photo_of_sp(taxon_id, photo_license = "CC0"):
	# Busca última foto de un determinado taxón, donde el organismo esté vivo y la foto de licencia abierta.
	url = f"https://api.inaturalist.org/v1/observations?photo_license={photo_license}&popular&photos&quality_grade=research&taxon_id={taxon_id}&term_id=17&term_value_id=18&per_page=1"
	response = requests.get(url)
	response_json = response.json()
	url_img_square = str(response_json["results"][0]["photos"][0]["url"])
	url_img = url_img_square.replace("square", "large")
	img_owner = str(response_json["results"][0]["user"]["login"])
	observation = str(response_json["results"][0]["id"])
	return url_img, img_owner, observation

print(get_photo_of_sp(taxon_id="144504"))
