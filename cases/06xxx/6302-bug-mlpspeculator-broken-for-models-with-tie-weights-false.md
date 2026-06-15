# vllm-project/vllm#6302: [Bug]: MLPSpeculator broken for models with `tie_weights=False`

| 字段 | 值 |
| --- | --- |
| Issue | [#6302](https://github.com/vllm-project/vllm/issues/6302) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MLPSpeculator broken for models with `tie_weights=False`

### Issue 正文摘录

### Your current environment n/a ### 🐛 Describe the bug If we start vLLM using an MLPSpeculator model with `tie_weights=False` (e.g., `granite-20b-code-instruct`) then we are crashing on all requests: ``` python -m vllm.entrypoints.openai.api_server --model ibm-granite/granite-20b-code-instruct --speculative-model ibm-granite/granite-20b-code-instruct-accelerator --use-v2-block-manager ``` any request sent to server will fail with: ``` | Traceback (most recent call last): | File "/home/zrltpa/miniforge3/envs/dev-env/lib/python3.11/site-packages/starlette/responses.py", line 261, in wrap | await func() | File "/home/zrltpa/miniforge3/envs/dev-env/lib/python3.11/site-packages/starlette/responses.py", line 250, in stream_response | async for chunk in self.body_iterator: | File "/home/zrltpa/vllm/vllm/entrypoints/openai/serving_completion.py", line 222, in completion_stream_generator | async for prompt_idx, res in result_generator: | File "/home/zrltpa/vllm/vllm/utils.py", line 318, in consumer | raise e | File "/home/zrltpa/vllm/vllm/utils.py", line 309, in consumer | raise item | File "/home/zrltpa/vllm/vllm/utils.py", line 293, in producer | async for item in iterator: | File "/hom...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: s=False` (e.g., `granite-20b-code-instruct`) then we are crashing on all requests: ``` python -m vllm.entrypoints.openai.api_server --model ibm-granite/granite-20b-code-instruct --speculative-model ibm-granite/granite-2...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: MLPSpeculator broken for models with `tie_weights=False` bug ### Your current environment n/a ### 🐛 Describe the bug If we start vLLM using an MLPSpeculator model with `tie_weights=False` (e.g., `granite-20b-code...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: have a fix, will put up a PR momentarily. It is not getting caught by CI because the model we are using in CI has `tie_weights=True`
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: MLPSpeculator broken for models with `tie_weights=False` bug ### Your current environment n/a ### 🐛 Describe the bug If we start vLLM using an MLPSpeculator model with `tie_weights=False` (e.g., `granite-20b-code...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
