#!/bin/bash
THREADS=16
IO_THREADS=4
TIMEOUT=1800 # 30 min

trap '[ -z $! ] || kill $!' SIGHUP SIGINT SIGQUIT SIGTERM
stress-ng --cpu $THREADS --io $IO_THREADS --timeout $TIMEOUT &

while [ -e /proc/$! ]; do
    sensors | grep Core | cut -d ' ' -f 9 | cut -c2-3 | awk -vORS=, '{ print $0 }' | sed 's/,$/\n/' >> $1
    sleep 1
done

