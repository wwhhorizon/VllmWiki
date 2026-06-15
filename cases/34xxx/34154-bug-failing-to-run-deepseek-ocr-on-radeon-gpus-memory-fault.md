# vllm-project/vllm#34154: [Bug]: Failing to run DeepSeek-OCR on Radeon GPUs (memory fault)

| 字段 | 值 |
| --- | --- |
| Issue | [#34154](https://github.com/vllm-project/vllm/issues/34154) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failing to run DeepSeek-OCR on Radeon GPUs (memory fault)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running DeepSeek-OCR crashes with memory-fault while initializing: ```python from vllm import LLM, SamplingParams from vllm.model_executor.models.deepseek_ocr import NGramPerReqLogitsProcessor import os import sys llm = LLM( model="deepseek-ai/DeepSeek-OCR", enable_prefix_caching=False, mm_processor_cache_gb=0, logits_processors=[NGramPerReqLogitsProcessor], ) ``` Output: ```bash ============================================================ Model: deepseek-ai/DeepSeek-OCR ENVIRONMENT: {'PYTORCH_TUNABLEOP_TUNING': '0', 'HOSTNAME': 'l-amd-dev-01', 'PYTHON_VERSION': '3.12', 'SCCACHE_IDLE_TIMEOUT': '', 'SAFETENSORS_FAST_GPU': '1', 'AITER_ROCM_ARCH': 'gfx942;gfx950', 'PWD': '/workspace', 'PYTORCH_TUNABLEOP_ENABLED': '1', 'SP_TEMPERATURE': '0.0', 'HOME': '/root', 'TOKENIZERS_PARALLELISM': 'false', 'RAY_EXPERIMENTAL_NOSET_ROCR_VISIBLE_DEVICES': '1', 'RAY_EXPERIMENTAL_NOSET_HIP_VISIBLE_DEVICES': '1', 'SP_MAX_TOKENS': '1024', 'UV_LINK_MODE': 'copy', 'HIP_FORCE_DEV_KERNARG': '1', 'DEVICE_NAME': 'Radeon RX 7900 XTX', 'HSA_NO_SCRATCH_RECLAIM': '1', 'UV_INDEX_STRATEGY': 'unsafe-best-match', 'SCCACHE_REGION': '', 'PYTORCH_ROCM_ARCH': 'gfx90a;gf...

## 现有链接修复摘要

#35485 [Bugfix][ROCm] Disable full CUDA graph capture on RDNA3/RDNA4 (gfx1x) | #36374 [Bugfix][ROCm] full graph capture on triton-attn fix - Option1

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: k-OCR crashes with memory-fault while initializing: ```python from vllm import LLM, SamplingParams from vllm.model_executor.models.deepseek_ocr import NGramPerReqLogitsProcessor import os import sys llm = LLM( model="de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Failing to run DeepSeek-OCR on Radeon GPUs (memory fault) bug;rocm ### Your current environment ### 🐛 Describe the bug Running DeepSeek-OCR crashes with memory-fault while initializing: ```python from vllm import...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: initializing: ```python from vllm import LLM, SamplingParams from vllm.model_executor.models.deepseek_ocr import NGramPerReqLogitsProcessor import os import sys llm = LLM( model="deepseek-ai/DeepSeek-OCR", enable_prefix...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: SION': '3.12', 'SCCACHE_IDLE_TIMEOUT': '', 'SAFETENSORS_FAST_GPU': '1', 'AITER_ROCM_ARCH': 'gfx942;gfx950', 'PWD': '/workspace', 'PYTORCH_TUNABLEOP_ENABLED': '1', 'SP_TEMPERATURE': '0.0', 'HOME': '/root', 'TOKENIZERS_PA...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35485](https://github.com/vllm-project/vllm/pull/35485) | closes_keyword | 0.95 | [Bugfix][ROCm] Disable full CUDA graph capture on RDNA3/RDNA4 (gfx1x) | Fix #34154. RDNA3/RDNA4 GPUs (gfx11xx/gfx12xx) crash with `Memory access fault ... Page not present or supervisor privilege` during FULL CUDA graph capture of Triton attention kern |
| [#36374](https://github.com/vllm-project/vllm/pull/36374) | closes_keyword | 0.95 | [Bugfix][ROCm] full graph capture on triton-attn fix - Option1 | Fix ROCm full CUDA graph capture fault with Triton attention (#35169) and (#34154). On ROCm, full graph capture triggered “Write access to read-only page” because the Triton 3D a |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
