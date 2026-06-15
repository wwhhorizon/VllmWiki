# vllm-project/vllm#14767: [Bug]: api_server.py log reports running http when https is running

| 字段 | 值 |
| --- | --- |
| Issue | [#14767](https://github.com/vllm-project/vllm/issues/14767) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: api_server.py log reports running http when https is running

### Issue 正文摘录

### Your current environment vLLM main branch. ### 🐛 Describe the bug Should be a simple fix. https://github.com/vllm-project/vllm/blob/01b3fd0af7d487f1a3b5aa11807b78d1f330ab95/vllm/entrypoints/openai/api_server.py#L958C9-L959C62 Shows `Starting vLLM API server on http:` even when it's running https. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
