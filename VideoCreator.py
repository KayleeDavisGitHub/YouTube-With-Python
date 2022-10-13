## Get Video --------

# Step I : Pytube:
# terminal: python - m pip install pytube

# Step II : In your script import the YouTube class from pytube package.
# from pytube import YouTube

# Step III : Create an object of YouTube bypassing the video URL
# yt = YouTube("<Your youtube URL>")

# Step IV : Use the filter method to specify the download format of the video
# mp4_files = yt.streams.filter(file_extension="mp4")

# Step V : Get the video you want by specifying the resolution
# mp4_369p_files = mp4_files.get_by_resolution("360p")

# Step VI : Save the downloaded video to the local file system
# mp4_369p_files.download("<Download folder path>")


from pytube import YouTube

def download_360p_mp4_videos(url: str, outpath: str = "./"):

    yt = YouTube(url)

    yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(outpath)


if __name__ == "__main__":

    download_360p_mp4_videos(
         "https://www.youtube.com/watch?v=TnlfHHw8Oiw" # put in bunch of video URLS
        "C:/Users/mailk/OneDrive/Documents/Python Scripts/scraped_videos", 
    )

## Get Subtitles ------
# Install
# pip install youtube_transcript_api

# we import the required package.
from youtube_transcript_api import YouTubeTranscriptApi 

# we create the generate_transcript() function, which accepts the video id as
#   a parameter and will return the transcript as well as the number of words in the transcript.
def generate_transcript(id):
     # we use the get_transcript() method of our package that gets the transcript
     #   of the id provided as a parameter. This function returns a list of dictionaries,
     #   so we need to do some processing to convert it to a single string.
	transcript = YouTubeTranscriptApi.get_transcript(id)
	script = ""

     # we run a loop to iterate over all the dictionary values and fetch the
     #   text for each time interval. Then, we combine it into a string.
	for text in transcript:
		t = text["text"]
		# we added a filter to skip the Music so that,
	     #   if there is any music in the video, it will not come to our final transcript string.
		if t != '[Music]': 
			script += t + " "
		
	return script, len(script.split()) # we return the values.

id = 'TnlfHHw8Oiw' # from URL above
transcript, no_of_words = generate_transcript(id) # we call our function by passing the video id.

# Print:
print(transcript)

## Translation ------

# Install:
# pip install googletrans
import googletrans
print(googletrans.LANGUAGES) # all languages and their shorthands


from googletrans import Translator
translator = Translator()

# Example:
result = translator.translate('Mitä sinä teet')
result = translator.translate(transcript, src='en', dest='uk')
print(result.src)
print(result.dest)
print(result.origin)
print(result.text)
print(result.pronunciation)



# pip install google_trans_new
from google_trans_new import google_translator  
translator = google_translator()  
translate_text = translator.translate("yes",lang_tgt='uk')  
print(translate_text)
 # https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group
