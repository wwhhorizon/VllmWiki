# vllm-project/vllm#16545: [Bug]: Unexpected behavior of `returned_token_ids` in Reward Modeling for LlamaForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#16545](https://github.com/vllm-project/vllm/issues/16545) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unexpected behavior of `returned_token_ids` in Reward Modeling for LlamaForCausalLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The [reward modeling documentation](https://docs.vllm.ai/en/latest/models/supported_models.html#reward-modeling-task-reward) provides the following example for using `LlamaForCausalLM` with `--task reward`: > For process-supervised reward models such as peiyi9979/math-shepherd-mistral-7b-prm, the pooling config should be set explicitly, e.g.: --override-pooler-config '{"pooling_type": "STEP", "step_tag_id": 123, "returned_token_ids": [456, 789]}'. However, the usage of `returned_token_ids` leads to unexpected behavior. Specifically, `returned_token_ids` is used to index into `hidden_states`, which are the intermediate representations before the final layer (4096 dimensions in Llama), **not the logits**. Using vocabulary token IDs `returned_token_ids` to select from these intermediate feature vectors doesn’t make sense. https://github.com/vllm-project/vllm/blob/6c11ecf8d337d3b89e891588c81640a0bd30f6e1/vllm/model_executor/layers/pooler.py#L192-L193 For example, setting a large number (e.g., greater than 4096) in `returned_token_ids` results in an error. When using `LlamaForCausalLM` for reward modeling with the current version of t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 9979/math-shepherd-mistral-7b-prm, the pooling config should be set explicitly, e.g.: --override-pooler-config '{"pooling_type": "STEP", "step_tag_id": 123, "returned_token_ids": [456, 789]}'. However, the usage of `ret...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Unexpected behavior of `returned_token_ids` in Reward Modeling for LlamaForCausalLM bug;stale ### Your current environment ### 🐛 Describe the bug The [reward modeling documentation](https://docs.vllm.ai/en/latest...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: vior of `returned_token_ids` in Reward Modeling for LlamaForCausalLM bug;stale ### Your current environment ### 🐛 Describe the bug The [reward modeling documentation](https://docs.vllm.ai/en/latest/models/supported_mode...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: e the bug The [reward modeling documentation](https://docs.vllm.ai/en/latest/models/supported_models.html#reward-modeling-task-reward) provides the following example for using `LlamaForCausalLM` with `--task reward`: >...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
