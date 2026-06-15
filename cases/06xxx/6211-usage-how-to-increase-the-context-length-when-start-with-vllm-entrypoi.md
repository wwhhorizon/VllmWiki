# vllm-project/vllm#6211: [Usage]: How to increase the context length when start with vllm.entrypoints.openai.api_server

| 字段 | 值 |
| --- | --- |
| Issue | [#6211](https://github.com/vllm-project/vllm/issues/6211) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;model_support |
| 子分类 |  |
| Operator 关键词 | cache |
| 症状 |  |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to increase the context length when start with vllm.entrypoints.openai.api_server

### Issue 正文摘录

### Your current environment I tried deepseek-coder-v2-lite-instruct can be started on 2 x L40 GPU with vllm 0.5.1，but the context cannot reach 128K, only 9415 tokens in my test. Below is my start cmd. ``` python3 -m vllm.entrypoints.openai.api_server --dtype float16 --trust-remote-code --model DeepSeek-Coder-V2-Lite-Instruct --port 9000 --host 0.0.0.0 --tensor-parallel-size 2 --max-seq-len 63040 --max-model-len 30720 ``` When I remove the --max-seq-len 63040 --max-model-len 30720, it will report error when start: ``` [rank0]: ValueError: The model's max seq len (163840) is larger than the maximum number of tokens that can be stored in KV cache (63040). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine. /usr/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 2 leaked shared_memory objects to clean up at shutdown warnings.warn('resource_tracker: There appear to be %d ' ```

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ow is my start cmd. ``` python3 -m vllm.entrypoints.openai.api_server --dtype float16 --trust-remote-code --model DeepSeek-Coder-V2-Lite-Instruct --port 9000 --host 0.0.0.0 --tensor-parallel-size 2 --max-seq-len 63040 -...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 63840) is larger than the maximum number of tokens that can be stored in KV cache (63040). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine. /usr/lib/python3.10/multipro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vllm.entrypoints.openai.api_server --dtype float16 --trust-remote-code --model DeepSeek-Coder-V2-Lite-Instruct --port 9000 --host 0.0.0.0 --tensor-parallel-size 2 --max-seq-len 63040 --max-model-len 30720 ``` When I rem...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: context length when start with vllm.entrypoints.openai.api_server usage;stale ### Your current environment I tried deepseek-coder-v2-lite-instruct can be started on 2 x L40 GPU with vllm 0.5.1，but the context cannot rea...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ith vllm 0.5.1，but the context cannot reach 128K, only 9415 tokens in my test. Below is my start cmd. ``` python3 -m vllm.entrypoints.openai.api_server --dtype float16 --trust-remote-code --model DeepSeek-Coder-V2-Lite-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
