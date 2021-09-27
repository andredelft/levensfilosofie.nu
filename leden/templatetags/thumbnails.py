from django import template
from django.utils.html import mark_safe

from cloudinary import CloudinaryImage

register = template.Library()

SIZE = 158
SIZES = {
    'width': SIZE,
    'height': SIZE
}
RESOLUTIONS = [1, 2]
CLOUDINARY_CONFIG = {
    'crop': 'thumb',
    'gravity': 'face'
}


@register.filter()
def thumbnail(image, sizes=SIZES, resolutions=RESOLUTIONS):
    image = CloudinaryImage(image.public_id)

    srcset = {
        res: image.build_url(
            transformation=[{
                "crop": "thumb",
                "gravity":
                "face",
                "dpr": res,
                **sizes
            }]
        ) for res in resolutions
    }

    return mark_safe(
        '<img height="{height}" width="{width}" src="{src}" srcset="{srcset}">'.format(
            src=srcset[resolutions[0]],
            srcset=",".join([f"{src_} {res}x" for res, src_ in srcset.items()]),
            **sizes
        )
    )
