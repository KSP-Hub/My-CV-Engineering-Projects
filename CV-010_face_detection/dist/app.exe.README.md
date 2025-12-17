При попытке загрузить изменения в репозиторий GitHub возникла ошибка, связанная с превышением лимита размера файлов (лимит — 100 МБ). Два моих файла превышают этот лимит:

- CV-010_face_detection/dist/app.exe (145,34 МБ);
- build/app/app.pkg (145,02 МБ).

Чтобы решить эту проблему, я воспользоваться следующими способами:

- Использовал Git Large File Storage (LFS), но проблема сохранилась;
- GitHub Releases: не разобрался. Страница выдаёт ошибку `404`  — [`https://github.com/features/releases`](https://github.com/features/releases);
- Выгрузил файл в облачное хранилице и сохранил ссылку на скачивание в репозитарий. Путь: `CV-010_face_detection/dist/app.exe.md`

Ссылка для скачивания: [`app.exe — Яндекс Диск`](https://disk.yandex.ru/d/kC3Y-VNp8wCJkw)