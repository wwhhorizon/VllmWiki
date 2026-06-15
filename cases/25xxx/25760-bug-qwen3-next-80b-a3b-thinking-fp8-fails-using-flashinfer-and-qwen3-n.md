# vllm-project/vllm#25760: [Bug]: Qwen3-Next-80B-A3B-Thinking-FP8 fails using flashinfer and `qwen3_next_mtp` spec decode

| 字段 | 值 |
| --- | --- |
| Issue | [#25760](https://github.com/vllm-project/vllm/issues/25760) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next-80B-A3B-Thinking-FP8 fails using flashinfer and `qwen3_next_mtp` spec decode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python import os os.environ["VLLM_USE_V1"] = "1" os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3" os.environ["VLLM_ATTENTION_BACKEND"] = "FLASHINFER" os.environ["VLLM_USE_FLASHINFER_SAMPLER"] = "1" os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn" os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "1" import torch major, minor = torch.cuda.get_device_capability() arch_version = f"{major}.{minor}" os.environ["TORCH_CUDA_ARCH_LIST"] = arch_version from vllm.config import CompilationConfig from transformers import AutoTokenizer import asyncio from vllm import SamplingParams from vllm.engine.arg_utils import AsyncEngineArgs from vllm.sampling_params import RequestOutputKind from vllm.v1.engine.async_llm import AsyncLLM model_path = "/data/pretrained_models/Qwen3-Next-80B-A3B-Thinking-FP8" tokenizer = AutoTokenizer.from_pretrained(model_path) async def stream_response(engine: AsyncLLM, prompt: str, request_id: str) -> None: """ Stream response from AsyncLLM and display tokens as they arrive. This function demonstrates the core streaming pattern: 1. Create SamplingParams with DELTA output kind 2. Call engine.generate() and iterate over...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 9: n3-Next-80B-A3B-Thinking-FP8 fails using flashinfer and `qwen3_next_mtp` spec decode bug;stale ### Your current environment ### 🐛 Describe the bug ```python import os os.environ["VLLM_USE_V1"] = "1" os.environ["CUDA_VIS...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: stale ### Your current environment ### 🐛 Describe the bug ```python import os os.environ["VLLM_USE_V1"] = "1" os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3" os.environ["VLLM_ATTENTION_BACKEND"] = "FLASHINFER" os.environ...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Qwen3-Next-80B-A3B-Thinking-FP8 fails using flashinfer and `qwen3_next_mtp` spec decode bug;stale ### Your current environment ### 🐛 Describe the bug ```python import os os.environ["VLLM_USE_V1"] = "1" os.environ...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: Qwen3-Next-80B-A3B-Thinking-FP8 fails using flashinfer and `qwen3_next_mtp` spec decode bug;stale ### Your current environment ### 🐛 Describe the bug ```python import os os.environ["VLLM_USE_V1"] = "1" os.environ...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: _size=len(os.environ["CUDA_VISIBLE_DEVICES"].split(",")), enable_expert_parallel=True, gpu_memory_utilization=0.9, kv_cache_dtype="fp8", enforce_eager=False, max_num_seqs=32, max_num_batched_tokens=2048, max_model_len=1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
