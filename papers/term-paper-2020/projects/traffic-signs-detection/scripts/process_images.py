import object_detection as od
from os import listdir
from os.path import isfile, join, abspath
import time
import matplotlib.image as maimg
from PIL import Image


if __name__ == '__main__':
    input_folder = "../assets/resources/images/input/cars_moscow/"
    output_folder = "../assets/resources/images/output/cars_moscow3/"

    weights_path = abspath("../assets/yolov3.weights")

    model = od.load_model(weights_path)

    source_images = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]

    for image in source_images:
        start = time.time()
        image_path = input_folder + "/" + image
        result_path = output_folder + "/processed_" + image
        image_src = maimg.imread(image_path)

        processed_image = od.process_image(model, image_src)
        im = Image.fromarray(processed_image.astype('uint8'))
        im.save(result_path)

        print(image + " processed. Time elapsed: " + str(time.time() - start))

