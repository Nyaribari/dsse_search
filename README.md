**Searching in the Dark:** 

***A Multi Client Symmetric Searchable Encryption Scheme with Forward Privacy***

**Intro:**

Symmetric Searchable Encryption (SSE) is a
promising encryption technique that allows users to
securely outsource private data to an untrusted party
– such as a cloud service provider (CSP). More
precisely, an SSE scheme allows users to encrypt
their data locally with a key that is not known to
the CSP while at the same time they can search
directly over the encrypted data stored in one of
the remote locations maintained by the CSP. This,
allows them to retrieve files matching a query, without
revealing to the CSP (i.e. an untrusted party), neither
the data contents, nor the searched keyword. Ideally,
an SSE scheme would leak absolutely no information
to the CSP during the search process. To achieve
this, techniques such as oblivious RAM (ORAM)
must be used. However, adopting such techniques
will result to a scheme that is even less efficient
than downloading the entire encrypted database and
perform the search locally .
