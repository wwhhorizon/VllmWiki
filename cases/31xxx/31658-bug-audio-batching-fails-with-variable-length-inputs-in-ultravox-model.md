# vllm-project/vllm#31658: [Bug] Audio batching fails with variable-length inputs in Ultravox model

| 字段 | 值 |
| --- | --- |
| Issue | [#31658](https://github.com/vllm-project/vllm/issues/31658) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support |
| 子分类 | throughput |
| Operator 关键词 | attention |
| 症状 | crash;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] Audio batching fails with variable-length inputs in Ultravox model

### Issue 正文摘录

### Your current environment - vLLM version: 0.13.0 - GPU: NVIDIA RTX 3090 (24GB) - PyTorch: 2.9.0+cu129 - Model: fixie-ai/ultravox-v0_6-llama-3_1-8b ### 🐛 Describe the bug When sending concurrent audio transcription requests to the vLLM server with audio samples of **different durations**, the engine crashes with: ``` ValueError: data contains inconsistent shapes: torch.Size([128, 325]) (index 0) vs torch.Size([128, 666]) (index 1) ``` Single requests work fine. Batching also works correctly when all audio samples are **padded to equal length**. ### Steps to reproduce 1. Start vLLM server with Ultravox: ```bash vllm serve fixie-ai/ultravox-v0_6-llama-3_1-8b --trust-remote-code --max-model-len 8192 ``` 2. Send concurrent requests with audio of different durations: ```python import asyncio import base64 import io import soundfile as sf from datasets import load_dataset from openai import AsyncOpenAI client = AsyncOpenAI(base_url="http://127.0.0.1:8000/v1", api_key="dummy") # Load MINDS-14 dataset (has variable-length audio) dataset = load_dataset("PolyAI/minds14", "en-US", split="train") async def transcribe(audio_b64): return await client.chat.completions.create( model="fixie-ai/u...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ble-length inputs in Ultravox model ### Your current environment - vLLM version: 0.13.0 - GPU: NVIDIA RTX 3090 (24GB) - PyTorch: 2.9.0+cu129 - Model: fixie-ai/ultravox-v0_6-llama-3_1-8b ### 🐛 Describe the bug When sendi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug] Audio batching fails with variable-length inputs in Ultravox model ### Your current environment - vLLM version: 0.13.0 - GPU: NVIDIA RTX 3090 (24GB) - PyTorch: 2.9.0+cu129 - Model: fixie-ai/ultravox-v0_6-llama-3_1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: model ### Your current environment - vLLM version: 0.13.0 - GPU: NVIDIA RTX 3090 (24GB) - PyTorch: 2.9.0+cu129 - Model: fixie-ai/ultravox-v0_6-llama-3_1-8b ### 🐛 Describe the bug When sending concurrent audio transcript...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: -8b ### 🐛 Describe the bug When sending concurrent audio transcription requests to the vLLM server with audio samples of **different durations**, the engine crashes with: ``` ValueError: data contains inconsistent shape...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tly when all audio samples are **padded to equal length**. ### Steps to reproduce 1. Start vLLM server with Ultravox: ```bash vllm serve fixie-ai/ultravox-v0_6-llama-3_1-8b --trust-remote-code --max-model-len 8192 ``` 2...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
