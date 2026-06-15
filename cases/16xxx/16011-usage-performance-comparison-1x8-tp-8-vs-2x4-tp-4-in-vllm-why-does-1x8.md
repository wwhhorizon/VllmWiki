# vllm-project/vllm#16011: [Usage]: Performance Comparison: 1x8 (TP=8) vs 2x4 (TP=4) in vLLM - Why Does 1x8 Outperform 2x4 in Concurrency?

| 字段 | 值 |
| --- | --- |
| Issue | [#16011](https://github.com/vllm-project/vllm/issues/16011) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | fp8 |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Performance Comparison: 1x8 (TP=8) vs 2x4 (TP=4) in vLLM - Why Does 1x8 Outperform 2x4 in Concurrency?

### Issue 正文摘录

### Your current environment The image I am using is 0.8.0. The NVIDIA GPUs I use are L40S, with 8 of them on a single server . ### Start Command ```bash vllm serve Qwen2.5-72B-Instruct-FP8 --tensor-parallel-size 8 --max-model-len 32000 --gpu-memory-utilization 0.95 --enforce-eager ``` ### Questions I am currently experimenting with the performance of vLLM on an 8-GPU setup and have encountered some unexpected results when comparing two configurations: 1. **1x8 (TP=8):** Using all 8 GPUs with tensor parallelism (TP=8), where the model weights are distributed across 8 GPUs. 2. **2x4 (TP=4):** Running two separate services, each using 4 GPUs with tensor parallelism (TP=4), effectively utilizing all 8 GPUs. From the articles I've read ([Performance: Llama 3 70B; vLLM does not scale beyond TP=4](https://github.com/vllm-project/vllm/issues/8089) and [Serving LLMs on AMD MI300X: Best Practices](https://blog.vllm.ai/2024/10/23/vllm-serving-amd.html)), I understand that: - **TP=8** is expected to reduce the first-token latency but may limit concurrency due to higher communication overhead. - **TP=4** is generally better for improving concurrency and throughput by running multiple instance...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: th 8 of them on a single server . ### Start Command ```bash vllm serve Qwen2.5-72B-Instruct-FP8 --tensor-parallel-size 8 --max-model-len 32000 --gpu-memory-utilization 0.95 --enforce-eager ``` ### Questions I am current...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: gle server . ### Start Command ```bash vllm serve Qwen2.5-72B-Instruct-FP8 --tensor-parallel-size 8 --max-model-len 32000 --gpu-memory-utilization 0.95 --enforce-eager ``` ### Questions I am currently experimenting with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: onfigurations: 1. **1x8 (TP=8):** Using all 8 GPUs with tensor parallelism (TP=8), where the model weights are distributed across 8 GPUs. 2. **2x4 (TP=4):** Running two separate services, each using 4 GPUs with tensor p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: s 2x4 (TP=4) in vLLM - Why Does 1x8 Outperform 2x4 in Concurrency? usage;stale ### Your current environment The image I am using is 0.8.0. The NVIDIA GPUs I use are L40S, with 8 of them on a single server . ### Start Co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: l)), I understand that: - **TP=8** is expected to reduce the first-token latency but may limit concurrency due to higher communication overhead. - **TP=4** is generally better for improving concurrency and throughput by...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
