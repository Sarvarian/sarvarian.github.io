
# Aban Graph Notation

## [0] What is AGN

AGN is a generic syntax, used by most
if not all aban family of languages.

What AGN is really doing is describing
a graph.

Semantic of information presented
is none of AGN concerns.

## [2] Documents

A computer text file can contain one or
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

CED can be omitted, and default CED
should be assumed abanascii.

Because UTF-8 is a superset of ASCII,
if parsers assume abanutf8, as default,
there should not be any problem.

# Document Purpose Directive

Purpose directive is just one line at
the start of every aban document, at
the start after CED if CED is not
omitted.

When context is clear,
purpose directive can just be referred
to as purpose; that is the purpose of
a document.

What purpose do is telling readers, like
parsers, what semantic been used for
that document.

Some of example purposes are:
'aban script', 'c module',
'project description',
'aban report document'.

Unlike CED that should come right at
the start of document, before purpose
directive can come non-meaningful tokens
like whitespaces or comments.

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

# Document Terminator












