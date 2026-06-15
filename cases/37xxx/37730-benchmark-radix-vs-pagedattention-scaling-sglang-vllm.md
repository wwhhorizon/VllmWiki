# vllm-project/vllm#37730: Benchmark: Radix vs. PagedAttention Scaling (SGLang / vLLM)

| 字段 | 值 |
| --- | --- |
| Issue | [#37730](https://github.com/vllm-project/vllm/issues/37730) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Benchmark: Radix vs. PagedAttention Scaling (SGLang / vLLM)

### Issue 正文摘录

# Benchmark: Radix vs. PagedAttention Scaling (SGLang / vLLM) ### Problem Description This issue documents a benchmark comparing **SGLang (RadixAttention)** and **vLLM (PagedAttention)** to observe the "Scaling Zero-Sum" trade-off. SGLang’s Radix tree optimizes prefix-sharing across requests but uses Python-based routing, which can be vulnerable to Python Global Interpreter Lock (GIL) contention under high concurrency. vLLM mitigates the Python GIL bottleneck by offloading its PagedAttention implementation into C++ CUDA extensions, allowing better multi-threading scaling. To observe this behavior, we ran a 150-concurrency load test against identical `Qwen/Qwen2.5-0.5B` deployments on a `g2-standard-32` Google Compute instance (1x NVIDIA L4, 32 vCPUs). ### Reproduction / Context **Hardware Context:** - **Machine Type:** `g2-standard-32` (Google Cloud) - **GPU:** 1x NVIDIA L4 (24GB VRAM) - **Host Cores:** 32 vCPUs - **Model:** `Qwen/Qwen2.5-0.5B` **The Load Test (barrage.py):** We sent concurrent requests querying a shared payload pool to saturate the backend event loops: - **Concurrency:** 150 simultaneous asynchronous workers - **Duration:** 45 seconds - **Endpoint:** `/v1/complet...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: oint:** `/v1/completions` ### Execution Diagnostics (Side-by-Side) The Docker hardware monitoring metrics showed the following results: #### 1. vLLM (PagedAttention) - **Total Requests Completed:** 16,369 - **Throughput...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: Benchmark: Radix vs. PagedAttention Scaling (SGLang / vLLM) # Benchmark: Radix vs. PagedAttention Scaling (SGLang / vLLM) ### Problem Description This issue documents a benchmark comparing **SGLang (RadixAttention)** an
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: GIL bottleneck by offloading its PagedAttention implementation into C++ CUDA extensions, allowing better multi-threading scaling. To observe this behavior, we ran a 150-concurrency load test against identical `Qwen/Qwen...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: adix tree optimizes prefix-sharing across requests but uses Python-based routing, which can be vulnerable to Python Global Interpreter Lock (GIL) contention under high concurrency. vLLM mitigates the Python GIL bottlene...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rve this behavior, we ran a 150-concurrency load test against identical `Qwen/Qwen2.5-0.5B` deployments on a `g2-standard-32` Google Compute instance (1x NVIDIA L4, 32 vCPUs). ### Reproduction / Context **Hardware Conte...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
