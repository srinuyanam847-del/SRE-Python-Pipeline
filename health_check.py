server = {
    "name": "SRVSOUTH01",
    "cpu": 75,
    "memory": 68,
    "disk": 45
}

if server["cpu"] >= 90 or server["memory"] >= 90 or server["disk"] >= 90:
    status = "CRITICAL"
elif server["cpu"] >= 80 or server["memory"] >= 80 or server["disk"] >= 80:
    status = "WARNING"
else:
    status = "OK"

print("Server:", server["name"])
print("CPU:", server["cpu"], "%")
print("Memory:", server["memory"], "%")
print("Disk:", server["disk"], "%")
print("Overall Status:", status)

if status == "CRITICAL":
    print("Pipeline check FAILED")
    raise SystemExit(1)
else:
    print("Pipeline check PASSED")