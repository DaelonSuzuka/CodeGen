from pathlib import Path
from codegen.utils import hrule, format

class Header():
    contents = []
    includes = []
    name = ''
    guard = ''

    def __init__(self, name='', contents=[], includes=[]):
        self.set_name(name)
        self.add_contents(contents)
        self.add_includes(includes)

    def add_includes(self, includes=[]):
        if includes:
            [self.includes.append(f'#include {i}') for i in includes]
            self.includes.append('')

    def add_contents(self, contents=[]):
        def flatten(list_of_lists):
            flat_list = []
            for l in list_of_lists:
                flat_list.extend(l)
                flat_list.append('\n')
            return flat_list

        self.contents.extend(flatten(contents))

    def erase_contents(self):
        self.contents = []

    def set_name(self, name):
        self.name = name
        self.guard = '_' + Path(name).name.replace('.', '_').upper() + '_'

    def assemble(self):
        header = [
            f'#ifndef {self.guard}',
            f'#define {self.guard}',
            '',
        ]

        if self.includes:
            header.extend(self.includes)

        header.extend([
            hrule(),
            '',
        ])
        header.extend(self.contents)
        header.extend([
            '',
            f'#endif /* {self.guard} */',
        ])
        return format(header)

    def write(self):
        with open(self.name, 'w') as f:
            f.write(self.assemble())