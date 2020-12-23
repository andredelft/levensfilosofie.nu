from datetime import date

from .models import *

def post(data):
    sym_date = date(*data.pop('date'))
    talks = data.pop('talks')
    program = data.pop('program')

    print(f'Posting symposium with {len(talks)} talks and {len(program)} program items')
    symposium = Symposium(**data, date=sym_date)
    symposium.save()
    Talk.objects.bulk_create(
        Talk(symposium=symposium, number=i+1, **talk) for i, talk in enumerate(talks)
    )
    ProgramItem.objects.bulk_create(
        ProgramItem(symposium=symposium, number=i+1, **program_item) for i, program_item in enumerate(program)
    )
