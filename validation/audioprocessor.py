import os
import ffmpeg
from pytube import YouTube

class AudioProcessor:
    def __init__(self, output_directory="data/full_audio/30_sec_splits/"):
        self.output_directory = output_directory
        os.makedirs(self.output_directory, exist_ok=True)

    def download_audio_stream(self, url):
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        self.file_name = audio_stream.download(output_path='data/full_audio', filename='track.mp3')
        #print(f"Downloaded audio stream: {self.file_name}")

    def load_file(self):
        try:
            audio_info = ffmpeg.probe(self.file_name)
            self.duration_ms = float(audio_info['format']['duration']) * 1000
            #print(f"Loaded input file: {self.file_name} (Duration: {audio_info['format']['duration']} seconds)")
        except Exception as e:
            print(f"Error loading file {self.file_name}: {e}")
            exit(1)

    def split_audio_segments(self):
        buffer_ms = 30 * 1000  # 30 seconds in milliseconds
        counter = 1
        while self.duration_ms > 0:
            try:
                output_file = os.path.join(self.output_directory, f"split_{counter}_{os.path.basename(self.file_name)}")
                ffmpeg.input(self.file_name, ss=(counter - 1) * 30, t=30).output(output_file, codec='libmp3lame', qscale=2).run(overwrite_output=True)
                #print(f"Written: {output_file} (Duration: 30 seconds)")
            except Exception as e:
                print(f"Error processing segment {counter}: {e}")
            counter += 1
            self.duration_ms -= buffer_ms

# Example usage:
'''if __name__ == "__main__":
    processor = AudioProcessor()
    processor.download_audio_stream('https://www.youtube.com/watch?v=gNhN6lT-y5U')
    processor.load_file()
    processor.split_audio_segments()
'''