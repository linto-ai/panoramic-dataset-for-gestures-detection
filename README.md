# Panoramic_Database

* This database contains 2085 annotated panoramic images of work meetings at LINAGORA.

* In addition, this database contains annotations of gestures, such as hand_up, voting.

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
	<filename>frame1043.jpg</filename>
	<path>/home/ons/conf_data/data/frame1043.jpg</path>
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
		<name>hand_up</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>1033</xmin>
			<ymin>257</ymin>
			<xmax>1088</xmax>
			<ymax>372</ymax>
		</bndbox>
	</object>
	<object>
		<name>person</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>62</xmin>
			<ymin>292</ymin>
			<xmax>226</xmax>
			<ymax>460</ymax>
		</bndbox>
	</object>
	<object>
		<name>person</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>259</xmin>
			<ymin>299</ymin>
			<xmax>383</xmax>
			<ymax>439</ymax>
		</bndbox>
	</object>
	<object>
		<name>person</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>413</xmin>
			<ymin>256</ymin>
			<xmax>573</xmax>
			<ymax>432</ymax>
		</bndbox>
	</object>
	<object>
		<name>person</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>727</xmin>
			<ymin>266</ymin>
			<xmax>860</xmax>
			<ymax>436</ymax>
		</bndbox>
	</object>
	<object>
		<name>person</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>872</xmin>
			<ymin>265</ymin>
			<xmax>1053</xmax>
			<ymax>500</ymax>
		</bndbox>
	</object>
	<object>
		<name>person</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>1022</xmin>
			<ymin>254</ymin>
			<xmax>1172</xmax>
			<ymax>432</ymax>
		</bndbox>
	</object>
</annotation>
 ```
