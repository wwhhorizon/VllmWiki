# vllm-project/vllm#13005: [Feature]: Chat Prefix Completion

| 字段 | 值 |
| --- | --- |
| Issue | [#13005](https://github.com/vllm-project/vllm/issues/13005) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Chat Prefix Completion

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The chat prefix completion follows the Chat Completion API, where users provide an assistant's prefix message for the model to complete the rest of the message. This allows the user to manually specify the prefix returned by assistant, which is very helpful for existing reasoning models (Deepseek R1's response should start with ) or code generation(response start with ```python). Another very useful feature is to allow the model to continue outputting after the model output stops due to length ### Alternatives Here are the providers I know of that offer this functionality: 1. [DeepSeek](https://api-docs.deepseek.com/guides/chat_prefix_completion) Chat Prefix Completion 2. [Aliyun Dashscope](https://help.aliyun.com/zh/model-studio/user-guide/partial-mode) Partial mode 3. [siliconflow](https://docs.siliconflow.cn/guides/prefix) prefix 4. [Mistral AI](https://docs.mistral.ai/guides/prefix/) Different providers have different parameter formats, for me I prefer the deepseek and mistral formats, here's an example from deepseek. ```python from openai import OpenAI client = OpenAI( api_key=" ", base_url="https://api.deepseek.com/beta", ) messages =...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: to complete the rest of the message. This allows the user to manually specify the prefix returned by assistant, which is very helpful for existing reasoning models (Deepseek R1's response should start with ) or code gen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ompletion API, where users provide an assistant's prefix message for the model to complete the rest of the message. This allows the user to manually specify the prefix returned by assistant, which is very helpful for ex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ld we implement this feature only in the frontend, similar to the beam search that was removed from the engine earlier. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Chat Prefix Completion feature request ### 🚀 The feature, motivation and pitch The chat prefix completion follows the Chat Completion API, where users provide an assistant's prefix message for the model to co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
