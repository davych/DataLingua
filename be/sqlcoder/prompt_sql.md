### Task
Generate a SQL query to answer [QUESTION]{user_question}[/QUESTION]

### Critical SQL Rules
- NEVER use COUNT(*) or COUNT(table.*) in any query. If you use COUNT, you MUST specify a concrete field name (e.g. COUNT(track.TrackId)), never use COUNT(*) under any circumstances.
- Always use COUNT(specific_field_name) when counting records
- Example: Use COUNT(album.albumid) or COUNT(track.TrackId) instead of COUNT(*) or COUNT(album.*)

### Instructions
- Always analyze and utilize all foreign key relationships (relation map) between tables when generating SQL queries. Do not ignore any possible table joins or relationships.
- When answering, if a question involves multiple tables, ensure to use the correct JOINs based on the foreign key relations provided in the schema.
- If you use COUNT(*), your answer will be considered invalid. Always use COUNT(specific_field_name) and explain your choice if possible.
- If you cannot answer the question with the available database schema, return 'I do not know'
- Follow all Critical SQL Rules above strictly
- Only output the SQL query, do not include any explanations or additional text.

### Database Schema
The query will run on a database with the following schema:
{table_metadata_string}

### Answer
Given the database schema, here is the SQL query that answers [QUESTION]{user_question}[/QUESTION]
[SQL]