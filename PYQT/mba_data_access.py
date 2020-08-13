import requests
from matplotlib import pyplot as plt
import numpy as np
import json
from PIL import Image
from io import BytesIO
import requests
from __main__ import *
import matplotlib as plt
from skimage.segmentation import quickshift, mark_boundaries
from skimage.future import graph
import matplotlib
def returnImg(threSize):
    image_url = "http://brainarchitecture.org/fcgi-bin/iipsrv.fcgi?FIF=/PMD2057/PMD2057%262056-N9-2015.03.12-02.58.18_PMD2057_1_0025.jp2&GAM=1&WID=1087&RGN=0.5435,0.4529166666666667,0.04529166666666667,0.04529166666666667&MINMAX=1:10,255&MINMAX=3:10,255&MINMAX=2:10,255&CVT=jpeg"
    print(threSize)
    res = requests.get(image_url)
    img = Image.open(BytesIO(res.content))
    img_npy = np.asarray(img)
    nr,nc,_ = img_npy.shape
    nr,nc
    im_2 = img_npy[:nr//2,:nc//2,:] # 200%
    im_2_2 = im_2[:nr//4,:nc//4,:]  # 400%
    im_2_2_2 = im_2_2[:nr//8,:nr//8,:] # 800%
    def _weight_mean_color(graph, src, dst, n):
        diff = graph.nodes[dst]['mean color'] - graph.nodes[n]['mean color']
        diff = np.linalg.norm(diff)
        return {'weight': diff}


    def merge_cb(graph, src, dst):
        graph.nodes[dst]['total color'] += graph.nodes[src]['total color']
        graph.nodes[dst]['pixel count'] += graph.nodes[src]['pixel count']
        graph.nodes[dst]['mean color'] = (graph.nodes[dst]['total color'] /
                                         graph.nodes[dst]['pixel count'])

    from skimage.segmentation import quickshift, mark_boundaries
    from skimage.future import graph
    labels1 = quickshift(im_2_2, kernel_size=3, max_dist=6, ratio=0.5)
    rag = graph.rag_mean_color(im_2_2, labels1,mode='distance',sigma=200)
    labels2 = graph.merge_hierarchical(labels1, rag, thresh=threSize, rag_copy=False,
                                       in_place_merge=True,
                                       merge_func=merge_cb,
                                       weight_func=_weight_mean_color)
    res1 = mark_boundaries(im_2_2, labels1,mode='subpixel')
    res2 = mark_boundaries(im_2_2, labels2, mode='outer')
    cells=np.unique(labels2)

    matplotlib.image.imsave("PYQT/samples/test.png", res2)
    with open('PYQT/samples/person.txt', 'w') as json_file:
               json.dump(int(len(cells)), json_file)
    #exec(open('CorrectSlider.py').read(),myVars)
    #if not False:
     #   plt.figure(figsize = (18,18))
      ## plt.subplot(2,2,1)
       # plt.imshow(res1)

        #plt.subplot(2,2,2)
        #plt.imshow(res2)

        #plt.subplot(2,2,4)
        #plt.imshow(labels2,cmap='jet')
    
    #from CorrectSlider import __init__
   # exec(open('CorrectSlider.py.py').read(),myVars)
    print("end")
    matplotlib.image.imsave('PYQT/samples/initial_tessellation.png',(255*res1).astype('uint8'))
    matplotlib.image.imsave('PYQT/samples/rag_hier_merged.png',(255*res2).astype('uint8'))
    matplotlib.image.imsave('PYQT/samples/first_pass_labels.png',labels2.astype('uint8'))




