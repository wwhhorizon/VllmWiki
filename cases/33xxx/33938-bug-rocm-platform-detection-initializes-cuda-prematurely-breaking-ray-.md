# vllm-project/vllm#33938: [Bug][ROCm] Platform detection initializes CUDA prematurely, breaking Ray multi-GPU allocation

| 字段 | 值 |
| --- | --- |
| Issue | [#33938](https://github.com/vllm-project/vllm/issues/33938) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][ROCm] Platform detection initializes CUDA prematurely, breaking Ray multi-GPU allocation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On ROCm, importing `vllm.platforms` triggers `torch.cuda.get_device_properties()` at module load time. This initializes CUDA before Ray workers can set `CUDA_VISIBLE_DEVICES`, locking `device_count()` to the total number of GPUs. As a result, when running multiple vLLM engines with `tensor_parallel_size=1`, all workers incorrectly use GPU 0 instead of their assigned GPUs. Probably related issues: - https://github.com/ROCm/ROCm/issues/5780 - https://github.com/vllm-project/vllm/issues/12572 ## Minimal reproduction ```python import os for key in ["CUDA_VISIBLE_DEVICES", "HIP_VISIBLE_DEVICES", "ROCR_VISIBLE_DEVICES"]: os.environ.pop(key, None) import torch from vllm.platforms import current_platform os.environ["CUDA_VISIBLE_DEVICES"] = "0" assert torch.cuda.device_count() == 1, f"Expected 1, got {torch.cuda.device_count()}" ``` ## Problematic code in `vllm/platforms/rocm.py` ```python @cache def on_gfx9() -> bool: GPU_ARCH = torch.cuda.get_device_properties("cuda").gcnArchName # Initializes CUDA! return any(arch in GPU_ARCH for arch in ["gfx90a", "gfx942", "gfx950"]) # Similar for on_gfx1x(), on_mi3xx(), on_gfx942(), on_gfx950(), et...

## 现有链接修复摘要

#34108 [ROCm][Bugfix] Resolve Dynamo tracing crash from amdsmi calls in on_gfx* arch detection

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug][ROCm] Platform detection initializes CUDA prematurely, breaking Ray multi-GPU allocation bug;rocm ### Your current environment ### 🐛 Describe the bug On ROCm, importing `vllm.platforms` triggers `torch.cuda.get_de...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: g;rocm ### Your current environment ### 🐛 Describe the bug On ROCm, importing `vllm.platforms` triggers `torch.cuda.get_device_properties()` at module load time. This initializes CUDA before Ray workers can set `CUDA_VI...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;kernel;operator;sampling;triton build_error;nan_inf env_dependency #34108 [ROCm][Bugfix] Resolve Dynamo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: gits;scheduler_memory;speculative_decoding cuda;kernel;operator;sampling;triton build_error;nan_inf env_dependency #34108 [ROCm][Bugfix] Resolve Dynamo tracing crash from amdsmi calls in on_gfx* arch detection Your curr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;kernel;operator;sampling;triton build_error;nan_inf env_dependency #34108...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34108](https://github.com/vllm-project/vllm/pull/34108) | closes_keyword | 0.95 | [ROCm][Bugfix] Resolve Dynamo tracing crash from amdsmi calls in on_gfx* arch detection | fixed: pytest -s -v "tests/models/language/pooling_mteb_test/test_nomic.py::test_embed_models_mteb[model_info3]" ``` <details> <summary>Verify #33938 (early CUDA init) is still f |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
