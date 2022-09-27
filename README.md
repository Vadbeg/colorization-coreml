# Colorization CoreML
Repository for image colorization using CoreML

![res1](results/res1.png)
![res2](results/res2.png)

## Installation

1. Install all requirements:
```shell
pip install -r requirements.txt
```
2. Use the project :tada:

## Usage

To run use command below:
```shell
python run_colorization.py --data-root images
```

If image is not black & white it will be converter to b&w and then colorized

## Models

First model [colorizer_core.mlmodel](weights/colorizer_core.mlmodel) expects PIL.Image
`image_small` of size (3, 256, 256). It returns `result`, A and B from LAB colorspace as array, (2, 256, 256).

Then you need to resize `result` to original image size. Let's name resized `result` as `ab`

Second model [colorizer_tail.mlmodel](weights/colorizer_tail.mlmodel). It expects original PIL.Image
of any size, `image`. And `ab`, resized `result` from previous network. This model returns
colorized image array `colorized_image` of original size.

## Built With

* [coremltools](https://github.com/apple/coremltools) - The NNs inference framework used
* [OpenCV](https://opencv.org/) - Images processing framework used

## Authors

* **Vadim Titko** aka *Vadbeg* -
[LinkedIn](https://www.linkedin.com/in/vadtitko/) |
[GitHub](https://github.com/Vadbeg/PythonHomework/commits?author=Vadbeg)
