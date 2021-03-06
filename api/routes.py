"""The routes file for handling the enpoints"""

from flask_restful import Api
from api.mediafile import MediaFileAPI, MediaFilesAPI


def create_routes(api: Api):
    api.add_resource(MediaFileAPI, '/')
    api.add_resource(MediaFilesAPI, "/media/<audioFileType>/", "/media/<audioFileType>/<audioFileID>")