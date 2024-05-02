import webview
import settings
window=webview.create_window(settings.app.name,settings.app.url)
webview.start()