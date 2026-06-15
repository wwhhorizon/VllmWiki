# vllm-project/vllm#32218: [RFC]: Consolidate Multimodal Related Info

| 字段 | 值 |
| --- | --- |
| Issue | [#32218](https://github.com/vllm-project/vllm/issues/32218) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Consolidate Multimodal Related Info

### Issue 正文摘录

### Background + Motivation We are introducing `model_arch_config` https://github.com/vllm-project/vllm/pull/28454, which defines explicitly what kind of information vLLM engine need from hugggingface config/ user-defined config, so we could avoid `hf_config`/`getattr(hf_config, xxx)` got passing around in engine. ### Previous Discussion For whether `model_arch_config` should contains multimodal related info, https://github.com/vllm-project/vllm/issues/24384#issuecomment-3489703720 suggested that we should put `supports_multimodal` into `model_arch_config` as it's something purely from model architecture, which we hope to get from standardized hugggingface config or user-defined config. https://github.com/vllm-project/vllm/pull/28454#issuecomment-3638695628 also suggested to bring more folks related to MM for discussion. The original plan would be: - delete `supports_multimodal` in model_info - in `model_arch_config_convertor`, call registry to check if a model is multimodal. See discussion in https://github.com/vllm-project/vllm/pull/28454#issuecomment-3638695628 - call `model_arch_config.is_multimodal_model` to know if a model is multimodal ### Current Questions One tricky case...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [RFC]: Consolidate Multimodal Related Info RFC;stale ### Background + Motivation We are introducing `model_arch_config` https://github.com/vllm-project/vllm/pull/28454, which defines explicitly what kind of information...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Consolidate Multimodal Related Info RFC;stale ### Background + Motivation We are introducing `model_arch_config` https://github.com/vllm-project/vllm/pull/28454, which defines explicitly what kind of information...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: timodal Related Info RFC;stale ### Background + Motivation We are introducing `model_arch_config` https://github.com/vllm-project/vllm/pull/28454, which defines explicitly what kind of information vLLM engine need from...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ted Info RFC;stale ### Background + Motivation We are introducing `model_arch_config` https://github.com/vllm-project/vllm/pull/28454, which defines explicitly what kind of information vLLM engine need from hugggingface...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
