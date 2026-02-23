#!/usr/bin/env python3
"""
Bright Finch Coaching — Image Downloader
Downloads all images from the old Squarespace site and saves them
with the correct names for the new site.

Run from inside the brightfinch/ folder:
    python3 download_images.py

Requirements: Python 3 (built-in libraries only)
"""

import urllib.request
import urllib.error
import os
import sys

# ── Image targets ────────────────────────────────────────────────────────────
# Format: (save_as, url, description)
IMAGES = [
    (
        "images/logo.png",
        "https://images.squarespace-cdn.com/content/v1/683103b3e875307a3a8112f6/320c30cd-7def-4a6d-8afe-9f7fe2004126/logo.png?format=1500w",
        "Bright Finch logo"
    ),
    (
        "images/hero.jpg",
        "https://images.squarespace-cdn.com/content/v1/683103b3e875307a3a8112f6/e5a03523-0b99-429f-ab10-a79bd8f070a4/zebra-finches-1676671_1280.jpg",
        "Hero — zebra finches"
    ),
    (
        "images/offering-1.jpg",
        "https://images.squarespace-cdn.com/content/v1/683103b3e875307a3a8112f6/1748043781046-BNU7ALEZM6Z2HK5CW2IR/unsplash-image-eLC1Bd3PLu4.jpg",
        "Offering 1 — Clarity & Momentum"
    ),
    (
        "images/offering-2.jpg",
        "https://images.squarespace-cdn.com/content/v1/683103b3e875307a3a8112f6/1748044141709-HDXO10UA8EMRW3C4T8Y9/unsplash-image--YTfSdXKFec.jpg",
        "Offering 2 — Rise & Realign"
    ),
    (
        "images/offering-3.jpg",
        "https://images.squarespace-cdn.com/content/v1/683103b3e875307a3a8112f6/1748044705179-UYCX7ONDM3SJJ1MPHC5I/unsplash-image-V72Hk6LjjjI.jpg",
        "Offering 3 — Reset & Reconnect"
    ),
    (
        "images/retreat.jpg",
        "https://images.squarespace-cdn.com/content/v1/683103b3e875307a3a8112f6/1758170168172-V0BJ6VCGB049NADHJ0HO/unsplash-image-Bs046wbyTi8.jpg",
        "Retreat — Clarity Uncorked / Bordeaux"
    ),
    (
        "images/jen.jpg",
        "https://images.squarespace-cdn.com/content/v1/683103b3e875307a3a8112f6/b555f04b-1799-4404-8b38-61eb09f7f2af/IMG_8474+copy.jpeg",
        "Jen's headshot"
    ),
]

# The contact section uses the same image as the retreat on the old site
ALIASES = [
    ("images/contact.jpg", "images/retreat.jpg"),
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# ─────────────────────────────────────────────────────────────────────────────

def progress_bar(downloaded, total):
    if total <= 0:
        return ""
    pct = downloaded / total
    filled = int(pct * 30)
    bar = "█" * filled + "░" * (30 - filled)
    mb = downloaded / 1_048_576
    total_mb = total / 1_048_576
    return f"  [{bar}] {pct*100:.0f}%  {mb:.1f}/{total_mb:.1f} MB"


def download(save_as, url, description):
    os.makedirs(os.path.dirname(save_as), exist_ok=True)

    print(f"\n→ {description}")
    print(f"  Saving to: {save_as}")

    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            total = int(resp.getheader("Content-Length", 0))
            downloaded = 0
            chunk = 65536  # 64 KB

            with open(save_as, "wb") as f:
                while True:
                    data = resp.read(chunk)
                    if not data:
                        break
                    f.write(data)
                    downloaded += len(data)
                    print(f"\r{progress_bar(downloaded, total)}", end="", flush=True)

        size_kb = os.path.getsize(save_as) / 1024
        print(f"\r  ✓ Done — {size_kb:.0f} KB saved" + " " * 20)
        return True

    except urllib.error.HTTPError as e:
        print(f"\r  ✗ HTTP {e.code}: {e.reason}")
        return False
    except urllib.error.URLError as e:
        print(f"\r  ✗ Network error: {e.reason}")
        return False
    except Exception as e:
        print(f"\r  ✗ Error: {e}")
        return False


def make_alias(src, dest):
    """Copy a file to another name (e.g. contact.jpg = retreat.jpg)."""
    import shutil
    if os.path.exists(dest):
        shutil.copy2(dest, src)
        print(f"  ✓ Aliased {src} ← {dest}")
    else:
        print(f"  ✗ Could not alias {src} — source {dest} missing")


def main():
    print("=" * 55)
    print("  Bright Finch Coaching — Image Downloader")
    print("=" * 55)
    print(f"  Downloading {len(IMAGES)} images...\n")

    ok, fail = 0, 0
    for save_as, url, desc in IMAGES:
        if download(save_as, url, desc):
            ok += 1
        else:
            fail += 1

    # Handle aliases (files that reuse another downloaded image)
    if ALIASES:
        print("\n── Aliases ──────────────────────────────────────────")
        for alias, source in ALIASES:
            make_alias(alias, source)

    print("\n" + "=" * 55)
    print(f"  Complete: {ok} downloaded, {fail} failed")
    if fail:
        print("  ⚠️  Some images failed. Check URLs or try again.")
        print("     You may need to manually save them from the old site.")
    else:
        print("  🎉 All images ready! Drop the images/ folder into")
        print("     your brightfinch/ site directory and you're set.")
    print("=" * 55 + "\n")

    sys.exit(0 if fail == 0 else 1)


if __name__ == "__main__":
    main()
