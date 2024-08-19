# Load extensions from 'extensions' directory layout without having to
# turn them into `.rpe` ZIP.
#
# To convert this into a Ren'Py extension, from this file's directory:
# Run `zip extension.rpe autorun.py` then place the file in your
# game's `game/` directory

import os
import sys
import renpy

for dir in renpy.config.searchpath:
    for root, dirs, files in os.walk(os.path.join(dir, '..', 'extensions')):
        for d in sorted(dirs):
            dir_path = os.path.join(root, d)
            autorun_path = os.path.join(dir_path, 'autorun.py')
            if os.path.isfile(autorun_path):
                with open(autorun_path, 'r') as f:
                    autorun = f.read()
                if dir_path in sys.path:
                    sys.path.remove(dir_path)
                sys.path.insert(0, dir_path)
                exec(autorun, {'__file__': autorun_path})
