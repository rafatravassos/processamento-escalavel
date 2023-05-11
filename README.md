# processamento-escalavel
Estudo de aplicação de processamento distribuído de forma escalável


docker run --name redis-server -d redis

docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' redis-server

run -it --name redis-client redis redis-cli -h <ip-address-of-redis-server>
