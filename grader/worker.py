"""Read-only subprocess for evaluating one untrusted student's challenge."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import resource
import sys

def run():
    student, slug, cases_file, output_file = sys.argv[1:5]
    resource.setrlimit(resource.RLIMIT_CPU, (7, 8))
    resource.setrlimit(resource.RLIMIT_FSIZE, (1048576, 1048576))
    file = Path(student) / "problems" / slug / "solution.py"
    cases = json.loads(Path(cases_file).read_text())
    fn = None
    error = None
    try:
        spec = importlib.util.spec_from_file_location("submitted_solution", file)
        if not spec or not spec.loader:
            raise ImportError("Could not import solution.py")
        module = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(module)
        fn = getattr(module, "solution", None)
        if not callable(fn):
            raise AttributeError("Expected a function named solution")
    except BaseException as exc:
        error = f"{type(exc).__name__}: {exc}"[:350]
    results = []
    for item in cases:
        name, args, expected = item
        if error:
            results.append({"name":name,"pass":False,"message":error})
            continue
        try:
            args = json.loads(json.dumps(args))
            if slug == "robot-maze-navigator":
                args[1] = tuple(args[1])
                args[2] = tuple(args[2])
            with contextlib.redirect_stdout(io.StringIO()):
                received = fn(*args)
            ok = type(received) is type(expected) and received == expected
            message = "" if ok else f"Expected {expected!r} ({type(expected).__name__}); received {received!r} ({type(received).__name__})"
            results.append({"name":name,"pass":ok,"message":message[:350]})
        except BaseException as exc:
            results.append({"name":name,"pass":False,"message":f"{type(exc).__name__}: {exc}"[:350]})
    Path(output_file).write_text(json.dumps(results))

if __name__ == "__main__":
    run()
