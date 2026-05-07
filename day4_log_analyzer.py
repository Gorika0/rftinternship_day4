Logs=["ERROR DISK FULL","INFO STARTED","ERROR FILE MISSING","WARNING MEMORY LOW"]
error_count=0
info_count=0
warning_count=0
for log in Logs:
    log=log.upper()
    if "ERROR" in log:
        error_count+=1
    elif "INFO" in log:
        info_count+=1
    elif "WARNING" in log:
        warning_count+=1
print("ERROR:",error_count)
print("INFO:",info_count)
print("WARNING:",warning_count)
count={
    "ERROR":error_count,
    "INFO":info_count,
    "WARNING":warning_count
}
most_frequent=max(count,key=count.get)
print("most frequent log type:",most_frequent)
