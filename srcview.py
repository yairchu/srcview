import inspect
import os


def open(obj):
    "Open the source code of given object in your editor"

    try:
        code = inspect.getsourcefile(obj)
        line_no = inspect.getsourcelines(obj)[1]
    except TypeError:
        open(type(obj))
        return

    editor = os.environ.get("EDITOR", "code")

    if editor == "code":
        arg = f"--goto {code}:{line_no}"
    elif editor == "subl":
        arg = f"{code}:{line_no}"
    elif editor.endswith("vim"):
        # Open in remote editor to avoid making notebooks stuck!
        arg = f"--remote +{line_no} {code}"
    else:
        arg = f"+{line_no} {code}"

    os.system(f"{editor} {arg}")
