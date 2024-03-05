#!/bin/bash

file_path="./Cas_list.txt"

if [ -f "$file_path" ]; then
    # Read the file line by line
	    while IFS= read -r line; do
        # Process each line
        echo "Processing line: $line"
		filename=$(basename "$line")
		echo "Filename: $filename"
		journal="/file/read-case-data/
				${line}
				file/export/ascii \"./${filename%.*}\" () yes temperature no nh3 h2 o2 oh h2o no2 nh2 n2 quit yes ok
				exit
				yes
				exit"

				echo "$journal" >> journal.jou
				module load ansys/R2019R3
				fluent 2ddp -t0 -g -i journal.jou 
				rm journal.jou

    done < "$file_path"
else
    echo "File not found: $file_path"
fi


