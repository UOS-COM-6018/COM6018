"""Evaluate a model on the eval1 dataset.

Requires the eval1.joblib file to be present in the current directory.

Usage:
    python evaluate_model.py <model_file> <n_pixels>

    model_file: Path to the model file.
"""

from argparse import ArgumentParser
from joblib import load
import os

try:
    from train import *
except ImportError:
    print("No custom models supplied. Skipping import")


def evaluate(model_file):
    """Evaluate a model on the eval1 dataset.

    Args:
        model_file (str): Path to the model file.
    """

    print(f"Evaluating {model_file}")

    # Check that model file is no larger than 20 MB
    if os.path.getsize(model_file) > 80 * 1024 * 1024:
        print("ERROR: Model file is larger than the allowed 80 MB limit.")
        return

    model = load(model_file)

    eval_data = load(open("data/eval1.joblib", "rb"))
    x_test = eval_data["data"]
    y_test = eval_data["target"]

    score = model.score(x_test, y_test)
    print("Score:", score * 100, "%")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("model_file", type=str)
    args = parser.parse_args()
    evaluate(args.model_file)
