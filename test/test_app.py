import json

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}


def test_create_success(app, client):


    data = {
        "audioFileType":"song",
        "audioFileMetadata":{
            "name":"Fast Lane",
            "duration":240
        }
    }

    url = '/'

    response = client.create_routes.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 200

def test_get_success(app, client):
    audioFileType = 'song'
    audioFileID = "60432d11218002ba3785490b"
    response = client.get('/media/{}/{}'.format(audioFileType, audioFileID))
    assert response.content_type == mimetype
    assert response.status_code == 200



def test_put_success(app, client):
    data = {
        "audioFileType":"song",
        "audioFileMetadata":{
            "name":"Fast Lane",
            "duration":240
        }
    }

    audioFileMetadata = data['audioFileMetadata']
    audioFileType = data['audioFileType']


    audioFileID = "60432d11218002ba3785490b"

    response = client.put('/media/{}/{}'.format(audioFileType, audioFileID), data = json.dumps(audioFileMetadata), headers=headers)
    assert response.content_type == mimetype
    assert response.status_code == 200


def test_delete_success(app, client):
    audioFileID = "60432d11218002ba3785490b"
    audioFileMetadata = data['audioFileMetadata']

    response = client.delete('/media/{}/{}'.format(audioFileType, audioFileID))
    assert response.content_type == mimetype
    assert response.status_code == 200