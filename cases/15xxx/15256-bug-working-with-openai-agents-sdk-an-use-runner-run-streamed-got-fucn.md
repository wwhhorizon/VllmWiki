# vllm-project/vllm#15256: [Bug]: working with openai-agents sdk an use Runner.run_streamed() got fucntion call error

| 字段 | 值 |
| --- | --- |
| Issue | [#15256](https://github.com/vllm-project/vllm/issues/15256) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: working with openai-agents sdk an use Runner.run_streamed() got fucntion call error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug working with openai-agents sdk and use Runner.run_streamed(), i got error below: **on the calling side ：** === Run starting === Agent updated: Joker Traceback (most recent call last): File "/home/zhouxiang/file_server/my_agent.py", line 64, in asyncio.run(main()) File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete return future.result() ^^^^^^^^^^^^^^^ File "/home/zhouxiang/file_server/my_agent.py", line 43, in main async for event in result.stream_events(): File "/home/zhouxiang/file_server/venv/lib/python3.12/site-packages/agents/result.py", line 182, in stream_events raise self._stored_exception File "/home/zhouxiang/file_server/venv/lib/python3.12/site-packages/agents/run.py", line 537, in _run_streamed_impl turn_result = await cls._run_single_turn_streamed( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/zhouxiang/file_server/venv/lib/python3.12/site...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: File "/home/zhouxiang/file_server/my_agent.py", line 64, in asyncio.run(main()) File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: any_jokes], model="/home/zx/vLLM/model/Qwen2.5-14B-Instruct-GPTQ-Int4" ) result = Runner.run_streamed( agent, input="Hello", ) print("=== Run starting ===") async for event in result.stream_events(): # We'll ignore the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s/run.py", line 639, in _run_single_turn_streamed async for event in model.stream_response( File "/home/zhouxiang/file_server/venv/lib/python3.12/site-packages/agents/models/openai_chatcompletions.py", line 413, in stre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: =") ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: enai-agents sdk an use Runner.run_streamed() got fucntion call error bug;stale ### Your current environment ### 🐛 Describe the bug working with openai-agents sdk and use Runner.run_streamed(), i got error below: **on th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
