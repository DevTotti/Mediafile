# Mediafile
A Microservice that handles the CRUD operations of audio files on the server


To run the application, you need to install dependencies first.

Taking a linux environment as a point of reference, first you need to clone this repo.

```
git clone https://github.com/DevTotti/Mediafile.git
```

then navigate to the folder

```bash
cd MediaFile
```

then you have to setup a vitrual environment

```bash
python3 -m venv env

source env/bin/activate
```

Now that is done, we need to install all dependencies needed for the app

```bash
pip install -r requirements.txt
```


Now we are all set. There is a .env file that contains the credentials, you have to create a new env file or change the ```credentials.env``` to just ```.env``` and set your credentials.

## Run Tests
First we have to run Unit test on the app to be sure everything works well 
But to run test, you have to supply some test data which includes ```audioFileID``` and ```audioFileType``` in functions
```test_get_one_success``` ```test_put_success``` ```test_delete_success``` for adequate test results

```
python -m pytest
```
or simply

```
pytest
```

#Usage
To run the server, by default the server runs on 5000 but you can change it to anything. You can do this by reading the comment in ```app.py``` line 89

When all is set, run the server using

```
python app.py


#Routes
NAME     			                | END POINT                             |  PARAMS / BODY DATA
------------------------------------| --------------------------------------| ---------------
Create Audio file [POST]            | /                                     |{ audioFileType: str}, { audioFileMetadata: dict{ name: str,  duration: int}}
Get existing audiofile [GET]        | /media/<audioFileType>/               |<audioFileType>/
Get one existing audiofile [GET]    | /media/<audioFileType>/<audioFileID>  |<audioFileType>/<audioFileID>
Delete existing audiofile [DELETE]  | /media/<audioFileType>/<audioFileID>  |<audioFileType>/<audioFileID>
Update Audio file [PUT]             | /                                     |{ audioFileType: str}, { audioFileMetadata: dict{ name: str,  duration: int}}


I hope you found it easy

Paul