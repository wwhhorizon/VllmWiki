# vllm-project/vllm#36084: [Bug]: prefix cach hit降到了0，running的seq也是逐步下降到0

| 字段 | 值 |
| --- | --- |
| Issue | [#36084](https://github.com/vllm-project/vllm/issues/36084) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: prefix cach hit降到了0，running的seq也是逐步下降到0

### Issue 正文摘录

### Your current environment vllm==0.16.1rc1.dev214+gd6e04f4c4 ### 🐛 Describe the bug 启动命令： vllm serve /path/Qwen3.5/Qwen3.5-27B \ --tensor-parallel-size 8 \ --host 0.0.0.0 \ --port 8011 \ --enable-prefix-caching 在使用后一段时间后，prefix cach hit降到了0，running的seq也是逐步下降到0，这是什么bug啊。 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: g啊。 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 6.1rc1.dev214+gd6e04f4c4 ### 🐛 Describe the bug 启动命令： vllm serve /path/Qwen3.5/Qwen3.5-27B \ --tensor-parallel-size 8 \ --host 0.0.0.0 \ --port 8011 \ --enable-prefix-caching 在使用后一段时间后，prefix cach hit降到了0，running的seq也是逐...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
