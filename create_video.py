from moviepy.editor import ImageClip, AudioFileClip
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont

text = "معلومة اليوم: العقل البشري يحتوي على أكثر من 80 مليار خلية عصبية."

tts = gTTS(text=text, lang="ar")
tts.save("voice.mp3")

img = Image.new("RGB",(1080,1920),"black")

draw = ImageDraw.Draw(img)

font = ImageFont.load_default()

draw.text((100,900),text,fill="white",font=font)

img.save("frame.jpg")

audio = AudioFileClip("voice.mp3")

clip = ImageClip("frame.jpg").set_duration(60)

video = clip.set_audio(audio)

video.write_videofile("video.mp4",fps=24)