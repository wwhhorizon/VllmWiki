# vllm-project/vllm#22719: [Bug]: Qwen2.5vl-3b OOM but 7b works fine

| 字段 | 值 |
| --- | --- |
| Issue | [#22719](https://github.com/vllm-project/vllm/issues/22719) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5vl-3b OOM but 7b works fine

### Issue 正文摘录

### Your current environment vllm 0.9.2 ### 🐛 Describe the bug Hi there, I use vllm-0.9.2 to serve qwen2.5vl-7b model works fine, but when switch to 3b, it raised OOM error, it is quite strange because i did not change any line of the script. script to serve: `vllm serve /yyyy --port 8000 --served-model-name xxx --gpu_memory_utilization 0.9 --max-model-len 8192 --max-seq-len-to-capture 8192 --max-num-seqs 64 --tensor-parallel-size 1` error: `RuntimeError: CUDA out of memory occurred when warming up sampler with 64 dummy requests. Please try lowering `max_num_seqs` or `gpu_memory_utilization` when initializing the engine.` and i see the log, it seems that the 3b model can only support 48 max-num-seqs ? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 192 --max-num-seqs 64 --tensor-parallel-size 1` error: `RuntimeError: CUDA out of memory occurred when warming up sampler with 64 dummy requests. Please try lowering `max_num_seqs` or `gpu_memory_utilization` when initi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2.5vl-3b OOM but 7b works fine bug;stale ### Your current environment vllm 0.9.2 ### 🐛 Describe the bug Hi there, I use vllm-0.9.2 to serve qwen2.5vl-7b model works fine, but when switch to 3b, it raised OOM...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Qwen2.5vl-3b OOM but 7b works fine bug;stale ### Your current environment vllm 0.9.2 ### 🐛 Describe the bug Hi there, I use vllm-0.9.2 to serve qwen2.5vl-7b model works fine, but when switch to 3b, it raised OOM...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: Qwen2.5vl-3b OOM but 7b works fine bug;stale ### Your current environment vllm 0.9.2 ### 🐛 Describe the bug Hi there, I use vllm-0.9.2 to serve qwen2.5vl-7b model works fine, but when switch to 3b, it raised OOM...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance distributed_parallel;model_support cuda oom Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
