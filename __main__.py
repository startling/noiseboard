'''
Thank you for taking your time to read the source code.
This code is, unfortunately, full of workarounds and redundant.
I might have to rewrite it later. In the meanwhile, at least it works!
>> You have to rewrite it? Sweet, I'll take that as consent to break everything.
'''

from time import sleep
import subprocess
from datetime import datetime
import bart
import muni


while True:
    messages = []

    messages.append(bart.get_predictions())
    messages.append(muni.get_predictions())

    text = ''.join(messages)
    display_text = "<ID01><PA>    <FT>{}  {}   \r\n".format(datetime.now().strftime('%H:%M'), text)
    print display_text
    subprocess.call('printf "{text}" > /dev/ttyS0'.format(text=display_text), shell=True)

    sleep(60)
