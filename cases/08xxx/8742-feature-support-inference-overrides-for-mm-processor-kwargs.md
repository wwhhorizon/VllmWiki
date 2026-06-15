# vllm-project/vllm#8742: [Feature]: Support Inference Overrides for mm_processor_kwargs

| 字段 | 值 |
| --- | --- |
| Issue | [#8742](https://github.com/vllm-project/vllm/issues/8742) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Inference Overrides for mm_processor_kwargs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Follow-up on https://github.com/vllm-project/vllm/pull/8657, which added support for passing initialization time `mm_processor_kwargs` to be used by the input mapper / processor / max token count calculations / dummy data if they're added to architecture-specific implementations as keyword arguments. It would be nice to also be to pass such kwargs as input values at inference time as part of the multi-modal data, e.g.,: ```python llm.generate({"multi_modal_data": {"image": {"data": image, "mm_processor_kwargs": image_kwargs}}}) ``` Such that for models that support additional `mm_processor_kwargs`: - [ ] The initialization time `mm_processor_kwargs` take priority over the config values - [ ] The inference time `mm_processor_kwargs` take priority over the config values and the initialization `mm_processor_kwargs` ### Alternatives Keep `mm_processor_kwargs` as initialization time only ### Additional context For per-request `mm_processor_kwargs`, it needs to be correctly handled: - In the input mapper - In the input processor Some care needs to be taken around the input mapper, which falls back to a wrapper around HF resources, e.g., image proc...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: data": image, "mm_processor_kwargs": image_kwargs}}}) ``` Such that for models that support additional `mm_processor_kwargs`: - [ ] The initialization time `mm_processor_kwargs` take priority over the config values - [...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: oken count calculations / dummy data if they're added to architecture-specific implementations as keyword arguments. It would be nice to also be to pass such kwargs as input values at inference time as part of the multi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rocessor / max token count calculations / dummy data if they're added to architecture-specific implementations as keyword arguments. It would be nice to also be to pass such kwargs as input values at inference time as p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support Inference Overrides for mm_processor_kwargs feature request ### 🚀 The feature, motivation and pitch Follow-up on https://github.com/vllm-project/vllm/pull/8657, which added support for passing initial...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
