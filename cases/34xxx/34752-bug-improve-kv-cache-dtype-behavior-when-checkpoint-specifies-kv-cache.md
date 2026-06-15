# vllm-project/vllm#34752: [Bug]: Improve `--kv-cache-dtype` behavior when checkpoint specifies `kv_cache_quant_algo`

| 字段 | 值 |
| --- | --- |
| Issue | [#34752](https://github.com/vllm-project/vllm/issues/34752) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Improve `--kv-cache-dtype` behavior when checkpoint specifies `kv_cache_quant_algo`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The `--kv-cache-dtype` flag doesn't properly handle models that specify `kv_cache_quant_algo` in their checkpoint config (e.g., [nvidia/Qwen3-30B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3-30B-A3B-NVFP4/blob/main/hf_quant_config.json#L8)). Currently, `--kv-cache-dtype auto` falls back to `model_config.dtype` instead of using the checkpoint's specified FP8 quantization. Additionally, explicitly overriding with `--kv-cache-dtype bfloat16` raises an error. ## Expected Behavior **For models that specify `kv_cache_quant_algo` in checkpoint:** | `--kv-cache-dtype` | Expected behavior | Current behavior | Status | |---|---|---|---| | `auto` | Use checkpoint's specified dtype (e.g., FP8) | Falls back to `model_config.dtype` | ❌ Bug | | `fp8` | Use FP8 | Uses FP8 | ✅ Works | | `bfloat16` | Use BF16 (override checkpoint) | Raises error | ❌ Bug | | *(not specified)* | Use checkpoint's specified dtype | Uses checkpoint's specified dtype | ✅ Works | ### For models that DON'T specify `kv_cache_quant_algo` | `--kv-cache-dtype` | Expected behavior | Current behavior | Status | |---|---|---|---| | `auto` | Use `model_config.dtype` | Uses `mod...

## 现有链接修复摘要

#35185 Fix --kv-cache-dtype behavior when checkpoint specifies kv_cache_quant_algo | #35762 fix: raise ValueError when --kv-cache-dtype conflicts with checkpoint kv_cache_quant_algo

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: [Bug]: Improve `--kv-cache-dtype` behavior when checkpoint specifies `kv_cache_quant_algo` bug ### Your current environment ### 🐛 Describe the bug The `--kv-cache-dtype` flag doesn't properly handle models that specify...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 🐛 Describe the bug The `--kv-cache-dtype` flag doesn't properly handle models that specify `kv_cache_quant_algo` in their checkpoint config (e.g., [nvidia/Qwen3-30B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3-30B-A3B...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 57748) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/attention/backends/flashinfer.py", line 1341, in forward (EngineCore_DP0 pid=57748) torch.ops._C_cache_ops.reshape_and_cache_flash( (EngineCore_DP0 pid=57748)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Improve `--kv-cache-dtype` behavior when checkpoint specifies `kv_cache_quant_algo` bug ### Your current environment ### 🐛 Describe the bug The `--kv-cache-dtype` flag doesn't properly handle models that specify...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35185](https://github.com/vllm-project/vllm/pull/35185) | closes_keyword | 0.95 | Fix --kv-cache-dtype behavior when checkpoint specifies kv_cache_quant_algo | Fixes #34752 This PR resolves the `--kv-cache-dtype` configuration issues when models specify `kv_cache_quant_algo` in their checkpoint config. ## Issues Fixed ### 1. `--kv-cac |
| [#35762](https://github.com/vllm-project/vllm/pull/35762) | closes_keyword | 0.95 | fix: raise ValueError when --kv-cache-dtype conflicts with checkpoint kv_cache_quant_algo | Fixes #34752 --- Contributed with appreciation for the vLLM maintainers' dedication to robust and user-friendly quantization support. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
