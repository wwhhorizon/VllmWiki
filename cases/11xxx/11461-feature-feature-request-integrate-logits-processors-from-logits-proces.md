# vllm-project/vllm#11461: [Feature]: ✨ Feature Request: Integrate Logits Processors from logits-processor-zoo into vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#11461](https://github.com/vllm-project/vllm/issues/11461) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: ✨ Feature Request: Integrate Logits Processors from logits-processor-zoo into vLLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch # Feature Request: Integrate Logits Processors from logits-processor-zoo into vLLM ## Description I am writing to request the integration of several advanced logits processors from the [logits-processor-zoo](https://github.com/NVIDIA/logits-processor-zoo) into the vLLM framework. These processors provide enhanced control over the text generation process, enabling more sophisticated and context-aware outputs. ## Proposed Logits Processors for Integration 1. **GenLengthLogitsProcessor** - **Purpose:** Adjusts the likelihood of the end-of-sequence (EOS) token based on the generated sequence length, encouraging or discouraging shorter or longer responses. - **Use Cases:** Controlling response length in chatbots, ensuring concise or detailed answers as needed. 2. **MultipleChoiceLogitsProcessor** - **Purpose:** Guides the model to select from predefined multiple-choice options by boosting the logits of the specified choices. - **Use Cases:** Implementing multiple-choice questions, surveys, or structured decision-making processes within generated text. 3. **CiteFromPromptLogitsProcessor** - **Purpose:** Boosts or diminishes the likelihood of token...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: - **Use Cases:** Controlling response length in chatbots, ensuring concise or detailed answers as needed. 2. **MultipleChoiceLogitsProcessor** - **Purpose:** Guides the model to select from predefined multiple-choice op...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: eded. 2. **MultipleChoiceLogitsProcessor** - **Purpose:** Guides the model to select from predefined multiple-choice options by boosting the logits of the specified choices. - **Use Cases:** Implementing multiple-choice...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: ✨ Feature Request: Integrate Logits Processors from logits-processor-zoo into vLLM feature request ### 🚀 The feature, motivation and pitch # Feature Request: Integrate Logits Processors from logits-processor-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ns: ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
