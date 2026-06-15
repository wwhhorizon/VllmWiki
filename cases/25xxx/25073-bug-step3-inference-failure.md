# vllm-project/vllm#25073: [Bug]: Step3 inference failure

| 字段 | 值 |
| --- | --- |
| Issue | [#25073](https://github.com/vllm-project/vllm/issues/25073) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Step3 inference failure

### Issue 正文摘录

### Your current environment vllm 0.10.2 torch 2.8.0 transformers 4.56.1 ### 🐛 Describe the bug when I use sample code: https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/vision_language.py for step3 inference. my scripts is `VLLM_USE_V1=1 python3 vision_language.py --model-type step3` get error message as: `TypeError: Invalid type of HuggingFace proceesor. Expected type: , but found type: ` The error occurs at `xxx/vllm/transformers_utils/processor.py, line 128, in get_processor` Please tell me the solution for this error, thanks a lot ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ep3 inference. my scripts is `VLLM_USE_V1=1 python3 vision_language.py --model-type step3` get error message as: `TypeError: Invalid type of HuggingFace proceesor. Expected type: , but found type: ` The error occurs at...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lot ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Step3 inference failure bug;stale ### Your current environment vllm 0.10.2 torch 2.8.0 transformers 4.56.1 ### 🐛 Describe the bug when I use sample code: https://github.com/vllm-project/vllm/blob/main/examples/of...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
