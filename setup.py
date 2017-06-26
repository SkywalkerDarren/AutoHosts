import cx_Freeze

exe = [cx_Freeze.Executable("updatehosts.py")]

cx_Freeze.setup( name = "updatehosts", version = "1.0",
                 options = {"build_exe": {"packages": ["requests", "os", "tkinter"], "include_files": []}},
                 executables = exe )