# vllm-project/vllm#15188: [Bug]: Extra Characters in `content` When Using `enable_reasoning` with `stop` Parameter

| 字段 | 值 |
| --- | --- |
| Issue | [#15188](https://github.com/vllm-project/vllm/issues/15188) |
| 状态 | closed |
| 标签 | bug;structured-output;stale;tool-calling |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Extra Characters in `content` When Using `enable_reasoning` with `stop` Parameter

### Issue 正文摘录

![Image](https://github.com/user-attachments/assets/59d64b2b-986e-46e1-8ff1-d66588bd431e) ### Your current environment #### Environment - vLLM version: 0.7.3 - Model: DeepSeek R1 - Running on: H20 ### 🐛 Describe the bug #### Description When running the **DeepSeek R1** model with the `vllm` framework and enabling the `enable_reasoning` parameter, the model’s response is structured into two fields: - **`reasoning_content`**: Represents the reasoning process. - **`content`**: Represents the final output. However, when specifying the `stop` parameter with any stop sequence, the `content` field in the response contains extra unintended characters. This issue does not occur when `enable_reasoning` is disabled. #### Steps to Reproduce 1. Start `vllm` with `--enable-reasoning`. 2. Query the model with a `stop` parameter (e.g., `stop=["\nObservation"]`). 3. Observe that the `content` field includes additional characters beyond the expected stop sequence. #### Expected Behavior - The `content` field should properly respect the `stop` parameter without introducing unintended characters. #### Actual Behavior - The `content` field contains unexpected extra characters when `enable_reasoning` i...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 1-d66588bd431e) ### Your current environment #### Environment - vLLM version: 0.7.3 - Model: DeepSeek R1 - Running on: H20 ### 🐛 Describe the bug #### Description When running the **DeepSeek R1** model with the `vllm` f...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: sue does not occur when `enable_reasoning` is disabled. #### Steps to Reproduce 1. Start `vllm` with `--enable-reasoning`. 2. Query the model with a `stop` parameter (e.g., `stop=["\nObservation"]`). 3. Observe that the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # Your current environment #### Environment - vLLM version: 0.7.3 - Model: DeepSeek R1 - Running on: H20 ### 🐛 Describe the bug #### Description When running the **DeepSeek R1** model with the `vllm` framework and enabl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: hen Using `enable_reasoning` with `stop` Parameter bug;structured-output;stale;tool-calling ![Image](https://github.com/user-attachments/assets/59d64b2b-986e-46e1-8ff1-d66588bd431e) ### Your current environment #### Env...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
