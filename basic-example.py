import whisper
import os

# FILENAME="audio.mp3"
FOLDER_PATH = "input"
filenames = os.listdir(FOLDER_PATH)

def format_output(segment):
      return f"{segment['start']}: {segment['text']} \n"

model = whisper.load_model("base")
for filename in filenames:
    result = model.transcribe(f"./{FOLDER_PATH}/{filename}")
    with open(f"./output/{filename}.txt", 'w') as f:
        f.write(result["text"])
    lines = [format_output(segment) for segment in result["segments"]] 
    with open(f"./output/{filename}-timestamps.txt", 'w') as g:
                g.writelines(lines)    

