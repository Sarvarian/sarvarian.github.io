
# Aban Simple Object Notation

## Verse 0 What is ASON

This a simple serialization format for
aban language system.

Something like JSON or YAML.

Despite the name, it is not spouse
to be a superset of JSON, even though
implementations can be compatible with
JSON.


## Verse 1 Grand Struction of a Document

A document, lets say it starts with opening
of a file, may have 3 or 4 thing.

First document format directive.

Second document purpose directive.

Third the content.

Forth a document terminator in order to
start a new document in the same file.
Like YAML.


## Verse 2 Document Format Directive

This is optional, and may omit.

This directive will come as token
right after start of the document,
or the file.

Preferably no space or new line
before it

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


