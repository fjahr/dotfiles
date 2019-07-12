def Settings( **kwargs ):
    return {
        'flags': ['-fsyntax-only', '-std=c++11', '-xc++',   '-I/usr/lib/', '-I/usr/include/', '-Isrc', '-DNDEBUG', '-ferror-limit=10000', '-fexceptions', '-Wno-variadic-macros', '-Wno-long-long', '-Werror', '-Wextra', '-Wall']
    }
