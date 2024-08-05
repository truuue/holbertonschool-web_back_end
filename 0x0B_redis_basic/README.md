# Redis basic

![img](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/1/40eab4627f1bea7dfe5e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240805%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240805T093612Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=323bca974ff27534d61c728591e76cdf320aa06dec7a91b2ce0c93a43138128e)

## Resources

Read or watch:

- [Redis commands](https://redis.io/docs/latest/commands/)
- [Redis python client](https://redis-py.readthedocs.io/en/stable/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)
- [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

### Learning Objectives

Learn how to use redis for basic operations
Learn how to use redis as a simple cache

## Requirements

- All of your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All of your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- The first line of all your files should be exactly #!/usr/bin/env python3
- Your code should use the pycodestyle style (version 2.5)
- All your modules should have documentation (python3 -c 'print(**import**("my_module").**doc**)')
- All your classes should have documentation (python3 -c 'print(**import**("my_module").MyClass.**doc**)')
- All your functions and methods should have documentation (python3 -c 'print(**import**("my_module").my_function.**doc**)' and python3 -c 'print(**import**("my_module").MyClass.my_function.**doc**)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Install Redis on Ubuntu 18.04

```
  $ sudo apt-get -y install redis-server
  $ pip3 install redis
  $ sed -i "s/bind .\*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

## Use Redis in a container

Redis server is stopped by default - when you are starting a container, you should start it with: `service redis-server start`
