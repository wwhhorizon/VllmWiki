# vllm-project/vllm#22140: [Bug]: GLM-4.5 not working

| 字段 | 值 |
| --- | --- |
| Issue | [#22140](https://github.com/vllm-project/vllm/issues/22140) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM-4.5 not working

### Issue 正文摘录

### Your current environment I'm getting errors in vllm 10.0 and 10.1 trying AWQ, GPTQ and FP8 non work with or without tensor parallelism with my 6000 blackwell cards ### 🐛 Describe the bug I'm getting errors in vllm 10.0 and 10.1 trying AWQ, GPTQ and FP8 non work with or without tensor parallelism with my 6000 blackwell cards ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: d 10.1 trying AWQ, GPTQ and FP8 non work with or without tensor parallelism with my 6000 blackwell cards ### 🐛 Describe the bug I'm getting errors in vllm 10.0 and 10.1 trying AWQ, GPTQ and FP8 non work with or without...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: vironment I'm getting errors in vllm 10.0 and 10.1 trying AWQ, GPTQ and FP8 non work with or without tensor parallelism with my 6000 blackwell cards ### 🐛 Describe the bug I'm getting errors in vllm 10.0 and 10.1 trying...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: GLM-4.5 not working bug;stale ### Your current environment I'm getting errors in vllm 10.0 and 10.1 trying AWQ, GPTQ and FP8 non work with or without tensor parallelism with my 6000 blackwell cards ### 🐛 Describe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
