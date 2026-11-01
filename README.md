# 待办事项 API 项目 (FastAPI Todo API)

这是一个基于 FastAPI 开发的待办事项后端 API 练手项目，实现了完整的 CRUD（增删改查）及筛选功能。

## 环境要求
- Python 3.10+
- Git

## 安装与启动说明
1. 克隆代码到本地：
   `git clone <你的仓库HTTPS地址>`
2. 进入项目目录：
   `cd fastapi-todo-api`
3. 创建并激活虚拟环境：
   - Windows: `python -m venv .venv` 然后 `.venv\Scripts\activate`
   - Mac/Linux: `python3 -m venv .venv` 然后 `source .venv/bin/activate`
4. 安装依赖：
   `pip install -r requirements.txt`
5. 启动服务：
   `fastapi dev main.py`
6. 打开浏览器访问交互式文档：
   `http://127.0.0.1:8000/docs`

## 接口示例
- `GET /tasks` 查询所有任务（可带 `?completed=true/false` 筛选）
- `POST /tasks` 新增任务，Body: `{"title": "学习"}`
- `PATCH /tasks/{task_id}` 局部更新，Body: `{"completed": true}`
- `DELETE /tasks/{task_id}` 删除任务（返回 204）