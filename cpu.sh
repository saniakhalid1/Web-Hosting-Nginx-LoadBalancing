while true; do
    echo "$(date)" >> cpu_usage.log
    docker stats --no-stream >> cpu_usage.log
    echo "------------------------------------" >> cpu_usage.log
    sleep 60
done
