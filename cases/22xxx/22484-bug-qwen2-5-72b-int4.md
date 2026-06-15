# vllm-project/vllm#22484: [Bug]: 请问用同样的模型qwen2.5-72b-int4，在单卡和双卡上输出结果会不一样

| 字段 | 值 |
| --- | --- |
| Issue | [#22484](https://github.com/vllm-project/vllm/issues/22484) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 请问用同样的模型qwen2.5-72b-int4，在单卡和双卡上输出结果会不一样

### Issue 正文摘录

### Your current environment 主要是比较精细的输出，例如输出绘制Mermaid的代码。双卡上图表的数字有时是全角字符，但在单卡上运行基本正常。 vllm的版本是0.9.1 ### 🐛 Describe the bug ## ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: 请问用同样的模型qwen2.5-72b-int4，在单卡和双卡上输出结果会不一样 bug;stale ### Your current environment 主要是比较精细的输出，例如输出绘制Mermaid的代码。双卡上图表的数字有时是全角字符，但在单卡上运行基本正常。 vllm的版本是0.9.1 ### 🐛 Describe the bug ## ### Before submitting a new issue.....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ## ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: 请问用同样的模型qwen2.5-72b-int4，在单卡和双卡上输出结果会不一样 bug;stale ### Your current environment 主要是比较精细的输出，例如输出绘制Mermaid的代码。双卡上图表的数字有时是全角字符，但在单卡上运行基本正常。 vllm的版本是0.9.1 ### 🐛 Describe the bug ## ### Before submitting a new issue.....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: 请问用同样的模型qwen2.5-72b-int4，在单卡和双卡上输出结果会不一样 bug;stale ### Your current environment 主要是比较精细的输出，例如输出绘制Mermaid的代码。双卡上图表的数字有时是全角字符，但在单卡上运行基本正常。 vllm的版本是0.9.1 ### 🐛 Describe the bug ## ### Before submitting a new issue.....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
