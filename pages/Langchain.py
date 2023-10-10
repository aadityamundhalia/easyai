import streamlit as st
from repository.IndexRepository import IndexRepository
from repository.PromptRepository import PromptRepository
from langchain.chat_models import ChatOllama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatLiteLLM
from service.IndexService import IndexService

index_name = "langchain"
indexRepository = IndexRepository(index_name)
promptRepository = PromptRepository()
ollamaPath = "http://ollama:11434"
modelName = "mistral"
temperature = 0.1

vectorstore = indexRepository.vestorstore()

st.title("Langchain")

chat_model = ChatOllama(
                base_url=ollamaPath,
                model=modelName,
                temperature=temperature,
                callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
                verbose=True
            )
# chat_model = ChatLiteLLM(
#     model="ollama/mistral", 
#     api_base=ollamaPath,
#     temperature=temperature,
#     stream=True
# )

qa = RetrievalQA.from_chain_type(
                chat_model,
                retriever=vectorstore.as_retriever(),
                chain_type_kwargs={"prompt": promptRepository.basicPrompt()},
            )

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = qa({"query": prompt})['result']
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

with st.sidebar:
    uploadedfile = st.file_uploader("Upload")
    if uploadedfile is not None:
        uploadService = UploadService(uploadedfile)
        st.write(uploadService.embedFile())

    indexRepository = IndexService("files")
    for row in indexRepository.getDocuments("*")['hits']:
        st.write(row.get('filePath', ""))
