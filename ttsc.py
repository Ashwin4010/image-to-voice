from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from builtins import open
from builtins import str
# etc., as needed

from future import standard_library
standard_library.install_aliases()
from gtts import gTTS

import codecs
f = codecs.open('output.txt', 'r', 'UTF-8')
print (f)


a=f.read().rstrip('\n')
print(a)
    
    
tts = gTTS(text=a, lang="hi")
tts.save("play.mp3")

