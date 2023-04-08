"""
    pygments.lexers.spice
    ~~~~~~~~~~~~~~~~~~~~~

    Lexers for the Spice programming language.

    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, bygroups, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Whitespace

__all__ = ['SpiceLexer']


class SpiceLexer(RegexLexer):
    """
    For Spice source.

    .. versionadded:: 2.11
    """
    name = 'Spice'
    url = 'https://www.spicelang.com'
    filenames = ['*.spice']
    aliases = ['spice', 'spicelang']
    mimetypes = ['text/x-spice']

    tokens = {
        'root': [
            (r'\n', Whitespace),
            (r'\s+', Whitespace),
            (r'\\\n', Text),
            # comments
            (r'//(.*?)\n', Comment.Single),
            (r'/(\\\n)?[*]{2}(.|\n)*?[*](\\\n)?/', String.Doc),
            (r'/(\\\n)?[*](.|\n)*?[*](\\\n)?/', Comment.Multiline),
            # keywords
            (r'(import|as)\b', Keyword.Namespace),
            (r'(f|p|type|struct|enum)\b', Keyword.Declaration),
            (words(('if', 'else', 'for', 'foreach', 'while', 'break',
                    'continue', 'return', 'assert', 'thread', 'unsafe', 'ext',
                    'dll'), suffix=r'\b'), Keyword),
            (words(('const', 'signed', 'unsigned', 'inline', 'public'),
                   suffix=r'\b'), Keyword.Pseudo),
            (words(('new', 'switch', 'case', 'yield', 'stash', 'pick', 'sync',
                    'class'), suffix=r'\b'), Keyword.Reserved),
            (r'(true|false|nil)\b', Keyword.Constant),
            (words(('double', 'int', 'short', 'long', 'byte', 'char', 'string',
                    'bool', 'dyn'), suffix=r'\b'), Keyword.Type),
            (words(('printf', 'sizeof', 'len', 'tid', 'join'), suffix=r'\b(\()'),
             bygroups(Name.Builtin, Punctuation)),
            # numeric literals
            (r'[0-9]*[.][0-9]+', Number.Double),
            (r'0[bB][01]+[sl]?', Number.Bin),
            (r'0[oO][0-7]+[sl]?', Number.Oct),
            (r'0[xXhH][0-9a-fA-F]+[sl]?', Number.Hex),
            (r'(0[dD])?[0-9]+[sl]?', Number.Integer),
            # string literal
            (r'"(\\\\|\\[^\\]|[^"\\])*"', String),
            # char literal
            (r'\'(\\\\|\\[^\\]|[^\'\\])\'', String.Char),
            # tokens
            (r'<<=|>>=|<<|>>|<=|>=|\+=|-=|\*=|/=|\%=|\|=|&=|\^=|&&|\|\||&|\||'
             r'\+\+|--|\%|\^|\~|==|!=|::|[.]{3}|[+\-*/&]', Operator),
            (r'[|<>=!()\[\]{}.,;:\?]', Punctuation),
            # identifiers
            (r'[^\W\d]\w*', Name.Other),
        ]
    }
