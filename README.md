## TVModule

`TVModule` поставляется как опциональный git submodule и нужен только для функционала телевизора (`VLC + yt-dlp`).

### Подключение после клонирования проекта
```bash
git submodule update --init Modules/TVModule
```

### Если проект клонируется с нуля
```bash
git clone --recurse-submodules <REPO_URL>
```

### Если используются LFS-файлы
Установите Git LFS и подтяните бинарники:
```bash
git lfs install
git lfs pull
```

### Обновление модуля
```bash
git submodule update --remote Modules/TVModule
```

> Если `TVModule` не установлен, ТВ-функционал будет недоступен, но основной проект продолжит работать.

### Установка для пользователей (Windows x64)

В NeuroMita с поддержкой установщика откройте настройки YouTube на телевизоре
и нажмите «Установить модуль». Загрузка, проверка SHA256 и распаковка выполняются
автоматически. При обращении к TV установленный модуль автоматически проверяется
на обновления (не чаще раза в сутки); новая версия скачивается в отдельную папку.
Кнопка «Проверить обновления» позволяет выполнить проверку и загрузку вручную.
Новая версия применяется после перезапуска игры;
в Play Mode после перезапуска редактора Unity. Настройки и cookies сохраняются.

Для ручной установки скачайте `TVModule-1.0.2-win-x64.zip` из Releases и
распакуйте его содержимое в `Modules/TVModule` рядом с игрой. В этой папке
должны сразу находиться `module.json`, `VLC`, `Tools` и `LICENSES`, без
дополнительного уровня вложенности.

Сначала попробуйте воспроизведение без cookies. При запросе YouTube настройте
источник сессии в TV: браузер или собственный файл cookies в Netscape-формате.
Chrome/Edge на Windows могут не позволять читать зашифрованные cookies напрямую;
используйте Firefox либо локальный экспорт. Никому не отправляйте cookies.
Установка модуля не выполняет вход в YouTube и не решает CAPTCHA автоматически.

### Подготовка релиза

`python build_release.py` создаёт ZIP и файл SHA256 в `dist`. Скрипт включает
только заданный набор файлов, исключая `.git`, Unity `.meta`, `config.json`
и cookies. При изменении состава VLC/yt-dlp обновите лицензии и уведомления.
Сведения об исходниках и лицензиях находятся в `THIRD_PARTY_NOTICES.md`.

Git-копии модуля обновляются через Git. Для проверки установки в редакторе
перенесите текущий submodule за пределы `Modules`, не удаляя `.git/modules`.

### YouTube JavaScript runtime

TVModule 1.0.2 includes QuickJS-NG 0.17.0 in `Tools/qjs.exe` and yt-dlp nightly
2026.10.10.233141. The Unity integration explicitly passes `JSRUNTIME_PATH`
to yt-dlp; no JavaScript installation in the user's PATH is required.
The challenge solver scripts are bundled in the official yt-dlp executable.
The runtime runs as a child process during extraction, not permanently.
Preserve `LICENSES/QuickJS-NG-LICENSE.txt` when redistributing the module.

The Unity integration keeps yt-dlp on the nightly channel for current YouTube
fixes. Warnings are recorded even when extraction succeeds. An unavailable
browser profile or a cookie decryption failure is not an authentication request;
check the technical details and change the browser/profile or use a local
Netscape cookies export. No anonymous fallback silently replaces the selected
account session.
