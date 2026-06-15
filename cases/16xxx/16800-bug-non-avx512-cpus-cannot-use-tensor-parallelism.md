# vllm-project/vllm#16800: [Bug]: Non-avx512 CPUs cannot use tensor parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#16800](https://github.com/vllm-project/vllm/issues/16800) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Non-avx512 CPUs cannot use tensor parallelism

### Issue 正文摘录

### 🐛 Describe the bug init_shm_manager is not implemented when NOT AVX512_FOUND, which makes it impossible to use tensor parallel on non-avx512 CPUs Cause #15934 vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-7B -tp=2 --distributed-executor-backend mp On CPUs without avx512 support or AVX512_DISABLED ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Non-avx512 CPUs cannot use tensor parallelism bug ### 🐛 Describe the bug init_shm_manager is not implemented when NOT AVX512_FOUND, which makes it impossible to use tensor parallel on non-avx512 CPUs Cause #15934...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rve deepseek-ai/DeepSeek-R1-Distill-Qwen-7B -tp=2 --distributed-executor-backend mp On CPUs without avx512 support or AVX512_DISABLED ### Before submitting a new issue... - [x] Make sure you already searched for relevan...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: on-avx512 CPUs Cause #15934 vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-7B -tp=2 --distributed-executor-backend mp On CPUs without avx512 support or AVX512_DISABLED ### Before submitting a new issue... - [x] Make su...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
