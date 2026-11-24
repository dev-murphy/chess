import webview
from pathlib import Path
import sys

from api import ChessAPI

def get_resource_path(relative_path: str) -> Path:
    """Resolve resources in development and packaged builds."""
    if getattr(sys, "frozen", False):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parent.parent

    return base_path / relative_path


def main():
    # Initialize chess api
    api = ChessAPI('1')

    # Get URLs for dev and production server
    DEV_URL = "http://localhost:5173"
    PROD_URL = get_resource_path("ui/dist/index.html")

    # Check the mode being used by the app: (--dev) or (--prod)
    mode = sys.argv[1] if len(sys.argv) > 1 else "--prod"

    # If it is production and the production files (vite build) is not found
    # then throw File Exception
    if mode == "--prod" and not PROD_URL.exists():
        raise FileNotFoundError(f"Production frontend not found: {PROD_URL}")

    # Pass production files as a plain path (not a file:// URI) so pywebview
    # serves them over its built-in HTTP server. WebView2 (Windows) and
    # QtWebEngine (Linux) refuse to load Vite's module scripts from file://
    url = DEV_URL if mode == "--dev" else str(PROD_URL)
    webview.create_window(
        title="Chess", 
        url=url, 
        width=950, 
        height=750, 
        resizable=False,
        js_api=api
    )

    webview.start(
        icon=get_resource_path("ui/src/assets/logo.png"), debug=mode == "--dev"
    )


if __name__ == "__main__":
    main()
