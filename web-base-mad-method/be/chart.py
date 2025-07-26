def recommend_chart(sql: str, data: list) -> list:
    sql_lower = sql.lower()
    if "group by" in sql_lower and any(isinstance(row, dict) and len(row) == 2 for row in data):
        return ["bar", "pie", "table"]
    if "count(" in sql_lower:
        return ["pie", "bar", "table"]
    return ["table"]
