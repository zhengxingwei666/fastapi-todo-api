# main.py
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from routers import tasks  # 导入刚才写好的路由模块

# 保持解决白屏的配置
app = FastAPI(title="待办事项 API", docs_url=None)

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_js_url="https://cdn.bootcdn.net/ajax/libs/swagger-ui/5.17.14/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.bootcdn.net/ajax/libs/swagger-ui/5.17.14/swagger-ui.css",
        swagger_favicon_url="https://cdn.bootcdn.net/ajax/libs/swagger-ui/5.17.14/favicon-32x32.png"
    )

@app.get("/health")
def health_check():
    return {"status": "ok"}

# 将任务路由注册到主应用中
app.include_router(tasks.router)