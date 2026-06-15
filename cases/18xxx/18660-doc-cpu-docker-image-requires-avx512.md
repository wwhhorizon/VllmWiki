# vllm-project/vllm#18660: [Doc]: CPU Docker Image Requires AVX512

| 字段 | 值 |
| --- | --- |
| Issue | [#18660](https://github.com/vllm-project/vllm/issues/18660) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: CPU Docker Image Requires AVX512

### Issue 正文摘录

### 📚 The doc issue I'm finding a way to run vLLM on CPU without compilation. Following the documentation at https://docs.vllm.ai/en/stable/getting_started/installation/cpu.html#troubleshooting, I used the Docker image `public.ecr.aws/q9t5s3a7/vllm-cpu-release-repo:v0.8.5.post1`. However, when running vLLM directly, it throws a SIGILL error. After debugging with GDB, I confirmed there's a AVX512 instruction `vinserti64x4`. But documentation only mentions "AVX512 (optional, recommended)", the ​​Docker image appears to **enforce this requirement**—a critical detail not mentioned anywhere.. ### Suggest a potential alternative/fix - Adding a clear note here (e.g., "This Docker image requires AVX512") - Or providing an additional image without AVX512 requirement, for example https://github.com/vllm-project/vllm/pull/5452 . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Doc]: CPU Docker Image Requires AVX512 documentation;stale ### 📚 The doc issue I'm finding a way to run vLLM on CPU without compilation. Following the documentation at https://docs.vllm.ai/en/stable/getting_started/ins...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 2 . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: CPU Docker Image Requires AVX512 documentation;stale ### 📚 The doc issue I'm finding a way to run vLLM on CPU without compilation. Following the documentation at https://docs.vllm.ai/en/stable/getting_started/ins...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
