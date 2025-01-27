import dbt

cursor = conn.cursor()
cursor.execute("SELECT * FROM TEST_TABLE")
results = cursor.fetchall()
for row in results:
    print(row)
