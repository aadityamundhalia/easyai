import streamlit as st
from service.IndexService import IndexService

tab1, tab2, tab3 = st.tabs(["Indexes", "Files", "Documents"])

with tab1:
    indexRepository = IndexService()
    indexes = indexRepository.listIndex()
    st.table(indexes)

with tab2:
    indexRepository = IndexService("files")
    st.table(indexRepository.getDocuments("*")['hits'])

with tab3:
    indexRepository = IndexService("langchain")
    st.table(indexRepository.getDocuments("*")['hits'])

