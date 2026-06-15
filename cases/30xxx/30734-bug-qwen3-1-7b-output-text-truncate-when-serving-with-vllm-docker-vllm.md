# vllm-project/vllm#30734: [Bug]: qwen3-1.7b output text truncate when serving with vllm docker。在默认参数下，vllm推理结果异常截断

| 字段 | 值 |
| --- | --- |
| Issue | [#30734](https://github.com/vllm-project/vllm/issues/30734) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen3-1.7b output text truncate when serving with vllm docker。在默认参数下，vllm推理结果异常截断

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug output by vllm api: while infer with huggingface transformers, result in: '“张岱的《湖心亭看雪》”中，“大雪三日”后面一句是：\n\n**“天与云与山与水，上下一白。”**\n\n这句话出自张岱的《湖心亭看雪》，原文如下：\n\n> **“余强饮三大白醉，间从秦氏口授童子文。中圣天竺国，见大雪三日，天与云与山与水，上下一白。”**\n\n完整句子是：\n\n> **“天与云与山与水，上下一白。”**\n\n这是描写雪景非常传神的一句，表达了作者在雪夜赏雪的孤寂与清冷，同时也体现了文人的闲适心境。' vllm api only return the first few words “张岱的《湖心亭看雪》”中，“大雪”， are there any params to set？or something went wrong? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen3-1.7b output text truncate when serving with vllm docker。在默认参数下，vllm推理结果异常截断 bug ### Your current environment ### 🐛 Describe the bug output by vllm api: while infer with huggingface transformers, result in:
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: qwen3-1.7b output text truncate when serving with vllm docker。在默认参数下，vllm推理结果异常截断 bug ### Your current environment ### 🐛 Describe the bug output by vllm api: while infer with huggingface transformers, result in:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
