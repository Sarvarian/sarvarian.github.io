
# Aban Graph Notation

## [0] What is AGN

AGN is a generic syntax, used by most
if not all aban family of languages.

What AGN is really doing is describing
a graph in text format.

Semantic of information presented
is none of AGN concerns.


## [2] Documents

A computer text file may contain one or
more aban documents.

Each document possibly contains three
meta pieces plus its main content.

These four pieces are as follows:

First, Document Character Encoding
Directive, or CED for short.

Second, Document Purpose Directive, or
just the Purpose if context is clear.

Third, the main content that we will
talk about later.

Forth, Document Terminator, that signals
the end of a document and possibly start
of a new document in the same file.


## [3] Document Character Encoding Directive

We are just going to call this one CED
for short.

CED tells the parser, what character
encoding to use, and also the character
set used from that encoding.

for example, for a default abanascii
CED, the valid character set would be
set of a-z, A-Z, 0-9, [], '', "", -, .,
,, ;, /, \, new line, tab, and space
characters (If I am not missed
anything).
Any other character, even
ASCII, would be invalid.

CED should come right at the start of
any document. At the first line, no
space before it. Something like
the following example:

```
abanancii

"this document has abanascii CED"

```

Some examples of CED are:
'abanascii', 'abanfa', and 'abanutf8'.

CED may be omitted, and default CED
should be assumed abanascii.

Because UTF-8 is a superset of ASCII,
if parsers assume abanutf8, as default,
there should not be any problem.


## [4] Document Purpose Directive

Purpose directive is just one line at
the start of every aban document, at
the start after CED if CED is not
omitted.

When context is clear,
purpose directive may just be referred
to as purpose; that is the purpose of
the document.

What purpose do is telling readers, like
parsers, what semantic been used for
that document.

Some of example purposes are:
'aban script', 'c module',
'project description',
'aban report document'.

Unlike CED that should come right at
the start of document, before purpose
directive, may come non-meaningful
tokens, like whitespaces or comments.

Examples follows:

```
abanascii
aban report document
```

Or

```
#! /usr/bin/aban
aban script
```


## [5] Document Terminator

Just like YAML, we may have multiple
aban documents in one file using what
is called a document terminator.

In an aban document, three dots at
the start of a line denote the end of
the document, and allow for the start
of a new document in the same file.

Example follows:

```

'This is first document in this file.'

...

'This is second doucument in this file.'

```

Three dots of document terminator,
signal the end of document.
So, everything after it will be content
of a new document.

So technically CED of the new document
should come right after three dots,
something like the following example:

```

'First Document'

...abanascii

'Second Document'

```

But as a fault tolerance mechanism,
the new document would not be started
until the first non-whitespace
character or newline.
So, the following examples are also
valid.

```

'First Document'

... abanfa

'Second Document'

...
abanutf8

'Third Document'

```


## [6] Document Break Limbo

As mentioned at the end of the previous 
verse, for fault tolerance purpose,
after a document terminator, may come
some whitespace characters and a newline
character, before the start of the new
document.

Now, this presents us with a problem.

The Previous document is terminated and
the new document is not started.
So, what is CED to define character
encoding for whitespace and newline
characters?

We refer to this or these sections of
aban files as document break limbo, or
just limbo when the context is clear.

I like to say it is undefined and 
depends on parsers to decide.

But for the sake of having a common
standard, CED of the terminated
document defines whitespace and newline
encoding of limbo.

Still, parsers are encouraged to do
their best judgment; Bringing documents,
they are reading at the time of parsing,
into consideration.


## [7] Content

About the main content.

When it comes to AGN syntax,
aban documents are composition of
nodes and how they link to each other.

In terms of graph theory, we can think
of an aban document as a tree.

Comparing to graph theory, I will use
these terminologies:

I will use nodes as opposed to vertices.

I will use links as opposed to edges.

I will use author node as opposed to
parent node or top node.

I will use subject node as opposed to
child node or sub node.

I will refer to a set of subjects of a
node to as its domain.


## [8] Node Forms

There are three ways to describe a
node in AGN; We call these forms.

These three forms are as follows:
Token form, numeric form, string form.

I describe these forms as for abanascii.
For other CEDs, please refer to their
documentation to see how nodes are
formatted.


## [9] Token Node Form

Tokens are strings of ASCII characters
limited to: lowercase and uppercase
a to z letters, one to nine number
characters, underline character,
dash character, and finally 
period character.

```
  a-z  A-Z  0-9  _  -  .
```

First note that tokens should not start
with numbers or dash character.

Second note that any space character in
the middle of a token will break it
and allow for the start of a new node.

BNF for tokens are as follow:

```
<TokenStart>  ::=  [a-z]
               |   [A-Z]
               |   "_"
               |   "." <TokenStart>

<Token>       ::=  <TokenStart>
               |   <Token> [a-z]
               |   <Token> [A-Z]
               |   <Token> [0-9]
               |   <Token> "_"
               |   <Token> "-"
               |   <Token> "."
               |   <Token> <Token>
```


## [10] Numeric Node Form

Numeric nodes are exactly like tokens,
but they should start with numbers.


## [11] String Node Form

Any consecutive amount of not mixed
single quotation mark or double
quotation marks will start a string node.

Reading of a string node shall end
when parser reached the same number of
the same quotation mark characters as
it is started it.

The content inside a string node shall
be of any kind and encoding and
formatting, even binary.
String nodes are provided as strings of
bytes or buffers of data from parsers
to applications.

There are three escape sequences.
Parsers, reading string node shall
substitute these sequences before
providing them to applications.

Escape sequences are: double forward
slash, forward slash single quotation
mark, and forward slash double
quotation mark.

```
  \\  \'  \"
```

Double forward slash shall be replaced
by just a slash character.

```
  \\    \
```

Forward slash single quotation mark
shall be replaced by just a quotation
mark character.

```
  \'    '
```

Forward slash double quotation mark
shall be replaced by just a double
quotation mark character.

```
  \"    "
```

These escape sequences are just
a standard behavior.
Parsers considering semantic of
an application may alter this behavior.

## [12] Annotated String

String forms can be annotated.
By prefixing them with a token form,
right before their starting quotation
mark.

Note that there should not be any space
between annotation and start quotation
mark.

Example:

```
myAnnotaiton'My string content'
```


## [13] Link Forms

There are three ways to link nodes
in AGN; We call these link forms.

These three link forms are as follows:
Space form, bracket form,
comma and semicolon form.

I describe these forms as for abanascii.
For other CEDs, please refer to their
documentation to see what are their
alternatives to these link forms.


## [14] Space Link Form


Space link form has three constructs,
as following:

Space that is just simple ASCII space
character.

Tab that is just simple ASCII tab
character.

```
<Space>   ::=  0x20
<Tab>     ::=  0x9
<Newline> ::=  0xA
           |   0xD 0xA
           |   0xD
```

Consecutive space characters are counted
as one space.

Unlike space, consecutive tabs have
significant.
Consecutive tabs are counted and their
count is stored as their indent level.

----------------------------------------

There are three constructs that we need
to talk about.
Space, tab, and newline characters.

Space is just 

Newline characters are any of the following
ASCII pattern, in order of significant:

```
\n     0xA
\n\r   0xD 0xA
\r     0xD
```





## Bracket Link Form


## Comma and Semicolon Link Form


## Comment

```
#
--
[-
-]
[-]
--]
[-
```

## Reserved for Extensions

```
()
{}
```


## Some General Formatting Guidelines

Have at least one empty line at the
start and at the end of any aban
document.
Except for CED, that is better to come
right at the start of the document.

........................................














