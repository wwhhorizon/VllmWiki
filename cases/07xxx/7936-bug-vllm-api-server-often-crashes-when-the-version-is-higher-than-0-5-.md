# vllm-project/vllm#7936: [Bug]: vllm api_server often crashes when the version is higher than 0.5.3.

| 字段 | 值 |
| --- | --- |
| Issue | [#7936](https://github.com/vllm-project/vllm/issues/7936) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm api_server often crashes when the version is higher than 0.5.3.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Sglang blog has reported this crash. see https://lmsys.org/blog/2024-07-25-sglang-llama3/#appendix-a-detailed-benchmark-setups Start command ```shell python -m vllm.entrypoints.openai.api_server --model meta-llama/Meta-Llama-3.1-8B --host 0.0.0.0 --trust-remote-code --port 8084 ``` It often crashes, the logs like below. ```shell Exception in callback functools.partial( , error_callback= >) handle: , error_callback= >)> Traceback (most recent call last): File "/home/ubuntu/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 55, in _log_task_completion return_value = task.result() File "/home/ubuntu/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 930, in run_engine_loop result = task.result() File "/home/ubuntu/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 873, in engine_step request_outputs = await self.engine.step_async(virtual_engine) File "/home/ubuntu/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 301, in step_async virtual_engine].schedule() File "/home/ubuntu/minic...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: vllm api_server often crashes when the version is higher than 0.5.3. bug;stale ### Your current environment ### 🐛 Describe the bug Sglang blog has reported this crash. see https://lmsys.org/blog/2024-07-25-sglang-llama3...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: vllm api_server often crashes when the version is higher than 0.5.3. bug;stale ### Your current environment ### 🐛 Describe the bug Sglang blog has reported this crash. see https://lmsys.org/blog/2024-07-25-sglang...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: k_group: File "/home/ubuntu/.local/lib/python3.10/site-packages/anyio/_backends/_asyncio.py", line 658, in __aexit__ raise BaseExceptionGroup( exceptiongroup.ExceptionGroup: unhandled errors in a TaskGroup (1 sub-except...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: og has reported this crash. see https://lmsys.org/blog/2024-07-25-sglang-llama3/#appendix-a-detailed-benchmark-setups Start command ```shell python -m vllm.entrypoints.openai.api_server --model meta-llama/Meta-Llama-3.1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
