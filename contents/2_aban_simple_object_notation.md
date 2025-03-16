
# ASON

## [0] What is ASON

Aban Simple Object Notation

This a simple serialization format for
aban language system.

Something like JSON or YAML.

Despite the name, it is not spouse
to be a superset of JSON, even though
implementations can be compatible with
JSON.


## [1] Grand Struction of a Document

A document, lets say it starts with opening
of a file, may have 3 or 4 thing.

First document format directive.

Second document purpose directive.

Third the content.

Forth a document terminator in order to
start a new document in the same file.
Like YAML.


## [2] Document Format Directive

This is optional, and may omit.

This directive will come as token
right after start of the document,
or the file.

Preferably no space or new line
before it.

And certainly no content or token or
directive before it.

The token of the directive should be
recognizable by the parser.

Some of the possible document formats
are: 'abanascii', 'abanutf8', 'abanfa'.

By specification, if document format
directive omitted, default should be
'abanascii', but because UTF8 encoding
is a superset of ASCII encoding,
implementations, may choose 'abanutf8'
as default.

## [3] Document Purpose

As any aban Language variation,
the first token of any document
should be the document purpose,
with the exception of format directive

In case of omission of purpose directive,
fault tolerance system may or may not
deduce the purpose of the document by
its content.

But it is strongly suggested to include
the document purpose at the start of
every document.

For a simple ASON document, purpose
document may be 'ason' or
'aban simple object notation'.

## [4] Content

An ASON document is like a graph.
The file is the root, each token or
string in the file is like a node.

There are 3 types of nodes: tokens,
strings, and numbers.

Unlike JSON and other serialization
languages, ASON specification is not
concern with types, so there is no
types like boolean or integers define
by the specification.

Any type inference is application specific
and may define by the application(s) using
ASON for data serialization.
ASON specification is only concern with how
to produce and parse information in a cohesive
language. Semantic of information is not
responsibility of ASON specification.

## [5] Tokens

Tokens are words, aka string of characters,
like variable names and type names in other
languages.

They may start with any letter, and include
numbers but not as the first character.
No space is allowed.

What characters and letters are allowed are
depend on document format, checkout Document
Format Directive.

For example 'abanascii' only allow use of
ASCII english letters and numbers and
underline, '_', to be used for tokens.
Plus and stated before, no number as the
first character of a token and no space.

## [6] Strings

Strings may start with 'single quote' or
"double quote" character and end when parser
reaches the same character.

Contents inside quotation marks may be
any byte and formating or encoding
regardless of the document format. Heck,
you can embed binary encodings as strings.

There is only 3 escape characters define
by this specification for contents inside
strings.

The quotation mark that started the string
maybe escaped using a forward slash, '\\'.
something like example below:

```ason
'single quoted \' string'
"double quoted \" string'
```

Just to be sure and everyone be in the same
page, no matter of the string type or what
symbol exactly started the string lets say
by the specification we have 3 escape 
characters as follows:

```ason
'single quoted \' escape'
'double quoted \" esacpe'
'and one forward slash \\'
```

By specification any other use of forward
slash inside strings are just read as they
are, and they would not escape or altered
by the parser.
Unless parser is subjected by application
specific settings.

Other than the 3 escape characters define
above, and string bounds using single and
double quotation characters, any other
parsing and encoding of the content inside
strings are responsibilities of
the application using ASON and not ASON
as a language.

## [7] Numbers



## [8] Annotated Strings

This a bonus feature and I would say by
default should be disabled unless an
application requires it.

Annotated strings are strings annotated
with a token right before their quotation
mark. Something like following examples:

```
annotation'my string is annoatated'
another"Another annoated string"
hex'ff00'
date'2583-12-26'
time"13:23:47"
```

Attention, between annotation and the
string should not be any space or extra
characters. Annotations are subject
to rules on token. The only different
between annotations and tokens is the
quotation mark that comes right after
the annotation. Token recognition ends
with a space or newline or any form of
white characters.

Annotation have no effect on the syntax
of ASON, they can be used as a hint to
the application on how to read and parse
the content inside the string that came
right after the annotation.

Applications that does not need this
feature, their ASON parser may ignore
any annotated strings or produce error
on encountering any annotated string.
Depend on how strict they want to be
with their edition of ASON language.

As a default behavior, if I were to write
a generic ASON parser, I would produce
error on annotated strings. Unless
the application using the parser explicitly
set the parser to ignore annotated strings,
or enable this specific feature.



