import requests
from collections import Counter

res = requests.get("https://api.inaturalist.org/v1/observations?iconic_taxa=Aves&nelat=-34.3153204479677&nelng=-52.344795383944074&place_id=any&quality_grade=research&subview=map&swlat=-35.553690012709126&swlng=-57.571540989412824&per_page=200")
res_json = res.json()

observations = list()
for obs in res_json["results"]:
    observations.append(obs["taxon"]["name"])

# Cuenta cuántas observaciones hay por especie.
list_of_obs = Counter(observations)
# Crea un ranking de las más observadas a las menos.
rank_of_obs = list_of_obs.most_common()