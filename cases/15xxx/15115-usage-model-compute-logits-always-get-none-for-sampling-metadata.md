# vllm-project/vllm#15115: [Usage]: Model `compute_logits` always get None for `sampling_metadata`

| 字段 | 值 |
| --- | --- |
| Issue | [#15115](https://github.com/vllm-project/vllm/issues/15115) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Model `compute_logits` always get None for `sampling_metadata`

### Issue 正文摘录

### Your current environment ```text vllm 0.7.3 transformers 4.49.0 ``` ### How would you like to use vllm I'm writing a custom multi-modal model. The model does some special logits computes when prefill stage. I'm trying to use the `sampling_metadata` info to detect this. It works in v0, but in v1 engine, the model always get None for `sampling_metadata` arg. How to detect prefill stage correctly? Example code in v0: ```python class CustomModel(nn.Module, SupportsMultiModal): ... def compute_logits(self, hidden_states: torch.Tensor, sampling_metadata: SamplingMetadata): logits = self.language_model.compute_logits(hidden_states, sampling_metadata) if any(x.seq_len is not None for x in sampling_metadata.seq_groups): # do something for prefill stage ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tly? Example code in v0: ```python class CustomModel(nn.Module, SupportsMultiModal): ... def compute_logits(self, hidden_states: torch.Tensor, sampling_metadata: SamplingMetadata): logits = self.language_model.compute_l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Model `compute_logits` always get None for `sampling_metadata` usage;stale ### Your current environment ```text vllm 0.7.3 transformers 4.49.0 ``` ### How would you like to use vllm I'm writing a custom multi-m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e]: Model `compute_logits` always get None for `sampling_metadata` usage;stale ### Your current environment ```text vllm 0.7.3 transformers 4.49.0 ``` ### How would you like to use vllm I'm writing a custom multi-modal...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: use vllm I'm writing a custom multi-modal model. The model does some special logits computes when prefill stage. I'm trying to use the `sampling_metadata` info to detect this. It works in v0, but in v1 engine, the model...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Usage]: Model `compute_logits` always get None for `sampling_metadata` usage;stale ### Your current environment ```text vllm 0.7.3 transformers 4.49.0 ``` ### How would you like to use vllm I'm writing a custom multi-m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
