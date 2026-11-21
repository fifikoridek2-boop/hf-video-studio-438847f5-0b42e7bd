#!/usr/bin/env python3
"""
Asset Manager for Video Production
مدير الأصول البصرية والميمز والأيقونات والألوان لمشاريع المونتاج
يتيح تحميل أي أيقونة SVG، وميمز، ومقاطع GIF مجاناً وبدون مفاتيح API.
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

try:
    import requests
except ImportError:
    print("[!] مكتبة requests مطلوبة. قم بتثبيتها عبر: pip install requests")
    sys.exit(1)

base_dir = Path(__file__).resolve().parent
icons_dir = base_dir / "icons"
memes_dir = base_dir / "memes"
character_dir = base_dir / "character"
colors_dir = base_dir / "colors"

icons_dir.mkdir(parents=True, exist_ok=True)
memes_dir.mkdir(parents=True, exist_ok=True)
character_dir.mkdir(parents=True, exist_ok=True)
colors_dir.mkdir(parents=True, exist_ok=True)


def download_icon(name: str, color: str = None, collection: str = None) -> Path:
    """
    تحميل أي أيقونة فيكتور SVG مجاناً بالكامل من Iconify / Simple Icons
    يحتوي على أكثر من 200,000 أيقونة وشعار تقني (Docker, Python, Git, Terminal, CPU...)
    """
    # إذا تم تمرير بادئة مثل "lucide:terminal"
    if ":" in name:
        prefix, icon_name = name.split(":", 1)
    else:
        prefix = collection if collection else "simple-icons"
        icon_name = name.lower().strip()

    url = f"https://api.iconify.design/{prefix}/{icon_name}.svg"
    params = {}
    if color:
        params["color"] = color

    headers = {"User-Agent": "Mozilla/5.0"}
    print(f"[i] جاري البحث عن الأيقونة '{prefix}:{icon_name}' في Iconify...")
    res = requests.get(url, params=params, headers=headers, timeout=10)

    if res.status_code == 200 and "<svg" in res.text:
        out_path = icons_dir / f"{icon_name}.svg"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(res.text)
        print(f"[✓] تم حفظ الأيقونة بنجاح: {out_path}")
        return out_path
    else:
        # محاولة بديلة مع مجموعة lucide إذا كانت المجموعة الأولى simple-icons
        if prefix == "simple-icons":
            fallback_url = f"https://api.iconify.design/lucide/{icon_name}.svg"
            res2 = requests.get(fallback_url, params=params, headers=headers, timeout=10)
            if res2.status_code == 200 and "<svg" in res2.text:
                out_path = icons_dir / f"{icon_name}.svg"
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(res2.text)
                print(f"[✓] تم العثور على الأيقونة في مجموعة Lucide وحفظها: {out_path}")
                return out_path

        print(f"[ERROR] لم يتم العثور على أيقونة باسم '{icon_name}'. تأكد من الاسم بالإنجليزية.")
        return None


def download_meme(category: str = "programmerhumor") -> Path:
    """
    تحميل ميم تقني عشوائي مجاناً بدون مفتاح من أكبر مستودعات الميمز
    """
    url = f"https://meme-api.com/gimme/{category}"
    headers = {"User-Agent": "Mozilla/5.0"}
    print(f"[i] جاري جلب ميم من فئة '{category}'...")

    try:
        res = requests.get(url, headers=headers, timeout=10).json()
        img_url = res.get("url")
        title = res.get("title", "meme")
        if not img_url:
            print("[ERROR] تعذر جلب الميم.")
            return None

        ext = Path(img_url).suffix if Path(img_url).suffix else ".png"
        clean_title = "".join(c for c in title if c.isalnum() or c in " _-")[:25].strip()
        out_path = memes_dir / f"{clean_title}{ext}"

        img_data = requests.get(img_url, headers=headers, timeout=15).content
        with open(out_path, "wb") as f:
            f.write(img_data)

        print(f"[✓] تم تنزيل الميم: {out_path}")
        print(f"    العنوان: {title}")
        return out_path
    except Exception as e:
        print(f"[ERROR] خطأ أثناء جلب الميم: {e}")
        return None


def download_clip_with_ytdlp(url: str, output_name: str = "clip") -> Path:
    """
    تنزيل أي مقطع فيديو أو ميم من يوتيوب أو تيك توك أو تويتر عبر yt-dlp
    """
    out_template = str(memes_dir / f"{output_name}.%(ext)s")
    print(f"[i] جاري تنزيل المقطع عبر yt-dlp من: {url}...")
    cmd = [
        "yt-dlp",
        "-f", "mp4/best",
        "-o", out_template,
        url
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"[✓] تم تنزيل المقطع بنجاح في مجلد: {memes_dir}")
    except Exception as e:
        print(f"[ERROR] فشل تنزيل المقطع: {e}")


def list_palettes():
    """عرض أنظمة وباليتات الألوان المتاحة في المشروع"""
    pal_file = colors_dir / "palettes.json"
    if not pal_file.exists():
        print("[!] ملف الباليتات غير موجود.")
        return

    with open(pal_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    active = data.get("active_palette", "")
    print("\n" + "=" * 65)
    print(" 🎨 أنظمة الألوان المقترحة للمونتاج (Color Palettes):")
    print("=" * 65)
    for key, p in data.get("palettes", {}).items():
        is_active = " [الحالي ✓]" if key == active else ""
        print(f"\n* {p['name']}{is_active}:")
        print(f"  - الوصف:       {p['description']}")
        print(f"  - خلفية داكنة:  {p['background_dark']}")
        print(f"  - خلفية فاتحة: {p['background_light']}")
        print(f"  - لون رئيسي:   {p['accent_primary']}")
        print(f"  - لون ثانوي:   {p['accent_secondary']}")
        print(f"  - توهج وتمييز:  {p['highlight']}")
    print("=" * 65 + "\n")


def main():
    parser = argparse.ArgumentParser(description="مدير الأصول البصرية والميمز والأيقونات لمشاريع المونتاج")
    subparsers = parser.add_subparsers(dest="command")

    # أمر تحميل أيقونة
    icon_parser = subparsers.add_parser("icon", help="تنزيل أيقونة SVG مجانية بالاسم")
    icon_parser.add_argument("name", help="اسم الأيقونة (مثال: docker, python, git, terminal)")
    icon_parser.add_argument("--color", default=None, help="لون الأيقونة بصيغة HEX (مثال: '#00e5ff')")
    icon_parser.add_argument("--collection", default=None, help="مجموعة الأيقونات (simple-icons, lucide, tabler)")

    # أمر تحميل ميم
    meme_parser = subparsers.add_parser("meme", help="جلب ميم تقني عشوائي مجاناً")
    meme_parser.add_argument("--cat", default="programmerhumor", help="فئة الميم (الافتراضي: programmerhumor)")

    # أمر تحميل مقطع يوتيوب/تيك توك
    clip_parser = subparsers.add_parser("clip", help="تحميل مقطع ميم أو فيديو عبر رابط")
    clip_parser.add_argument("url", help="رابط الفيديو")
    clip_parser.add_argument("--name", default="meme_clip", help="اسم الملف الناتج")

    # أمر عرض الألوان
    subparsers.add_parser("colors", help="عرض أنظمة وباليتات الألوان المتاحة")

    args = parser.parse_args()

    if args.command == "icon":
        download_icon(args.name, color=args.color, collection=args.collection)
    elif args.command == "meme":
        download_meme(args.cat)
    elif args.command == "clip":
        download_clip_with_ytdlp(args.url, args.name)
    elif args.command == "colors":
        list_palettes()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
