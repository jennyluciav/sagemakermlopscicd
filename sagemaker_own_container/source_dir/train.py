from __future__ import absolute_import

import argparse
import os
import sys
import time
import numpy
import pandas
import sklearn
import requests
import scipy
import pytd
import boto3
import s3fs
import fsspec
import sagemaker
import botocore
import joblib

from utils import print_files_in_path, save_model_artifacts


def train(hp1, hp2, hp3, train_channel, validation_channel):

    print("\nList of files in train channel: ")
    print_files_in_path(os.environ["SM_CHANNEL_TRAIN"])

    print("\nList of files in validation channel: ")
    print_files_in_path(os.environ["SM_CHANNEL_VALIDATION"])

    # Dummy net.
    net = None

    # Run training loop.
    epochs = 5
    for x in range(epochs):
        print("\nRunning epoch {0}...".format(x))

        time.sleep(30)

        print("Completed epoch {0}.".format(x))

    # At the end of the training loop, we have to save model artifacts.
    model_dir = os.environ["SM_MODEL_DIR"]
    save_model_artifacts(model_dir + "/", net)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    # sagemaker-containers passes hyperparameters as arguments
    parser.add_argument("--hp1", type=str)
    parser.add_argument("--hp2", type=int, default=50)
    parser.add_argument("--hp3", type=float, default=0.1)

    # This is a way to pass additional arguments when running as a script
    # and use sagemaker-containers defaults to set their values when not specified.
    parser.add_argument("--train", type=str, default=os.environ["SM_CHANNEL_TRAIN"])
    parser.add_argument("--validation", type=str, default=os.environ["SM_CHANNEL_VALIDATION"])

    args = parser.parse_args()
    
    print(numpy.__version__)
    print(pandas.__version__)
    print(sklearn.__version__)
    print(requests.__version__)
    print(scipy.__version__)
    print(pytd.__version__)
    print(boto3.__version__)
    print(s3fs.__version__)
    print(fsspec.__version__)
    print(sagemaker.__version__)
    print(botocore.__version__)
    print(joblib.__version__)

    # train(args.hp1, args.hp2, args.hp3, args.train, args.validation)
