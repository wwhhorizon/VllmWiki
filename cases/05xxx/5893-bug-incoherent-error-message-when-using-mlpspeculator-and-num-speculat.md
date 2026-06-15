# vllm-project/vllm#5893: [Bug]: Incoherent error message when using MLPSpeculator and `num_speculative_tokens` is set too high

| 字段 | 值 |
| --- | --- |
| Issue | [#5893](https://github.com/vllm-project/vllm/issues/5893) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Incoherent error message when using MLPSpeculator and `num_speculative_tokens` is set too high

### Issue 正文摘录

### Your current environment n/a ### 🐛 Describe the bug When using `MLPSpeculator` as the speculative model, each model has an upper-limit on how `num_speculative_tokens` can be set. This corresponds to the value of `n_predict` in the config of the speculative model. Currently, if the user tries to set `num_speculative_tokens` to a value higher than what is supported we get a confusing message. For example, if one uses `ibm-fms/llama-13b-accelerator` and sets `num_speculative_tokens=4` we will get the following message: ``` ValueError: Expected both speculative_model and num_speculative_tokens to be provided, but found speculative_model='ibm-fms/llama-13b-accelerator' and num_speculative_tokens=4. ``` This model supports a maximum of `num_speculative_tokesn=3` (e.g., see config [here](https://huggingface.co/ibm-fms/llama-13b-accelerator/blob/main/config.json#L10)). It would better if we explicitly tell the user to reduce the value of `num_speculative_tokens`.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: a ### 🐛 Describe the bug When using `MLPSpeculator` as the speculative model, each model has an upper-limit on how `num_speculative_tokens` can be set. This corresponds to the value of `n_predict` in the config of the s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: -13b-accelerator/blob/main/config.json#L10)). It would better if we explicitly tell the user to reduce the value of `num_speculative_tokens`.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Incoherent error message when using MLPSpeculator and `num_speculative_tokens` is set too high bug ### Your current environment n/a ### 🐛 Describe the bug When using `MLPSpeculator` as the speculative model, each...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
