import tempfile

from PIL import Image


def downscale_image(source_path):
    output_path = tempfile.mktemp()
    im = Image.open(source_path)
    im.thumbnail((1000, 1000), Image.ANTIALIAS)
    im.save(output_path, format='JPEG', quality=65)
    return output_path
