from pathlib import Path


def read_text(filename):
    result = ''
    with open(filename, encoding='utf-8') as file:
        for line in file:
            result += line + '\n'
    return result


def write_text(filename, text):
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)


def parse(_str):
    _str = _str.replace('وإلا إذا كان ', 'elif ')
    _str = _str.replace('إذا كان ', 'if ')
    _str = _str.replace('وإلا', 'else ')
    _str = _str.replace('طالما ', 'while ')
    _str = _str.replace('لكل ', 'for ')
    _str = _str.replace(' استمر ', ' continue')
    _str = _str.replace(' استمر\n', ' continue\n')
    _str = _str.replace(' اكسر الحلقة ', ' break')
    _str = _str.replace(' اكسر الحلقة\n', ' break\n')

    _str = _str.replace(' في ', ' in ')

    _str = _str.replace('صح ', 'True')
    _str = _str.replace('خطأ', 'False')
    _str = _str.replace('مشيها', 'pass')
    _str = _str.replace('لا شيء', 'None')

    _str = _str.replace('٠', '0')
    _str = _str.replace('١', '1')
    _str = _str.replace('٢', '2')
    _str = _str.replace('٣', '3')
    _str = _str.replace('٤', '4')
    _str = _str.replace('٥', '5')
    _str = _str.replace('٦', '6')
    _str = _str.replace('٧', '7')
    _str = _str.replace('٨', '8')
    _str = _str.replace('٩', '9')

    _str = _str.replace('دالة ', 'def ')
    _str = _str.replace('فئة ', 'class ')

    _str = _str.replace('اطبع', 'print')
    _str = _str.replace('نوع', 'type')
    _str = _str.replace('قرب', 'round')
    _str = _str.replace('مدى', 'range')
    _str = _str.replace('رقم صحيح', 'int')
    _str = _str.replace('رقم كسري', 'float')

    return _str


if __name__ == '__main__':
    # contents = Path('test.pyar', encoding='utf-8').read_text()
    contents = read_text('test.pyar')
    result = ''

    str_prefixes = ['"', "'", '"""', "'''"]
    start = 0
    i = -1
    for str_prefix in str_prefixes:
        i = contents.find(str_prefix, start)
        while i != -1:
            result += parse(contents[start: i])

            start = i + 1
            i = contents.find(str_prefix, start)
            if i == -1:
                raise Exception('String error')

            result += contents[start-1 : i+1]
            start = i + 1

            i = contents.find(str_prefix, start)

    result += parse(contents[start : ])

    # Path('test.py').write_text(result)
    write_text('test.py', result)

    import test
