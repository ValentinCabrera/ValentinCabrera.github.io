import replicate

import os
os.environ["REPLICATE_API_TOKEN"] = "r8_Vua9S7gdelC3HpCwGaNw4CZjDZlzfxq1X3SJ4"

prompt = """
what time is it
"""
output = replicate.run(
    "replicate/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1",
    input={"prompt": prompt})
# The replicate/llama-2-70b-chat model can stream output as it's running.
# The predict method returns an iterator, and you can iterate over that output.
full_output = ""

for item in output:
    full_output += item
    print(item)

print(full_output)
