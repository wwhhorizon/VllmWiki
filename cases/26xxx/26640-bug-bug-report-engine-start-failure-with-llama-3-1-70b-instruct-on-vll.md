# vllm-project/vllm#26640: [Bug]: Bug Report: Engine start failure with Llama-3.1-70B-Instruct on vLLM 0.9.2 + ZenTorch 5.1 + PyTorch 2.7

| 字段 | 值 |
| --- | --- |
| Issue | [#26640](https://github.com/vllm-project/vllm/issues/26640) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Bug Report: Engine start failure with Llama-3.1-70B-Instruct on vLLM 0.9.2 + ZenTorch 5.1 + PyTorch 2.7

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When attempting to load the Llama-3.1-70B-Instruct model from Hugging Face using vLLM 0.9.2 with ZenTorch 5.1 and PyTorch 2.7, the engine process fails to start after loading roughly 50% of the model shards. The container logs show shard loading proceeding up to around 15 of 30 shards, then the engine shuts down with the following error: text RuntimeError: Engine process failed to start. See stack trace for the root cause. No additional details or exception information are provided in the logs. Environment vLLM version: 0.9.2 ZenTorch version: 5.1 PyTorch version: 2.7 Model source: Hugging Face official Llama-3.1-70B-Instruct weights, split into 30 .safetensors shards Hardware: AMD EPYC server, 1.5TiB RAM, CPU with bfloat16 support Containerization: Docker Compose, configured with shm_size: 128g and no Docker memory limits ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Bug Report: Engine start failure with Llama-3.1-70B-Instruct on vLLM 0.9.2 + ZenTorch 5.1 + PyTorch 2.7 bug;stale ### Your current environment ### 🐛 Describe the bug When attempting to load the Llama-3.1-70B-Inst...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ls or exception information are provided in the logs. Environment vLLM version: 0.9.2 ZenTorch version: 5.1 PyTorch version: 2.7 Model source: Hugging Face official Llama-3.1-70B-Instruct weights, split into 30 .safeten...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 30 .safetensors shards Hardware: AMD EPYC server, 1.5TiB RAM, CPU with bfloat16 support Containerization: Docker Compose, configured with shm_size: 128g and no Docker memory limits ### Before submitting a new issue... -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: its ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: th Llama-3.1-70B-Instruct on vLLM 0.9.2 + ZenTorch 5.1 + PyTorch 2.7 bug;stale ### Your current environment ### 🐛 Describe the bug When attempting to load the Llama-3.1-70B-Instruct model from Hugging Face using vLLM 0....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
