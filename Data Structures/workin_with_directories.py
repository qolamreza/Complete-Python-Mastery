from pathlib import Path

path = Path("ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename()

# for p in path.iterdir():
#     print(p)
pathes = [p for p in path.iterdir() if p.is_dir()]
# py_files = [p for p in path.glob("*.py")]
py_files = [p for p in path.rglob("*.py")]
print(py_files)
