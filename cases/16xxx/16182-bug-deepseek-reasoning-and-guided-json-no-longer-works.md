# vllm-project/vllm#16182: [Bug]: Deepseek reasoning and guided_json no longer works

| 字段 | 值 |
| --- | --- |
| Issue | [#16182](https://github.com/vllm-project/vllm/issues/16182) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Deepseek reasoning and guided_json no longer works

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using the exact same example of Reasoning with Structured Outputs from the vLLM docs: https://docs.vllm.ai/en/v0.8.1/features/reasoning_outputs.html#structured-output I expect to see both reasoning and content. Something like this: ``` reasoning_content: "Hmm, let me think for a bit... Wait, let me think a bit more..." content: {"name": "Ethan", "age": 28} ``` Instead I get: ``` reasoning_content: {"name": "Ethan", "age": 28} content: None ``` (I also tried guided_grammar, although it's not documented as supported with reasoning in the top of the same page. With that case, it worked, but was [unbearably slow](https://github.com/vllm-project/vllm/issues/12122#issuecomment-2782941708), 100% of one CPU, and didn't utilise the GPU. Hence I'm trying guided_json, which is very fast, but doesn't work, as above.) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e.) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
