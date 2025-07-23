# F1 2025 Race Simulator 🏎️

A realistic Formula 1 race simulation featuring all 20 drivers from the 2025 season.

## Features
- **Complete 2025 F1 Grid** - All current drivers and teams
- **Qualifying Session** - Determines starting positions
- **Race Simulation** - Realistic lap times and race dynamics
- **Live Results** - Final standings with time gaps
- **Race Statistics** - Winner time, fastest lap, and more

## How to Run
```bash
python f1_simulation_race.py
```

## Sample Output
```
🏎️ FORMULA 1 2025 SEASON RACE - MONACO GRAND PRIX 🏎️

📋 SIRA BELIRLEME TURLARI
1. #1  Max Verstappen    (Red Bull Racing) - 1:08.234 - Netherlands
2. #4  Lando Norris     (McLaren) - 1:08.567 - Great Britain
3. #16 Charles Leclerc  (Ferrari) - 1:08.891 - Monaco
4. #44 Lewis Hamilton   (Ferrari) - 1:09.123 - Great Britain
5. #63 George Russell   (Mercedes) - 1:09.456 - Great Britain
...

🏁 YARIS BASLIYOR! 🏁

⏱️ Yaris simulasyonu calisiyor...

🏆 YARIS SONUCLARI - FINAL SIRALAMASI
Pos #   Pilot              Takim           Sure         Fark        
----------------------------------------------------------------------
1. 🥇 #16 Charles Leclerc   Ferrari         1:33:45.123 Leader      
2. 🥈 #1  Max Verstappen    Red Bull Racing 1:33:47.891 +2.768s     
3. 🥉 #4  Lando Norris      McLaren         1:33:52.445 +7.322s     
4.    #44 Lewis Hamilton    Ferrari         1:33:54.789 +9.666s     
5.    #63 George Russell    Mercedes        1:33:58.234 +13.111s    
6.    #81 Oscar Piastri     McLaren         1:34:02.567 +17.444s    
7.    #14 Fernando Alonso   Aston Martin    1:34:05.891 +20.768s    
8.    #10 Pierre Gasly      Alpine          1:34:08.123 +23.000s    
...

🏆 PODIUM
🥇 1. Yer: Charles Leclerc (Ferrari) - Monaco
🥈 2. Yer: Max Verstappen (Red Bull Racing) - Netherlands  
🥉 3. Yer: Lando Norris (McLaren) - Great Britain

📊 YARIS ISTATISTIKLERI
🏁 Yaris Galibi: Charles Leclerc
⏱️ Kazanan Sure: 1:33:45.123
🏎️ Ortalama Hiz: ~165.2 km/h
🛣️ Toplam Mesafe: 78 tur (260.286 km)
📅 Tarih: 24/07/2025
⚡ En Hizli Tur: Max Verstappen - 1:10.234
```

## Tech Stack
- **Python 3.x**
- **Random module** for race dynamics
- **Datetime module** for timestamps

## Race Mechanics
- Random performance factors (±5%)
- Grid position advantages
- Strategy variations (±2%)
- Realistic Monaco GP timing
