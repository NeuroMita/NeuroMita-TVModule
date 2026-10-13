# TVModule 1.0.2 - Windows x64

- Added QuickJS-NG 0.17.0 (`Tools/qjs.exe`) with its upstream MIT license.
- Updated yt-dlp to nightly 2026.10.10.233141, including the new default
  `tv_samsung` client addressing "The page needs to be reloaded".
- Added `JSRUNTIME_PATH` so Unity enables the packaged runtime explicitly.
- Updated the build allowlist and upstream dependency license notices.
- VLC remains 3.0.21. User configuration and cookies are excluded.

Requires the Unity TV runtime update to pass the QuickJS path, retain warnings,
report native VLC errors, and retain the nightly update channel.

# TVModule 1.0.1 — Windows x64

Готовый пакет дополнительных инструментов телевизора NeuroMita.

- VLC 3.0.21 и yt-dlp 2026.08.19, сверенные с официальными дистрибутивами.
- Лицензии компонентов и уведомления включены в пакет.
- ZIP с фиксированной структурой и отдельной контрольной суммой SHA256.
- Личные настройки, cookies, Git-файлы и Unity .meta в архив не включаются.

В Unity-ветке `codex/tv-module-installer` реализована установка из TV-интерфейса
с прогрессом и отменой. При обращении к TV установленный модуль проверяется на
обновления; более новая версия автоматически скачивается и применяется после
перезапуска игры. В Play Mode обновление применяется после перезапуска редактора.
Git-копии модуля не перезаписываются. Настройки и cookies сохраняются.
Для использования этих функций требуется версия NeuroMita с установщиком.

Для ручной установки распакуйте содержимое `TVModule-1.0.1-win-x64.zip` в
`Modules/TVModule` рядом с игрой. `module.json` должен находиться непосредственно
в этой папке. Файл `.sha256` позволяет проверить целостность скачанного ZIP.

Установка инструментов не выполняет вход в YouTube. Если сервис запросит
авторизацию или проверку, настройте локальный источник cookies в TV-интерфейсе.
Chrome/Edge на Windows могут не поддерживать прямое чтение сессии из-за защиты
браузера; предусмотрен собственный файл cookies или сессия Firefox.

Исходники VLC и yt-dlp соответствующих версий приложены отдельно.
Дополнительные исходники зависимостей VLC доступны через upstream-рецепты
`contrib` в исходном архиве и https://download.videolan.org/pub/contrib/ .

## English

Installer-ready Windows x64 package containing VLC 3.0.21 and yt-dlp 2026.08.19.
Includes upstream license texts, notices and a SHA256 checksum. No user settings,
cookies, Git metadata or Unity .meta files are shipped.

NeuroMita versions with the TV installer can download and install this package
from the television. Newer releases are detected and staged automatically when
using TV, and applied on the next game launch (restart Unity Editor for Play Mode).
Local settings and cookies are preserved; Git development checkouts are protected.

Manual installation: extract the ZIP contents directly into `Modules/TVModule`
next to the game. YouTube authentication remains user-local and may require a
compatible browser session or a Netscape cookies file. Installation does not
guarantee that YouTube will accept a request.
