# Инструкция по внедрению исправлений для сайта ТЕСС

## ✅ ИСПРАВЛЕННЫЕ ФАЙЛЫ ГОТОВЫ К ИСПОЛЬЗОВАНИЮ

### 1. CSS-файл (ОБЯЗАТЕЛЬНО)
**Заменить:** `theme/tess-bootstrap/static/css/tess-working.css`  
**На:** `tess-working-fixed.css`

**Что исправлено:**
- ✅ Оптимизированы размеры всех иконок
- ✅ Добавлены классы для правильного отображения
- ✅ Убраны избыточные стили и `!important`
- ✅ Добавлена адаптивность для мобильных устройств
- ✅ Исправлены проблемы с черным фоном Bootstrap

### 2. Шаблоны HTML (ОБЯЗАТЕЛЬНО)

#### Услуги:
**Заменить:** `theme/tess-bootstrap/templates/services.html`  
**На:** `services-fixed.html`
- ✅ Добавлены иконки вместо эмодзи
- ✅ Fallback на эмодзи при отсутствии SVG
- ✅ Правильные размеры иконок (48x48px)

#### Контакты:
**Заменить:** `theme/tess-bootstrap/templates/contacts.html`  
**На:** `contacts-fixed.html`
- ✅ Добавлены иконки вместо эмодзи
- ✅ Улучшена структура контактной информации
- ✅ Разные размеры иконок для разных секций

#### Полезные статьи:
**Заменить:** `theme/tess-bootstrap/templates/articles.html`  
**На:** `articles-fixed.html`
- ✅ Маленькие иконки (28x28px) вместо больших
- ✅ Правильная карточная верстка
- ✅ Fallback на эмодзи

#### Материалы:
**Заменить:** `theme/tess-bootstrap/templates/leadmagnets.html`  
**На:** `leadmagnets-fixed.html`
- ✅ Маленькие иконки (40x40px) вместо больших
- ✅ Улучшенная форма обратной связи
- ✅ Правильное позиционирование элементов

### 3. Иконки SVG (РЕКОМЕНДУЕТСЯ)

**Создать папку:** `theme/tess-bootstrap/static/images/icons/`

**Необходимые файлы:** (см. icons-list.md для полного списка)
- tax-disputes.svg
- court-representation.svg
- corporate-deals.svg
- bankruptcy.svg
- privacy-protection.svg
- intellectual-property.svg
- phone.svg, email.svg, location.svg
- calendar.svg, author.svg
- checklist-shield.svg, legal-documents.svg
- и другие (всего ~25 иконок)

### 4. Файлы для удаления

**Удалить следующие файлы/папки:**
```
theme/tess-bootstrap/static/images/icons/11/ (всю папку)
theme/tess-bootstrap/static/images/icons/12/bankruptcy-phoenix.png.png
theme/tess-bootstrap/static/images/icons/12/checklist-shield.png.png
theme/tess-bootstrap/static/images/icons/12/court-practice.png.png
theme/tess-bootstrap/static/images/icons/12/legal-documents.png.png
theme/tess-bootstrap/static/images/icons/12/privacy-protection.png.png
theme/tess-bootstrap/static/images/icons/12/tax-planning.png.png
```

## 🚀 ПРОЦЕДУРА ВНЕДРЕНИЯ

### Шаг 1: Резервная копия
```bash
git commit -am "Backup before fixes"
git push origin main
```

### Шаг 2: Обновление CSS
1. Скачать `tess-working-fixed.css`
2. Переименовать в `tess-working.css`
3. Заменить файл в `theme/tess-bootstrap/static/css/`

### Шаг 3: Обновление шаблонов
1. Скачать все 4 исправленных HTML-файла
2. Удалить расширение `-fixed` из названий
3. Заменить соответствующие файлы в `theme/tess-bootstrap/templates/`

### Шаг 4: Создание иконок (опционально)
1. Создать SVG-иконки согласно списку
2. Разместить в `theme/tess-bootstrap/static/images/icons/`
3. Если не создавать — будут использоваться эмодзи как fallback

### Шаг 5: Очистка
1. Удалить неиспользуемые файлы из списка выше
2. Удалить папку `icons/11/` целиком

### Шаг 6: Тестирование
1. Запустить локальный сервер: `pelican --autoreload --listen`
2. Проверить все страницы:
   - Услуги (`/услуги/`)
   - Контакты (`/контакты/`) 
   - Полезные статьи (`/полезные-статьи/`)
   - Материалы (`/материалы-для-скачивания/`)

### Шаг 7: Публикация
```bash
pelican content
git add .
git commit -m "Fix icons and optimize templates"
git push origin main
```

## ⚠️ ВАЖНЫЕ ЗАМЕЧАНИЯ

### Fallback-система
- Если SVG-иконка не загружается, автоматически показывается эмодзи
- Сайт будет работать даже без создания SVG-файлов

### Размеры иконок исправлены:
- **Услуги:** 48x48px (было: огромные эмодзи)
- **Материалы:** 40x40px (было: огромные эмодзи)  
- **Контакты:** 32-48px (было: отсутствовали)
- **Статьи:** 28px (было: огромные эмодзи)

### Адаптивность:
- Планшеты: размеры уменьшаются на 10-20%
- Мобильные: размеры уменьшаются на 20-30%
- Малые экраны: дополнительные оптимизации

### Производительность:
- Удален избыточный CSS-код
- Убраны множественные `!important`
- Оптимизированы селекторы
- Добавлены переходы и анимации

## 📱 РЕЗУЛЬТАТ

После внедрения исправлений:
1. ✅ Иконки нормального размера на всех страницах
2. ✅ Единообразный дизайн иконок
3. ✅ Правильное отображение на всех устройствах
4. ✅ Улучшенная производительность
5. ✅ Чистый и поддерживаемый код
6. ✅ Автоматический fallback на эмодзи

Время внедрения: 15-30 минут
Сложность: Низкая (замена файлов)