# Copyright 2018 Jaewook Kang (jwkang10@gmail.com)
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===================================================================================
# -*- coding: utf-8 -*-

import os
from os import getcwd
from os import listdir
import argparse
import random


HOME                    =  getcwd()
DATASET_PATH            = '/images_for_annotation/'
# DATASET_TYPE            = '/dontbeturtle/croudworks/train_set_croudworks5_640x480'
DATASET_TYPE            = '/dontbeturtle/custom'
# DATASET_TYPE            = '/dontbeturtle/flic/0'
# DATASET_TYPE            = '/dontbeturtle/shortbbcpose/0'

# DATASET_TYPE            = '/train_set_croudworks_640x480/train_set_croudworks1_640x480/'
# DATASET_TYPE            = '/train_set_croudworks_640x480/train_set_croudworks2_640x480/'
# DATASET_TYPE            = '/train_set_croudworks_640x480/train_set_croudworks3_640x480/'
# DATASET_TYPE            = '/train_set_croudworks_640x480/train_set_croudworks4_640x480/'
# DATASET_TYPE              = '/train_set_croudworks_640x480/train_set_croudworks5_640x480/'
# DATASET_TYPE              = '/YouTube_Pose_dataset_1.0/images/'
# DATASET_TYPE            = '/lsp_dataset/images/'

# RESIED_DATASET_TYPE     = '/test_set_collected_resized/'
# RESIED_DATASET_TYPE     = '/train_set_croudworks_resized/'


def main(filename,samplenum=None):

    datapath = HOME + DATASET_PATH + DATASET_TYPE
    filelist = listdir(datapath)
    filelist.sort()

    try:
        filelist.remove('.DS_Store')
    except:
        print('No .DS_Store')

    if samplenum == None:
        samplenum = len(filelist)

    print('[main] Dataset path: %s' % datapath)
    if int(samplenum) < len(filelist):
        picked_filelist = random.sample(set(filelist),int(samplenum))
        print('[main] Randomly sample %s samples from set' % samplenum)
    else:
        picked_filelist = filelist
        print('[main] Randomly sample %s samples from set' % len(filelist))


    with open(filename,'w') as fp:
        for i in range(0,len(picked_filelist)):
            fp.write(picked_filelist[i] + '\n')



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--filename',
        default=['images.txt'],
        help='a list of filename for dataset',
        nargs='+',
        required=False
    )

    parser.add_argument(
        '--samplenum',
        default=[None],
        help='The number of image samples to pick',
        nargs='+',
        required = False
    )

    args = parser.parse_args()
    print ('[Main] args.filename = %s' % args.filename)
    print ('[Main] args.samplenum = %s' % args.samplenum)

    main(filename=args.filename[0],samplenum=args.samplenum[0])