from imageprocessor import ImageProcessor
from audioprocessor import AudioProcessor
from spectrogramprocessor import SpectrogramProcessor
import os
import shutil

def empty_folders(mp3_folder, directory):
    # Empty mp3_folder
    for filename in os.listdir(mp3_folder):
        file_path = os.path.join(mp3_folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)

    # Empty directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)

def main(url):
    model_path = 'export.pkl'
    mp3_folder="data/full_audio/30_sec_splits"
    directory = "data/full_audio/spectrograms"
    
    # Empty folders before processing
    empty_folders(mp3_folder, directory)

    # Create instances of the processors
    image_processor = ImageProcessor(model_path, directory)
    audio_processor = AudioProcessor()
    spectrogram_processor = SpectrogramProcessor(mp3_folder=mp3_folder, spectrogram_folder=directory)

    # Run the processors
    audio_processor.download_audio_stream(url)
    audio_processor.load_file()
    audio_processor.split_audio_segments()

    spectrogram_processor.process_files()

    outputs = image_processor.process_images()
    mode_output = image_processor.get_mode_output(outputs)
    if mode_output is not None:
        print("Mode output:", mode_output)
    else:
        print("No mode output found.")
    return mode_output

# Call the main function
if __name__ == "__main__":
    main()
