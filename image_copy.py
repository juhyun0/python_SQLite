import sys
from wand.image import Image

if len(sys.argv) < 2:
	print('{0} <ORIGINAL PATH>'.format(sys.argv[0]))
	sys.exit()

original_path = sys.argv[1]

with Image(filename=original_path) as image:
	print("Original : {0}, {1}".format(image.format, image.size))

	clone=image.clone()
	print("Clone : {0}, {1}".format(clone.format, clone.size))
	clone.save(filename='clone.{0}'.format(original_path))
