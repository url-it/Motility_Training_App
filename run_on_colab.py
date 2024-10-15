# library
import os
import shutil
import stat
import sys
import importlib

def go(s_home):
    s_bin = f'{s_home}/Motility_Train_App/bin'
    s_src = f'{s_home}/Motility_Train_App/bin/myproj'
    s_exe = f'{s_home}/Motility_Train_App/bin/myproj'
    s_wd = f'{s_home}/Motility_Train_App'

    # going home
    os.chdir(s_home)

    # install binary
    if not os.path.exists(s_exe):
        shutil.copy(src=s_src, dst =s_exe)
        os.chmod(s_exe, stat.S_IXOTH)
        sys.path.insert(0, s_bin)
    
    os.chdir(s_wd)
    import Motility_Train_App
    importlib.reload(Motility_Train_App)

    return Motility_Train_App.gui