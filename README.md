# processamento-escalavel
Estudo de aplicação de processamento distribuído de forma escalável


docker run --name redis-server -d redis

docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' redis-server

run -it --name redis-client redis redis-cli -h <ip-address-of-redis-server>


Iniciar o cluster
    docker swarm init --advertise-addr 187.22.128.91

Verificar os nós
    docker node ls

Criar os workers (replicas 3, significa que serão 3 workers)
    docker service create --replicas 3 a03_worker

Para verificar a execução
    docker logs -f <CONTAINER ID>