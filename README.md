# Colorization CoreML
Repository for image colorization using CoreML

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

## Model

Model input is Black&White PIL.Image of any shape. Model output is Float32
array of shape (3, H, W).

Input node name is `image`, output - `result`.

## Built With

* [coremltools](https://github.com/apple/coremltools) - The NNs inference framework used
* [OpenCV](https://opencv.org/) - Images processing framework used

## Authors

* **Vadim Titko** aka *Vadbeg* -
[LinkedIn](https://www.linkedin.com/in/vadtitko/) |
[GitHub](https://github.com/Vadbeg/PythonHomework/commits?author=Vadbeg)
