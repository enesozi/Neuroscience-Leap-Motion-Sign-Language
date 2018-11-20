import os, sys, inspect, time, platform

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))

if(platform.system() == 'Linux'):
    arch_dir = 'LeapSDK/lib/x64' if sys.maxsize > 2**32 else 'LeapSDK/lib/x86'
elif(platform.system() == 'Windows'):
    arch_dir = 'LeapSDKWin' if sys.maxsize > 2**32 else 'LeapSDKWin'
elif(platform.system() == 'Darwin'):
    arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap