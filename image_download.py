# Importing Necessary Modules
import urllib.request
import requests  # to get image from the web
import shutil  # to save it locally
from tqdm import tqdm  # progress bar

# Set up the image URL and filename
image_url = "https://i.kym-cdn.com/entries/icons/original/000/017/619/yuudachi_poi_by_yuries-d8emuqz.jpg"
filename = image_url.split("/")[-1]

# Open the url image, set stream to True, this will return the stream content.
r = requests.get(image_url, stream=True)

# setup progress bar
total_size_in_bytes = int(r.headers.get('content-length', 0))
block_size = 1024  # 1 Kibibyte
progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True

    # Open a local file with wb ( write binary ) permission.
    with open(filename, 'wb') as f:
        # for data in r.iter_content(block_size):
        #     progress_bar.update(len(data))
        shutil.copyfileobj(r.raw, f)

    progress_bar.close()

    print('Image sucessfully Downloaded: ', filename)
else:
    print('Image Couldn\'t be retreived')


# using urllib module
# setting filename and image URL
filename = 'poi.jpg'
image_url = "https://i.kym-cdn.com/photos/images/original/000/937/877/465.jpg"

# calling urlretrieve function to get resource
urllib.request.urlretrieve(image_url, filename)
