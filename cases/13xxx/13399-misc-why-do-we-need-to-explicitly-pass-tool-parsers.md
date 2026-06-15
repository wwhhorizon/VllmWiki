# vllm-project/vllm#13399: [Misc]: Why do we need to explicitly pass tool parsers?

| 字段 | 值 |
| --- | --- |
| Issue | [#13399](https://github.com/vllm-project/vllm/issues/13399) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Why do we need to explicitly pass tool parsers?

### Issue 正文摘录

### Anything you want to discuss about vllm. I was wondering why we need to explicitly pass tool parser as argument while loading models using vllm serve I understand that the response format can be dependent on the model (like and [TOOL] for llama and mistral) But I was taking a look at [Huggingface TGI](https://github.com/huggingface/text-generation-inference/) and they don't seem to have/need anything like that. So would it be possible to have a default parser which looks for json-esque tokens when auto tool choice is enabled but no parser is passed? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ing why we need to explicitly pass tool parser as argument while loading models using vllm serve I understand that the response format can be dependent on the model (like and [TOOL] for llama and mistral) But I was taki...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Misc]: Why do we need to explicitly pass tool parsers? stale ### Anything you want to discuss about vllm. I was wondering why we need to explicitly pass tool parser as argument while loading models using vllm serve I u...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: Why do we need to explicitly pass tool parsers? stale ### Anything you want to discuss about vllm. I was wondering why we need to explicitly pass tool parser as argument while loading models using vllm serve I u...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
