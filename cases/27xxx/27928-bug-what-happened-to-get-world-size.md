# vllm-project/vllm#27928: [Bug]: What happened to /get_world_size ?

| 字段 | 值 |
| --- | --- |
| Issue | [#27928](https://github.com/vllm-project/vllm/issues/27928) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: What happened to /get_world_size ?

### Issue 正文摘录

### Your current environment vllm 0.11.0 trl 0.24.0 python 3.12 linux amd64 ### 🐛 Describe the bug TRL is expecting a `/get_world_size` route https://github.com/huggingface/trl/blob/main/trl/extras/vllm_client.py#L279 for its GRPO trainer. That gives a 404 on the latest version of vLLM. Was this changed to another route? I can't seem to find it ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: vllm_client.py#L279 for its GRPO trainer. That gives a 404 on the latest version of vLLM. Was this changed to another route? I can't seem to find it ### Before submitting a new issue... - [x] Make sure you already searc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: it ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e the bug TRL is expecting a `/get_world_size` route https://github.com/huggingface/trl/blob/main/trl/extras/vllm_client.py#L279 for its GRPO trainer. That gives a 404 on the latest version of vLLM. Was this changed to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: What happened to /get_world_size ? bug;stale ### Your current environment vllm 0.11.0 trl 0.24.0 python 3.12 linux amd64 ### 🐛 Describe the bug TRL is expecting a `/get_world_size` route https://github.com/huggin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tras/vllm_client.py#L279 for its GRPO trainer. That gives a 404 on the latest version of vLLM. Was this changed to another route? I can't seem to find it ### Before submitting a new issue... - [x] Make sure you already...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
