# vllm-project/vllm#5961: [Bug]: vLLM crash when running Phi-3-small-8k-instruct with enable-chunked-prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#5961](https://github.com/vllm-project/vllm/issues/5961) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | attention |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM crash when running Phi-3-small-8k-instruct with enable-chunked-prefill

### Issue 正文摘录

### Your current environment ``` image": "vllm/vllm-openai:latest", --model=microsoft/Phi-3-small-8k-instruct --tensor-parallel-size=1 --disable-log-requests --trust-remote-code --enable-chunked-prefill --max-num-batched-tokens=2048 --max-model-len=4096 --gpu-memory-utilization=0.9", ``` Accelerator: 1x Nvidia L4 ### 🐛 Describe the bug ``` ERROR 06-28 13:26:18 async_llm_engine.py:52] Engine background task failed ERROR 06-28 13:26:18 async_llm_engine.py:52] Traceback (most recent call last): ERROR 06-28 13:26:18 async_llm_engine.py:52] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 42, in _log_task_completion ERROR 06-28 13:26:18 async_llm_engine.py:52] return_value = task.result() ERROR 06-28 13:26:18 async_llm_engine.py:52] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 532, in run_engine_loop ERROR 06-28 13:26:18 async_llm_engine.py:52] has_requests_in_progress = await asyncio.wait_for( ERROR 06-28 13:26:18 async_llm_engine.py:52] File "/usr/lib/python3.10/asyncio/tasks.py", line 445, in wait_for ERROR 06-28 13:26:18 async_llm_engine.py:52] return fut.result() ERROR 06-28 13:26:18 async_llm_engine.py:52...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 3:26:18 async_llm_engine.py:52] has_requests_in_progress = await asyncio.wait_for( ERROR 06-28 13:26:18 async_llm_engine.py:52] File "/usr/lib/python3.10/asyncio/tasks.py", line 445, in wait_for ERROR 06-28 13:26:18 asy...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: llm_engine.py:52] output = self.model_runner.execute_model(seq_group_metadata_list, ERROR 06-28 13:26:18 async_llm_engine.py:52] File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in de...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ug]: vLLM crash when running Phi-3-small-8k-instruct with enable-chunked-prefill bug ### Your current environment ``` image": "vllm/vllm-openai:latest", --model=microsoft/Phi-3-small-8k-instruct --tensor-parallel-size=1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ne.py:52] File "/usr/local/lib/python3.10/dist-packages/vllm/attention/backends/blocksparse_attn.py", line 376, in forward ERROR 06-28 13:26:18 async_llm_engine.py:52] or prefill_meta.block_tables.numel() == 0, \ ERROR...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: vLLM crash when running Phi-3-small-8k-instruct with enable-chunked-prefill bug ### Your current environment ``` image": "vllm/vllm-openai:latest", --model=microsoft/Phi-3-small-8k-instruct --tensor-parallel-size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
