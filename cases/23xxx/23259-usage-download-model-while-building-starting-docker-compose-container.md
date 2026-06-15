# vllm-project/vllm#23259: [Usage]: Download model while building/starting docker compose container

| 字段 | 值 |
| --- | --- |
| Issue | [#23259](https://github.com/vllm-project/vllm/issues/23259) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Download model while building/starting docker compose container

### Issue 正文摘录

### Your current environment ```text Windows 11 WSL 2 Docker Desktop ``` ### How would you like to use vllm I want to run inference of a "Qwen/Qwen3-32B-AWQ" with docker compose localy. I was create `docker-compose.yml` file: ``` vllm: image: vllm/vllm-openai:latest container_name: vllm restart: always networks: - app-network ports: - "8000:8000" volumes: # Пробрасываем volume для кэша моделей, чтобы не скачивать их каждый раз - vllm_models:/root/.cache/huggingface env_file: # Указываем путь к .env файлу для vllm - path: ./build/vllm/.env required: true command: ["--model", "${MODEL_NAME}", "--quantization", "awq"] healthcheck: test: ["CMD", "curl", "-f", "http://localhost:8000/v1/models"] interval: 30s timeout: 10s retries: 5 start_period: 1500s # Даем время на скачивание и загрузку модели в GPU 25 минут deploy: resources: reservations: devices: - driver: nvidia count: all capabilities: [gpu] ``` My Dockerfile from `.\build\vllm\Dockerfile`: ``` FROM vllm/vllm-openai:latest RUN uv pip install --system --no-cache-dir git+https://github.com/huggingface/transformers.git ``` My `.\build\vllm\.env`: ``` MODEL_NAME=Qwen/Qwen3-32B-AWQ HUGGING_FACE_HUB_TOKEN=hf_blablabla... ``` When I bu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Usage]: Download model while building/starting docker compose container usage ### Your current environment ```text Windows 11 WSL 2 Docker Desktop ``` ### How would you like to use vllm I want to run inference of a "Qw...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Download model while building/starting docker compose container usage ### Your current environment ```text Windows 11 WSL 2 Docker Desktop ``` ### How would you like to use vllm I want to run inference of a "Qw...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: | INFO 08-20 07:14:44 [__init__.py:241] Automatically detected platform cuda. vllm | (APIServer pid=1) INFO 08-20 07:14:45 [api_server.py:1805] vLLM API server version 0.10.1 vllm | (APIServer pid=1) INFO 08-20 07:14:45...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: r pid=1) huggingface_hub.errors.HFValidationError: Repo id must use alphanumeric chars or '-', '_', '.', '--' and '..' are forbidden, '-' and '.' cannot start or end the name, max length is 96: ''. vllm | (APIServer pid...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: .env required: true command: ["--model", "${MODEL_NAME}", "--quantization", "awq"] healthcheck: test: ["CMD", "curl", "-f", "http://localhost:8000/v1/models"] interval: 30s timeout: 10s retries: 5 start_period: 1500s #...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
