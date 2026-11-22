# Controller actions
> Source: official JustMc assets (documentation/ru_RU) — updated 2026-11. Icon column references the original repo icons — ignore the links.

| Icon | ID | Name | Description | Category/Subcategory | Arguments | Works with | Additional info | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![controller_async_run](../../../icons/actions/controller_async_run.png) | controller_async_run | Запуск в отдельном потоке | Запускает код внутри поршней в отдельном потоке, что может уменьшить нагрузку. Отмена и возврат события не будут работать после поршней. | controller |  |  | Некоторые действия внутри поршней могут не работать. | unused |
| ![controller_do_not_run](../../../icons/actions/controller_do_not_run.png) | controller_do_not_run | Игнорировать выполнение | Игнорирует код, находящийся внутри скобок, во время выполнения. | controller |  |  |  |  |
| ![controller_exception](../../../icons/actions/controller_exception.png) | controller_exception | Уловить ошибку | Улавливает ошибку в коде внутри поршней и присваивает её идентификатор к переменной (пример: function_not_found). | controller | variable: variable |  | Не улавливает глобальные и критические ошибки. |  |
| ![controller_isolated_selection](../../../icons/actions/controller_isolated_selection.png) | controller_isolated_selection | Изолировать выборку | Изолирует выборку внутри скобок. | controller | selection_mode: enum<br/>&nbsp;&nbsp;- DEFAULT<br/>&nbsp;&nbsp;- CURRENT<br/>&nbsp;&nbsp;- EMPTY<br/>&nbsp;&nbsp;- FOR_EACH |  | Созданная внутри выборка будет активна лишь в рамках скобок. |  |
| ![controller_label](../../../icons/actions/controller_label.png) | controller_label | Пометить код | Помечает код между поршнями указанным именем и позволяет его прервать. | controller | label: text |  | Работает в связке с действием "Выйти из блока с меткой" |  |
| ![controller_measure_time](../../../icons/actions/controller_measure_time.png) | controller_measure_time | Замерить время выполнения | Замеряет время выполнения кода внутри поршней и присваивает результат к переменной. | controller | variable: variable<br/>duration: enum<br/>&nbsp;&nbsp;- NANOSECONDS<br/>&nbsp;&nbsp;- MICROSECONDS<br/>&nbsp;&nbsp;- MILLISECONDS |  | Учитывает блоки "Ждать". |  |

## Quick ref
> Argument **names and types only**, one line per action/condition — scan this first. Exact enum values: see the full table row above. ⚠ deprecated = do not use.

- `controller_async_run` — (no arguments)
- `controller_do_not_run` — (no arguments)
- `controller_exception` — variable: variable
- `controller_isolated_selection` — selection_mode: enum
- `controller_label` — label: text
- `controller_measure_time` — variable: variable, duration: enum
