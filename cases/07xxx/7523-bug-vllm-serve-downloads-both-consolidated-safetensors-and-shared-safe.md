# vllm-project/vllm#7523: [Bug]: vllm serve downloads both consolidated.safetensors and shared safetensors, when it should only download one of them.

| 字段 | 值 |
| --- | --- |
| Issue | [#7523](https://github.com/vllm-project/vllm/issues/7523) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm serve downloads both consolidated.safetensors and shared safetensors, when it should only download one of them.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Some models like mistralai/Mistral-7B-Instruct-v0.3, provide both shared and consolidated safetensors. `vllm serve mistralai/Mistral-7B-Instruct-v0.3` downloads both, which is somewhat time-consuming. This could lead to some testcases timing out, such as in #5649 --------UPDATE--------- I raised this issue primarily for testing, and now there is a solution for testing: use the `--ignore-patterns` parameter to ignore unnecessary files in testcase.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: bug;stale ### Your current environment ### 🐛 Describe the bug Some models like mistralai/Mistral-7B-Instruct-v0.3, provide both shared and consolidated safetensors. `vllm serve mistralai/Mistral-7B-Instruct-v0.3` downlo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: rs and shared safetensors, when it should only download one of them. bug;stale ### Your current environment ### 🐛 Describe the bug Some models like mistralai/Mistral-7B-Instruct-v0.3, provide both shared and consolidate...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ownloads both, which is somewhat time-consuming. This could lead to some testcases timing out, such as in #5649 --------UPDATE--------- I raised this issue primarily for testing, and now there is a solution for testing:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
