import sys
import json

cat = 'cat'
from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi()
image = '../images/' + sys.argv[1]
result = clarifai_api.tag_images(open(image, 'rb'))
r = json.loads(result)
print r
