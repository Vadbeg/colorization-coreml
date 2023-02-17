"""Script for running colorization on folder with images"""

from pathlib import Path

import coremltools as ct
import matplotlib.pyplot as plt
import numpy as np
import typer
from cv2 import cv2
from PIL import Image


def _load_image(image_path: Path) -> Image.Image:
    image: Image.Image = Image.open(image_path)
    image = image.convert(mode="RGB")

    return image


def _resize_ab(ab: np.ndarray, original_height: int, original_width: int) -> np.ndarray:
    a_resized = cv2.resize(ab[0][0], dsize=(original_height, original_width))[
        np.newaxis, ...
    ]
    b_resized = cv2.resize(ab[0][1], dsize=(original_height, original_width))[
        np.newaxis, ...
    ]
    ab_resized = np.concatenate([a_resized, b_resized], axis=0)[np.newaxis, ...]

    return ab_resized


def run_enlighten(
    data_root: Path = typer.Option(
        default=..., help="Path to folder with *.jpg images"
    ),
    core_model_path: Path = typer.Option(
        default=Path("weights/colorizer_core.mlmodel"),
        help="Path to core colorization CoreML model",
    ),
    tail_model_path: Path = typer.Option(
        default=Path("weights/colorizer_tail.mlmodel"),
        help="Path to tail colorization CoreML model",
    ),
) -> None:
    """
    Script for image colorization, iterates threw .jpg or .png images in folder, shows the result.
    """

    core_model = ct.models.MLModel(str(core_model_path))
    tail_model = ct.models.MLModel(str(tail_model_path))

    image_paths = list(data_root.glob(pattern="**/*.jpg"))
    image_paths += list(data_root.glob(pattern="**/*.png"))

    for curr_image_path in image_paths:
        image = _load_image(image_path=curr_image_path)
        image_resized = image.resize((256, 256))

        colorized_small_image_array = core_model.predict(
            data={"image_small": image_resized}
        )["colorized_small_image"]
        colorized_small_image_array = colorized_small_image_array[0]
        colorized_small_image_array = colorized_small_image_array.astype(np.uint8)
        colorized_small_image_array = np.transpose(
            colorized_small_image_array, axes=(1, 2, 0)
        )

        colorized_small_image = Image.fromarray(colorized_small_image_array)
        original_height, original_width = image.size
        colorized_small_image = colorized_small_image.resize(
            size=(original_height, original_width)
        )

        colorized_image = tail_model.predict(
            data={"image": image, "ab": colorized_small_image}
        )["colorized_image"][0]

        colorized_image = np.transpose(colorized_image, axes=(1, 2, 0))
        colorized_image = np.uint8(colorized_image)

        fig, axs = plt.subplots(1, 2, figsize=(12, 8))
        axs = axs.flatten()

        axs[0].set_title("Original image")
        axs[0].imshow(np.array(image))

        axs[1].set_title("Colorized image")
        axs[1].imshow(colorized_image)

        plt.show()


if __name__ == "__main__":
    typer.run(run_enlighten)
