import sys
import json

cat = 'cat'
from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi()
image = '../images/' + sys.argv[1]
result = clarifai_api.tag_images(open(image, 'rb', cat))
#print result

def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                return k
    return None

print search(result, u'cat')
if cat in result:
    print(result[cat])
