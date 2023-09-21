from whisper_transcript import whisper_transcript
from audio import get_audio


def main():
    video_id = input("Enter the video id: ")
    
    if get_audio(video_id): 
        print('Audio Downloaded') 

        audio_file = open("audio.mp3", "rb")

        print('Audio Transcribed Succefully') if whisper_transcript(audio_file, video_id) else print('Audio Transcription Failed')
    else: 
        print('Audio Download Failed')


if __name__ == "__main__":
    main()
