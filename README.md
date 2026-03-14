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
