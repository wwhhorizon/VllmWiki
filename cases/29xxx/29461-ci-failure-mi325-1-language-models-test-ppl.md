# vllm-project/vllm#29461: [CI Failure]: mi325_1: Language Models Test (PPL)

| 字段 | 值 |
| --- | --- |
| Issue | [#29461](https://github.com/vllm-project/vllm/issues/29461) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | precision |
| Operator 关键词 | kernel |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Language Models Test (PPL)

### Issue 正文摘录

### Name of failing test `pytest -v -s models/language/generation_ppl_test` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **4 perplexity tests** - Comparing vLLM vs HuggingFace Transformers perplexity scores 1. `test_ppl[model_info0]` in `test_gemma.py` - google/gemma-2b perplexity test 2. `test_ppl[model_info1]` in `test_gemma.py` - google/gemma-2-2b perplexity test 3. `test_ppl[model_info2]` in `test_gemma.py` - google/gemma-3-4b-it perplexity test 4. `test_ppl[model_info0]` in `test_gpt.py` - openai-community/gpt2-large perplexity test **Failure:** AssertionError at `ppl_utils.py:128` - `assert differ < atol` **Configuration:** - Wikitext-2 dataset, MAX_LENGTH=1024, tolerance=0.01 (1%) - Test computes `differ = (vllm_ppl - hf_ppl) / hf_ppl` - Qwen models passed (2 passed tests) **Likely cause:** vLLM's perplexity scores exceed the 1% tolerance threshold compared to HuggingFace Transformers baseline on ROCm hardware. This is architecture-specific (affects Gemma and GPT2 but not Qwen), suggesting numerical differences in ROCm kernel implementations or precision han...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [CI Failure]: mi325_1: Language Models Test (PPL) ci-failure ### Name of failing test `pytest -v -s models/language/generation_ppl_test` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: /generation_ppl_test` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **4 perplexity tests** - Comparing...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_1: Language Models Test (PPL) ci-failure ### Name of failing test `pytest -v -s models/language/generation_ppl_test` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused b
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 1% tolerance threshold compared to HuggingFace Transformers baseline on ROCm hardware. This is architecture-specific (affects Gemma and GPT2 but not Qwen), suggesting numerical differences in ROCm kernel implementations...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: Face Transformers perplexity scores 1. `test_ppl[model_info0]` in `test_gemma.py` - google/gemma-2b perplexity test 2. `test_ppl[model_info1]` in `test_gemma.py` - google/gemma-2-2b perplexity test 3. `test_ppl[model_in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
