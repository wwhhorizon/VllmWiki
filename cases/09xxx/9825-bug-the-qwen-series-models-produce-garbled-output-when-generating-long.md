# vllm-project/vllm#9825: [Bug]: The Qwen series models produce garbled output when generating long texts.

| 字段 | 值 |
| --- | --- |
| Issue | [#9825](https://github.com/vllm-project/vllm/issues/9825) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The Qwen series models produce garbled output when generating long texts.

### Issue 正文摘录

### Your current environment vLLM version: v0.6.3.post1 ### 🐛 Describe the bug In the latest version v0.6.3.post1, when generating long texts (for example, when the number of tokens reaches 21,000), the generated content is basically garbled. Additionally, after verifying, the long text functionality in v0.6.2 works correctly using the qwen2-7b-instruct model. Furthermore, I also tested other models like qwen2.5-72b-instruct, which exhibit the same problem. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: The Qwen series models produce garbled output when generating long texts. bug ### Your current environment vLLM version: v0.6.3.post1 ### 🐛 Describe the bug In the latest version v0.6.3.post1, when generating lon...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: utput when generating long texts. bug ### Your current environment vLLM version: v0.6.3.post1 ### 🐛 Describe the bug In the latest version v0.6.3.post1, when generating long texts (for example, when the number of tokens...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: em. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: nvironment vLLM version: v0.6.3.post1 ### 🐛 Describe the bug In the latest version v0.6.3.post1, when generating long texts (for example, when the number of tokens reaches 21,000), the generated content is basically gar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
