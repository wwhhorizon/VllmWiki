# vllm-project/vllm#9339: [Usage]: --cpu-offload-gb no use

| 字段 | 值 |
| --- | --- |
| Issue | [#9339](https://github.com/vllm-project/vllm/issues/9339) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: --cpu-offload-gb no use

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm export MODEL_PATH=/data3/models/Qwen2.5-32B-Instruct python3 -m vllm.entrypoints.openai.api_server --model $MODEL_PATH --seed 1100 --dtype bfloat16 --trust-remote-code --port 8001 --gpu-memory-utilization 0.9 --cpu-offload-gb 30 gpu-out-mem, cpu-offload-gb no use ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -m vllm.entrypoints.openai.api_server --model $MODEL_PATH --seed 1100 --dtype bfloat16 --trust-remote-code --port 8001 --gpu-memory-utilization 0.9 --cpu-offload-gb 30 gpu-out-mem, cpu-offload-gb no use ### Before submi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: `python collect_env.py` ``` ### How would you like to use vllm export MODEL_PATH=/data3/models/Qwen2.5-32B-Instruct python3 -m vllm.entrypoints.openai.api_server --model $MODEL_PATH --seed 1100 --dtype bfloat16 --trust-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: use ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: --cpu-offload-gb no use usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm export MODEL_PATH=/data3/models/Qwen2.5-32B-Instruct python3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: --cpu-offload-gb no use usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm export MODEL_PATH=/data3/models/Qwen2.5-32B-Instruct python3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
