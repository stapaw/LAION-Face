import torch
import pyarrow.parquet as pq
import pyarrow as pa
import os
from tqdm import tqdm
import argparse

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("coco_meta_dir")
    parser.add_argument("coco_face_meta_dir")
    args=parser.parse_args()
    all_count=0
    coco_meta_dir=args.coco_meta_dir
    os.makedirs(args.coco_face_meta_dir,exist_ok=True)

    big_parquet_file=f"{coco_meta_dir}/mscoco.parquet"
    big_table=pq.read_table(big_parquet_file).to_pandas()[:15000]
    all_count+=len(big_table)
    print(all_count)
    pq.write_table(pa.Table.from_pandas(big_table), os.path.join(args.coco_face_meta_dir,f'mscoco_part_15K.parquet'))
