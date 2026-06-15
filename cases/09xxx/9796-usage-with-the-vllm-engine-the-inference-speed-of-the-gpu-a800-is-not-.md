# vllm-project/vllm#9796: [Usage]: With the vLLM engine, the inference speed of the GPU A800 is not as fast as RTX3090 block, is this normal?

| 字段 | 值 |
| --- | --- |
| Issue | [#9796](https://github.com/vllm-project/vllm/issues/9796) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: With the vLLM engine, the inference speed of the GPU A800 is not as fast as RTX3090 block, is this normal?

### Issue 正文摘录

### Your current environment My executable command is: xinference launch --model-engine vllm -u custom-llama-3.1-8b-instruct --model-name custom-llama-3.1-8b-instruct --size-in-billions 8 --model-format pytorch --quantization none --gpu_memory_utilization 0.9 --max_model_len 25600 Whether the performance of the A800 has been maximized ### How would you like to use vllm My executable command is: xinference launch --model-engine vllm -u custom-llama-3.1-8b-instruct --model-name custom-llama-3.1-8b-instruct --size-in-billions 8 --model-format pytorch --quantization none --gpu_memory_utilization 0.9 --max_model_len 25600 Whether the performance of the A800 has been maximized ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Your current environment My executable command is: xinference launch --model-engine vllm -u custom-llama-3.1-8b-instruct --model-name custom-llama-3.1-8b-instruct --size-in-billions 8 --model-format pytorch --quantizati...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: h the vLLM engine, the inference speed of the GPU A800 is not as fast as RTX3090 block, is this normal? usage;stale ### Your current environment My executable command is: xinference launch --model-engine vllm -u custom-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: stom-llama-3.1-8b-instruct --size-in-billions 8 --model-format pytorch --quantization none --gpu_memory_utilization 0.9 --max_model_len 25600 Whether the performance of the A800 has been maximized ### How would you like...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: LM engine, the inference speed of the GPU A800 is not as fast as RTX3090 block, is this normal? usage;stale ### Your current environment My executable command is: xinference launch --model-engine vllm -u custom-llama-3....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: d of the GPU A800 is not as fast as RTX3090 block, is this normal? usage;stale ### Your current environment My executable command is: xinference launch --model-engine vllm -u custom-llama-3.1-8b-instruct --model-name cu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
