# vllm-project/vllm#14364: [Usage]: STREAMING doesn't generate spaces

| 字段 | 值 |
| --- | --- |
| Issue | [#14364](https://github.com/vllm-project/vllm/issues/14364) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: STREAMING doesn't generate spaces

### Issue 正文摘录

### Your current environment When I run `CohereForAI/c4ai-command-r7b-arabic-02-2025` on streaming it doesn't generate spaces. but if I turn off streaming it generates spaces normally ### How would you like to use vllm I want to run inference of a [CohereForAI/c4ai-command-r7b-arabic-02-2025](https://huggingface.co/CohereForAI/c4ai-command-r7b-arabic-02-2025). When I run it on streaming it doesn't generate spaces. but if I turn off streaming it generates spaces normally ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ly ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: run inference of a [CohereForAI/c4ai-command-r7b-arabic-02-2025](https://huggingface.co/CohereForAI/c4ai-command-r7b-arabic-02-2025). When I run it on streaming it doesn't generate spaces. but if I turn off streaming it...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: STREAMING doesn't generate spaces usage;stale ### Your current environment When I run `CohereForAI/c4ai-command-r7b-arabic-02-2025` on streaming it doesn't generate spaces. but if I turn off streaming it genera...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
