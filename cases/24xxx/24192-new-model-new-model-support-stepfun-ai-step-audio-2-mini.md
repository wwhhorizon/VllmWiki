# vllm-project/vllm#24192: [New Model]: New model support stepfun-ai/Step-Audio-2-mini

| 字段 | 值 |
| --- | --- |
| Issue | [#24192](https://github.com/vllm-project/vllm/issues/24192) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: New model support stepfun-ai/Step-Audio-2-mini

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The model to consider. https://huggingface.co/stepfun-ai/Step-Audio-2-mini The closest model VLLM already supports. Qwen2.5 Omni: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/qwen2_5_omni_thinker.py Step Audio (branch): https://github.com/stepfun-ai/Step-Audio2 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: New model support stepfun-ai/Step-Audio-2-mini feature request;stale ### 🚀 The feature, motivation and pitch The model to consider. https://huggingface.co/stepfun-ai/Step-Audio-2-mini The closest model VLLM...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [New Model]: New model support stepfun-ai/Step-Audio-2-mini feature request;stale ### 🚀 The feature, motivation and pitch The model to consider. https://huggingface.co/stepfun-ai/Step-Audio-2-mini The closest model VLLM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
