# vllm-project/vllm#39096: [Bug]: Batch invariance breaks with torch.compile and/or CUDA graphs on SM<90

| 字段 | 值 |
| --- | --- |
| Issue | [#39096](https://github.com/vllm-project/vllm/issues/39096) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;kernel;operator |
| 症状 | build_error;nondeterministic |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Batch invariance breaks with torch.compile and/or CUDA graphs on SM<90

### Issue 正文摘录

Your current environment Reproducible on L4 (NVIDIA, compute capability 8.9). The broader class of issue is expected to affect any SM&lt;90 GPU (Ampere SM80, Ada Lovelace SM89, etc.) when running with batch invariance under torch.compile and/or CUDA graphs. Describe the bug On SM&lt;90 GPUs, VLLM_BATCH_INVARIANT=1 does not produce batch-invariant outputs when combined with either torch.compile or CUDA graphs (and both are enabled by default via enforce_eager=False ). This causes speculative decoding tests that rely on strict batch invariance (such as tests/v1/distributed/test_eagle_dp.py ) to fail intermittently, the same model with the same weights and the same input context produces different greedy argmax outputs depending on batch size. This is known and partially documented: tests/v1/determinism/utils.py notes # Note: For devices with SM &lt; 90, batch invariance does not support CUDA Graphs , and all 5 existing batch invariance tests in tests/v1/determinism/test_batch_invariance.py set enforce_eager=IS_DEVICE_CAPABILITY_BELOW_90 to work around it (introduced in #30018). However, the scope is broader than that comment suggests, disabling only CUDA graphs (with torch.compile s...

## 现有链接修复摘要

#27660 [Feature] Batch invariant torch.compile | #30018 [Feature] Batch-Invariant Support for FA2 and LoRA | #38938 Bug/test eagle dp v0

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 6: [Bug]: Batch invariance breaks with torch.compile and/or CUDA graphs on SM<90 bug Your current environment Reproducible on L4 (NVIDIA, compute capability 8.9). The broader class of issue is expected to affect any SM&lt;...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Batch invariance breaks with torch.compile and/or CUDA graphs on SM<90 bug Your current environment Reproducible on L4 (NVIDIA, compute capability 8.9). The broader class of issue is expected to affect any SM&lt;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Batch invariance breaks with torch.compile and/or CUDA graphs on SM<90 bug Your current environment Reproducible on L4 (NVIDIA, compute capability 8.9). The broader class of issue is expected to affect any SM&lt;...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: tch_invariant_mode() def rms_norm_native(x, weight, eps=1e-5): orig_dtype = x.dtype x = x.to(torch.float32) variance = x.pow(2).mean(dim=-1, keepdim=True) x = x * torch.rsqrt(variance + eps) x = x.to(orig_dtype) return...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tests/v1/distributed/test_eagle_dp.py ) to fail intermittently, the same model with the same weights and the same input context produces different greedy argmax outputs depending on batch size. This is known and partial...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27660](https://github.com/vllm-project/vllm/pull/27660) | mentioned | 0.45 | [Feature] Batch invariant torch.compile | as the first workaround for this class of issue.</li> <li><strong>pr #27660</strong> - earlier batch invariance + <code>torch.compile</code> work, tested on deepseek with h100-cla… |
| [#30018](https://github.com/vllm-project/vllm/pull/30018) | mentioned | 0.45 | [Feature] Batch-Invariant Support for FA2 and LoRA | - original flaky test issue (resolved by #38938).</li> <li><strong>pr #30018</strong> - introduced <code>enforce_eager=is_device_capability_below_90</code> across the determinism… |
| [#38938](https://github.com/vllm-project/vllm/pull/38938) | mentioned | 0.6 | Bug/test eagle dp v0 | is also implicated, not just CUDA graphs. The broader tracking is in [#39096](updated). Plus, adding the EAGLE DP tests to the Distributed Tests (2 GPUs)(H100) group. The PR inclu… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
