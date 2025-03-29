import os 
from dotenv import load_dotenv
from claudette import * 
from PIL import Image
import io

def create_test_image():
    # Create a small, valid PNG image
    img = Image.new('RGB', (50, 50), color = 'red')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()
  
def read_notes_image():
    # read a notes image from jpg format
    with open('notes_rivers.png', 'rb') as file:
      image_bytes = file.read()
    return image_bytes

def test_chat():
    print(models[1])
    img_bytes = create_test_image()
    load_dotenv()
    os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_KEY")
    chat = Chat(models[1])
    query = "what is there in the image ?"
    ans = chat([img_bytes,query])
    print(ans)

def test_chat2():
    print(models[1])
    img_bytes = read_notes_image()
    load_dotenv()
    os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_KEY")
    chat = Chat(models[1])
    query = "what is span of Ganga river?"
    ans = chat([img_bytes,query])
    print(ans)
