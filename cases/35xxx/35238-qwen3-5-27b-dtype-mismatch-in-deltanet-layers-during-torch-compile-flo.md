# vllm-project/vllm#35238: Qwen3.5-27B dtype mismatch in DeltaNet layers during torch.compile (float != c10::Half)

| 字段 | 值 |
| --- | --- |
| Issue | [#35238](https://github.com/vllm-project/vllm/issues/35238) |
| 状态 | closed |
| 标签 | torch.compile |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;gemm_linear;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;gemm;kernel;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Qwen3.5-27B dtype mismatch in DeltaNet layers during torch.compile (float != c10::Half)

### Issue 正文摘录

## Bug: dtype mismatch in DeltaNet linear attention layers during torch.compile ### Environment - **vLLM**: 0.16.0rc2.dev438+gfc8456c33 (nightly) - **PyTorch**: 2.10+cu130 - **GPUs**: 2x RTX 5090 (WSL2) - **CUDA Toolkit**: 13.0 - **Model**: `cyankiwi/Qwen3.5-27B-AWQ-4bit` (compressed-tensors quantization) ### Description When launching Qwen3.5-27B without `--enforce-eager`, torch.compile crashes during the memory profiling phase with a dtype mismatch in the DeltaNet linear attention layers. The compiled kernel attempts `extern_kernels.mm()` with a float32 buffer against a float16 weight. This also affects Qwen3-Next-80B-A3B models — same DeltaNet architecture, same crash. ### Error ``` RuntimeError: expected mat1 and mat2 to have the same dtype, but got: float != c10::Half ``` Full traceback points to a torch._inductor generated kernel: ``` File "/tmp/torchinductor_carl/7b/c7b76qoro4aew2bm5x5h2nsjlfzlm2evbwatoevs5juyksnx5277.py", line 1368, in call extern_kernels.mm(buf3, reinterpret_tensor(arg4_1, (3072, 5120), (1, 3072), 0), out=buf4) ``` The crash occurs during `model_runner.profile_run()` → `determine_available_memory()`. ### Reproduction ```bash vllm serve cyankiwi/Qwen3.5-27...

## 现有链接修复摘要

#35256 [Bugfix] Fix dtype mismatch in RMSNormGated.forward_native() during torch.compile

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: Qwen3.5-27B dtype mismatch in DeltaNet layers during torch.compile (float != c10::Half) torch.compile ## Bug: dtype mismatch in DeltaNet linear attention layers during torch.compile ### Environment - **vLLM**: 0.16.0rc2...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Qwen3.5-27B dtype mismatch in DeltaNet layers during torch.compile (float != c10::Half) torch.compile ## Bug: dtype mismatch in DeltaNet linear attention layers during torch.compile ### Environment - **vLLM**: 0.16.0rc2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Qwen3.5-27B dtype mismatch in DeltaNet layers during torch.compile (float != c10::Half) torch.compile ## Bug: dtype mismatch in DeltaNet linear attention layers during torch.compile ### Environment - **vLLM**: 0.16.0rc2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Qwen3.5-27B dtype mismatch in DeltaNet layers during torch.compile (float != c10::Half) torch.compile ## Bug: dtype mismatch in DeltaNet linear attention layers during torch.compile ### Environment - **vLLM**: 0.16.0rc2
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 5-27B without `--enforce-eager`, torch.compile crashes during the memory profiling phase with a dtype mismatch in the DeltaNet linear attention layers. The compiled kernel attempts `extern_kernels.mm()` with a float32 b...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35256](https://github.com/vllm-project/vllm/pull/35256) | closes_keyword | 0.95 | [Bugfix] Fix dtype mismatch in RMSNormGated.forward_native() during torch.compile | Fixes #35238. When `torch.compile` is active (the default with Inductor backend), vLLM disables custom ops (`custom_ops=["none"]`). This causes `RMSNormGated` to dispatch to `forw |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
