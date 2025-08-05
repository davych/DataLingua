### Task
Generate a SQL query to answer [QUESTION]{user_question}[/QUESTION]

### Critical SQL Rules
- NEVER use COUNT(*) or COUNT(table.*) in any query
- Always use COUNT(specific_field_name) when counting records
- Example: Use COUNT(album.albumid) instead of COUNT(*) or COUNT(album.*)

### Instructions
- If you cannot answer the question with the available database schema, return 'I do not know'
- Follow all Critical SQL Rules above strictly

### Database Schema
The query will run on a database with the following schema:
{table_metadata_string}

### Answer
Given the database schema, here is the SQL query that answers [QUESTION]{user_question}[/QUESTION]
[SQL]
