# vllm-project/vllm#12548: [Bug]: Distilled DeepSeek Models do not work with guided_json

| 字段 | 值 |
| --- | --- |
| Issue | [#12548](https://github.com/vllm-project/vllm/issues/12548) |
| 状态 | closed |
| 标签 | bug;structured-output;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Distilled DeepSeek Models do not work with guided_json

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using **DeepSeek distilled models** with **guided JSON output**, the response does not always adhere to the expected schema. Unlike the standard versions of the models (e.g., Llama 3), which complete the JSON properly within a given `max_tokens` limit, the distilled models often fail to do so. For example, when setting `max_tokens = x`, **Llama 3** correctly generates a full JSON response. However, with **DeepSeek's distilled versions**, the output is sometimes **incomplete**, often stopping at an **open bracket (`{`)** or other partial structures. This suggests that the distilled models may require a **higher `max_tokens` setting** than their non-distilled counterparts to function correctly. ## 🔍 Expected Behavior - The model should generate a **complete JSON response** within the specified `max_tokens` limit, just like other models do. ## ❌ Actual Behavior - The response is often **truncated**, failing to complete the JSON structure. - In some cases, only an **opening bracket (`{`)** is returned, with no further content. ## 🛠 Steps to Reproduce 1. Use any **DeepSeek distilled model**. 2....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ponse does not always adhere to the expected schema. Unlike the standard versions of the models (e.g., Llama 3), which complete the JSON properly within a given `max_tokens` limit, the distilled models often fail to do...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Distilled DeepSeek Models do not work with guided_json bug;structured-output;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using **DeepSeek distilled models**...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: g bracket (`{`)** is returned, with no further content. ## 🛠 Steps to Reproduce 1. Use any **DeepSeek distilled model**. 2. Set up a **guided JSON schema** for structured output. 3. Set `max_tokens` to a reasonable valu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ! 🙌 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: illed DeepSeek Models do not work with guided_json bug;structured-output;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using **DeepSeek distilled models** with **guid...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
