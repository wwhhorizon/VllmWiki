# vllm-project/vllm#38884: [Bug]: Gemma 4 torch._dynamo.exc.TorchRuntimeError: Dynamo failed to run FX node with fake tensors

| 字段 | 值 |
| --- | --- |
| Issue | [#38884](https://github.com/vllm-project/vllm/issues/38884) |
| 状态 | open |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 torch._dynamo.exc.TorchRuntimeError: Dynamo failed to run FX node with fake tensors

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I can't load Gemma 4 on my RTX A6000 Pro (96 GB VRAM), CUDA 0.13, transformers==5.5.0 ``` from vllm import LLM, SamplingParams from vllm.sampling_params import StructuredOutputsParams import time import torch model_name = "google/gemma-4-31B" # change to "google/gemma-3-27b-it" for Gemma 3 as a reference print("Loading model...", end=" ", flush=True) t0 = time.time() llm = LLM( model=model_name, quantization="bitsandbytes", dtype="bfloat16", max_model_len=16384, gpu_memory_utilization=0.88, max_num_seqs=128, trust_remote_code=True, enforce_eager=False, ) ``` ``` Loading model... INFO 04-03 06:14:00 [utils.py:233] non-default args: {'trust_remote_code': True, 'dtype': 'bfloat16', 'max_model_len': 16384, 'gpu_memory_utilization': 0.88, 'max_num_seqs': 128, 'disable_log_stats': True, 'quantization': 'bitsandbytes', 'model': 'google/gemma-4-31B'} INFO 04-03 06:14:01 [model.py:549] Resolved architecture: Gemma4ForConditionalGeneration INFO 04-03 06:14:01 [model.py:1678] Using max model len 16384 INFO 04-03 06:14:01 [scheduler.py:238] Chunked prefill is enabled with max_num_batched_tokens=16384. INFO 04-03 06:14:01 [config.py:104] Gemm...

## 现有链接修复摘要

#40321 Fix Gemma 4 + BitsAndBytes startup failure reported in #38884

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: TX A6000 Pro (96 GB VRAM), CUDA 0.13, transformers==5.5.0 ``` from vllm import LLM, SamplingParams from vllm.sampling_params import StructuredOutputsParams import time import torch model_name = "google/gemma-4-31B" # ch...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: terogeneous head dimensions (head_dim=256, global_head_dim=512). Forcing TRITON_ATTN backend to prevent mixed-backend numerical divergence. INFO 04-03 06:14:02 [vllm.py:790] Asynchronous scheduling is enabled. (EngineCo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: =" ", flush=True) t0 = time.time() llm = LLM( model=model_name, quantization="bitsandbytes", dtype="bfloat16", max_model_len=16384, gpu_memory_utilization=0.88, max_num_seqs=128, trust_remote_code=True, enforce_eager=Fa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: rrent environment ### 🐛 Describe the bug I can't load Gemma 4 on my RTX A6000 Pro (96 GB VRAM), CUDA 0.13, transformers==5.5.0 ``` from vllm import LLM, SamplingParams from vllm.sampling_params import StructuredOutputsP...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Gemma 4 torch._dynamo.exc.TorchRuntimeError: Dynamo failed to run FX node with fake tensors bug ### Your current environment ### 🐛 Describe the bug I can't load Gemma 4 on my RTX A6000 Pro (96 GB VRAM), CUDA 0.13...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40321](https://github.com/vllm-project/vllm/pull/40321) | closes_keyword | 0.95 | Fix Gemma 4 + BitsAndBytes startup failure reported in #38884 | fixes the Gemma 4 + BitsAndBytes startup failure reported in #38884. The root cause is a mismatch between the effective QKV weights and the BitsAndBytes quantization state for G |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
