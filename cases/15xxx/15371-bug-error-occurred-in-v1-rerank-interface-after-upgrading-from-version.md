# vllm-project/vllm#15371: [Bug]: Error occurred in v1/rerank interface after upgrading from version 0.7.3 to 0.8.1

| 字段 | 值 |
| --- | --- |
| Issue | [#15371](https://github.com/vllm-project/vllm/issues/15371) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Error occurred in v1/rerank interface after upgrading from version 0.7.3 to 0.8.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Start using docker compose, which is the content of the docker compose file ``` x-vllm-common: &common image: vllm/vllm-openai:latest restart: unless-stopped environment: VLLM_USE_MODELSCOPE: True HF_ENDPOINT: https://hf-mirror.com TZ: "Asia/Shanghai" volumes: - /root/.cache/modelscope/hub:/models # Please modify this to the actual model directory. networks: - vllm services: nginx: image: nginx:latest restart: unless-stopped ports: - "6090:80" volumes: - ./nginx.conf:/etc/nginx/nginx.conf # Mount the nginx configuration file. networks: - vllm depends_on: - reranker reranker: <<: *common deploy: resources: reservations: devices: - driver: nvidia capabilities: [ gpu ] count: all command: [ "--model","/models/AI-ModelScope/bge-reranker-v2-m3", "--host", "0.0.0.0", "--port", "5000", "--tensor-parallel-size", "2", "--task", "score", "--served-model-name", "bge-reranker-v2-m3", "--trust-remote-code"] networks: vllm: ``` Report an error when accessing interface /v1/rerank ``` INFO: 172.25.0.3:36030 - "POST /v1/rerank HTTP/1.0" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/opt/ve...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Error occurred in v1/rerank interface after upgrading from version 0.7.3 to 0.8.1 bug ### Your current environment ### 🐛 Describe the bug Start using docker compose, which is the content of the docker compose fil...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vllm-openai:latest restart: unless-stopped environment: VLLM_USE_MODELSCOPE: True HF_ENDPOINT: https://hf-mirror.com TZ: "Asia/Shanghai" volumes: - /root/.cache/modelscope/hub:/models # Please modify this to the actual...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ceive, sender) File "/opt/venv/lib/python3.12/site-packages/starlette/routing.py", line 714, in __call__ await self.middleware_stack(scope, receive, send) File "/opt/venv/lib/python3.12/site-packages/starlette/routing.p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: do？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ceive, sender) File "/opt/venv/lib/python3.12/site-packages/starlette/routing.py", line 714, in __call__ await self.middleware_stack(scope, receive, send) File "/opt/venv/lib/python3.12/site-packages/starlette/routing.p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
