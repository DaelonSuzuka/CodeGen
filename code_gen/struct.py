def struct(name='', members=[], options=[]):
    struct = []

    if 'typedef' in options:
        struct.append('typedef struct {')
    else:
        struct.append(f'struct {name} {{')

    [struct.append(f'{m};') for m in members]

    if 'typedef' in options:
        struct.append(f'}} {name};')
    else:
        struct.append('};')

    return struct
