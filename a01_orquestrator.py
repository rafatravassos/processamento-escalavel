import redis
r = redis.Redis(host='localhost', port=6379, db=0)
import aiodocker
import asyncio

def redis_get():
    while r.llen('file_queue')!=0:
        value = r.lpop('file_queue')
        return(str(value))
    return False

async def run_worker(filename, semaphore, worker_no=0, task_no=0):
    async with semaphore:
        print(F"........Iniciando worker {worker_no} - task {task_no} - Filename: {filename}")  
        async with aiodocker.Docker() as docker:
            container =  await docker.containers.create_or_replace(f"splitter_{worker_no}",
                config = {
                    'image': 'a03_worker:latest',
                    'Cmd': ['--filename', filename]
                },
            )
            await container.start()
            exit_code = await container.wait()
            logs = await container.log(stdout=True, stderr=True)
            print(logs)
            print(F"........Finalizando worker {worker_no} - task {task_no} com EXIT CODE {exit_code}")
            await container.delete()

async def main():
    max_containers=3
    sem = asyncio.Semaphore(max_containers)
    dont_stop = True
    task_no = 0
    while dont_stop:
        files=[]
        for i in range(max_containers):
            fileName=redis_get()
            if not fileName: 
                dont_stop = False
                continue
            files.append(fileName)
        if len(files)==0:
            break
        if len(files)<max_containers: 
            max_containers=len(files)
        tasks = [run_worker(files[i], sem, i, task_no) for i in range(max_containers)]
        task_no+=1
        await asyncio.gather(*tasks)
    
asyncio.run(main())

    
    