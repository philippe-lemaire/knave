import re

PATTERN = r"\d+’"


def convert_to_metric_spells(SPELLS):
    """Goes through the SPELLS dict and finds feet measurments, and turns them to metric."""
    for name, spell_desc in SPELLS.items():
        match = re.search(PATTERN, spell_desc)
        if match:
            found = re.findall(PATTERN, spell_desc)
            for amount in found:
                numeric_amount = int(amount[:-1])
                metric_amount = 30 * numeric_amount
                unit = "cm"
                if metric_amount >= 100:
                    metric_amount = round(metric_amount / 100, 2)
                    unit = "m"
                    if metric_amount.is_integer():
                        metric_amount = int(metric_amount)
                conversion = f"{metric_amount}{unit}"

                spell_desc = spell_desc.replace(amount, conversion)
            SPELLS[name] = spell_desc


def convert_to_metric_careers(d):
    """Takes in the careers dict and converts items inside to metric as needed"""
    for key, value in d.items():
        metric_items = []
        for item in value:
            match = re.search(PATTERN, item)
            if match:
                found = re.findall(PATTERN, item)
                for amount in found:
                    numeric_amount = int(amount[:-1])
                    metric_amount = 30 * numeric_amount
                    unit = "cm"
                    if metric_amount >= 100:
                        metric_amount = round(metric_amount / 100, 2)
                        unit = "m"
                        if metric_amount.is_integer():
                            metric_amount = int(metric_amount)
                    conversion = f"{metric_amount}{unit}"

                    item = item.replace(amount, conversion)

            metric_items.append(item)
        d[key] = metric_items
