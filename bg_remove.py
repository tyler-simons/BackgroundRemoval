import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO

st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## Remove background from your image")
st.write(
    ":dog: Try uploading an image to watch the background magically removed. Full quality images can be downloaded from the sidebar. This code is open source and available [here](https://github.com/tyler-simons/BackgroundRemoval) on GitHub. Special thanks to the [rembg library](https://github.com/danielgatis/rembg) :grin:"
)
st.sidebar.write("## Upload and download :gear:")

def changeColor(image):
    image = image.convert('L')
    return image
# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    
    st.sidebar.markdown("\n")
    if my_upload:
       filename = my_upload.name.split('.')[0]
       st.sidebar.download_button("Download fixed image", convert_image(fixed), f"{filename}_fixed.png", "image/png")
       options = ['original','grey', 'red', 'blue','green']
       selected_option = st.sidebar.selectbox('Select an Color', options)

       if selected_option!='original':
            if (selected_option=='grey'):
                grey_scale = changeColor(image)
                col1.write('Black and White')
                col1.image(grey_scale)
                col2.write('Gray Fixed')
                product= remove(grey_scale)
                col2.image(product)
                st.sidebar.download_button("Download fixed colored image", convert_image(product), f"{filename}_grey_fixed.png", "image/png")
            else:
                red_channel, green_channel, blue_channel = image.split()
                if selected_option == 'red':
                  color = 'Red'
                  scaled_image = Image.merge('RGB', (red_channel, Image.new('L', red_channel.size, 0), Image.new('L', red_channel.size, 0)))
                elif selected_option == 'blue':
                    color = 'Blue'
                    scaled_image = Image.merge('RGB', (Image.new('L', blue_channel.size, 0), Image.new('L', blue_channel.size, 0), blue_channel))
                else:
                    color = 'Green'
                    scaled_image = Image.merge('RGB', (Image.new('L', green_channel.size, 0), green_channel, Image.new('L', green_channel.size, 0)))

                col1.write(color)
                col1.image(scaled_image)
                col2.write(color + " Fixed")
                product = remove(scaled_image)
                col2.image(remove(product))
                st.sidebar.download_button("Download fixed colored image", convert_image(product), f"{filename}_{color.lower()}_fixed.png", "image/png")
                
            
            
col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:   
    fix_image(upload=my_upload)
else:
    fix_image("./zebra.jpg")


