docker exec -t immich_postgres pg_dumpall --clean --if-exists --username=postgres | gzip > "manual_dump.sql.gz"
