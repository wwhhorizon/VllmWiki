# vllm-project/vllm#17123: [Feature]: Automatically detect numerical issues

| 字段 | 值 |
| --- | --- |
| Issue | [#17123](https://github.com/vllm-project/vllm/issues/17123) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Automatically detect numerical issues

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Models such as Gemma-3 and GLM-4 may encounter numerical instability when `float16` dtype is used. Despite a warning message `Casting bfloat16 to float16` being printed, users can still get confused when the model returns empty or nonsense outputs. Examples: - https://github.com/vllm-project/vllm/issues/16489 - https://github.com/vllm-project/vllm/pull/16618#issuecomment-2814399522 It would be great if we could automatically detect numerical issues while running the model. We should at least check for this during startup. Inference-time checking should be optional since it harms the performance. ### Alternatives Hardcode specific models to not allow them to be run in float16, like `plamo2`: https://github.com/vllm-project/vllm/blob/4115f19958d8b3628606d78355c277b328f011e1/vllm/config.py#L2834 However, this has to be done manually. ### Additional context cc @youkaichao ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: dels such as Gemma-3 and GLM-4 may encounter numerical instability when `float16` dtype is used. Despite a warning message `Casting bfloat16 to float16` being printed, users can still get confused when the model returns...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: al issues feature request;stale ### 🚀 The feature, motivation and pitch Models such as Gemma-3 and GLM-4 may encounter numerical instability when `float16` dtype is used. Despite a warning message `Casting bfloat16 to f...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Feature]: Automatically detect numerical issues feature request;stale ### 🚀 The feature, motivation and pitch Models such as Gemma-3 and GLM-4 may encounter numerical instability when `float16` dtype is used. Despite a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Automatically detect numerical issues feature request;stale ### 🚀 The feature, motivation and pitch Models such as Gemma-3 and GLM-4 may encounter numerical instability when `float16` dtype is used. Despite a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: optional since it harms the performance. ### Alternatives Hardcode specific models to not allow them to be run in float16, like `plamo2`: https://github.com/vllm-project/vllm/blob/4115f19958d8b3628606d78355c277b328f011e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
