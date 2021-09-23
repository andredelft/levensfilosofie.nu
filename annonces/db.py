from datetime import date

from .models import Talk, ProgramItem, Symposium


def post_symposium(data):
    sym_date = date(*data.pop('date'))
    talks = data.pop('talks')
    program = data.pop('program')

    print(
        f'Posting symposium "{data.get("title")}" with {len(talks)} talks and '
        f'{len(program)} program items'
    )
    symposium = Symposium(**data, date=sym_date)
    symposium.save()
    Talk.objects.bulk_create(
        Talk(symposium=symposium, **talk) for talk in talks
    )
    ProgramItem.objects.bulk_create(
        ProgramItem(symposium=symposium, **program_item)
        for program_item in program
    )
