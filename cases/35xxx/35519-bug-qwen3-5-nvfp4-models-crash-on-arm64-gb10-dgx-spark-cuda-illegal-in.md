# vllm-project/vllm#35519: [Bug]: Qwen3.5 NVFP4 models crash on ARM64 GB10 DGX Spark (CUDA illegal instruction during generation)

| 字段 | 值 |
| --- | --- |
| Issue | [#35519](https://github.com/vllm-project/vllm/issues/35519) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 NVFP4 models crash on ARM64 GB10 DGX Spark (CUDA illegal instruction during generation)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On ARM64 architecture (Grace CPU) with a GB10 Blackwell GPU, the NVFP4 support for Qwen3.5 checkpoints (txn545/Qwen3.5-35B-A3B-NVFP4 and txn545/Qwen3.5-122B-A10B-NVFP4) fails to execute due to an underlying kernel incompatibility. Default Mode (CUDA Graphs Enabled): The engine initializes, profiles, and captures CUDA graphs successfully. It processes the prefill but crashes during generation (at around 31 tokens/s) with a CUDA illegal instruction error. Fallback Mode (--enforce-eager): The engine crashes earlier during the dummy run memory profiling phase with an AttributeError in layernorm.py due to a missing activation attribute. Workaround Attempted (Failed) I attempted to bypass the eager mode AttributeError by patching line 595 in vllm/model_executor/layers/layernorm.py from "activation=self.activation," to "activation=getattr(self, 'activation', None),". While this patch successfully allowed the engine to pass the profiling phase and begin generation, it immediately crashed with the exact same CUDA illegal instruction error seen in the default mode. This confirms the underlying NVFP4 math kernels contain instructions incomp...

## 现有链接修复摘要

#35947 fix: Software E2M1 conversion for SM12x NVFP4 activation quantization

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Qwen3.5 NVFP4 models crash on ARM64 GB10 DGX Spark (CUDA illegal instruction during generation) bug ### Your current environment ### 🐛 Describe the bug On ARM64 architecture (Grace CPU) with a GB10 Blackwell GPU,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: equently asked questions. correctness activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Qwen3.5 NVFP4 models crash on ARM64 GB10 DGX Spark (CUDA illegal instruction during generation) bug ### Your current environment ### 🐛 Describe the bug On ARM64 architecture (Grace CPU) with a GB10 Blackwell GPU,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: lizes, profiles, and captures CUDA graphs successfully. It processes the prefill but crashes during generation (at around 31 tokens/s) with a CUDA illegal instruction error. Fallback Mode (--enforce-eager): The engine c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: patibility. Default Mode (CUDA Graphs Enabled): The engine initializes, profiles, and captures CUDA graphs successfully. It processes the prefill but crashes during generation (at around 31 tokens/s) with a CUDA illegal...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35947](https://github.com/vllm-project/vllm/pull/35947) | closes_keyword | 0.95 | fix: Software E2M1 conversion for SM12x NVFP4 activation quantization | Fixes #35519, #30163 Contributed by [Second Nature Computing](https://joinsecondnature.com) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
