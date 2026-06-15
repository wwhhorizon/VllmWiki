# vllm-project/vllm#9670: [Bug]: Input length greater than 32K in nvidia/Llama-3.1-Nemotron-70B-Instruct-HF generate garbage on v0.6.3 ( issue is not seen in v0.6.2)

| 字段 | 值 |
| --- | --- |
| Issue | [#9670](https://github.com/vllm-project/vllm/issues/9670) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Input length greater than 32K in nvidia/Llama-3.1-Nemotron-70B-Instruct-HF generate garbage on v0.6.3 ( issue is not seen in v0.6.2)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Note : The issue is not seen in release [v0.6.2](https://github.com/vllm-project/vllm/releases/tag/v0.6.2) From release 0.6.3, any input larger than 32K tokens, the model out is garbage. Model deployed is : nvidia/Llama-3.1-Nemotron-70B-Instruct-HF with tensor-parallel-size 4 on 4 A100 GPU servers When i rolled back to 0.6.2 release the issue disappeared & the model is stable still 130K input token without any issue. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Input length greater than 32K in nvidia/Llama-3.1-Nemotron-70B-Instruct-HF generate garbage on v0.6.3 ( issue is not seen in v0.6.2) bug;stale ### Your current environment ### Model Input Dumps _No response_ ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: dia/Llama-3.1-Nemotron-70B-Instruct-HF with tensor-parallel-size 4 on 4 A100 GPU servers When i rolled back to 0.6.2 release the issue disappeared & the model is stable still 130K input token without any issue. ### Befo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nstruct-HF generate garbage on v0.6.3 ( issue is not seen in v0.6.2) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Note : The issue is not seen in release [v0.6.2](htt...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
