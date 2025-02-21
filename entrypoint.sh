#!/bin/sh
echo "Starting application"

if [ "${LOCAL}" = "True" ]; then
    uvicorn main:app --host 0.0.0.0 --reload
else
    uvicorn main:app --host 0.0.0.0
fi

exec "$@"