from urllib.request import urlretrieve
url = "https://file-examples-com.github.io/uploads/2017/11/file_example_WAV_10MG.wav"
filename = "speech.wav"
urlretrieve(url, filename)
