class Struct():
    name = ''
    members = []
    options = []

    def __init__(self, name='', members=[], options=[]):
        self.name = name
        self.options = options
        self.members = members

    def erase_contents(self):
        self.members = []

    def add_members(self, members=''):
        def flatten(list_of_lists):
            flat_list = []
            for l in list_of_lists:
                flat_list.extend(l)
                flat_list.append('\n')
            return flat_list

        self.members.extend(flatten(members))

    def add_member(self, member_type, name):
        self.members.append(f'{member_type} {name};')

    def add_bitfield(self, name, size=1):
        self.members.append(f'unsigned {name} : {size};')

    def assemble(self):
        struct = []

        if 'typedef' in self.options:
            struct.append('typedef struct {')
        else:
            struct.append(f'struct {self.name} {{')

        [struct.append(f'{m};') for m in self.members]

        if 'typedef' in self.options:
            struct.append(f'}} {self.name};')
        else:
            struct.append('};')

        return struct
