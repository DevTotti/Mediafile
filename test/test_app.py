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


    response = client.post('/', data=json.dumps(data), headers=headers)
    assert response.status_code == 200




def test_get_one_success(app, client):
    audioFileType = 'song'
    audioFileID = "60433070562ac133f1fb5159"
    response = client.get('/media/{}/{}'.format(audioFileType, audioFileID))
    assert response.content_type == mimetype
    assert response.status_code == 200



def test_get_all_success(app, client):
    audioFileType = 'song'
    response = client.get('/media/{}/'.format(audioFileType))
    assert response.content_type == mimetype
    assert response.status_code == 200




def test_put_success(app, client):
    data = {
        "audioFileType":"song",
        "audioFileMetadata":{
            "name":"Self Made",
            "duration":248
        }
    }

    audioFileMetadata = data['audioFileMetadata']
    audioFileType = data['audioFileType']


    audioFileID = "60433070562ac133f1fb5159"

    response = client.put('/media/{}/{}'.format(audioFileType, audioFileID), data = json.dumps(data), headers=headers)
    assert response.content_type == mimetype
    assert response.status_code == 200




def test_delete_success(app, client):
    audioFileType = 'song'
    audioFileID = "6043b809d97d22589ceab834"

    response = client.delete('/media/{}/{}'.format(audioFileType, audioFileID))
    assert response.content_type == mimetype
    assert response.status_code == 200