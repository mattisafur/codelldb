import sys
if 'darwin' in sys.platform:
    sys.path.append('/Applications/Xcode.app/Contents/SharedFrameworks/LLDB.framework/Resources/Python')
sys.path.append('.')

import adapter
adapter.run_tcp_server(multiple=False)
