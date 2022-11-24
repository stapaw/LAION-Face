#!/bin/bash

folder="$2"
echo $folder
mkdir $folder
for i in $(seq -f "%05g" 0 0)
do
    echo "start download part $i"
    img2dataset --url_list $1/mscoco_part_15K.parquet --input_format "parquet" \
        --url_col "URL" --caption_col "TEXT" --output_format webdataset\
        --output_folder $folder/split_$i --processes_count 1 --thread_count 1 --resize_mode border \
#            --save_additional_columns '["NSFW","similarity","LICENSE","SAMPLE_ID"]'
    echo "end download part $i"
done