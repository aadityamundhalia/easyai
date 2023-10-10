import streamlit as st
from litellm import completion


def llm(messages):
    return completion(
            model="ollama/mistral",
            messages=[
                {
                    "content": m["content"],
                    "role": m["role"]
                }
                for m in messages
            ],
            api_base="http://ollama:11434",
            stream=True,
            temperature=0.8,
        )


st.set_page_config(
        page_title="EasyAi",
        page_icon=':maple_leaf:',
        layout="wide",
    )


if "messages" not in st.session_state:
    st.session_state.messages = []
    # response = ""
    # results = llm([{"role": "user", "content": ""}])
    # for result in results:
    #     response += result['choices'][0]['delta'].get("content", "")
    # st.session_state.messages.append({"role": "assistant", "content": response})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in llm(st.session_state.messages):
            full_response += response['choices'][0]['delta'].get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})


