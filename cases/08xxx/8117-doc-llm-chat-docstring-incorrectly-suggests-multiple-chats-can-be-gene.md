# vllm-project/vllm#8117: [Doc]: `LLM.chat()` docstring incorrectly suggests multiple chats can be generated in one call

| 字段 | 值 |
| --- | --- |
| Issue | [#8117](https://github.com/vllm-project/vllm/issues/8117) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: `LLM.chat()` docstring incorrectly suggests multiple chats can be generated in one call

### Issue 正文摘录

### 📚 The doc issue According to the docstring for the LLM class's `chat()` method, > **messages** – A list of messages to generate responses for. Each message is a list of dictionaries with ‘role’ and ‘content’ keys. This implies `messages` can be a list containing multiple lists, each of which is one chat conversation with the dictionaries for role and content. However, that's not the case: `messages` must be a list of dictionaries, not a list of lists of dictionaries, because only one conversation is supported. See this example: https://github.com/vllm-project/vllm/issues/6416#issuecomment-2318413123 ### Suggest a potential alternative/fix Two options: 1. The docstring is edited to say "A list of messages to generate responses for. Each message is a dictionary with ‘role’ and ‘content’ keys." Under Returns, say something like "A list containing one RequestOutput object with the generated response." 2. Make the function actually do what the docstring says. If you have multiple conversations you want responses to, doing them in a batch is much more efficient than doing them one at a time by repeatedly calling `chat()`. In my application, I need 12,000 chat responses, and calling...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: versations you want responses to, doing them in a batch is much more efficient than doing them one at a time by repeatedly calling `chat()`. In my application, I need 12,000 chat responses, and calling `chat()` 12,000 t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: wo. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ontent’ keys." Under Returns, say something like "A list containing one RequestOutput object with the generated response." 2. Make the function actually do what the docstring says. If you have multiple conversations you...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
