from transcript_summarize import transcript_summarize
from whisper_transcript import whisper_transcript
from audio import get_audio


def main():
    # Get video id from user
    video_id = input("Enter the video id: ")
    
    # Get audio from YouTube video
    if get_audio(video_id): 
        print('Audio Downloaded') 

        # Open audio file
        audio_file = open("audio.mp3", "rb")

        # Transcribe audio using OpenAI's Whisper model
        print('Audio Transcribed Succefully') if whisper_transcript(audio_file, video_id) else print('Audio Transcription Failed')

        # Summarize transcript using OpenAI's GPT-4 model
        summarize = input("Do you want to summarize the transcript? (y/n): ")
        if summarize.lower() == 'y' or summarize.lower() == 'yes':
            print('Transcript Summarized Succefully') if transcript_summarize(video_id) else print('Transcript Summerization Failed')
    else: 
        print('Audio Download Failed')


if __name__ == "__main__":
    main()
