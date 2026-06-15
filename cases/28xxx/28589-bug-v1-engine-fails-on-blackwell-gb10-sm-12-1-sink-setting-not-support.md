# vllm-project/vllm#28589: [Bug]: V1 Engine fails on Blackwell GB10 (SM 12.1): "sink setting not supported" by all compatible attention backends

| 字段 | 值 |
| --- | --- |
| Issue | [#28589](https://github.com/vllm-project/vllm/issues/28589) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;moe;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 Engine fails on Blackwell GB10 (SM 12.1): "sink setting not supported" by all compatible attention backends

### Issue 正文摘录

### Your current environment # [Bug] V1 Engine fails on Blackwell GB10 (SM 12.1): "sink setting not supported" by all compatible attention backends ## System Information - **GPU**: NVIDIA GB10 (Blackwell architecture, SM 12.1) - **vLLM Version**: 0.11.1rc7.dev41+g6c3c0f823.d20251112 - **PyTorch Version**: 2.6.0 - **CUDA Version**: 13.0 - **Python Version**: 3.12.3 - **OS**: Linux 6.11.0-1016-nvidia ### 🐛 Describe the bug ## Reproduction Steps ### Environment Setup ```bash # Build vLLM from source (commit 6c3c0f823) git clone https://github.com/vllm-project/vllm.git cd vllm git checkout 6c3c0f823 # Patch CUTLASS MoE to avoid undefined symbol error # Comment out lines 256-264 in csrc/quantization/w8a8/cutlass/scaled_mm_entry.cu # (SM100 CUTLASS MoE path - not compiled but referenced) # Build VLLM_TARGET_DEVICE=cuda MAX_JOBS=4 uv pip install -e . ``` ### Attempted Commands All of these fail with the same "sink setting not supported" error: ```bash # Attempt 1: XFormers backend export VLLM_USE_FLASHINFER_MOE_MXFP4_BF16=1 export VLLM_ATTENTION_BACKEND=XFORMERS export VLLM_USE_V1=0 vllm serve openai/gpt-oss-120b \ --quantization mxfp4 \ --dtype bfloat16 \ --max-model-len 16384 \ --no-en...

## 现有链接修复摘要

#33516 [Bugfix] Add SM110/SM120 device capability checks for NVFP4 MoE backends

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 9: MoE to avoid undefined symbol error # Comment out lines 256-264 in csrc/quantization/w8a8/cutlass/scaled_mm_entry.cu # (SM100 CUTLASS MoE path - not compiled but referenced) # Build VLLM_TARGET_DEVICE=cuda MAX_JOBS=4 uv...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: - **GPU**: NVIDIA GB10 (Blackwell architecture, SM 12.1) - **vLLM Version**: 0.11.1rc7.dev41+g6c3c0f823.d20251112 - **PyTorch Version**: 2.6.0 - **CUDA Version**: 13.0 - **Python Version**: 3.12.3 - **OS**: Linux 6.11.0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: V1 Engine fails on Blackwell GB10 (SM 12.1): "sink setting not supported" by all compatible attention backends bug ### Your current environment # [Bug] V1 Engine fails on Blackwell GB10 (SM 12.1): "sink setting n...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: GB10 (SM 12.1): "sink setting not supported" by all compatible attention backends bug ### Your current environment # [Bug] V1 Engine fails on Blackwell GB10 (SM 12.1): "sink setting not supported" by all compatible atte...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tting not supported" by all compatible attention backends ## System Information - **GPU**: NVIDIA GB10 (Blackwell architecture, SM 12.1) - **vLLM Version**: 0.11.1rc7.dev41+g6c3c0f823.d20251112 - **PyTorch Version**: 2....

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33516](https://github.com/vllm-project/vllm/pull/33516) | closes_keyword | 0.95 | [Bugfix] Add SM110/SM120 device capability checks for NVFP4 MoE backends | Fixes #29141 Related to #28589 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
