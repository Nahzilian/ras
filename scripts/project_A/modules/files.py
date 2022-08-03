from datetime import datetime, date


def write_to_file(file_name: str, content: str) -> None:
    now = datetime.now()

    second = now.second
    minute = now.minute
    hour = now.hour

    day = now.day
    month = now.month
    year = now.year
    
    time = f'{day}_{month}_{year}.{hour}.{minute}.{second}'
    with open(f'txt/{file_name}_{time}.txt', 'w') as f:
        f.write(content)
