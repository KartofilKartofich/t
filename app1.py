import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates

real_code = st.secrets["real_code"]

if "written_code" not in st.session_state:
    st.session_state["written_code"] = []

value = streamlit_image_coordinates("IMG_7195.PNG",
                                    #height=480, 
                                    width=st.secrets["width"],
                                    #use_column_width="always", # always нельзя использовать, меняются координаты при изменении размера вкладки
                                    #use_column_width="auto",
                                    cursor="crosshair")#'always')
st.write(value)

button_width = 54
button_height = 33
st.write(value)

if value:
    b_row = ""
    b_col = ""

    if value['x']>53 and value['x']<53+button_width:
        st.write("147x")
        b_row = "147x"
    elif value['x']>121 and value['x']<121+button_width:
        st.write("2580")
        b_row = "2580"
    elif value['x']>189 and value['x']<189+button_width:
        st.write("369v")
        b_row = "369v"

    if value['y']>231 and value['y']<231+button_height:
        st.write("123")
        b_col = "123"
    elif value['y']>276 and value['y']<276+button_height:
        st.write("456")
        b_col = "456"
    elif value['y']>321 and value['y']<321+button_height:
        st.write("789")
        b_col = "789"
    elif value['y']>366 and value['y']<366+button_height:
        st.write("789")
        b_col = "x0v"
    
    if b_row != "" and b_col != "": 
        letter_set = set(b_row)&set(b_col)
        st.write(letter_set)
        for letter in letter_set:
            if letter == "x":
                if len(st.session_state["written_code"])>0:
                    st.session_state["written_code"].pop()
            elif letter == "v":
                if "".join(st.session_state["written_code"]) == real_code:
                    st.write("Верный код")
                else: 
                    st.session_state["written_code"] = []
                    st.write("Неверный код")
            else:
                st.session_state["written_code"].append(letter)

st.write(st.session_state["written_code"])
st.text(len(st.session_state["written_code"])*"*")
