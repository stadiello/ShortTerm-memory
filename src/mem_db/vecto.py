import chromadb
from chromadb.errors import NotFoundError

chroma_client = chromadb.PersistentClient(path="./chroma_memory")
    

def get_or_create_collection(collection_name):
    try:
        return chroma_client.get_collection(name=collection_name)
    except NotFoundError:
        return chroma_client.create_collection(name=collection_name)