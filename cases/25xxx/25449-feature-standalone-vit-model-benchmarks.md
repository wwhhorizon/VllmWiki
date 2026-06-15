# vllm-project/vllm#25449: [Feature]: Standalone ViT model benchmarks

| 字段 | 值 |
| --- | --- |
| Issue | [#25449](https://github.com/vllm-project/vllm/issues/25449) |
| 状态 | closed |
| 标签 | feature request;multi-modality |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Standalone ViT model benchmarks

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This is a followup post from our biweekly meeting today. Currently vLLM only support E2E benchmarks. For multimodal workloads, results can have very high variance due to dependency on network (i.e. media download) as well as CPU-intensive preprocessing. As a result, E2E benchmarks are unreliable for multimodal optimizations. Since recently there have been many efforts into optimizing ViT, we will need a standalone ViT benchmark where it loads a given model's vision encoder with dummy weights, and runs forward passes with different fake inputs. Automatic input size sweep can be very useful as well. cc. @ywang96 @wwl2755 @DarkLight1337 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Standalone ViT model benchmarks feature request;multi-modality ### 🚀 The feature, motivation and pitch This is a followup post from our biweekly meeting today. Currently vLLM only support E2E benchmarks. For...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Standalone ViT model benchmarks feature request;multi-modality ### 🚀 The feature, motivation and pitch This is a followup post from our biweekly meeting today. Currently vLLM only support E2E benchmarks. For...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ks. For multimodal workloads, results can have very high variance due to dependency on network (i.e. media download) as well as CPU-intensive preprocessing. As a result, E2E benchmarks are unreliable for multimodal opti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Standalone ViT model benchmarks feature request;multi-modality ### 🚀 The feature, motivation and pitch This is a followup post from our biweekly meeting today. Currently vLLM only support E2E benchmarks. For...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
