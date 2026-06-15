# vllm-project/vllm#24805: [Feature]: More Frequently Updated Docker Images

| 字段 | 值 |
| --- | --- |
| Issue | [#24805](https://github.com/vllm-project/vllm/issues/24805) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: More Frequently Updated Docker Images

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Docker is one of the fastest and easiest ways to run vLLM. However, the currently provided [docker images](https://hub.docker.com/r/vllm/vllm-openai/tags) are very rarely updated. The most recent vllm/vllm-openai:latest is from 24 days ago. I believe these line up with full releases, however it would be helpful to have a more frequently updated one, especially as support for newer hardware is gradually getting better and better. And as new models are being released. Something like a `vllm/vllm-openai-prerelease` or a `vllm/vllm-openai-nightly` Could be automatically done with some build automation. Would save a lot of us significant time and effort recompiling everything locally to test new changes with docker. I hope you'll consider it, thank you! ### Alternatives Right now, rebuilding the images locally as changes are merged in, which usually takes several hours. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of freque...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Feature]: More Frequently Updated Docker Images feature request;stale ### 🚀 The feature, motivation and pitch Docker is one of the fastest and easiest ways to run vLLM. However, the currently provided [docker images](h...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: More Frequently Updated Docker Images feature request;stale ### 🚀 The feature, motivation and pitch Docker is one of the fastest and easiest ways to run vLLM. However, the currently provided [docker images](h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rt for newer hardware is gradually getting better and better. And as new models are being released. Something like a `vllm/vllm-openai-prerelease` or a `vllm/vllm-openai-nightly` Could be automatically done with some bu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: t;stale ### 🚀 The feature, motivation and pitch Docker is one of the fastest and easiest ways to run vLLM. However, the currently provided [docker images](https://hub.docker.com/r/vllm/vllm-openai/tags) are very rarely...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
