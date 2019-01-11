#!/bin/sh

if [ ! -z "$DB_PORT" ]; then 
    echo "DB_PORT is set $DB_PORT";
    DB_PORT_STR="-p $DB_PORT";
fi

pip install -r requirements.txt

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$DB_HOST" $DB_PORT_STR -U "$POSTGRES_USER" "$POSTGRES_DB" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 2
done

if $INITIALIZE_DB ; then
    echo "Initializing database..."
    python initdb.py
    echo "Done."
fi

echo "Initializing Centaurus..."
python app.py
