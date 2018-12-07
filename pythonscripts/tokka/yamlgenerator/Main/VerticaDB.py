import vertica_db_client

db = vertica_db_client.connect(database="default", user='healthe_intent_load_user', password='CernerAnalytics')
cur = db.cursor()
cur.execute("SELECT * FROM DEV_15STPDEP.RC_F_BALANCE_AR where encounter_classification_primary_display not like '%Inpatient%'")
rows = cur.fetchall()
print(rows)