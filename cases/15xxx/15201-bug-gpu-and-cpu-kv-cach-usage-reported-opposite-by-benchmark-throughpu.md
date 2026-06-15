# vllm-project/vllm#15201: [Bug]: GPU and CPU KV cach usage reported opposite by benchmark_throughput

| 字段 | 值 |
| --- | --- |
| Issue | [#15201](https://github.com/vllm-project/vllm/issues/15201) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPU and CPU KV cach usage reported opposite by benchmark_throughput

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running benchmark_throughput.py on a platform with TD (VM protected by TDX) without GPU (no CUDA) I realized that benchmark_throughput.py reports: INFO 03-20 09:13:34 [metrics.py:481] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 4.1 tokens/s, Running: 4 reqs, Swapped: 0 reqs, Pending: 496 reqs, **GPU KV cache usage: 89.5%, CPU KV cache usage: 0.0%.**. It suggests that GPU KV cache is used (changing) instead of CPU KV cache, which is always 0.0% ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding cache;cuda;operator;sampling;triton build_error;nan_inf;slowdown env_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: GPU and CPU KV cach usage reported opposite by benchmark_throughput bug ### Your current environment ### 🐛 Describe the bug Running benchmark_throughput.py on a platform with TD (VM protected by TDX) without GPU...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: hroughput.py on a platform with TD (VM protected by TDX) without GPU (no CUDA) I realized that benchmark_throughput.py reports: INFO 03-20 09:13:34 [metrics.py:481] Avg prompt throughput: 0.0 tokens/s, Avg generation th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: upport;sampling_logits;speculative_decoding cache;cuda;operator;sampling;triton build_error;nan_inf;slowdown env_dependency Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 4.1 tokens/s, Running: 4 reqs, Swapped: 0 reqs, Pending: 496 reqs, **GPU KV cache usage: 89.5%, CPU KV cache usage: 0.0%.**. It suggests that GPU KV cache is used (changing) instead of CPU KV cache, which is always 0.0%...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
