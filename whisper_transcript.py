import openai
import os


def whisper_transcript(audio_file, video_id):
    try:
        # Set OpenAI API Key
        openai.api_key = open("OPENAI_API_KEY.txt", "r").read().strip()

        # Transcribe audio using OpenAI API
        response = openai.Audio.transcribe('whisper-1', audio_file, response_format="verbose_json")
        
        # Create output directory if it doesn't exist
        if not os.path.exists('output'):
            os.makedirs('output')

        # Write transcription to file
        with open(f'output/{video_id}.txt', 'w', encoding='utf-8') as txt_file:
            for i in response["segments"]:
                txt_file.write(f"{round(i['start'], 2)}: {i['text']}\n")
        
        return True
    except:
        return False


#audio_file = open("audio.mp3", "rb")
#whisper_transcript(audio_file, 'dQw4w9WgXcQ')
