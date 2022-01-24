from django.conf import settings


def provide_tags(request):
    return (
        settings.TAILWIND_CLASSLISTS if hasattr(settings, "TAILWIND_CLASSLISTS") else {}
    )
