import sys
import scanpy as sc
import squidpy as sq
import numpy as np
import pandas as pd
from anndata import AnnData
import skimage
import time
from joblib import Parallel, delayed

from cellpose import models


# import tangram for spatial deconvolution
import tangram as tg

threshold = float(sys.argv[1])
channel = int(sys.argv[2])

sc.logging.print_header()
print(f"squidpy=={sq.__version__}")
print(f"tangram=={tg.__version__}")


def cellpose_he(img, min_size=15, flow_threshold=0.4, channel_cellpose=0):
    model = models.Cellpose(model_type='nuclei')
    res, _, _, _ = model.eval(
        img,
        channels=[channel_cellpose, 0],
        diameter=None,
        min_size=min_size,
        invert=True,
        flow_threshold=flow_threshold,
    )
    return res

def segment(image, library):
    sq.im.segment(img=image, layer=library , channel=None, flow_threshold=threshold, method=cellpose_he,  channel_cellpose=channel)
    image.save(output_dir + 'zarr/' + 'full' + library + "_segmented_Cellpose" + "_" + str(threshold) + "_" + str(channel))

output_dir = '/exports/humgen/cnovellarausell/SevtapSpatial/Notebooks/'


library_id = ['Control', 'pkd_1', 'pkd_2', 'pkd_3']
img = []

for i,library in enumerate(library_id):
    img.append(sq.im.ImageContainer('/exports/archive/hg-groep-peters/Spatial_Transcriptomics_Snowball_Sevtap/Raw_Slide_Images/A{}.tif'.format(i+1), layer=library))
    
def joblib_loop():
    Parallel(n_jobs=4)(delayed(segment)(image, library_id[i]) for i, image in enumerate(img))

start = time.process_time()
joblib_loop()
print(time.process_time() - start)
