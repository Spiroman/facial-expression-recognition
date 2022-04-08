#!/bin/bash
for tiff in jaffedbase/*; 
do; 
		j=${tiff/tiff/jpg}; 
		j2=${j/jaffedbase/jaffejpeg}; 
		convert $tiff $j2; 
done;
