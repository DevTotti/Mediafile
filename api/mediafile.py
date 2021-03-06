from flask import Response, request, jsonify
from flask_restful import Resource
from models.media import Song, Podcast, Audiobook
from api.errors import invalid_request


class MediaTypeDatabase():

    def __init__(self):

        self.audiofile = {
            'song': Song,
            'podcast': Podcast,
            'audiobook': Audiobook
        }

    def database(self):
        return self.audiofile




class MediaFileAPI(Resource):

    def __init__(self):
        self.database = MediaTypeDatabase().database()

    def post(self) -> Response:
        audioFileType = request.get_json()['audioFileType']
        audioFileMetadata = request.get_json()['audioFileMetadata']
        db = self.database[audioFileType]
        
        if audioFileType == 'song':
            try:
                post_data = db(**audioFileMetadata).save()
                result = {'id', str(post_data.id)}
                return Response(status=200)
            
            except:
                return Response(status=500)
        
        elif audioFileType == 'podcast':
            try:
                post_data = db(**audioFileMetadata).save()
                result = {'id', str(post_data.id)}
                return Response(status=200)

            except:
                return Response(status=500)

        elif audioFileType == 'audiobook':
            try:
                post_data = db(**audioFileMetadata).save()
                result = {'id', str(post_data.id)}
                return Response(status=200)

            except:
                return Response(status=500)

        else:
            return invalid_request()





class MediaFilesAPI(Resource):
    def __init__(self):
        self.database = MediaTypeDatabase().database()


    def get(self, audioFileType: str = None, audioFileID: str = None) -> Response:
        db = self.database[audioFileType]
        
        if audioFileID is not None:
            
            data = db.objects.get(id=audioFileID)
            response = jsonify({'data': data})
            response.status_code = 200
            return response

        else:

            data = db.objects()
            response = jsonify({'data': data})
            response.status_code = 200
            return response

    
    def put(self, audioFileType: str , audioFileID: str) -> Response:
        db = self.database[audioFileType]
        audioFileMetadata = request.get_json()['audioFileMetadata']
        try:
            data = db.objects(id=audioFileID).update(**audioFileMetadata)
            response = jsonify(({'result': 'audio file updated'}))
            response.status_code = 200
            return response
        
        except:
            return Response(status=400)




    def delete(self, audioFileType: str = None, audioFileID: str = None) -> Response:
        db = self.database[audioFileType]
        try:
            data = db.objects(id=audioFileID).delete()
            response = jsonify({'result': 'audio file deleted'})
            response.status_code = 200
            return response
        
        except:
            return Response(status=400)

