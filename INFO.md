# LAION-face dataset  


### Info

LAION-Face is the human face subset of [LAION-400M](https://laion.ai/laion-400-open-dataset/), it consists of 50 million image-text pairs. Face detection is conducted to find images with faces. Apart from the 50 million full-set(LAION-Face 50M), we also provide a 20 million sub-set(LAION-Face 20M) for fast evaluation.

### Setup
```
pip install -r requirements.txt
```
We need `pyarrow` to read and write parque file, `img2dataset` to download images.

#### Download the metadata

We provide the list of sample_id in [huggingface](https://huggingface.co/datasets/FacePerceiver/laion-face/resolve/main/laion_face_ids.pth).

Download and convert the metadata with the following commands. 

```bash
wget -l1 -r --no-parent https://the-eye.eu/public/AI/cah/laion400m-met-release/laion400m-meta/
mv the-eye.eu/public/AI/cah/laion400m-met-release/laion400m-meta/ .
wget https://huggingface.co/datasets/FacePerceiver/laion-face/resolve/main/laion_face_ids.pth
python convert_parquet.py ./laion_face_ids.pth ./laion400m-meta ./laion_face_meta
```

Edit `convert_parquet.py` file to create a parquet file with a subset of images (from one data split, filtered etc.)
For LAION-face filtering images with faces is done in this step

#### Download the images with img2dataset
When metadata is ready, you can start download the images.

```bash
bash download.sh ./laion_face_meta ./laion_face_data
```
Use resize mode `border` to scale imgs.

Please be patient, this command might run over days, and cost about 2T disk space, and it will download 50 million image-text pairs as 32 parts.

- To use the **LAION-Face 50M**, you should use all the 32 parts.
- To use the **LAION-Face 20M**, you should use these parts.
    ```
    0,2,5,8,13,15,17,18,21,22,24,25,28
    ```


checkout `download.sh` and [img2dataset](https://github.com/rom1504/img2dataset) for more details and parameter setting.

# MS COCO-face dataset 
Same as above: base parquet file and desc [here](https://github.com/rom1504/img2dataset/blob/main/dataset_examples/mscoco.md)

To investigate:
1) Do not know why, but with this parquet file I got each images 5 times with diff ids.
2) For MS COCO-face filtering images with faces is done by retina-face in notebook code (laion_vs_coco.ipynb) using tensorboard impl:
```bash
pip install retina-face
```
Python:
```Python
from retinaface import RetinaFace
```

# Simple preliminary viz
1) Use laion_vs_coco.ipynb (sorry for CQ)
2) Viz online with https://projector.tensorflow.org/