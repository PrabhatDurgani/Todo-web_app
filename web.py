import streamlit as st
import functions

todos = functions.get_todos()

<<<<<<< HEAD
st.set_page_config(layout="wide",
                   page_title="Todo_app",
                   page_icon="🧊")

=======
>>>>>>> 2893ee3b832af860df7809260a132be6c9ed5608
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("ToDo-App")
st.subheader("This is my todo app.")
<<<<<<< HEAD
st.write("This app is build to increase <b>productivity</b>.",
         unsafe_allow_html=True)

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
=======
st.write("This app is build to increase productivity.")

>>>>>>> 2893ee3b832af860df7809260a132be6c9ed5608

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

<<<<<<< HEAD
=======
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
>>>>>>> 2893ee3b832af860df7809260a132be6c9ed5608

print("hello")