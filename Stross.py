from time import time
from utils_ import *
import os



CONTENT_PATH = ""
STYLE_PATH = ""


CONTENT = os.listdir(CONTENT_PATH)
STYLE = os.listdir(STYLE_PATH)



content = "content.png"
style = "style.png"
weight = 1
output = "strotss.png"
device = "cuda:0"  
ospace = "uniform"
resize_to = 1024

    # make 256 the smallest possible long side, will still fail if short side is <
    # if args.resize_to < 2**8:
    #     print("Resulution too low.")
    #     exit(1)

content_pil, style_pil = pil_loader(content), pil_loader(style)
content_weight = weight * 16.0

start = time()
result = strotss(pil_resize_long_edge_to(content_pil, resize_to), 
                pil_resize_long_edge_to(style_pil, resize_to), content_weight, device, ospace)
result.save(output)
print(f'Done in {time()-start:.3f}s')
