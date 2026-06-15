# vllm-project/vllm#22152: [Bug]: An error occurred when using Eagle3 to load the Qwen3 series.

| 字段 | 值 |
| --- | --- |
| Issue | [#22152](https://github.com/vllm-project/vllm/issues/22152) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: An error occurred when using Eagle3 to load the Qwen3 series.

### Issue 正文摘录

### Your current environment 4 X 4090 ### 🐛 Describe the bug The official Eagle3 project has already released weights for the Qwen3 series, so why can't they be loaded in vLLM? Value error, Eagle3 is only supported for Llama models. Got self.target_model_config.hf_text_config.model_type='qwen3' [type=value_error, input_value=ArgsKwargs((), {'method':...able_log_stats': False}), input_type=ArgsKwargs] ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: An error occurred when using Eagle3 to load the Qwen3 series. bug;stale ### Your current environment 4 X 4090 ### 🐛 Describe the bug The official Eagle3 project has already released weights for the Qwen3 series,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ### Your current environment 4 X 4090 ### 🐛 Describe the bug The official Eagle3 project has already released weights for the Qwen3 series, so why can't they be loaded in vLLM? Value error, Eagle3 is only supported for...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: gs] ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: =value_error, input_value=ArgsKwargs((), {'method':...able_log_stats': False}), input_type=ArgsKwargs] ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: An error occurred when using Eagle3 to load the Qwen3 series. bug;stale ### Your current environment 4 X 4090 ### 🐛 Describe the bug The official Eagle3 project has already released weights for the Qwen3 series,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
