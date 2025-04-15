-- docs table
-- has the document id (did), and the document name (docname)
create table docs (did serial primary key , docname varchar(255));

-- fragment table
-- has the fid - fragment id
-- did - documents id to the document from which this fragment came
-- content - the human-readable text of the fragment
-- embedding - the vector embedding for the fragment with 768 dimensions
create table fragments (fid serial primary key , did integer references docs(did),
    content text, embedding vector(768));
