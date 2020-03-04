# python 异步



if 0:


  import time

  def hello():
      time.sleep(1)

  def run():
      for i in range(5):
          hello()
          print('Hello World:%s' % time.time())  # 任何伟大的代码都是从Hello World 开始的！
  if __name__ == '__main__':
      run()



if 1:
  import time
  import asyncio


  # 定义异步函数
  async def hello():
    asyncio.sleep(1)
    print('Hello World:%s' % time.time())


  def run():
    for i in range(5):
      loop.run_until_complete(hello())


  loop = asyncio.get_event_loop()
  if __name__ == '__main__':
    run()
