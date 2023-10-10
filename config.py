from dotenv import load_dotenv
import os

load_dotenv()

marqo_url :str = os.getenv("MARQO_URL", "localhost:8882")
index_name :str = os.getenv("INDEX_NAME", "default")
chunk_size :int = int(os.getenv("CHUNK_SIZE", 1000))
chunk_overlap :int = int(os.getenv("CHUNK_OVERLAP", 0))
ollama_url :str = os.getenv("OLLAMA_URL", "localhost:11434")
model_name :str = os.getenv("MODEL_NAME", "llama2")
temprature :float = float(os.getenv("TEMPRATURE", 0.7))
file_index : str = os.getenv("FILE_INDEX", "files")
llm : str = os.getenv("LLM", "llama")
