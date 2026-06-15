# vllm-project/vllm#27093: [Feature]: Process-level PD Disaggregation within Single Instance

| 字段 | 值 |
| --- | --- |
| Issue | [#27093](https://github.com/vllm-project/vllm/issues/27093) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | activation;attention;cache;cuda;kernel |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Process-level PD Disaggregation within Single Instance

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Description of the Feature Proposal This proposal outlines a new scheduling and execution mechanism called "Process-level PD Disaggregation". The core idea is to spatially partition a single GPU's resources to run compute-bound prefill operations and memory-bound decode operations concurrently. This is achieved by launching separate processes for prefill and decode on the same GPU, managed by NVIDIA MPS and multiple stream. This approach enables resource sharing between the two distinct workloads, improving overall GPU utilization and allowing the system to meet strict SLOs for both TTFT and ITL. ### Motivation for the Proposal LLM serving in production environments faces a critical challenge: simultaneously optimizing for TTFT and ITL. During traffic surges, single-instance deployments struggle to balance these two metrics, making it difficult to meet strict SLOs, such as TTFT 400ms (%) | 4% | 39.40% | 72% | 82% | | Stutters per Request | 1 | 1.29 | 2.22 | 3.85 | | Stutter Rate (%) | 3.760% | 5.700% | 23.000% | 81.000% | | Position of First Stutter | 204 | 269 | 228 | 92 | ### Resource Utilization in LLM To understand the root cause, we...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: Feature]: Process-level PD Disaggregation within Single Instance feature request;stale ### 🚀 The feature, motivation and pitch ### Description of the Feature Proposal This proposal outlines a new scheduling and executio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: re Proposal This proposal outlines a new scheduling and execution mechanism called "Process-level PD Disaggregation". The core idea is to spatially partition a single GPU's resources to run compute-bound prefill operati...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: | 92 | ### Resource Utilization in LLM To understand the root cause, we profiled the SM utilization of different operations during the prefill stage on a vLLM 0.9.1 deployment (Qwen2-32B, 8 x H20). The results confirm t...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: emory Management: A unified memory manager will be created to handle the KV cache. This manager will use CUDA IPC to share GPU memory handles between the Prefill and Decode processes, ensuring the Decode process can sea...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ifferent operations during the prefill stage on a vLLM 0.9.1 deployment (Qwen2-32B, 8 x H20). The results confirm that prefill is a compute-bound phase, with many kernels achieving high SM utilization. In contrast, the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
