"""Build the ChatGPT plugin ZIP: python chatgpt/build_zip.py <demo-video-url>."""

import json
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).parent
PLUGIN = HERE.parent / "plugin"
OUTPUT = HERE.parent / "dist" / "communityscale-chatgpt-plugin.zip"
LIMITS = {"displayName": 30, "shortDescription": 30, "longDescription": 4000, "developerName": 80}


def main() -> None:
    if len(sys.argv) != 2 or not sys.argv[1].startswith("https://"):
        sys.exit("usage: python chatgpt/build_zip.py https://<reviewer-accessible-demo-video>")
    manifest = (HERE / "plugin.json").read_text().replace("__DEMO_RECORDING_URL__", sys.argv[1])
    interface = json.loads(manifest)["extensions"]["com.openai"]["interface"]
    for field, limit in LIMITS.items():
        if len(interface[field]) > limit:
            sys.exit(f"{field} is over {limit} characters")
    if any(len(prompt) > 128 for prompt in interface["defaultPrompt"]):
        sys.exit("a defaultPrompt is over 128 characters")
    json.loads((HERE / "mcp.json").read_text())

    OUTPUT.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("plugin.json", manifest)
        archive.write(HERE / "mcp.json", "mcp.json")
        archive.write(PLUGIN / "assets" / "logo.png", "assets/logo.png")
        for path in sorted((PLUGIN / "skills").rglob("*")):
            if path.is_file() and path.name != ".DS_Store":
                archive.write(path, path.relative_to(PLUGIN))
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
