import os
import librosa
import numpy as np
import skimage.io


class SpectrogramProcessor:
    def __init__(self, mp3_folder="data/full_audio/30_sec_splits", 
                 spectrogram_folder="data/full_audio/30_sec_splits/spectrograms"):
        self.mp3_folder = mp3_folder
        self.spectrogram_folder = spectrogram_folder
        os.makedirs(self.spectrogram_folder, exist_ok=True)

    def scale_minmax(self, X, min=0.0, max=255.0):
        X_std = (X - X.min()) / (X.max() - X.min())
        X_scaled = X_std * (max - min) + min
        return X_scaled.astype(np.uint8)

    def process_file(self, file_name):
        try:
            # Load the MP3 file
            y, sr = librosa.load(file_name)

            # Create the spectrogram
            spect = librosa.feature.melspectrogram(y=y, sr=sr)
            spect = np.log(spect + 1e-9)
            spect = self.scale_minmax(spect)

            # Check if spectrogram contains invalid values
            if np.isnan(spect).any() or np.isinf(spect).any():
                raise ValueError("Spectrogram contains invalid values.")

            # Flip spectrogram vertically
            spect = np.flip(spect, axis=0)

            # Invert colors for better visualization
            spect = 255 - spect

            # Get original filename
            original_filename = os.path.basename(file_name)

            # Construct output filename
            output_filename = f"{original_filename[:-4]}.png"
            output_path = os.path.join(self.spectrogram_folder, output_filename)

            # Save spectrogram
            skimage.io.imsave(output_path, spect)

            # Increment counter for tracking progress
            self.c += 1
            if self.c % 1000 == 0:
                print(f"Processed {self.c} files")

        except Exception as e:
            print(f"Error processing {file_name}: {e}")

    def process_files(self):
        self.c = 0
        files = []
        for root, dirs, files_in_dir in os.walk(self.mp3_folder):
            for file in files_in_dir:
                if file.endswith(".mp3"):
                    files.append(os.path.join(root, file))

        for file_name in files:
            self.process_file(file_name)

# Example usage:
'''if __name__ == "__main__":
    processor = SpectrogramProcessor()
    processor.process_files()'''
