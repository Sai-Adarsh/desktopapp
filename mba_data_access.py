import requests
from matplotlib import pyplot as plt
import numpy as np
import json
from PIL import Image
from io import BytesIO
import requests

def returnImg(kernSize, thresSize):
    image_url = "http://braincircuits.org/cgi-bin/iipsrv.fcgi?FIF=/PMD2057/PMD2057%262056-N9-2015.03.12-02.58.18_PMD2057_1_0025.jp2&GAM=1&WID=1087&RGN=0.5435,0.4529166666666667,0.04529166666666667,0.04529166666666667&MINMAX=1:10,255&MINMAX=3:10,255&MINMAX=2:10,255&CVT=jpeg"
    res = requests.get(image_url)
    img = Image.open(BytesIO(res.content))
    img_npy = np.asarray(img)
    nr,nc,_ = img_npy.shape
    nr,nc
    im_2 = img_npy[:nr//2,:nc//2,:] # 200%
    im_2_2 = im_2[:nr//4,:nc//4,:]  # 400%
    im_2_2_2 = im_2_2[:nr//8,:nr//8,:] # 800%
    def _weight_mean_color(graph, src, dst, n):
        diff = graph.node[dst]['mean color'] - graph.node[n]['mean color']
        diff = np.linalg.norm(diff)
        return {'weight': diff}


    def merge_cb(graph, src, dst):
        graph.node[dst]['total color'] += graph.node[src]['total color']
        graph.node[dst]['pixel count'] += graph.node[src]['pixel count']
        graph.node[dst]['mean color'] = (graph.node[dst]['total color'] /
                                         graph.node[dst]['pixel count'])

    from skimage.segmentation import quickshift, mark_boundaries
    from skimage.future import graph
    labels1 = quickshift(im_2_2, kernel_size=kernSize, max_dist=6, ratio=0.5)
    rag = graph.rag_mean_color(im_2_2, labels1,mode='distance',sigma=200)
    labels2 = graph.merge_hierarchical(labels1, rag, thresh=thresSize, rag_copy=False,
                                       in_place_merge=True,
                                       merge_func=merge_cb,
                                       weight_func=_weight_mean_color)
    res1 = mark_boundaries(im_2_2, labels1,mode='subpixel')
    res2 = mark_boundaries(im_2_2, labels2, mode='outer')
    plt.imsave("static/test.png", res2)
    if not False:
        plt.figure(figsize = (18,18))
        plt.axis(False)
        plt.subplot(2,2,1)
        plt.imshow(res1)

        plt.subplot(2,2,2)
        plt.imshow(res2)

        plt.subplot(2,2,4)
        plt.imshow(labels2,cmap='jet')
    print("end")
    plt.imsave('static/initial_tessellation.png',(255*res1).astype('uint8'))
    plt.imsave('static/rag_hier_merged.png',(255*res2).astype('uint8'))
    plt.imsave('static/first_pass_labels.png',labels2.astype('uint8'))
