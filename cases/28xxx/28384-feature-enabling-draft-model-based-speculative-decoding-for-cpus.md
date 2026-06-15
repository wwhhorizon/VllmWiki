# vllm-project/vllm#28384: [Feature]:  Enabling draft model based speculative decoding for CPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#28384](https://github.com/vllm-project/vllm/issues/28384) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:  Enabling draft model based speculative decoding for CPUs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Current Implementation Status This [branch](https://github.com/zihaoanllm/vllm/tree/model/integrate-pard-0521) is the PARD implementation of Speculative decoding for V0. However, this was done a few months ago and is unsupported with V1. With V1, speculative decoding with vLLM does not have draft model support. It raises the following error. ```NotImplementedError: Draft model speculative decoding is not supported yet. Please consider using other speculative decoding methods such as ngram, medusa, eagle, or mtp.``` Other speculative decoding methods such as eagle, ngram etc also raise the following assertion when run on CPU. ```AssertionError: spec decode is not supported.``` [PermaLink](https://github.com/vllm-project/vllm/blob/11fd69dd54060a59c6f62a6d217e1ecc47d74a68/vllm/v1/worker/cpu_model_runner.py#L27) I found a [PR](https://github.com/vllm-project/vllm/pull/24322) that has been created to add draft model support. But there is no mention of support for CPUs. ### Feature Request Enabling draft model based speculative decoding for CPUs ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new iss...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Feature]: Enabling draft model based speculative decoding for CPUs feature request;stale ### 🚀 The feature, motivation and pitch ### Current Implementation Status This [branch](https://github.com/zihaoanllm/vllm/tree/m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: en run on CPU. ```AssertionError: spec decode is not supported.``` [PermaLink](https://github.com/vllm-project/vllm/blob/11fd69dd54060a59c6f62a6d217e1ecc47d74a68/vllm/v1/worker/cpu_model_runner.py#L27) I found a [PR](ht...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Enabling draft model based speculative decoding for CPUs feature request;stale ### 🚀 The feature, motivation and pitch ### Current Implementation Status This [branch](https://github.com/zihaoanllm/vllm/tree/m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
