from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF

# Cargar archivo original
g = Graph()
g.parse("datos_enriquecidos.ttl", format="ttl")

# Namespaces
ex = Namespace("http://example.org/")
g.bind("ex", ex)

# Lista de relaciones a actualizar: predicado, patrón base para URI
relaciones = [
    (ex.ContenidoFK, ex.contenido),
    (ex.EjemplarFK, ex.ejemplar),
    (ex.ObraFK, ex.obra),
    (ex.BibliotecaFK, ex.biblioteca),
    (ex.TemaFK, ex.tema),
    (ex.IlustracionFK, ex.ilustracionejemplar)
]

# Reemplazo de literales numéricos por URIs
nuevos_triples = []
triples_a_eliminar = []

for s, p, o in g:
    for predicado, base_uri in relaciones:
        if p == predicado and isinstance(o, Literal) and o.datatype is None:
            try:
                nuevo_obj = URIRef(f"{base_uri}/{int(o)}")
                nuevos_triples.append((s, p, nuevo_obj))
                triples_a_eliminar.append((s, p, o))
            except ValueError:
                continue

# Aplicar cambios
for t in triples_a_eliminar:
    g.remove(t)
for t in nuevos_triples:
    g.add(t)

# Guardar nuevo archivo
g.serialize("datos_enriquecidos_URIs.ttl", format="turtle")
print("Archivo actualizado guardado como datos_enriquecidos_URIs.ttl")
