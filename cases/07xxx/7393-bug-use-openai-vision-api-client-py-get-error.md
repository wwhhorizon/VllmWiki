# vllm-project/vllm#7393: [Bug]: use `openai_vision_api_client.py` get error

| 字段 | 值 |
| --- | --- |
| Issue | [#7393](https://github.com/vllm-project/vllm/issues/7393) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: use `openai_vision_api_client.py` get error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug use `vllm serve /mnt/models --trust-remote-code --load-format safetensors --tensor-parallel-size 2 --chat-template template_llava.jinja`deploy `llava-1.5-7b-hf`model. vllm server log is ``` INFO 08-10 11:59:39 launcher.py:14] Available routes are: INFO 08-10 11:59:39 launcher.py:22] Route: /openapi.json, Methods: GET, HEAD INFO 08-10 11:59:39 launcher.py:22] Route: /docs, Methods: GET, HEAD INFO 08-10 11:59:39 launcher.py:22] Route: /docs/oauth2-redirect, Methods: GET, HEAD INFO 08-10 11:59:39 launcher.py:22] Route: /redoc, Methods: GET, HEAD INFO 08-10 11:59:39 launcher.py:22] Route: /health, Methods: GET INFO 08-10 11:59:39 launcher.py:22] Route: /tokenize, Methods: POST INFO 08-10 11:59:39 launcher.py:22] Route: /detokenize, Methods: POST INFO 08-10 11:59:39 launcher.py:22] Route: /v1/models, Methods: GET INFO 08-10 11:59:39 launcher.py:22] Route: /version, Methods: GET INFO 08-10 11:59:39 launcher.py:22] Route: /v1/chat/completions, Methods: POST INFO 08-10 11:59:39 launcher.py:22] Route: /v1/completions, Methods: POST INFO 08-10 11:59:39 launcher.py:22] Route: /v1/embeddings, Methods: POST INFO: Started server process [335]...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: our current environment ### 🐛 Describe the bug use `vllm serve /mnt/models --trust-remote-code --load-format safetensors --tensor-parallel-size 2 --chat-template template_llava.jinja`deploy `llava-1.5-7b-hf`model. vllm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: beddings, Methods: POST INFO: Started server process [335] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://0.0.0.0:8081 (Press CTRL+C to quit) ``` and use `open...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: te: /v1/models, Methods: GET INFO 08-10 11:59:39 launcher.py:22] Route: /version, Methods: GET INFO 08-10 11:59:39 launcher.py:22] Route: /v1/chat/completions, Methods: POST INFO 08-10 11:59:39 launcher.py:22] Route: /v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: hub.com/vllm-project/vllm/blob/main/examples/openai_vision_api_client.py test vllm,get this error ``` Error code: 400 - {'object': 'error', 'message': '', 'type': 'BadRequestError', 'param': None, 'code': 400} Traceback...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
