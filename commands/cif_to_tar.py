from .base_command import BaseCommand
import os
import random
import numpy as np
import webdataset as wds
import cv2
import matplotlib.pyplot as plt
from tqdm import tqdm

class CifToTar(BaseCommand):
    def __init__(self,inputs):
        self.add_arg('i','input','path to the input folder')
        self.add_arg('o','out','path to save ds')
        super().__init__(inputs)
        self.fold = self.pathify(self.args.input)
        self.out = self.pathify(self.args.out)

    def submit(self):
        allfiles = list()
        for path, currentDirectory, files in os.walk(self.fold):
            for file in files:
                allfiles.append(os.path.join(path, file))
        random.shuffle(allfiles)
        folds = np.array_split(allfiles, 8)
        for key, fold in enumerate(folds):
            sink = wds.TarWriter(f'{self.out}b_{key}.tar', encoder=True)

            for nm, imgp in tqdm(enumerate(fold),total=len(fold)):
                img = cv2.imread(imgp)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                lable = imgp.split('/')[2]
                sink.write({
                    '__key__': f'{nm}',
                    'npy':img,
                    'lable':lable
                })

            sink.close()

