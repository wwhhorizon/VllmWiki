# vllm-project/vllm#27755: [RFC]: `reasoning_content` -> `reasoning`

| 字段 | 值 |
| --- | --- |
| Issue | [#27755](https://github.com/vllm-project/vllm/issues/27755) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: `reasoning_content` -> `reasoning`

### Issue 正文摘录

### Motivation. When GPT-OSS was released, OpenAI provided guidance that chain of thought content should be returned in the `reasoning` field of the response. They recommend this for Chat Completions API even though it does not officially support returning chain of thought in the official API. Since vLLM implements the OpenAI API, it makes sense to conform to their recommendations. Before https://github.com/vllm-project/vllm/pull/27752, vLLM used `reasoning_content` as this is what DeepSeek originally used. That PR makes the change from `reasoning_content` to `reasoning`, maintaining backwards compatibility. ### Proposed Change. Remove `reasoning_content` completely to avoid confusion. ### Feedback Period. 2 weeks ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: They recommend this for Chat Completions API even though it does not officially support returning chain of thought in the official API. Since vLLM implements the OpenAI API, it makes sense to conform to their recommenda...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [RFC]: `reasoning_content` -> `reasoning` RFC ### Motivation. When GPT-OSS was released, OpenAI provided guidance that chain of thought content should be returned in the `reasoning` field of the response. They recommend...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
