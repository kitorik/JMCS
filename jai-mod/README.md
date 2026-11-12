# JAI Mod

Клиентский Fabric-мод для сервера **JustMC** (Creative+).

## Что делает

Команда `/jai code <запрос>`:

1. Отправляет `<запрос>` в нейросеть через **OpenRouter** (модель настраивается).
2. Полученный JSON-модуль JustMC заливает на **paste.rs** (открытый API).
3. Паста автоматически удаляется через 5 минут (DELETE-запрос).
4. Отправляет за игрока команду `/module load-url <ссылка>`.
5. Когда открывается книга установки («ПРИНЯТЬ / ОТКАЗ») — мод сам «нажимает» **ПРИНЯТЬ** (выполняет click-event кнопки).

## Установка

1. Нужен Fabric Loader + Fabric API (MC 1.21.x — версию можно поменять в `gradle.properties`).
2. `./gradlew build` — готовый jar будет в `build/libs/`.
3. Положить jar в папку `mods/`.

## Настройка

После первого запуска появится `config/jaimod.json`:

| Поле | Описание |
|------|----------|
| `openRouterApiKey` | Ключ с https://openrouter.ai/keys — **впиши свой** |
| `model` | Модель OpenRouter, например `anthropic/claude-3.5-sonnet`, `google/gemini-2.0-flash-001`, `openai/gpt-4o-mini` |
| `systemPromptExtra` | Системный промпт для генерации JustMC-модуля (можно вставить выдержки из JAI.md) |
| `autoAccept` | Автонажатие «ПРИНЯТЬ» (вкл/выкл) |
| `acceptDelayTicks` | Задержка перед нажатием в тиках |
| `deleteAfterSeconds` | Через сколько секунд удалять пасту (по умолчанию 300 = 5 мин) |

## Сборка и разработка

```bash
./gradlew build        # сборка jar
./gradlew runClient    # запуск тестового клиента
```

## Как это работает внутри

- `JaiCommand` — клиентская команда `/jai code` (Fabric Client Command API).
- `OpenRouterClient` — HTTP-запрос к `chat/completions`.
- `PasteClient` — `POST https://paste.rs` → URL, затем `DELETE` через N секунд.
- `BookAcceptHandler` + `BookScreenMixin` — тик-хук ловит открытие `BookScreen`, находит текстовый компонент «ПРИНЯТЬ» и выполняет его `ClickEvent` (RUN_COMMAND), как настоящий клик игрока.

## Важно

- Ключ API хранится в `config/jaimod.json` локально — не коммить его.
- Если JustMC меняет текст кнопки («ПРИНЯТЬ» с пробелами/цветами), автонажатие нормализует пробелы и регистр.
- paste.rs — публичный сервис; для приватных миров лучше поднять свой pastebin и поменять `pasteUrl` в конфиге.
