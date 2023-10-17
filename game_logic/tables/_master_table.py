import os
from .char_names import (
    male_first_names,
    female_first_names,
    surnames_first_part,
    surnames_last_part,
)
from .delusions import delusions

_master_table = {
    "male_first_names": male_first_names,
    "female_first_names": female_first_names,
    "surnames_first_part": surnames_first_part,
    "surnames_last_part": surnames_last_part,
    "delusions": delusions,
}


if __name__ == "__main__":
    print(_master_table.keys())
