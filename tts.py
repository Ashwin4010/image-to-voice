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
tts = gTTS(text="यह सम्पूर्ण पृष्ठ या इसके कुछ विभाग हिन्दी के अतिरिक्त अन्य भाषा(ओं) में भी लिखे गए हैं। आप इनका अनुवाद करके विकिपीडिया की सहायता कर सकते हैं।", lang="hi")
tts.save("output.mp3")

