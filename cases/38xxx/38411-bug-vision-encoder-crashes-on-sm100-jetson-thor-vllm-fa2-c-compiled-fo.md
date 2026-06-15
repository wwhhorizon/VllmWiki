# vllm-project/vllm#38411: [Bug]: Vision encoder crashes on SM100 (Jetson Thor) — `_vllm_fa2_C` compiled for SM80-only, no override available for vision encoder

| 字段 | 值 |
| --- | --- |
| Issue | [#38411](https://github.com/vllm-project/vllm/issues/38411) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 |  |
| Operator 关键词 | attention;cache;cuda;gemm;operator;triton |
| 症状 | build_error;crash;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Vision encoder crashes on SM100 (Jetson Thor) — `_vllm_fa2_C` compiled for SM80-only, no override available for vision encoder

### Issue 正文摘录

### Your current environment **Human Context** I'm running vLLM on an NVIDIA AGX Thor Developer Kit (built on the Blackwell architecture, SM110a, and listed as a supported production target in NVIDIA's NGC container release notes. The issue is narrow and reproducible: we know that language model path works on this hardware because the setting `--attention-backend TRITON_ATTN ` hides the SM80-compiled _vllm_fa2_C library from running. However, the vision encoder path has no equivalent escape, so any multimodal model that uses MMEncoderAttention crashes unconditionally at startup on SM100 hardware during the profiling pass before the server even starts accepting requests. I've verified this across three different container environments (jetson-containers vLLM 0.19.0, NGC vLLM 26.02, and the NVIDIA NIM container), and the failure is consistent and deterministic. The fix appears conceptually straightforward — extend the attention backend override to MMEncoderAttention the same way it already works for the language model — though I recognize I may be missing architectural constraints that make this harder than it looks. **AI** **Environment** - vLLM version: 0.19.0 - Hardware: NVIDIA A...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Vision encoder crashes on SM100 (Jetson Thor) — `_vllm_fa2_C` compiled for SM80-only, no override available for vision encoder bug ### Your current environment **Human Context** I'm running vLLM on an NVIDIA AGX...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Vision encoder crashes on SM100 (Jetson Thor) — `_vllm_fa2_C` compiled for SM80-only, no override available for vision encoder bug ### Your current environment **Human Context** I'm running vLLM on an NVIDIA AGX...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ase notes. The issue is narrow and reproducible: we know that language model path works on this hardware because the setting `--attention-backend TRITON_ATTN ` hides the SM80-compiled _vllm_fa2_C library from running. H...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: arget in NVIDIA's NGC container release notes. The issue is narrow and reproducible: we know that language model path works on this hardware because the setting `--attention-backend TRITON_ATTN ` hides the SM80-compiled...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ttention crashes unconditionally at startup on SM100 hardware during the profiling pass before the server even starts accepting requests. I've verified this across three different container environments (jetson-containe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
