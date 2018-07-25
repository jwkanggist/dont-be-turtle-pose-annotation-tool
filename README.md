# pose-annotation-tool for dont be turtle proj

## About
This is 

## Installation

### Compiling
```bash
$ cmake CMakeLists.txt
$ make
```

### Running

```bash
$ ./pose_annotation_tool images_list.txt
```

## How to use


### Using the tool
The image is loaded and displayes on screen one by one.

Press ENTER to annoate current image

Press SPACE to skip current image


#### Once the image has been selected for annotation

Left Click - Visible joint

Right Click - Occluded joint

TAB - Current joint is not applicable for current image

Any key - register the annotation and move to next joint

#### After all the joints are annotated the joint coordinates is written to file and next image is loaded.

## Components

#### generate_imagetxt.py
- Generate image files list included in image annotation

#### convert_lspdata_label_to_json.py
- Conversion the original lsp label set to a label set for dont be turtle proj

#### rename_train_set_croudworks.py
- rename cloudwork dataset to remove phonename and attach image index

#### resize_image.py
- resize cloudwork dataset to the size 640 X 480

 

## Code Reference
- [ https://github.com/suriyasingh/pose-annotation-tool]( https://github.com/suriyasingh/pose-annotation-tool )