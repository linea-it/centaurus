#!/bin/sh

if $INITIALIZE_DB ; then
    echo "Initializing database..."
    python initdb.py
    echo "Done."
fi

echo "Initializing Centaurus..."
python app.py