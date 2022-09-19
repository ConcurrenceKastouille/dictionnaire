                 # Compréhension des dictionnaires

# Je crée un dictionnaire avec comme nom "logins". Un dictionnaire fonctionne
# avec une valeur et la clé(=nom de la valeur, là où elle sera stocké dans le
# dictionnaire). Un dictionnaire n'a pas d'ordre, donc pas d'indices.

logins={"vonneumann":"azerty","jobs":"12345","bernerslee":"mdp","vanrossum":"toto"}

# Je crée une liste par compréhension comportant toutes les clés de logins

L=[x for x in logins.keys()]

# J'échange les valeurs de deux clés de logins

logins["bernerslee"],logins["vanrossum"]=logins["vanrossum"],logins["bernerslee"]

# Pour changer la clé d'une valeur, il faut recréer une clé en lui mettant
# la valeur de sa clé actuelle, puis la supprimer pour qu'elle ne soit
# pas en doublon

logins["VON-NEUMANN"]=logins["vonneumann"]
logins.pop("vonneumann")

# Testez par vous même avec vos propres dictionnaires afin de mieux comprendre
# le comportement des dictionnaires


