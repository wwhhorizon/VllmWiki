# vllm-project/vllm#32992: [Bug]: Batch invariance fails on NVIDIA B200 (Blackwell) with torch.compile

| 字段 | 值 |
| --- | --- |
| Issue | [#32992](https://github.com/vllm-project/vllm/issues/32992) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Batch invariance fails on NVIDIA B200 (Blackwell) with torch.compile

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Describe the bug Batch invariance mode (`VLLM_BATCH_INVARIANT=1`) fails on B200 (Blackwell) but works correctly on H200 (Hopper). Tested with model `Qwen/Qwen2.5-7B-Instruct` using both FLASH_ATTN and FLASHINFER backends. | GPU | Architecture | `enforce_eager=False` | `enforce_eager=True` | |-----|--------------|----------------------|---------------------| | H200 | Hopper (SM 90) | **PASS** | **PASS** | | B200 | Blackwell (SM 100) | **FAIL** | **PASS** | When `enforce_eager=False` (default), `torch.compile` is enabled. The issue appears to be non-deterministic code generation by PyTorch Inductor on Blackwell architecture. ### Minimal reproduction ```python #!/usr/bin/env python3 """ B200 Batch Invariance Test Tests batch invariance (BS=1 vs BS=N logprobs match) on both FLASH_ATTN and FLASHINFER backends. Compares enforce_eager=False (torch.compile) vs enforce_eager=True (eager mode). """ import os os.environ["VLLM_BATCH_INVARIANT"] = "1" import torch from vllm import LLM, SamplingParams def test_batch_invariance(enforce_eager: bool, backend: str, num_prompts: int = 32): """Test batch invariance across multiple batch sizes.""...

## 现有链接修复摘要

#33383 [Bugfix] Disable torch.compile for batch invariance on Blackwell to ensure determinism

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: Batch invariance fails on NVIDIA B200 (Blackwell) with torch.compile bug;torch.compile ### Your current environment ### 🐛 Describe the bug ### Describe the bug Batch invariance mode (`VLLM_BATCH_INVARIANT=1`) fai...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Batch invariance fails on NVIDIA B200 (Blackwell) with torch.compile bug;torch.compile ### Your current environment ### 🐛 Describe the bug ### Describe the bug Batch invariance mode (`VLLM_BATCH_INVARIANT=1`) fai...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ls on B200 (Blackwell) but works correctly on H200 (Hopper). Tested with model `Qwen/Qwen2.5-7B-Instruct` using both FLASH_ATTN and FLASHINFER backends. | GPU | Architecture | `enforce_eager=False` | `enforce_eager=True...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: [Bug]: Batch invariance fails on NVIDIA B200 (Blackwell) with torch.compile bug;torch.compile ### Your current environment ### 🐛 Describe the bug ### Describe the bug Batch invariance mode (`VLLM_BATCH_INVARIANT=1`) fai...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: lel_size=1, max_num_seqs=32, max_model_len=8192, dtype="bfloat16", gpu_memory_utilization=0.9, enforce_eager=enforce_eager, attention_config={"backend": backend}, ) sp = SamplingParams(temperature=0.6, top_p=1.0, max_to...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33383](https://github.com/vllm-project/vllm/pull/33383) | closes_keyword | 0.95 | [Bugfix] Disable torch.compile for batch invariance on Blackwell to ensure determinism | Fixes #32992 ### Observation - Batch invariance works on Blackwell with `enforce_eager=True` - Batch invariance fails on Blackwell with `torch.compile` enabled - Batch invariance |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
