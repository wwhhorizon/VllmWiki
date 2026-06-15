# vllm-project/vllm#20808: [Feature]: Dynamic Chunked Pipeline Parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#20808](https://github.com/vllm-project/vllm/issues/20808) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | attention |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Dynamic Chunked Pipeline Parallelism

### Issue 正文摘录

## 🚀 Feature Request: Dynamic Chunked Pipeline Parallelism (DCPP) for Long-Context Inference ### 🔍 Background vLLM already supports: * ✅ **Pipeline parallelism** * ✅ **Chunked prefill** These enable an implicit form of **Chunked Pipeline Parallelism (CPP)** — long prompt sequences are split into fixed-size chunks and processed across pipeline-parallel stages. --- ### ❗️Problem #### ⚠️ Imbalanced Computation In **long-context inference** (e.g. 64K–128K tokens), we observe **severe execution imbalance** between pipeline stages when using large fixed-size chunks: * ⚡ Early chunks (short KV history) → fast attention * 🐢 Later chunks (long KV history) → slow attention (due to quadratic cost) * ⏳ This leads to **pipeline bubbles**, where some stages are idle while others are overloaded #### ❌ Failures in PD-disaggregated + Pipeline-parallel Mode We tested several configurations under **PD-disaggregated + pipeline-parallel** setups using the following benchmark: * **Model**: Qwen 2.5 7B * **Dataset**: RandomDataset \[18000×0.2, 18000×1.8], seed = 41 * **Total input tokens**: 411,406 (20 requests) | Setup | TTFT (ms) | Notes | | ------------------------ | --------- | ---------------------...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: loaded #### ❌ Failures in PD-disaggregated + Pipeline-parallel Mode We tested several configurations under **PD-disaggregated + pipeline-parallel** setups using the following benchmark: * **Model**: Qwen 2.5 7B * **Data...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: Dynamic Chunked Pipeline Parallelism feature request ## 🚀 Feature Request: Dynamic Chunked Pipeline Parallelism (DCPP) for Long-Context Inference ### 🔍 Background vLLM already supports: * ✅ **Pipeline paralle...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Failures in PD-disaggregated + Pipeline-parallel Mode We tested several configurations under **PD-disaggregated + pipeline-parallel** setups using the following benchmark: * **Model**: Qwen 2.5 7B * **Dataset**: RandomD...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Dynamic Chunked Pipeline Parallelism feature request ## 🚀 Feature Request: Dynamic Chunked Pipeline Parallelism (DCPP) for Long-Context Inference ### 🔍 Background vLLM already supports: * ✅ **Pipeline paralle...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ✅ **Pipeline parallelism** * ✅ **Chunked prefill** These enable an implicit form of **Chunked Pipeline Parallelism (CPP)** — long prompt sequences are split into fixed-size chunks and processed across pipeline-parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
