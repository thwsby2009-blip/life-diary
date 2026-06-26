# 生活日記 (Life Diary)

純 client-side 的生活記錄 Web App，拍照為主，支援 8 種風格濾鏡。

## 功能

- 📷 拍照記錄生活（Camera Web API）
- 🎨 8 種風格濾鏡：漫畫風、黑白藝術、復古底片、日系清新、賽博龐克、水彩渲染、像素風、極簡素描
- ✏️ 支援一行文字備註（可選）
- 📁 日記總覽（過去所有記錄）
- 📱 可安裝成 PWA（離線可用）

## 技術

- 純 HTML/CSS/JS，無需後端
- Canvas API 實作 8 種濾鏡
- IndexedDB 儲存記錄
- Service Worker + Manifest = PWA

## 開發

```bash
# 本地預覽（任意 HTTP server 皆可）
python3 -m http.server 8080
# 然後開 http://localhost:8080
```

## 部署

推送 GitHub 後在 Streamlit Cloud 或任意 Static hosting 即可。PWA 功能需要 HTTPS（localhost 除外）。

## 8 種濾鏡說明

| 名稱 | 效果 |
|------|------|
| 原圖 | 無濾鏡 |
| 漫畫風 | 邊緣偵測 + 扁平化色塊 |
| 黑白藝術 | 高對比黑白 + 顆粒感 |
| 復古底片 | 暖色調 + 輕微漏光 |
| 日系清新 | 低飽和、偏青灰 |
| 賽博龐克 | 霓虹色調 + 暗部加深 |
| 水彩渲染 | 邊緣柔化 + 暈開感 |
| 像素風 | 8-bit 像素化 |
| 極簡素描 | 純線條藝術 |

## License

MIT