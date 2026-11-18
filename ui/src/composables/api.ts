import type { PywebviewChessApi } from "~/types/api";

let apiPromise: Promise<PywebviewChessApi> | null = null;

export function usePywebviewApi(): Promise<PywebviewChessApi> {
  if (!apiPromise) {   
    apiPromise = new Promise((resolve) => {
      if (window.pywebview?.api) {
        resolve(window.pywebview.api);
      } else {
        window.addEventListener('pywebviewready', () => {
          if (window.pywebview?.api) {
            resolve(window.pywebview.api);
          }
        }, {
          once: true
        })
      }
    });
  }
  return apiPromise;
}
