# Run resolve_to_IP.py 
```
python resolve_to_IP.py 
```

# URL to IP resolver 🚀

&#x20;

This is a custom project created to resolve URLs to IP address.
    
If the Input URL in the CSV is in 1st column as shown below, the script will process it step by step, and the final output will match the values shown in the “Final Output” column.
```
|-----------------------------------|---------------------------------------|-----------------------------------------|-------------------------------|---------------------------------|-----------------------------|
| Input URL                         | Step 1: Remove http/https & trim path | Step 2: Handle port                     | Step 3: Resolve to IP         | Final CSV Output (Resolved_IP)  | Notes                       |
|-----------------------------------|---------------------------------------|-----------------------------------------|-------------------------------|---------------------------------|-----------------------------|
| `http://10.10.10.10`              | `10.10.10.10`                         | No port removal                         | `10.10.10.10`                 | `10.10.10.10`                   | IP without port, kept as-is |
| `https://10.10.10.10:8080/path`   | `10.10.10.10:8080`                    | IP + port → keep                        | `10.10.10.10:8080`            | `10.10.10.10:8080`              | IP with port, port preserved|
| `http://example.com`              | `example.com`                         | No port                                 | `93.184.216.34`               | `93.184.216.34`                 | Hostname resolved to IP     |
| `https://example.com:8080/path`   | `example.com:8080`                    | Hostname + port → strip → `example.com` | `93.184.216.34`               | `93.184.216.34`                 | Hostname with port → port stripped |
| `10.10.10.10:9090`                | `10.10.10.10:9090`                    | IP + port → keep                        | `10.10.10.10:9090`            | `10.10.10.10:9090`              | IP with port, no scheme     |
| `example.com:9090`                | `example.com:9090`                    | Hostname + port → strip → `example.com` | `93.184.216.34`               | `93.184.216.34`                 | Hostname with port → port stripped |
| `http://example.com/path/to/page` | `example.com`                         | No port                                 | `93.184.216.34`               | `93.184.216.34`                 | Path removed                |
| `https://10.10.10.10/some/path`   | `10.10.10.10`                         | No port                                 | `10.10.10.10`                 | `10.10.10.10`                   | IP, path removed            |
|-----------------------------------|---------------------------------------|-----------------------------------------|-------------------------------|---------------------------------|-----------------------------|
```

## Sample Output:
Output will be saved in Public_IPs_results-YYYYMMDD.csv
```
|-----------------------------------|---------------------------------------|
| Original value                    |Resolved IP                            |
|-----------------------------------|---------------------------------------|
| test.example.com                  | 1.1.1.1                               |
| example.com                       | 2.2.2.2                               |
|-----------------------------------|---------------------------------------|
```
