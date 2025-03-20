
# Aban Graph Notation

## What is AGN

It is a basis for all languages
under aban language family.

It describes the syntax of most
if not all aban languages.

AGN is all about a simple syntax
that you can use to describe a
graph in a simple text file
document.

AGN is not concern with the
semantics of the information
describe in the document, only
syntax.

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


