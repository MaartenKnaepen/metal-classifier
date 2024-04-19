from fastai.vision.all import *
import os
from statistics import mode

class ImageProcessor:
    def __init__(self, model_path, directory):
        self.learn_inf = load_learner(model_path)
        self.directory = directory

    def process_images(self):
        files = os.listdir(self.directory)
        outputs = []
        for file in files:
            if file.endswith(".png"):
                file_path = os.path.join(self.directory, file)
                try:
                    image = PILImage.create(file_path)
                    pred = self.learn_inf.predict(image)
                    outputs.append(pred[0])
                except Exception as e:
                    print(f"Error processing image {file}: {e}")
        return outputs

    def get_mode_output(self, outputs):
        try:
            mode_output = mode(outputs)
            return mode_output
        except StatisticsError:
            return None

# Example usage:
'''if __name__ == "__main__":
    model_path = 'export.pkl'
    directory = "data/full_audio/30_sec_splits/spectrograms"
    processor = ImageProcessor(model_path, directory)
    outputs = processor.process_images()
    mode_output = processor.get_mode_output(outputs)
    if mode_output is not None:
        print("Mode output:", mode_output)
    else:
        print("No mode output found.")'''
