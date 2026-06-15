# vllm-project/vllm#29945: [Bug]: Got different `max model len` using MTP with Qwen3 next

| 字段 | 值 |
| --- | --- |
| Issue | [#29945](https://github.com/vllm-project/vllm/issues/29945) |
| 状态 | open |
| 标签 | bug;speculative-decoding;unstale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Got different `max model len` using MTP with Qwen3 next

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python import os os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3" os.environ["VLLM_ATTENTION_BACKEND"] = "FLASHINFER" os.environ["VLLM_USE_FLASHINFER_SAMPLER"] = "0" os.environ["FLASHINFER_DISABLE_VERSION_CHECK"] = "1" os.environ["VLLM_MARLIN_USE_ATOMIC_ADD"] = "1" import torch major, minor = torch.cuda.get_device_capability() arch_version = f"{major}.{minor}" os.environ["TORCH_CUDA_ARCH_LIST"] = arch_version from vllm.config import CompilationConfig from transformers import AutoTokenizer import asyncio from vllm import SamplingParams from vllm.engine.arg_utils import AsyncEngineArgs from vllm.sampling_params import RequestOutputKind from vllm.v1.engine.async_llm import AsyncLLM import time model_path = "/data/pretrained_models/Qwen3-Next-80B-A3B-Thinking-FP8" tokenizer = AutoTokenizer.from_pretrained(model_path) async def stream_response(engine: AsyncLLM, prompt: str, request_id: str) -> None: """ Stream response from AsyncLLM and display tokens as they arrive. This function demonstrates the core streaming pattern: 1. Create SamplingParams with DELTA output kind 2. Call engine.generate() and iterate over the async generator 3....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: stale ### Your current environment ### 🐛 Describe the bug ```python import os os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3" os.environ["VLLM_ATTENTION_BACKEND"] = "FLASHINFER" os.environ["VLLM_USE_FLASHINFER_SAMPLER"]...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Got different `max model len` using MTP with Qwen3 next bug;speculative-decoding;unstale ### Your current environment ### 🐛 Describe the bug ```python import os os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3" os.e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: time model_path = "/data/pretrained_models/Qwen3-Next-80B-A3B-Thinking-FP8" tokenizer = AutoTokenizer.from_pretrained(model_path) async def stream_response(engine: AsyncLLM, prompt: str, request_id: str) -> None: """ St...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: s.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3" os.environ["VLLM_ATTENTION_BACKEND"] = "FLASHINFER" os.environ["VLLM_USE_FLASHINFER_SAMPLER"] = "0" os.environ["FLASHINFER_DISABLE_VERSION_CHECK"] = "1" os.environ["VLLM_MAR...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: environment ### 🐛 Describe the bug ```python import os os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3" os.environ["VLLM_ATTENTION_BACKEND"] = "FLASHINFER" os.environ["VLLM_USE_FLASHINFER_SAMPLER"] = "0" os.environ["FLASH...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
