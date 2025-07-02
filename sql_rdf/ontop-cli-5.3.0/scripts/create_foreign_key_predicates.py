import json

# Carga el archivo del esquema
with open("./sql_rdf/ontop-cli-5.3.0/archivos_generados/schema_metadata_enriched.json", encoding="utf-8") as f:
    schema = json.load(f)

# Diccionario para almacenar las relaciones semánticas
foreign_key_predicates = {}

# Generar predicados por cada relación entre tablas
for table_name, info in schema.items():
    for fk in info.get("foreign_keys", []):
        key = (table_name, fk["references_table"])
        predicate_uri = f"http://bdovidiana.es/ontology/refTo{fk['references_table'].capitalize()}"
        foreign_key_predicates[key] = predicate_uri

# Guardar en JSON
with open("./sql_rdf/ontop-cli-5.3.0/archivos_generados/FOREIGN_KEY_PREDICATES.json", "w", encoding="utf-8") as f:
    json.dump(
        {f"{k[0]}->{k[1]}": v for k, v in foreign_key_predicates.items()},
        f, indent=2, ensure_ascii=False
    )

print("FOREIGN_KEY_PREDICATES.json generado correctamente.")
