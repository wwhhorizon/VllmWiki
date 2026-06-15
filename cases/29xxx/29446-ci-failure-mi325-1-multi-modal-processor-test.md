# vllm-project/vllm#29446: [CI Failure]: mi325_1: Multi-Modal Processor Test

| 字段 | 值 |
| --- | --- |
| Issue | [#29446](https://github.com/vllm-project/vllm/issues/29446) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Multi-Modal Processor Test

### Issue 正文摘录

### Name of failing test `pip install git+https://github.com/TIGER-AI-Lab/Mantis.git && pytest -v -s models/multimodal/processing` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This test validates **multimodal input processing correctness** for vision-language models in vLLM, comparing cached vs non-cached processing paths. **Purpose:** Ensures that the `MultiModalProcessorOnlyCache` produces identical results to baseline (uncached) processing across different multimodal inputs (images, videos, audio). **Test Flow:** 1. **Parameterized testing** across multiple models, hit rates, and batch configurations 2. **Generates random multimodal data** with controlled cache hit rates (0.3, 0.5, 1.0) 3. **Creates two processors**: baseline (no cache) and cached versions 4. **Compares outputs** for both text and token prompts 5. **Validates equivalence** of processed inputs using `_assert_inputs_equal` **Special Handling:** - Model-specific patches for GLM4.1V and Qwen3-VL (video metadata requirements) - Skipped models: `google/gemma-3n-E2B-it`, `OpenGVLab/InternVL2-2B`, `jina...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: p install git+https://github.com/TIGER-AI-Lab/Mantis.git && pytest -v -s models/multimodal/processing` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: mi325_1: Multi-Modal Processor Test ci-failure ### Name of failing test `pip install git+https://github.com/TIGER-AI-Lab/Mantis.git && pytest -v -s models/multimodal/processing` ### Basic information - [
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ultimodal/processing` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This test validates **multimodal i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ial Handling:** - Model-specific patches for GLM4.1V and Qwen3-VL (video metadata requirements) - Skipped models: `google/gemma-3n-E2B-it`, `OpenGVLab/InternVL2-2B`, `jinaai/jina-reranker-m0` (marked "Fix later") - Igno...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: .1V and Qwen3-VL (video metadata requirements) - Skipped models: `google/gemma-3n-E2B-it`, `OpenGVLab/InternVL2-2B`, `jinaai/jina-reranker-m0` (marked "Fix later") - Ignores specific keys for certain models (e.g., Ultra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
