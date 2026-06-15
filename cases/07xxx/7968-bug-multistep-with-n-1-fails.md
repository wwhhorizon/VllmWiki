# vllm-project/vllm#7968: [Bug]: Multistep with n>1 Fails

| 字段 | 值 |
| --- | --- |
| Issue | [#7968](https://github.com/vllm-project/vllm/issues/7968) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Multistep with n>1 Fails

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Launched server with: ```bash vllm serve $MODEL --num-scheduler-steps 8 ``` Sent the following request: ```python from openai import OpenAI # Modify OpenAI's API key and API base to use vLLM's API server. openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( # defaults to os.environ.get("OPENAI_API_KEY") api_key=openai_api_key, base_url=openai_api_base, ) models = client.models.list() model = models.data[0].id # Completion API stream = False completion = client.completions.create( model=model, prompt="A robot may not injure a human being", echo=False, n=2, stream=stream) print("Completion results:") if stream: for c in completion: print(c) else: print(completion) ``` Got the following output: ```bash INFO: Finished server process [1668044] INFO 08-28 19:29:45 server.py:222] vLLM ZMQ RPC Server was interrupted. Future exception was never retrieved future: Traceback (most recent call last): File "/home/rshaw/vllm/vllm/entrypoints/openai/rpc/server.py", line 111, in generate async for request_output in results_generator: File "/home/rshaw/vllm/vllm/engine/async_llm_engine.py", line 1050, in generate...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Multistep with n>1 Fails bug;stale ### Your current environment ### 🐛 Describe the bug Launched server with: ```bash vllm serve $MODEL --num-scheduler-steps 8 ``` Sent the following request: ```python from openai...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: cheduler-steps 8 ``` Sent the following request: ```python from openai import OpenAI # Modify OpenAI's API key and API base to use vLLM's API server. openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1"...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^ RuntimeError: shape mismatch: value tensor of shape [2] cannot be broadcast to indexing result of shape [1, 1] ``` ### Before submitting a new issue... - [X] Make sure you a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ent.models.list() model = models.data[0].id # Completion API stream = False completion = client.completions.create( model=model, prompt="A robot may not injure a human being", echo=False, n=2, stream=stream) print("Comp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t ### 🐛 Describe the bug Launched server with: ```bash vllm serve $MODEL --num-scheduler-steps 8 ``` Sent the following request: ```python from openai import OpenAI # Modify OpenAI's API key and API base to use vLLM's A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
