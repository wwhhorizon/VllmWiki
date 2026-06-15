# vllm-project/vllm#19709: [Feature]: Simplify speculative-config format for vllm serve

| 字段 | 值 |
| --- | --- |
| Issue | [#19709](https://github.com/vllm-project/vllm/issues/19709) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Simplify speculative-config format for vllm serve

### Issue 正文摘录

### 🚀 The feature, motivation and pitch To enable speculative decoding via `vllm serve`, currently we need to pass in `speculative-config` arg as a valid json string, such as: > '{"method": "eagle", "model": "yuhuili/EAGLE-LLaMA3.1-Instruct-8B", "num_speculative_tokens": 3, "draft_tensor_parallel_size": 1, "max_model_len": 2048}' The above json string contains empty spaces and single / double quotes, which can get tricky to pass in as command line argument in some production environments. Using the following format where each setting is separated by a comma can solve this problem: > method:eagle,model:yuhuili/EAGLE-LLaMA3.1-Instruct-8B,num_speculative_tokens:3,draft_tensor_parallel_size:1,max_model_len:2048 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Simplify speculative-config format for vllm serve feature request ### 🚀 The feature, motivation and pitch To enable speculative decoding via `vllm serve`, currently we need to pass in `speculative-config` arg...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Simplify speculative-config format for vllm serve feature request ### 🚀 The feature, motivation and pitch To enable speculative decoding via `vllm serve`, currently we need to pass in `speculative-config` arg...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
