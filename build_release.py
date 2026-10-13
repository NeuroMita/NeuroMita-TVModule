"""Build an installer-ready ZIP from an explicit payload allowlist."""
import hashlib
import json
import pathlib
import zipfile

root = pathlib.Path(__file__).resolve().parent
version = json.loads((root / "module.json").read_text(encoding="utf-8-sig"))["Version"]
output = root / "dist"
output.mkdir(exist_ok=True)
archive = output / f"TVModule-{version}-win-x64.zip"
files = [root / name for name in ("module.json", "README.md", "LICENSE", "THIRD_PARTY_NOTICES.md", "Tools/yt-dlp.exe", "Tools/qjs.exe")]
files += [p for folder in ("VLC", "LICENSES") for p in (root / folder).rglob("*") if p.is_file() and p.suffix != ".meta"]
with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as package:
    for path in sorted(files):
        relative = path.relative_to(root).as_posix()
        if "cookies" in relative.lower() or relative == "config.json" or ".git" in path.parts:
            raise ValueError(f"Private file in package: {relative}")
        package.write(path, relative)
digest = hashlib.sha256(archive.read_bytes()).hexdigest()
archive.with_suffix(".zip.sha256").write_text(f"{digest}  {archive.name}\n", encoding="ascii")
with zipfile.ZipFile(archive) as package:
    if package.testzip() is not None:
        raise ValueError("Archive integrity check failed")
print(f"{archive.name}: {archive.stat().st_size} bytes; SHA256 {digest}")
