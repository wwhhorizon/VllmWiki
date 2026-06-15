# vllm-project/vllm#29762: [Bug]: MemoryError throw by transformers_utils.utils module's parse_safetensors_file_metadata function when loading some gptq or awq quantization models since vllm 0.11.1

| 字段 | 值 |
| --- | --- |
| Issue | [#29762](https://github.com/vllm-project/vllm/issues/29762) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MemoryError throw by transformers_utils.utils module's parse_safetensors_file_metadata function when loading some gptq or awq quantization models since vllm 0.11.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm transformers utils' parse_safetensors_file_metadata function throws MemoryError when vllm serve awq models with model weights on local (e.g. offical qwen3-32b awq weights) since vllm 0.11.1. since vllm 0.11.1, awq_marlin.py added a function maybe_update_config, and get_safetensors_params_metadata -> parse_safetensors_file_metadata -> json.loads caused MemoryError no such issue on same machine and same startup command with vllm 0.11.0. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ensors_file_metadata function when loading some gptq or awq quantization models since vllm 0.11.1 bug;unstale ### Your current environment ### 🐛 Describe the bug vllm transformers utils' parse_safetensors_file_metadata...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: s parse_safetensors_file_metadata function when loading some gptq or awq quantization models since vllm 0.11.1 bug;unstale ### Your current environment ### 🐛 Describe the bug vllm transformers utils' parse_safetensors_f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .0. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: yError throw by transformers_utils.utils module's parse_safetensors_file_metadata function when loading some gptq or awq quantization models since vllm 0.11.1 bug;unstale ### Your current environment ### 🐛 Describe the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: hen loading some gptq or awq quantization models since vllm 0.11.1 bug;unstale ### Your current environment ### 🐛 Describe the bug vllm transformers utils' parse_safetensors_file_metadata function throws MemoryError whe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
