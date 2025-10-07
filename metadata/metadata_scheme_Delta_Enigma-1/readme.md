Get new metadata schema to Yoda

Start docker container with Ubuntu and iCommands

Copy file to docker
docker cp /Users/jellevanmiltenburg/git/delta-enigma/metadata/metadata_scheme_Delta_Enigma-1/metadata.json ub20icommands:/tmp/metadata.json

Enter Docker container:
docker exec -it ub20icommands /bin/bash

Put new schema in place:
iput -f /tmp/metadata.json "/deltaenigma/yoda/schemas/delta-enigma-1/"
iput -f /tmp/uischema.json "/deltaenigma/yoda/schemas/delta-enigma-1/"