# vllm-project/vllm#23491: [Feature]: Add support for `seed_oss` tool-call parser in official vLLM image

| 字段 | 值 |
| --- | --- |
| Issue | [#23491](https://github.com/vllm-project/vllm/issues/23491) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add support for `seed_oss` tool-call parser in official vLLM image

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Seed-OSS-36B-Instruct provides tool-calling but requires a custom parser (`seed_oss`). The official vLLM Docker image does not include it, so starting with --enable-auto-tool-choice --tool-call-parser=seed_oss throws “Invalid tool call parser”. Please add native support for `seed_oss` in vLLM and bundle it into the official Docker image, so users can deploy Seed-OSS directly without custom builds. ### Alternatives - Rebuild custom Docker images with patched vLLM/Transformers (works but adds maintenance cost). - Patch containers at runtime (fragile and user-unfriendly). - Remove tool-calling (not acceptable for most use cases). ### Additional context I am running Seed-OSS-36B-Instruct in production with vLLM. Tool-calling works only if I maintain a patched image. Official support for `seed_oss` would simplify deployment and benefit the broader community. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Feature]: Add support for `seed_oss` tool-call parser in official vLLM image feature request;stale ### 🚀 The feature, motivation and pitch Seed-OSS-36B-Instruct provides tool-calling but requires a custom parser (`seed...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: d support for `seed_oss` tool-call parser in official vLLM image feature request;stale ### 🚀 The feature, motivation and pitch Seed-OSS-36B-Instruct provides tool-calling but requires a custom parser (`seed_oss`). The o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ty. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
