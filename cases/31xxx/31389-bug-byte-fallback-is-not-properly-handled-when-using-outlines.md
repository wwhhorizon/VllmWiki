# vllm-project/vllm#31389: [Bug]: Byte fallback is not properly handled when using outlines

| 字段 | 值 |
| --- | --- |
| Issue | [#31389](https://github.com/vllm-project/vllm/issues/31389) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Byte fallback is not properly handled when using outlines

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The following request crashes the server hosted with outlines backed: ```python from openai import OpenAI client = OpenAI(api_key='xxx', base_url='http://localhost:8000/v1') schema = { "type": "string", "enum": [ "🤗", # Can be any string which byte fallbacks. ] } req = { "messages": [ { "role": "user", "content": "test" }, ], "extra_body": {"structured_outputs": {"json": schema}}, "model": "openai/gpt-oss-20b", } response = client.chat.completions.create(**req) ``` To reproduce the error, you just serve an arbitrary model which does not have `🤗` as a token, e.g., `openai/gpt-oss-20b`: ```shell % vllm serve openai/gpt-oss-20b --structured-outputs-config '{"backend": "outlines"}' ``` and then run the script above: ```shell % python ./test.py Traceback (most recent call last): File "...test.py", line 22, in response = client.chat.completions.create(**req) File "/usr/local/lib/python3.13/dist-packages/openai/_utils/_utils.py", line 286, in wrapper return func(*args, **kwargs) File "/usr/local/lib/python3.13/dist-packages/openai/resources/chat/completions/completions.py", line 1192, in create return self._post( ~~~~~~~~~~^ "/chat/comp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t crashes the server hosted with outlines backed: ```python from openai import OpenAI client = OpenAI(api_key='xxx', base_url='http://localhost:8000/v1') schema = { "type": "string", "enum": [ "🤗", # Can be any string w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: }, ], "extra_body": {"structured_outputs": {"json": schema}}, "model": "openai/gpt-oss-20b", } response = client.chat.completions.create(**req) ``` To reproduce the error, you just serve an arbitrary model which does no...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: g ### Your current environment ### 🐛 Describe the bug The following request crashes the server hosted with outlines backed: ```python from openai import OpenAI client = OpenAI(api_key='xxx', base_url='http://localhost:8...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Byte fallback is not properly handled when using outlines bug ### Your current environment ### 🐛 Describe the bug The following request crashes the server hosted with outlines backed: ```python from openai import...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
