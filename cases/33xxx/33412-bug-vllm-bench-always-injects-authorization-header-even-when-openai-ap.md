# vllm-project/vllm#33412: [Bug]: vllm bench always injects Authorization header even when OPENAI_API_KEY is unset

| 字段 | 值 |
| --- | --- |
| Issue | [#33412](https://github.com/vllm-project/vllm/issues/33412) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm bench always injects Authorization header even when OPENAI_API_KEY is unset

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running `vllm bench serve` against a remote `vllm serve` instance via `--base-url`, all benchmark requests fail with `401 Unauthorized` if `OPENAI_API_KEY` is not set. #### Root cause `vllm/benchmarks/lib/endpoint_request_func.py` unconditionally sets: ```python headers = { "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}", } ``` If the env var is unset, this results in Authorization: Bearer None, which is rejected by vllm.entrypoints.openai.server_utils.verify_token(). ### Steps to reproduce 1. Start a vLLM server without authentication requirement: ```bash vllm serve ``` 2. From another machine (or environment), run benchmark using --base-url without setting OPENAI_API_KEY: ```bash unset OPENAI_API_KEY vllm bench serve \ --backend openai \ --base-url http:// : ``` 3. Observe that all benchmark requests fail with: ``` /app/.venv/lib/python3.12/site-packages/vllm/benchmarks/serve.py:886: UserWarning: All requests failed. This is likely due to a misconfiguration on the benchmark arguments. ``` 4. Inspect outgoing request headers: ``` Authorization: Bearer None ``` #### Expected behavior Do not include Authorizatio...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_de...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ing OPENAI_API_KEY: ```bash unset OPENAI_API_KEY vllm bench serve \ --backend openai \ --base-url http:// : ``` 3. Observe that all benchmark requests fail with: ``` /app/.venv/lib/python3.12/site-packages/vllm/benchmar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rve.py:886: UserWarning: All requests failed. This is likely due to a misconfiguration on the benchmark arguments. ``` 4. Inspect outgoing request headers: ``` Authorization: Bearer None ``` #### Expected behavior Do no...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ` against a remote `vllm serve` instance via `--base-url`, all benchmark requests fail with `401 Unauthorized` if `OPENAI_API_KEY` is not set. #### Root cause `vllm/benchmarks/lib/endpoint_request_func.py` unconditional...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
