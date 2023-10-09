import re 


def convert_to_metric_spells(SPELLS):
    pattern = r"\d+’"
    for name, spell_desc in SPELLS.items():
    
        match  = re.search(pattern, spell_desc)
        if match:
            found = re.findall(pattern, spell_desc)
            for amount in found:
                numeric_amount = int(amount[:-1])
                metric_amount = 30* numeric_amount
                unit = "cm"
                if metric_amount >=100:
                    metric_amount = round(metric_amount / 100,2)
                    unit = "m"
                    if metric_amount.is_integer():
                        metric_amount = int(metric_amount)
                conversion = f"{metric_amount}{unit}"
                
                spell_desc = spell_desc.replace(amount, conversion)
            SPELLS[name] = spell_desc

def convert_to_metric_careers(d):
    for key, value in d.items():
        if "’" in "".join(value):
            
            metric_items = []
            for item in value:
                print(item)
                if "’" in item:
                    length, thing = item.split()
                    try:
                        metric_length = int(length[:-1]) * 30
                        unit = 'cm'
                    except ValueError:
                        continue
                    if metric_length >= 100:
                        metric_length = round(metric_length // 100)
                        unit = 'm'
                    item = f"{metric_length}{unit} {thing}"
                metric_items.append(item)
                d[key] = metric_items