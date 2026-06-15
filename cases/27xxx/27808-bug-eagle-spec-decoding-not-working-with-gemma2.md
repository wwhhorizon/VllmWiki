# vllm-project/vllm#27808: [Bug]: `Eagle` spec decoding not working with Gemma2

| 字段 | 值 |
| --- | --- |
| Issue | [#27808](https://github.com/vllm-project/vllm/issues/27808) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `Eagle` spec decoding not working with Gemma2

### Issue 正文摘录

### Your current environment VLLM: `0.9.1` Docker container: `vllm/vllm-openai:v0.9.1` ` python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model /opt/ml/checkpoints/final_model/base-model --seed 42 -tp 1 --gpu_memory_utilization 0.8 --max-model-len 2048 --speculative_config '{"method":"eagle","model":"/opt/ml/checkpoints/final_model","num_speculative_tokens": 5,"max_model_len":2048}' ` ### 🐛 Describe the bug I train Eagle1 (Llama) on Gemma2. However, I could not deploy Gemma with Eagle. I could deploy other model with Eagle such as LLama, Qwen. In short, vllm complains about the head size of Attention. `ValueError: Head size 288 is not supported by FlashAttention. Supported head sizes are: [32, 64, 96, 128, 160, 192, 224, 256]. Set VLLM_USE_V1=0 to use another attention backend.` Is Gemma + Eagle supported? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: `Eagle` spec decoding not working with Gemma2 bug;stale ### Your current environment VLLM: `0.9.1` Docker container: `vllm/vllm-openai:v0.9.1` ` python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: head size of Attention. `ValueError: Head size 288 is not supported by FlashAttention. Supported head sizes are: [32, 64, 96, 128, 160, 192, 224, 256]. Set VLLM_USE_V1=0 to use another attention backend.` Is Gemma + Eag...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: `Eagle` spec decoding not working with Gemma2 bug;stale ### Your current environment VLLM: `0.9.1` Docker container: `vllm/vllm-openai:v0.9.1` ` python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: orking with Gemma2 bug;stale ### Your current environment VLLM: `0.9.1` Docker container: `vllm/vllm-openai:v0.9.1` ` python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model /opt/ml/checkpoints/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
