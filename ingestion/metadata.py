def enrich_metadata(chunks):
    for chunk in chunks:
        chunk.metadata["source_type"]="PDF"
    return chunks