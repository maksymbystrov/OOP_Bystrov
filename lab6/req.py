from jikanpy import Jikan

jikan = Jikan()
# Отримання даних поточного сезону
current_season = jikan.seasons(extension='now')

print("--- Аніме поточного сезону ---")
for anime in current_season["data"][:5]: # Виводимо топ-5
    title = anime.get("title")
    score = anime.get("score", "Оцінка формується")
    print(f"Назва: {title} | Оцінка: {score}")