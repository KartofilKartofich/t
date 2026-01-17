import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates

value = streamlit_image_coordinates("IMG_7195.PNG",
                                    #height=480, 
                                    width=st.secrets["width"],
                                    #use_column_width="always", # always нельзя использовать, меняются координаты при изменении размера вкладки
                                    #use_column_width="auto",
                                    cursor="crosshair")#'always')
st.write(value)
