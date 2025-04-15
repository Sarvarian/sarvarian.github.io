
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

## [6] New Document Limbo

As mentioned at the end of the previous 
verse, for fault tolerance purpose,
after a document terminator may come
some whitespace and a newline
characters before the start of the new
document.

Now, this presents us with a problem.

The Previous document is terminated and
the new document is not started.
So, what is CED to define character
encoding for whitespace and newline
characters?

We refer to this or these sections of
aban files as new document limbo, or
just limbo when the context is clear.

I like to say it is undefined and 
depends on parsers to decide.

But for the sake of having a common
standard, CED of the terminated
document defines whitespace and newline
encoding of limbo.

Still, parsers are encouraged to do
their best judgment; Bringing documents
they are reading at the time of parsing
into consideration.

## [7] Content





