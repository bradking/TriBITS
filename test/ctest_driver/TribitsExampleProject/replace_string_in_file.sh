#!/bin/bash -e

FILE_TO_EDIT=$1
STRING_TO_REPLACE=$2
REPLACEMENT_STRING=$3

sed -i "s/$STRING_TO_REPLACE/$REPLACEMENT_STRING/g" $FILE_TO_EDIT
