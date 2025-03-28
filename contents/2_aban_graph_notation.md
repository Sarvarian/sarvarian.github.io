
# Aban Graph Notation

## What is AGN

It is a basis for all languages
under aban language family.

It describes the syntax of most
if not all aban languages.

AGN is all about syntax, a simple syntax
that you can use to describe a graph in
a text file.

AGN is NOT concern with semantics in any
shape or form, only syntax.

## An Aban Document

A text file is a document.

But a text file can be divided
into multiple documents by using
what's called 'Document Terminator'.

Just like YAML files, you can
use three period characters '...'
to end a document and start a new
document.

```
'This is a document.'
...
'This is a second document.'
```

After a document terminator,
the rules for when the new
document actually starts is as
follows:

First, if there is anything came
right after the document terminator,
that thing is the first data of
the new document.

Second, if there is spaces between
the document terminator and the
thing, spaces shall get ignored
and the new document starts with
the thing.

Third, a new line after document
terminator, will start the new
document on that new line. Spaces
after document terminator shall
get ignored.

```
first_document


...second_document_starts_with_this


...   third_document_starts_with_this


...
fourth_document_start_with_this


...

fifth_document_starts_from_the_line_above


```

## Document Character Encoding Directive

Right at the start of a document,
you may specify what's called a
'Character Encoding Directive'.

CED tells the parser, what
character encoding to use for the
document at hand.

This can be omitted and default
encoding by specification shall
be 'abanascii' but because UTF-8
is compatible with ASCII encoding,
optionally parsers can default to
'abanutf8'.

Examples follows:

```
abanascii
'This document is encoded
in with ASCII characters.'


...abanutf8
'This document is encoded
in UTF-8 characters.'


...
'CED is ommited, so encoding
defualted to ASCII.'


```

Note that CED may influence more
than just character encoding.
Some of other features are as
follows:

Different CEDs may have the same
character encodings but limit their
document to different character-sets.

CED may alternate keyword names
in its document.

CED may use for internationalization
and translations.

## Document Purpose Directive

'Purpose Directive', or just
'Purpose' if context is clear,
specifies document's semantic.

AGN specification is only concern
is about syntax and this
specification specifies no semantic.
Therefore, there are what's called
'Aban Language Variations' or
'Editions', that are specify
different semantics on top of AGN
syntax. Some examples are:
'aban report document',
'aban script',
'project description',
'c module', etc.

Purpose directive should be the
first meaningful token after CED
in any document. If CED omitted,
then purpose directive would be
the first token.

Unlike CED that should come right
at the start of a document, before
a purpose directive, non-meaningful
tokens like spaces, white spaces,
new lines, and comments are allowed.

Example follows:

```
#! /usr/bin/aban
aban script


...abanascii
aban report document


...
abanfa
c module


```

## Content

After all these boilerplates are
said and done, we get to the main
content of aban documents.

There are two main topics to talk
about, nodes and node types, and
links and linking methods.

## 










