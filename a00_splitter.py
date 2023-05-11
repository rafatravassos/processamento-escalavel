file_path = "files/test.txt"
splited_path = "splited"
import redis
import time
r = redis.Redis(host='172.17.0.2', port=6379, db=0)

def split_file():
    lines_per_file = 300
    smallfile = None
    with open(file_path) as bigfile:
        for lineno, line in enumerate(bigfile):
            if lineno % lines_per_file == 0:
                if smallfile:
                    smallfile.close()
                    r.rpush("file_queue", small_filename)
                small_filename = 'splited/small_file_{}.txt'.format(lineno + lines_per_file)
                smallfile = open(small_filename, "w")
            smallfile.write(line)
        if smallfile:
            smallfile.close()


if __name__ == "__main__":
    print("Dividindo arquivo")
    split_file()
    print("Aguardando...")
    
