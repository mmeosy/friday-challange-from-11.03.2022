from flask import Blueprint, json

from flaskr.list_of_s3 import list_objects

api_bp = Blueprint("api", __name__)


@api_bp.route('/bucket/<bucketname>')
def bucket_objects(bucketname):
    objects = list_objects(bucketname)
    result = []
   
    
    for object in objects:
        mapped_objects = {
            
            "key": object["Key"]
            
        }
        result.append(mapped_objects)
    
    
    return json.dumps(result)
    