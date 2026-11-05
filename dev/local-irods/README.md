# Local iRODS test server (unfinished)

An early attempt at running a local iRODS server in Docker, for testing scripts without touching Yoda. It does not work yet:

- `docker-compose.yml` is not valid Compose syntax.
- The iRODS packages are not in Ubuntu's default package sources; the Dockerfile needs to add the iRODS apt repository (https://packages.irods.org/) first.

The tutorial scripts do not use this; they connect to the Delta Enigma Yoda environment.
