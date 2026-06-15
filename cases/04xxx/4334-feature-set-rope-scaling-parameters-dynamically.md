# vllm-project/vllm#4334: [Feature]: Set RoPE scaling parameters dynamically

| 字段 | 值 |
| --- | --- |
| Issue | [#4334](https://github.com/vllm-project/vllm/issues/4334) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Set RoPE scaling parameters dynamically

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As it was implemented in #555, specifying RoPE parameters is only available from the model's `config.json`, and I haven't found a way to set it dynamically in my code. Is there currently a way of doing this? Related to #910. ### Alternatives Right now, unless providing a modified `config.json` (which is very inconvenient in my setup), I haven't found an alternative. I've tried monkey patching `vllm.transformers_utils.config.get_config` function to no avail (Ray uses it in a way I don't understand). ### Additional context For context - specific to my setup - I'm using 2 GPUs to run a quantized Llama-3-70B (casperhansen's). Thus vLLM is using Ray.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: plemented in #555, specifying RoPE parameters is only available from the model's `config.json`, and I haven't found a way to set it dynamically in my code. Is there currently a way of doing this? Related to #910. ### Al...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: # 🚀 The feature, motivation and pitch As it was implemented in #555, specifying RoPE parameters is only available from the model's `config.json`, and I haven't found a way to set it dynamically in my code. Is there curr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: context For context - specific to my setup - I'm using 2 GPUs to run a quantized Llama-3-70B (casperhansen's). Thus vLLM is using Ray.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Set RoPE scaling parameters dynamically feature request ### 🚀 The feature, motivation and pitch As it was implemented in #555, specifying RoPE parameters is only available from the model's `config.json`, and...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
