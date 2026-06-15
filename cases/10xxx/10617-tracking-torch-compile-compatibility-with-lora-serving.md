# vllm-project/vllm#10617: tracking torch.compile compatibility with lora serving

| 字段 | 值 |
| --- | --- |
| Issue | [#10617](https://github.com/vllm-project/vllm/issues/10617) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> tracking torch.compile compatibility with lora serving

### Issue 正文摘录

### Your current environment N/A ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using `torch.compile` with lora with fail, because vLLM's support for multi-lora (punica kernel) is very complicated. The punica wrapper defined in https://github.com/vllm-project/vllm/blob/571841b7fcc67f8b1d171522f6249ed4224033e1/vllm/lora/punica.py#L179 is very similar to attention ops. If we want to support `torch.compile` for it, we need to do something similar to https://github.com/vllm-project/vllm/pull/10558 , i.e. hiding the whole punica operation from `torch.compile` . The difference is, attention ops have quite uniform signature, and we only need to register it once; while punica ops have several signatures, and are applied to various layers, including linear / embedding etc. Even if we wrap all ops into pytorch custom ops for `torch.compile`, there's not much left for `torch.compile` to accelerate. Therefore, I tend to leave lora as-is, and just ignore `torch.compile` for it. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/late...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tracking torch.compile compatibility with lora serving bug;stale ### Your current environment N/A ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using `torch.compile` with lora with fail, because vLLM's supp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: it. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ility with lora serving bug;stale ### Your current environment N/A ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using `torch.compile` with lora with fail, because vLLM's support for multi-lora (punica kern...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tracking torch.compile compatibility with lora serving bug;stale ### Your current environment N/A ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using `torch.compile` with lora with fail, because vLLM's supp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
