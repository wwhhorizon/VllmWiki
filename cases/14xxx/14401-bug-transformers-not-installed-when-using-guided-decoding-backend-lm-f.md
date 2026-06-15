# vllm-project/vllm#14401: [Bug]: "transformers not installed" when using --guided-decoding-backend lm-format-enforcer

| 字段 | 值 |
| --- | --- |
| Issue | [#14401](https://github.com/vllm-project/vllm/issues/14401) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: "transformers not installed" when using --guided-decoding-backend lm-format-enforcer

### Issue 正文摘录

### Your current environment docker: vllm/vllm-openai:latest parameters: ``` --model /data/models/mistralai/Mistral-Large-Instruct-2407 --disable-log-requests --trust-remote-code --tensor-parallel-size 4 --max-model-len 100000 --enforce-eager --enable-auto-tool-choice --tool-call-parser mistral --tokenizer-mode mistral --config-format mistral --guided-decoding-backend lm-format-enforcer --enable-chunked-prefill --enable-prefix-caching ``` ### 🐛 Describe the bug error: ``` ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/lmformatenforcer/integrations/transformers.py", line 5, in from transformers.generation.logits_process import LogitsWarper, PrefixConstrainedLogitsProcessor ImportError: cannot import name 'LogitsWarper' from 'transformers.generation.logits_process' (/usr/local/lib/python3.12/dist-packages/transformers/generation/logits_process.py) During handling of the above exception, another exception occurred: Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi result = await app( # type: ignore[func-returns-value] ^...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: "transformers not installed" when using --guided-decoding-backend lm-format-enforcer bug;stale ### Your current environment docker: vllm/vllm-openai:latest parameters: ``` --model /data/models/mistralai/Mistral-L...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: g]: "transformers not installed" when using --guided-decoding-backend lm-format-enforcer bug;stale ### Your current environment docker: vllm/vllm-openai:latest parameters: ``` --model /data/models/mistralai/Mistral-Larg...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: t installed" when using --guided-decoding-backend lm-format-enforcer bug;stale ### Your current environment docker: vllm/vllm-openai:latest parameters: ``` --model /data/models/mistralai/Mistral-Large-Instruct-2407 --di...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: "transformers not installed" when using --guided-decoding-backend lm-format-enforcer bug;stale ### Your current environment docker: vllm/vllm-openai:latest parameters: ``` --model /data/models/mistralai/Mistral-L...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
