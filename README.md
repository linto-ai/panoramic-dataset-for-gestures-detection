# Panoramic_Database

* This database contains 2085 annotated panoramic images of work meetings at LINAGORA.

* In addition, this database contains annotations of person's gestures, such as speaking, voting.

* The database note format is [VocPascal](https://medium.com/towards-artificial-intelligence/understanding-coco-and-pascal-voc-annotations-for-object-detection-bb8ffbbb36e3)

* Our VocPascal repository is made up of the following files:

 ```
 .

 │   ├── Annotations  (2085 .xml)

 │   ├── ImageSets    # Contain four Main/*.txt which split the dataset

 │   │   └── Main    

 │   └── JPEGImages (2085 .jpg)
 ```

All labels are annotated by [LabelImage](https://github.com/tzutalin/labelImg)

* The `Annotations` : The VOC format `.xml` for Object Detection, automatically generate by the label tools. Below is an example of `.xml` file.

 ```xml
<annotation>
        <folder>data</folder>
        <filename>image1.jpg</filename>
        <path>/home/linagora/Desktop/new_data_linagora/gest/data/image1.jpg</path>
        <source>
                <database>Unknown</database>
        </source>
        <size>
                <width>1280</width>
                <height>640</height>
                <depth>3</depth>
        </size>
        <segmented>0</segmented>
        <object>
                <name>speaking</name>
                <pose>Unspecified</pose>
                <truncated>0</truncated>
                <difficult>0</difficult>
                <bndbox>
                        <xmin>126</xmin>
                        <ymin>305</ymin>
                        <xmax>154</xmax>
                        <ymax>383</ymax>
                </bndbox>
        </object>
	<object>
                <name>voting</name>
                <pose>Unspecified</pose>
                <truncated>0</truncated>
                <difficult>0</difficult>
                <bndbox>
                        <xmin>382</xmin>
                        <ymin>255</ymin>
                        <xmax>433</xmax>
                        <ymax>365</ymax>
                </bndbox>
        </object>
</annotation>

 ```
