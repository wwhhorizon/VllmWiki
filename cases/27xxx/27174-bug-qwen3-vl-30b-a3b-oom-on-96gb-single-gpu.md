# vllm-project/vllm#27174: [Bug]: Qwen3-VL-30B-A3B OOM on 96GB single gpu

| 字段 | 值 |
| --- | --- |
| Issue | [#27174](https://github.com/vllm-project/vllm/issues/27174) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-30B-A3B OOM on 96GB single gpu

### Issue 正文摘录

### Your current environment Consistently getting an OOM despite using a 96gb gpu Using FP8 on latest VLLM on GH200 ### 🐛 Describe the bug OOM even when model is small (30gb) Potentially a memory leak? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: on latest VLLM on GH200 ### 🐛 Describe the bug OOM even when model is small (30gb) Potentially a memory leak? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3-VL-30B-A3B OOM on 96GB single gpu bug;stale ### Your current environment Consistently getting an OOM despite using a 96gb gpu Using FP8 on latest VLLM on GH200 ### 🐛 Describe the bug OOM even when model is...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: environment Consistently getting an OOM despite using a 96gb gpu Using FP8 on latest VLLM on GH200 ### 🐛 Describe the bug OOM even when model is small (30gb) Potentially a memory leak? ### Before submitting a new issue....
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: Qwen3-VL-30B-A3B OOM on 96GB single gpu bug;stale ### Your current environment Consistently getting an OOM despite using a 96gb gpu Using FP8 on latest VLLM on GH200 ### 🐛 Describe the bug OOM even when model is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Qwen3-VL-30B-A3B OOM on 96GB single gpu bug;stale ### Your current environment Consistently getting an OOM despite using a 96gb gpu Using FP8 on latest VLLM on GH200 ### 🐛 Describe the bug OOM even when model is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
