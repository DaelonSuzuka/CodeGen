def function(name='func', ret='void', params='void', body=None, options=[]):
    if isinstance(params, str):
        pass
    else:
        params = ', '.join(params)

    signature = ''

    if 'extern' and 'static' in options:
        raise Exception(f'conflicting options provided: {options}')

    if 'extern' in options:
        signature += 'extern '

    if 'static' in options:
        signature += 'static '

    signature += f'{ret} {name} ({params})'

    function = [signature]
    if body:
        function.append('{')
        [function.append(line) for line in body]
        function.append('}')
    else:
        function.append(';')

    return function