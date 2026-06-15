# vllm-project/vllm#23698: [Usage]: How to limit the size of input images in commands

| 字段 | 值 |
| --- | --- |
| Issue | [#23698](https://github.com/vllm-project/vllm/issues/23698) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to limit the size of input images in commands

### Issue 正文摘录

### Your current environment my commands CUDA_VISIBLE_DEVICES=6 vllm serve "/models/vlmmodels/prithivMLmods/finetune/full/base_20250822/OCR-2B-VKIE-1round/" \ --max-model-len 10240 \ --host 0.0.0.0 \ --port 8055 \ --served-model-name OCR-2B-VKIE ### How would you like to use vllm How to solve ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: images in commands usage;stale ### Your current environment my commands CUDA_VISIBLE_DEVICES=6 vllm serve "/models/vlmmodels/prithivMLmods/finetune/full/base_20250822/OCR-2B-VKIE-1round/" \ --max-model-len 10240 \ --hos...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: our current environment my commands CUDA_VISIBLE_DEVICES=6 vllm serve "/models/vlmmodels/prithivMLmods/finetune/full/base_20250822/OCR-2B-VKIE-1round/" \ --max-model-len 10240 \ --host 0.0.0.0 \ --port 8055 \ --served-m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to limit the size of input images in commands usage;stale ### Your current environment my commands CUDA_VISIBLE_DEVICES=6 vllm serve "/models/vlmmodels/prithivMLmods/finetune/full/base_20250822/OCR-2B-VKIE-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
