# vllm-project/vllm#15864: [Bug]: qwen2.5-omni model failed to start

| 字段 | 值 |
| --- | --- |
| Issue | [#15864](https://github.com/vllm-project/vllm/issues/15864) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen2.5-omni model failed to start

### Issue 正文摘录

### Your current environment vllm：0.8.2 transformers：4.51.0.dev0 export VLLM_USE_V1=0 && vllm serve Qwen2.5-Omni-7B --dtype half --cpu-offload-gb 1 --gpu-memory-utilization 0.9 --host 0.0.0.0 --port 9000 ### 🐛 Describe the bug qwen2.5-omni model failed to start ![Image](https://github.com/user-attachments/assets/fd207dcc-4891-4fa0-9f86-257b9ec78a0d) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen2.5-omni model failed to start bug;stale ### Your current environment vllm：0.8.2 transformers：4.51.0.dev0 export VLLM_USE_V1=0 && vllm serve Qwen2.5-Omni-7B --dtype half --cpu-offload-gb 1 --gpu-memory-utiliz...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ormers：4.51.0.dev0 export VLLM_USE_V1=0 && vllm serve Qwen2.5-Omni-7B --dtype half --cpu-offload-gb 1 --gpu-memory-utilization 0.9 --host 0.0.0.0 --port 9000 ### 🐛 Describe the bug qwen2.5-omni model failed to start ![I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0d) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 0 export VLLM_USE_V1=0 && vllm serve Qwen2.5-Omni-7B --dtype half --cpu-offload-gb 1 --gpu-memory-utilization 0.9 --host 0.0.0.0 --port 9000 ### 🐛 Describe the bug qwen2.5-omni model failed to start ![Image](https://git...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: qwen2.5-omni model failed to start bug;stale ### Your current environment vllm：0.8.2 transformers：4.51.0.dev0 export VLLM_USE_V1=0 && vllm serve Qwen2.5-Omni-7B --dtype half --cpu-offload-gb 1 --gpu-memory-utiliz...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
