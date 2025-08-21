# Список необходимых SVG-иконок для сайта ТЕСС

## Папка: theme/tess-bootstrap/static/images/icons/

### Иконки для услуг (services.html):
- tax-disputes.svg - Налоговые споры (весы правосудия)
- court-representation.svg - Судебное представительство (здание суда)
- corporate-deals.svg - Корпоративные сделки (офисное здание)
- bankruptcy.svg - Банкротство (стрелки обновления)
- privacy-protection.svg - Защита персональных данных (замок безопасности)
- intellectual-property.svg - Интеллектуальная собственность (лампочка)

### Иконки для контактов (contacts.html):
- phone.svg - Телефон
- email.svg - Электронная почта
- location.svg - Местоположение
- clock.svg - Часы работы
- urgent.svg - Срочные вопросы (молния)
- handshake.svg - Рукопожатие
- email-method.svg - Email метод связи
- phone-method.svg - Телефон метод связи
- meeting.svg - Личная встреча
- consultation.svg - Консультация
- check.svg - Галочка проверки
- phone-white.svg - Белый телефон для кнопок
- email-outline.svg - Контурный email

### Иконки для статей (articles.html):
- calendar.svg - Календарь для даты
- author.svg - Автор статьи

### Иконки для материалов (leadmagnets.html):
- checklist-shield.svg - Чек-лист с защитой
- legal-documents.svg - Юридические документы  
- bankruptcy-phoenix.svg - Банкротство феникс
- tax-planning.svg - Налоговое планирование
- court-practice.svg - Судебная практика
- pdf.svg - PDF файл
- docx.svg - DOCX файл
- archive.svg - Архив
- download.svg - Скачивание

## Характеристики иконок:

### Размеры:
- Иконки услуг: 48x48px
- Иконки материалов: 40x40px  
- Иконки контактов: 32x32px (обычные), 48x48px (методы связи)
- Иконки статей: 28x28px

### Стиль:
- Монохромные SVG
- Минималистичный дизайн
- Толщина линий: 2px
- Закругленные углы
- Совместимы с CSS-переменными цветов

### Цвета:
- Основной: var(--color-primary) #21808d
- Вторичный: var(--color-text) #134252
- Фон: var(--color-surface) или прозрачный

## Файлы для удаления:

### Удалить двойные расширения:
- bankruptcy-phoenix.png.png → bankruptcy-phoenix.svg
- checklist-shield.png.png → checklist-shield.svg  
- court-practice.png.png → court-practice.svg
- legal-documents.png.png → legal-documents.svg
- privacy-protection.png.png → privacy-protection.svg
- tax-planning.png.png → tax-planning.svg

### Неиспользуемые файлы:
- Папка static/images/icons/11/ (все файлы generated_image*.png)
- generated_image.png в корне static/images/
- generated_image_1.png в корне static/images/

## Исправления в исходниках:

### 1. Заменить файл CSS:
`theme/tess-bootstrap/static/css/tess-working.css` → использовать `tess-working-fixed.css`

### 2. Заменить шаблоны:
- `theme/tess-bootstrap/templates/services.html` → использовать `services-fixed.html`
- `theme/tess-bootstrap/templates/contacts.html` → использовать `contacts-fixed.html`  
- `theme/tess-bootstrap/templates/articles.html` → использовать `articles-fixed.html`
- `theme/tess-bootstrap/templates/leadmagnets.html` → использовать `leadmagnets-fixed.html`

## Fallback решение:
Все иконки имеют fallback на эмодзи через onerror="" для обеспечения работоспособности до загрузки SVG-иконок.

## Тестирование:
1. Проверить отображение на всех устройствах
2. Убедиться в корректной загрузке всех иконок  
3. Протестировать fallback эмодзи
4. Проверить адаптивность размеров