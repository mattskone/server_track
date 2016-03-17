# ServerTrack
An example, asynchronous, RESTful web service using Python and Tornado

### Motivation
This project is a brief demonstration of an asynchronous web service built on Python 3.4 and the Tornado 4.3 web framework in response to the following fictional business requirements:

First, record load for a given server
This should take a:
  - server name (string)
  - CPU load (float)
  - RAM load (float)

and apply the values to an in-memory model used to provide the data in #2.

Second, display loads for a given server
This should return data (if it has any) for the given server:
  - A list of the average load values for the last 60 minutes broken down by minute
  - A list of the average load values for the last 24 hours broken down by hour
 
Assume these endpoints will be under a continuous load being called for thousands of individual servers every minute.


### Implementation
The service supports a single `/server` endpoint with `GET` and `POST` operations.

Add data to the service by POSTing to the `/server/name` endpoint, where `name` is the name of the server.  Server names may contain upper- and lower-case letters, digits, and the underscore character.  The request payload should be a JSON object like this:
```json
{
  "cpu": 12.04,
  "ram": 46.3
}
```

`GET` requests to the `/server/name` endpoint will return a summary of log data for the named server as described above.  Values will be `null` for minutes/hours for which no log data exists.  The summary is returned as a JSON object like this:
```json
{
  "last_60_minutes": {
    "cpu": [3.4, 12.8, ..., 9.2],
    "ram": [45.7, 31.4, ..., 55.1]
  },
  "last_24_hours": {
    "cpu": [23.3, 44.1, ..., 20.9],
    "ram": [12.2, 43.4, ..., 50.2]
  }
}
```

### Operation
1. Install Python 3.4 (earlier versions may work, but I haven't tested them)
2. Install Tornado 4.3 (likewise)
3. `python ./server.py` and browse to the API root at [http://localhost:8888](http://localhost:8888)

### Contributions
Contributions and feedback are always welcome - just send me a pull request.

### License
Use of this software governed by the MIT license [here](LICENSE).
