
# Aban Graph Notation

## [0] What is AGN

It is a basis for all languages
under aban language family.

It describes the syntax of most
if not all aban languages.

AGN is all about syntax, a simple syntax
that you can use to describe a graph in
a text file.

AGN is NOT concern with semantics in any
shape or form, only syntax.

## [1] Variations

Aban languages, sometimes called
'Variations', sometimes 'Editions'.

AGN is the base syntax of most, if not
all, aban languages.

Variations define semantics for
information presented in aban documents.

## [2] Documents

A computer text file can contain one or
more aban documents.

Each document possibly contain three
meta pieces plus its main content.

These four pieces are as follows:

First, Document Character Encoding
Directive, or CED for short.

Second, Document Purpose Directive, or
just the Purpose if context is clear.

Third, the main content, that we  will
talk about later.

Forth, Document Terminator, that signals
end of a document and possibly start of
a new document in the same file.

## [3] Document Character Encoding Directive

We are just going to call this one CED
for short.

CED tells the parser, what character
encoding to use, and also the character
set used from that encoding.

for example, for a default 'abanascii'
CED, the valid character set would be
set of a-z, A-Z, 0-9, [], '', "", -, .,
,, ;, /, \, new line, tab, and space
characters. (If I'm not missed
anything!) Any other character, even
ASCII, would be invalid.

CED should come right at the start of
any document. At the first line, no
space before it. Something like
following example:

```
abanancii

"this document has 'abanascii' CED"

```

Some examples of CED are: 'abanascii',
'abanfa', and 'abanutf8'.

CED and be omitted, and default CED
should be assumed 'abanascii', but
because UTF-8 is a superset of ASCII, so
if a parser assume 'abanutf8' as
default, there should not be a problem.





