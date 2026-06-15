# vllm-project/vllm#10790: [Feature]: Access draft model directly

| 字段 | 值 |
| --- | --- |
| Issue | [#10790](https://github.com/vllm-project/vllm/issues/10790) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Access draft model directly

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently vLLM supports speculative decoding whereby a smaller model outputs speculative tokens for the main model to verify. Since both models are already loaded in VRAM, it would be helpful to be able to access the draft model directly and request inferencing from this bypassing the larger model (for cases where speed is more important than quality). If both models are exposed, then the incoming request can specify which model to use and vLLM can direct to the correct one. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Access draft model directly feature request;stale ### 🚀 The feature, motivation and pitch Currently vLLM supports speculative decoding whereby a smaller model outputs speculative tokens for the main model to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: helpful to be able to access the draft model directly and request inferencing from this bypassing the larger model (for cases where speed is more important than quality). If both models are exposed, then the incoming re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: vation and pitch Currently vLLM supports speculative decoding whereby a smaller model outputs speculative tokens for the main model to verify. Since both models are already loaded in VRAM, it would be helpful to be able...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Access draft model directly feature request;stale ### 🚀 The feature, motivation and pitch Currently vLLM supports speculative decoding whereby a smaller model outputs speculative tokens for the main model to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
