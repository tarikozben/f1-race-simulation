import random
import time as time_module
from datetime import datetime, timedelta

# 2025 F1 Pilotları ve Takımları
f1_drivers_2025 = {
    "Max Verstappen": {"team": "Red Bull Racing", "country": "Netherlands", "number": 1},
    "Yuki Tsunoda": {"team": "Red Bull Racing", "country": "Japan", "number": 22},
    "Liam Lawson": {"team": "Racing Bulls", "country": "New Zealand", "number": 30},
    "Isack Hadjar": {"team": "Racing Bulls", "country": "France", "number": 31},
    "Charles Leclerc": {"team": "Ferrari", "country": "Monaco", "number": 16},
    "Lewis Hamilton": {"team": "Ferrari", "country": "Great Britain", "number": 44},
    "George Russell": {"team": "Mercedes", "country": "Great Britain", "number": 63},
    "Kimi Antonelli": {"team": "Mercedes", "country": "Italy", "number": 12},
    "Lando Norris": {"team": "McLaren", "country": "Great Britain", "number": 4},
    "Oscar Piastri": {"team": "McLaren", "country": "Australia", "number": 81},
    "Fernando Alonso": {"team": "Aston Martin", "country": "Spain", "number": 14},
    "Lance Stroll": {"team": "Aston Martin", "country": "Canada", "number": 18},
    "Pierre Gasly": {"team": "Alpine", "country": "France", "number": 10},
    "Franco Colapinto": {"team": "Alpine", "country": "Argentina", "number": 43},
    "Esteban Ocon": {"team": "Haas", "country": "France", "number": 31},
    "Oliver Bearman": {"team": "Haas", "country": "Great Britain", "number": 87},
    "Alexander Albon": {"team": "Williams", "country": "Thailand", "number": 23},
    "Carlos Sainz": {"team": "Williams", "country": "Spain", "number": 55},
    "Nico Hulkenberg": {"team": "Kick Sauber", "country": "Germany", "number": 27},
    "Gabriel Bortoleto": {"team": "Kick Sauber", "country": "Brazil", "number": 40}
}


def generate_qualifying_times():
    """Sira belirleme turlari icin zamanlama uret"""
    # Base time: Monaco pisti referansı (1:10.500 civarı)
    base_time = 70.500  # saniye

    times = []
    for driver in f1_drivers_2025.keys():
        # Her pilot için rastgele varyasyon ekle (±2.5 saniye)
        variation = random.uniform(-2.5, 2.5)
        lap_time = base_time + variation
        times.append((driver, lap_time))

    # Zamana göre sırala (en hızlıdan en yavaşa)
    times.sort(key=lambda x: x[1])
    return times


def format_time(seconds):
    """Saniyeyi 1:XX.XXX formatına çevir"""
    minutes = int(seconds // 60)
    secs = seconds % 60
    return f"{minutes}:{secs:06.3f}"


def generate_race_results(qualifying_order):
    """Yarış sonuçlarını üret"""
    race_results = []

    # Yarış süresi base: Monaco için ~78 tur, her tur ~72 saniye
    base_race_time = 78 * 72  # 5616 saniye (93.6 dakika)

    for position, (driver, quali_time) in enumerate(qualifying_order, 1):
        # Yarış performansı rastgele faktörleri
        performance_factor = random.uniform(0.95, 1.05)  # ±%5 performans değişimi
        strategy_factor = random.uniform(0.98, 1.02)  # ±%2 strateji etkisi
        luck_factor = random.uniform(0.99, 1.01)  # ±%1 şans faktörü

        # Grid pozisyonunun etkisi (önden başlayanlar avantajlı)
        grid_advantage = 1 - (position - 1) * 0.001  # Her grid pozisyonu için %0.1 dezavantaj

        # Final yarış süresi hesaplama
        final_time = base_race_time * performance_factor * strategy_factor * luck_factor * grid_advantage

        # Küçük rastgele karışıklık ekle (gerçekçi yarış için)
        position_shuffle = random.randint(-3, 3)
        new_position = max(1, min(20, position + position_shuffle))

        race_results.append((driver, final_time, new_position))

    # Yarış sonucuna göre tekrar sırala
    race_results.sort(key=lambda x: x[1])

    return race_results


def calculate_gaps(results):
    """Pilotlar arası zaman farklarını hesapla"""
    if not results:
        return []

    leader_time = results[0][1]
    gaps = []

    for i, (driver, race_time, _) in enumerate(results):
        if i == 0:
            gap = "Leader"
        else:
            gap_seconds = race_time - leader_time
            if gap_seconds < 60:
                gap = f"+{gap_seconds:.3f}s"
            else:
                minutes = int(gap_seconds // 60)
                seconds = gap_seconds % 60
                gap = f"+{minutes}:{seconds:06.3f}"
        gaps.append((driver, race_time, gap))

    return gaps


def print_race_simulation():
    """Tam yarış simülasyonunu yazdır"""
    print("=" * 80)
    print("🏎️  FORMULA 1 2025 SEZON YARIŞI - MONACO GRAND PRIX  🏎️")
    print("=" * 80)
    print()

    print(f"📋 SIRA BELIRLEME TURLARI")
    print("-" * 50)
    qualifying_results = generate_qualifying_times()

    for pos, (driver, time) in enumerate(qualifying_results, 1):
        team = f1_drivers_2025[driver]["team"]
        country = f1_drivers_2025[driver]["country"]
        number = f1_drivers_2025[driver]["number"]
        print(f"{pos:2d}. #{number:2d} {driver:<18} ({team:<15}) - {format_time(time)} - {country}")

    print("\n" + "=" * 80)
    print("🏁 YARIS BAŞLIYOR! 🏁")
    print("=" * 80)

    # Simülasyon için kısa bekleme
    print(f"⏱️  Yarıs simulasyonu calisiyor...")
    time_module.sleep(2)

    # Yarış sonuçlarını üret
    race_results = generate_race_results(qualifying_results)
    final_results = calculate_gaps(race_results)

    print("\n🏆 YARIS SONUCLARI - FINAL SIRALAMASI")
    print("-" * 70)
    print(f"{'Pos':<4} {'#':<3} {'Pilot':<18} {'Takım':<15} {'Süre':<12} {'Fark':<12}")
    print("-" * 70)

    for pos, (driver, race_time, gap) in enumerate(final_results, 1):
        team = f1_drivers_2025[driver]["team"]
        number = f1_drivers_2025[driver]["number"]
        race_time_formatted = format_time(race_time)

        # Podium pozisyonları için özel işaretler
        if pos == 1:
            emoji = "🥇"
        elif pos == 2:
            emoji = "🥈"
        elif pos == 3:
            emoji = "🥉"
        else:
            emoji = "  "

        print(f"{pos:2d}. {emoji} #{number:2d} {driver:<18} {team:<15} {race_time_formatted:<12} {gap:<12}")

    print("\n" + "=" * 80)
    print("🏆 PODIUM")
    print("=" * 80)
    podium = final_results[:3]
    for pos, (driver, race_time, gap) in enumerate(podium, 1):
        team = f1_drivers_2025[driver]["team"]
        country = f1_drivers_2025[driver]["country"]
        if pos == 1:
            print(f"🥇 1. Yer: {driver} ({team}) - {country}")
        elif pos == 2:
            print(f"🥈 2. Yer: {driver} ({team}) - {country}")
        elif pos == 3:
            print(f"🥉 3. Yer: {driver} ({team}) - {country}")

    print("\n" + "=" * 80)
    print("📊 YARIS ISTATISTIKLERI")
    print("=" * 80)
    winner_time = final_results[0][1]
    print(f"🏁 Yarış Galibi: {final_results[0][0]}")
    print(f"⏱️  Kazanan Sure: {format_time(winner_time)}")
    print(f"🏎️  Ortalama Hiz: ~165.2 km/h")
    print(f"🛣️  Toplam Mesafe: 78 tur (260.286 km)")
    print(f"📅 Tarih: {datetime.now().strftime('%d/%m/%Y')}")

    # En hızlı tur
    fastest_lap_driver = random.choice(final_results[:10])[0]  # İlk 10'dan birisi
    fastest_lap_time = random.uniform(68.5, 71.2)
    print(f"⚡ En Hızlı Tur: {fastest_lap_driver} - {format_time(fastest_lap_time)}")

    print("\n🎯 Not: Bu simulasyon tamamen rastgele üretilmiştir ve gerçek yarıs sonuclarını yansıtmaz.")


# Yarış simülasyonunu çalıştır
if __name__ == "__main__":
    print_race_simulation()