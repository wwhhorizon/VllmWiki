# vllm-project/vllm#43576: [Bug]: TurboQuant crashes on T4/Turing (SM75) — FlashAttention capability not checked

| 字段 | 值 |
| --- | --- |
| Issue | [#43576](https://github.com/vllm-project/vllm/issues/43576) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;kernel |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TurboQuant crashes on T4/Turing (SM75) — FlashAttention capability not checked

### Issue 正文摘录

### Your current environment ``` vLLM 0.21.0 (pip install) GPU: Tesla T4 (SM75, Turing) — Kaggle free tier CUDA: 12.4 OS: Ubuntu 22.04 (Kaggle) Python: 3.11 ``` ### 🐛 Describe the bug Running any model with `--kv-cache-dtype turboquant_4bit_nc` on a T4 GPU crashes immediately during prefill: ``` RuntimeError: FlashAttention only supports Ampere GPUs or newer. ``` The TQ backend has a working SDPA fallback path (`F.scaled_dot_product_attention`) gated behind `if not _HAS_FLASH_ATTN`, but it never activates on CUDA because `is_flash_attn_varlen_func_available()` returns `True` on all CUDA platforms — it checks package availability, not hardware compute capability. ### How to reproduce ```python from vllm import LLM llm = LLM( model="Qwen/Qwen2.5-0.5B", kv_cache_dtype="turboquant_4bit_nc", enforce_eager=True, max_model_len=2048, gpu_memory_utilization=0.5, ) # Crashes during engine init on T4 ``` ### Root cause `turboquant_attn.py` line 60: ```python _HAS_FLASH_ATTN = is_flash_attn_varlen_func_available() if _HAS_FLASH_ATTN: from vllm.v1.attention.backends.fa_utils import flash_attn_varlen_func ``` `is_flash_attn_varlen_func_available()` (in `fa_utils.py`) checks whether the `flash_a...

## 现有链接修复摘要

#43577 fix(turboquant): use SDPA prefill fallback on pre-Ampere GPUs

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: apability not checked ### Your current environment ``` vLLM 0.21.0 (pip install) GPU: Tesla T4 (SM75, Turing) — Kaggle free tier CUDA: 12.4 OS: Ubuntu 22.04 (Kaggle) Python: 3.11 ``` ### 🐛 Describe the bug Running any m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: TurboQuant crashes on T4/Turing (SM75) — FlashAttention capability not checked ### Your current environment ``` vLLM 0.21.0 (pip install) GPU: Tesla T4 (SM75, Turing) — Kaggle free tier CUDA: 12.4 OS: Ubuntu 22.0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: TurboQuant crashes on T4/Turing (SM75) — FlashAttention capability not checked ### Your current environment ``` vLLM 0.21.0 (pip install) GPU: Tesla T4 (SM75, Turing) — Kaggle free tier CUDA: 12.4 OS: Ubuntu 22.0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: TurboQuant crashes on T4/Turing (SM75) — FlashAttention capability not checked ### Your current environment ``` vLLM 0.21.0 (pip install) GPU: Tesla T4 (SM75, Turing) — Kaggle free tier CUDA: 12.4 OS: Ubuntu 22.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ntu 22.04 (Kaggle) Python: 3.11 ``` ### 🐛 Describe the bug Running any model with `--kv-cache-dtype turboquant_4bit_nc` on a T4 GPU crashes immediately during prefill: ``` RuntimeError: FlashAttention only supports Ampe...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43577](https://github.com/vllm-project/vllm/pull/43577) | closes_keyword | 0.95 | fix(turboquant): use SDPA prefill fallback on pre-Ampere GPUs | Closes #43576 ## Summary - Fix `RuntimeError: FlashAttention only supports Ampere GPUs or newer` when running TurboQuant on T4/Turing (SM75) - The SDPA fallback path already exis |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
