
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
numerics and strings.

Unlike JSON and other serialization
languages, ASON specification is not
concern with types, so there is no
types like boolean or integers define
by the specification.

Any type inference is application specific
and may define by each application.
ASON specification is only concern with how
to author and parse information in a cohesive
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
depend on document format, checkout [Document
Format Directive](#2-document-format-directive).

For example 'abanascii' only allow use of
ASCII english letters, numbers, '_underline',
and '.period' to be used for tokens.
Plus and stated before, no number as the
first character of a token and no space.

## [6] Numerics

Numerics are just numbers. Kind of like
tokens but just numbers. They start
with numbers, no space, and supposedly
no letter or other characters.

As stated before ASON do not assume type.
Numerics here are just string of numeric
characters/symbols. There types are
subjected to the parser and semantic
of the application.

But as some extra features, parsers
may support some extra features for
numerics, like having a period mark in
the middle of numeric strings to
specify that the number has fractions,
or underline, '_',  in between digits
to make long numbers more readable but
get ignore by the parser, or some other
formats to define different floating point
values or maybe some other types that has
numeric representations. The important
point about ASON numerics is that they
start with numeric symbols and like
tokens end with white spaces.

I do not specify any extra feature about
numerics in this specification. Any more
feature, like the examples in the previous
paragraph, are subjected to the parser
reading the document and may vary.
Sorry for inconvenience. I know this would
cause incompatibility among parsers.

But for one, you are writing ASON with
semantic of a specific application in
mind, so you can take parser of the
application into consideration while
authoring ASON documents.

For second, each parser, given some time,
will start adding more and more features,
more or less, eventually. So, even if
there is no standard, a common ground
will be reached, eventually.

If you are really concern about standard
of numeric parsing of ASON, start a committee
and standardise new features every 3 years,
until no parser can keep up with the standard!

So, as far as I and this specification is
concern, numerics are numbers, no fancy feature.
Keep it simple and allow any newbie programmer
be able to write an ASON parser in a weekend.
(I'm taking about myself here!)

## [7] Strings

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

```
'single quoted \' string'
"double quoted \" string'
```

Just to be sure and everyone be in the same
page, no matter of the string type or what
symbol exactly started the string lets say
by the specification we have 3 escape 
characters as follows:

```
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

## [9] ASON Graph

When you author an ASON document,
essentially you are describing a
graph.

We talk about nodes of the graph
before. Tokens, numerics, and
strings are all different ways
to describe a node in an ASON
graph.

Beyond nodes, there are 3 different
method to connet nodes togather
and eventually shape a graph.
We call them linking methods.

First method is spacing.

Second method is using brackets.

Third method is commas and semicolons.

You can use them, avoid them, or
mix these 3 different methods as
you please.

## [10] Basic Linking

For start, let us consider the most
basic form of linking. This essentially
is a part of spacing method, but I
talk about spacing method in detail
in another section.

Considering an ASON file, or an ASON
document, as the root node of our graph.
Each Line is node. Following example:

```
firstNode
'secondNode'
33
```

As simple as that. You divide nodes
into lines. Empty lines will get
and should get ignored. You can
have as many empty line in your
document as you want. Unless specify
otherwise by an application and
its parser. Also, this may or may not
get overrule by other linking methods!

Now what about multiple nodes in
one line? You may ask! Example follows:

```
person1 'Sara' 23
person2 'Ali'  25
```

The first node in the line consider
the top node and every other node
that came after it in the same line
will be directly linked to the first
node as its sub node. So, in example
above, you have string 'Sara' and
numeric 23 directly linked
to token 'person1'. More advanced
linking methods may overrule this,
and we will talk about this in the
future.

So, as some basic linking rules,
just remember the line division
rule, and the that nodes in
the same line all get linked
as sub nodes to the first node
in that line.

## [11] Space Linking

In extension to those basic linking
rules, as the first linking method
we use space and indentation to
describe node hierarchies.

If you know languages like python or
haskell, indentation rules are almost
similar.

## [12] Bracket Linking

## [13] Comma and Semicolon Linking



