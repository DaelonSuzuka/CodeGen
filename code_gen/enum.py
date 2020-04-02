def enum(name='', values=[], prefix='', postfix='', options=[]):
    enum = []

    if 'typedef' in options:
        enum.append('typedef enum {')
    else:
        enum.append(f'enum {name} {{')

    if isinstance(values, list):
        if 'explicit' in options:
            [
                enum.append(f'{prefix}{v}{postfix} = {i},')
                for i, v
                in enumerate(values)
            ]
        else:
            [enum.append(f'{prefix}{v}{postfix},') for v in values]
    elif isinstance(values, dict):
        [enum.append(f'{prefix}{v}{postfix} = {values[v]},') for v in values]

    if 'typedef' in options:
        enum.append(f'}} {name};')
    else:
        enum.append('};')

    return enum