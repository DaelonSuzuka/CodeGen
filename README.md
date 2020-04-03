CodeGen
=======

Generate C source code in a more structured way that raw string manipulation.
Works great with Ned Batchelder's CogApp.(link)

## Features

- Supports many C constructs
- Formatting via clang-format(must have clang-format installed, obviously!)


## Supported C constructs

- types (only some)
- variables
- functions
- enums
- structs
- header files

## Requirements

Codegen uses clang-format to clean up its output

## Installation

```
git clone https://github.com/DaelonSuzuka/CodeGen.git
cd CodeGen
pip install .
```


## Example

```
>>> import codegen as code
```

Let's create the simplest possible function:

```
>>> code.format(code.function())
'void func(void);'
```

Valid, but not terribly useful.

We need to at least give it a name:

```
>>> code.format(code.function('test')) 
'void test(void);'
>>> code.format(code.function(name='test2')) 
'void test2(void);'
```

Alright, now how about some parameters or a return type?

```
>>> code.format(code.function('test', params=['int x', 'bool y']))
'void test(int x, bool y);'
>>> code.format(code.function('test2', ret='bool'))
'bool test2(void);'
```

But wait, these have all been function declarations. How do we make a definition?

```
>>> code.format(code.function('test', body=['// this is a comment', 'foo();']))
'void test(void) {\n  // this is a comment\n  foo();\n}'
```

That's not quite right, let's try that again:
```
>>> print(code.format(code.function('test', body=['// this is a comment', 'foo();']))) 
void test(void) {
  // this is a comment
  foo();
}
```

Much better!