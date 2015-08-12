import requests
import sys
from xml.etree import ElementTree
from xml.etree.ElementTree import tostring

# Variables

max_num = 500
sort = 'id'
nbdno = '50000'

# API key provided by api.data.gov
key = 'sOVKDSGodD60TJ7SpClM8xkXB4rD6vq6bnsvEqY2'
url = 'http://api.nal.usda.gov/ndb/'
type_list = url + 'list?api_key='
type_item = url + 'reports/?api_key='

url_request = {'list': type_list,
                  'item': type_item}

url = url_request['list'] + key

"""Optional arguments include lt, max, offset and sort
See http://ndb.nal.usda.gov/ndb/doc/apilist/API-LIST.md for documentation

In the GUI, the user will be able to select optional parameters.
When the button is clicked/populated, the dict will add the optional param
"""
optional = {'format': 'xml',
            'ndbno': nbdno,
            'max': str(max_num),
            'sort': sort,
            'lt': '',
            'offset': '0',
            'type': '',
            'format1': ''}


def get_url(url, request_kwargs=None):
    # Get response
    response = requests.get(url, params=request_kwargs)
    
    return response

def update_food_list():
    """Assuming we get a response, use tree as the base xml response.

    Any additional requests will append their data to the base tree var.
    type(tree) = xml.etree.ElementTree.Element

    Keep requesting the data until there is no more

    Since the api only allows a max of 500 items (max_num) per request,
    check the value of 'total' in the repsonse xml.

    Keep requesting for a response until count < 500"""
    r = get_url(url, optional)
    tree = ElementTree.fromstring(r.content)
    root = tree.getchildren()
    count = max_num
    total = max_num

    while count == max_num:
        optional['offset'] = str(int(optional['offset']) + max_num)
        r = get_url(url, optional)

        """ Convert request to XML tree

        temp_tree = additional data to be added to the base tree var

        root = list of all the elements in tree

        Until it is possible to automatically update the tree's
        attributes, it must be done manually
        """
        temp_tree = ElementTree.fromstring(r.content)
        temp_root = temp_tree.getchildren()
        
        tree.extend(temp_root)

        count = int(temp_tree.attrib['end'])
        total += count
        
        tree.attrib['end'] = str(total)
        tree.attrib['total'] = str(total)

    # Change filename based on ndbno value
    filename = 'xml/food_list.xml'

    # Convert XML tree to string
    out = tostring(tree)

    # Open file to modify
    target = open(filename, 'w')

    # Write XML to file
    target.write(out)

    # Close file
    target.close()
