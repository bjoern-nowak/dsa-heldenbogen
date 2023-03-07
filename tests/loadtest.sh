#!/bin/bash

CONCURRENCY=1
REQUESTS=20
TIMEOUT=1

#### Main
echo ""
echo "###########################"
echo "######## Load Test ########"
echo "###########################"
echo ""

START="$(date -u +%s.%3N)"

for i in `seq 1 $CONCURRENCY`; do
  curl -s --output /dev/null -X 'POST' \
    'http://127.0.0.1:8000/api/v1/hero/validate?rulebooks=dsa5&rulebooks=dsa5_aventurisches_kompendium_2&rulebooks=dsa5_aventurisches_g%C3%B6tterwirken_2' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    --connect-timeout "$TIMEOUT" \
    --data "@./tests/loadtest.json" & pidlist="$pidlist $!"
  echo "Finalized $((REQUESTS*i)) requests "
done

# Execute and wait
FAIL=0
for job in $pidlist; do
  #echo $job
  wait $job || let "FAIL += 1"
done

# Verify if any failed
END="$(date -u +%s.%3N)"

echo "Failed Requests : ($FAIL) of ($((CONCURRENCY * REQUESTS))) "
TOTAL="$(bc <<<"scale=5;$END-$START")"
TIMEREQUEST=`echo "scale=5;$TOTAL / $REQUESTS * $CONCURRENCY" | bc -l`
echo "Total Time: $TOTAL [s]"
RT=`echo "scale=5;$TIMEREQUEST/1000" | bc -l`
echo "Time/Request: " $RT