import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64


# set full screen width
st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## Remove background from your image")
st.write(
    ":dog: Try uploading an image to see the before and after. Full quality images can be downloaded from the sidebar. This code is open source and available on GitHub. Special thanks to the [rembg library](https://github.com/danielgatis/rembg) :grin:"
)
st.sidebar.write("## Upload and settings :gear:")


# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


col1, col2 = st.columns(2)

my_image = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
# alpha_matting = st.sidebar.checkbox("Include alpha matting (can sometimes improve removal)", value=False)
# if alpha_matting:
#     alpha_matting_background_threshold = st.sidebar.number_input(
#         "Alpha matting background", value=10, min_value=0, max_value=2000, step=1
#     )
#     alpha_matting_foreground_threshold = st.sidebar.number_input(
#         "Alpha matting foreground", value=240, min_value=0, max_value=500, step=5
#     )


if my_image is not None:
    image = Image.open(my_image)
    col1.write("Original Image :camera:")
    col1.image(image)
#     if alpha_matting:
#         fixed = remove(
#             image,
#             alpha_matting=alpha_matting,
#             alpha_matting_background_threshold=alpha_matting_background_threshold,
#             alpha_matting_foreground_threshold=alpha_matting_foreground_threshold,
#         )
#     else:
    fixed = remove(image)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")
