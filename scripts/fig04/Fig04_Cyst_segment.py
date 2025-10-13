from skimage import io, measure, filters
from skimage.segmentation import clear_border
import numpy as np
import pandas as pd


img_greyscale = io.imread('/exports/archive/hg-groep-peters/Spatial_Transcriptomics_Snowball_Sevtap/Raw_Data/Raw_Slide_Images/A3_segmented_cyst.tif')[..., 0]

threshold = filters.threshold_otsu(img_greyscale)
mask = img_greyscale > threshold

cleared = clear_border(mask)

labeled_mask = measure.label(cleared)

perimeters = []

for region in measure.regionprops(labeled_mask):
    object_mask = labeled_mask == region.label
    contours = measure.find_contours(object_mask, level=0.5)

    if contours:
        contour = contours[0]
        xy_coords = contour[:, [1, 0]]
        for x, y in xy_coords:
            perimeters.append({'label': region.label, 'x': x, 'y': y})

df = pd.DataFrame(perimeters)
df.to_csv('/exports/humgen/cnovellarausell/SevtapSpatial/segmented_objects_coordinates.csv', index=False)

