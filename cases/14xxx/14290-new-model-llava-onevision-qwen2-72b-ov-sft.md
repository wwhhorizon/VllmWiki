# vllm-project/vllm#14290: [New Model]: llava-onevision-qwen2-72b-ov-sft

| 字段 | 值 |
| --- | --- |
| Issue | [#14290](https://github.com/vllm-project/vllm/issues/14290) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: llava-onevision-qwen2-72b-ov-sft

### Issue 正文摘录

### The model to consider. Thank you for put vllm，it is a great work. Could you help me add [llava-onevision-qwen2-72b-ov-sft](https://huggingface.co/lmms-lab/llava-onevision-qwen2-72b-ov-sft), I tried use function _run_llava_onevision_ but it has an error: ValueError: Model architectures ['TransformersModel'] failed to be inspected. Please check the logs for more details. ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: llava-onevision-qwen2-72b-ov-sft new-model;stale ### The model to consider. Thank you for put vllm，it is a great work. Could you help me add [llava-onevision-qwen2-72b-ov-sft](https://huggingface.co/lmms-la...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: se function _run_llava_onevision_ but it has an error: ValueError: Model architectures ['TransformersModel'] failed to be inspected. Please check the logs for more details. ### The closest model vllm already supports. _...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: llava-onevision-qwen2-72b-ov-sft new-model;stale ### The model to consider. Thank you for put vllm，it is a great work. Could you help me add [llava-onevision-qwen2-72b-ov-sft](https://huggingface.co/lmms-la...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
