# vllm-project/vllm#586: OOM killer - actor is dead

| 字段 | 值 |
| --- | --- |
| Issue | [#586](https://github.com/vllm-project/vllm/issues/586) |
| 状态 | closed |
| 标签 |  |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> OOM killer - actor is dead

### Issue 正文摘录

I have 4x16GB GPU cards, I'm loading the vicuna 13b.v1.3 model, and I'm getting the following error; `The actor is dead because its worker process has died. Worker exit type: SYSTEM_ERROR Worker exit detail: Worker unexpectedly exits with a connection error code 2. End of file. There are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected errors. The actor never ran - it was cancelled before it started running.` The command I'm using is this: ```RAY_memory_usage_threshold=0.7 RAY_memory_monitor_refresh_ms=0 CUDA_VISIBLE_DEVICES=0,1,2,3 python -m vllm.entrypoints.api_server --model ../models/vicuna-13b-v1.3/ --gpu-memory-utilization 0.9 --swap-space 1 --tokenizer hf-internal-testing/llama-tokenizer --tensor-parallel-size 4```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: - actor is dead I have 4x16GB GPU cards, I'm loading the vicuna 13b.v1.3 model, and I'm getting the following error; `The actor is dead because its worker process has died. Worker exit type: SYSTEM_ERROR Worker exit det...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: this: ```RAY_memory_usage_threshold=0.7 RAY_memory_monitor_refresh_ms=0 CUDA_VISIBLE_DEVICES=0,1,2,3 python -m vllm.entrypoints.api_server --model ../models/vicuna-13b-v1.3/ --gpu-memory-utilization 0.9 --swap-space 1 -...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: OOM killer - actor is dead I have 4x16GB GPU cards, I'm loading the vicuna 13b.v1.3 model, and I'm getting the following error; `The actor is dead because its worker process has died. Worker exit type: SYSTEM_ERROR Work
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 1.3/ --gpu-memory-utilization 0.9 --swap-space 1 --tokenizer hf-internal-testing/llama-tokenizer --tensor-parallel-size 4```

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
