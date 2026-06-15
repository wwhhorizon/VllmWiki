# vllm-project/vllm#21695: [Bug]: can not support InternVL3-78B-AWQ

| 字段 | 值 |
| --- | --- |
| Issue | [#21695](https://github.com/vllm-project/vllm/issues/21695) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: can not support InternVL3-78B-AWQ

### Issue 正文摘录

### Your current environment ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size. ### 🐛 Describe the bug code: CUDA_VISIBLE_DEVICES=3,4 vllm serve ./InternVL3-78B-AWQ --gpu-memory-utilization 0.95 --max-model-len 32768 --quantization awq --enforce-eager --host 0.0.0.0 --port 11441 --tensor-parallel-size 2 --dtype half --trust-remote-code error: ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: current environment ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size. ### 🐛 Describe the bug code: CUDA_VISIBLE_DEVICES=3,4 vllm serve ./Int...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: aused by too large tensor parallel size. ### 🐛 Describe the bug code: CUDA_VISIBLE_DEVICES=3,4 vllm serve ./InternVL3-78B-AWQ --gpu-memory-utilization 0.95 --max-model-len 32768 --quantization awq --enforce-eager --host...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: can not support InternVL3-78B-AWQ bug;stale ### Your current environment ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size. ### 🐛 Desc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: can not support InternVL3-78B-AWQ bug;stale ### Your current environment ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size. ### 🐛 Desc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
