import os
import sys
import time
import random
import math
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from rich.table import Table
from pyfiglet import Figlet
from rich.style import Style
from rich.console import Group
from rich.align import Align
from auth import authenticate
from report import report_instagram, view_statistics, cancel_report
from settings import settings
from export import export_to_csv
from update import check_for_updates
from help import show_help
from search import search_reported_accounts
from category_report import report_by_category
from batch_report import batch_report
from report_summary import generate_report_summary
from account_analysis import analyze_target_account
from schedule_report import schedule_reports
from notification import show_desktop_notification
from new_features import (
    generate_hashtags,
    create_content_calendar,
    perform_sentiment_analysis,
    detect_bot_accounts,
    generate_engagement_report,
    create_backup,
    implement_two_factor_auth,
    create_custom_report_templates,
    integrate_with_other_platforms,
    implement_machine_learning
)

console = Console()

def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def glitch_effect(text):
    """Membuat efek glitch pada teks."""
    glitch_chars = ['̴̢', '̶̢', '̷̢', '̸̢', '̢̹', '̢̺', '̢̻', '̢̼', '̢̽', '̢̾', '̢̿', '̢̀', '̢́']
    glitched_text = ''
    for char in text:
        glitched_text += char
        if random.random() < 0.1:
            glitched_text += random.choice(glitch_chars)
    return glitched_text

def print_animated_text(text, delay=0.03):
    """Mencetak teks dengan animasi ketik."""
    for char in text:
        console.print(char, end='', style="bold green")
        time.sleep(delay)
    console.print()

def print_header():
    """Mencetak header aplikasi dengan animasi."""
    clear_screen()
    f = Figlet(font='slant')
    header = f.renderText('IG Spam Report')
    
    with Live(console=console, refresh_per_second=20) as live:
        for i in range(5):
            text = Text()
            for line in header.split('\n'):
                text.append(glitch_effect(line) + '\n', style="bold cyan")
            live.update(text)
            time.sleep(0.2)
    
    subheader = "[ Hacker Edition ]"
    print_animated_text(subheader)
    
    # Add creator's name with prominent styling and full animation
    creator_style = Style(color="yellow", bold=True, underline=True)
    animate_text("Created by SYAAIKOO", creator_style)
    time.sleep(1)
    bouncing_text("SYAAIKOO", creator_style)
    time.sleep(1)
    spiral_text("SYAAIKOO", creator_style)
    
    # Add supportive message with attractive styling and full animation
    support_style = Style(color="magenta", italic=True)
    rainbow_support = rainbow_text("disupport oleh abang dan pacar tercintaaaa")
    animate_text(rainbow_support, support_style, speed=0.05)
    time.sleep(1)
    bouncing_text(rainbow_support, support_style, bounces=2)

def spinning_cursor():
    """Menghasilkan kursor berputar."""
    while True:
        for cursor in '|/-\\':
            yield cursor

def rainbow_text(text):
    """Create rainbow-colored text."""
    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    rainbow = ""
    for i, char in enumerate(text):
        rainbow += f"[{colors[i % len(colors)]}]{char}[/]"
    return rainbow

def animate_text(text, style, speed=0.1):
    """Animate text with a typing effect."""
    with console.screen() as screen:
        for i in range(len(text) + 1):
            screen.update(Group(
                Align.center(Text(text[:i], style=style), vertical="middle")
            ))
            time.sleep(speed)

def bouncing_text(text, style, bounces=3, height=10):
    """Create a bouncing text animation."""
    with console.screen() as screen:
        for _ in range(bounces):
            for y in range(height, -1, -1) + range(height):
                screen.update(Group(
                    Align.center(Text(text, style=style), vertical="middle", height=y)
                ))
                time.sleep(0.05)

def spiral_text(text, style, revolutions=2):
    """Create a spiral text animation."""
    with console.screen() as screen:
        center_x, center_y = console.width // 2, console.height // 2
        for i in range(360 * revolutions):
            angle = math.radians(i)
            r = i / (360 * revolutions) * min(console.width, console.height) / 4
            x = int(center_x + r * math.cos(angle))
            y = int(center_y + r * math.sin(angle))
            screen.update(Align.center(
                Text(text, style=style),
                width=console.width, height=console.height,
                crop=False
            ).position(x, y))
            time.sleep(0.01)


def main():
    """
    Loop program utama untuk Laporan Spam Instagram dengan antarmuka yang lebih menarik.
    """
    username = authenticate()
    
    while True:
        print_header()
        
        menu_items = [
            "Kirim Laporan Spam",
            "Lihat Statistik Laporan",
            "Batalkan Laporan Terakhir",
            "Pengaturan",
            "Ekspor Data Laporan ke CSV",
            "Cek Pembaruan",
            "Bantuan",
            "Cari Akun yang Dilaporkan",
            "Lapor Berdasarkan Kategori",
            "Laporan Massal",
            "Hasilkan Ringkasan Laporan PDF",
            "Analisis Akun Target",
            "Jadwalkan Laporan",
            "Generate Hashtags",
            "Buat Kalender Konten",
            "Analisis Sentimen",
            "Deteksi Akun Bot",
            "Laporan Engagement",
            "Buat Backup",
            "Implementasi Autentikasi Dua Faktor",
            "Buat Template Laporan Kustom",
            "Integrasi dengan Platform Lain",
            "Implementasi Machine Learning",
            "Keluar"
        ]
        
        table = Table(title=f"Selamat datang, {glitch_effect(username)}!", box=None, expand=False, show_header=False, show_edge=False)
        for i, item in enumerate(menu_items, 1):
            table.add_row(f"[{i}]", item)
        
        console.print(Panel(table, expand=False, border_style="cyan"))
        
        spinner = spinning_cursor()
        choice = ''
        while not choice:
            console.print(f"\r[cyan]Masukkan pilihan Anda (1-24): {next(spinner)}[/cyan]", end='')
            if console.input_text(keys=['enter']):
                choice = console.input("[cyan]\nMasukkan pilihan Anda (1-24): [/cyan]").strip()
        
        if choice == '1':
            report_instagram(username)
        elif choice == '2':
            view_statistics(username)
        elif choice == '3':
            cancel_report(username)
        elif choice == '4':
            settings(username)
        elif choice == '5':
            export_to_csv(username)
        elif choice == '6':
            check_for_updates()
        elif choice == '7':
            show_help()
        elif choice == '8':
            search_reported_accounts(username)
        elif choice == '9':
            report_by_category(username)
        elif choice == '10':
            batch_report(username)
        elif choice == '11':
            generate_report_summary(username)
        elif choice == '12':
            analyze_target_account()
        elif choice == '13':
            schedule_reports(username)
        elif choice == '14':
            generate_hashtags()
        elif choice == '15':
            create_content_calendar()
        elif choice == '16':
            perform_sentiment_analysis()
        elif choice == '17':
            detect_bot_accounts()
        elif choice == '18':
            generate_engagement_report()
        elif choice == '19':
            create_backup()
        elif choice == '20':
            implement_two_factor_auth()
        elif choice == '21':
            create_custom_report_templates()
        elif choice == '22':
            integrate_with_other_platforms()
        elif choice == '23':
            implement_machine_learning()
        elif choice == '24':
            clear_screen()
            print_header()
            print_animated_text("[magenta]Terima kasih telah menggunakan aplikasi ini.[/magenta]")
            sys.exit()
        else:
            console.print("[red]Pilihan tidak valid! Silakan pilih opsi yang tersedia (1-24).[/red]")
        
        input("\nTekan Enter untuk kembali ke menu utama...")

if __name__ == "__main__":
    main()

