# vllm-project/vllm#29509: [CI Failure]: mi325_1: Multi-Modal Models Test (Extended) 3

| 字段 | 值 |
| --- | --- |
| Issue | [#29509](https://github.com/vllm-project/vllm/issues/29509) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Multi-Modal Models Test (Extended) 3

### Issue 正文摘录

### Name of failing test `pip install git+https://github.com/TIGER-AI-Lab/Mantis.git && pytest -v -s models/multimodal/generation/test_common.py -m 'split(group=1) and not core_model'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Multiple tests in `test_common.py` across different model architectures: - `test_single_image_models` (kimi_vl, pixtral_hf, glm4_1v, glm4v) - `test_multi_image_models` (gemma3, kimi_vl, pixtral_hf, glm4_1v) - `test_custom_inputs_models` (glm4_1v-video) **Total: 23 failed tests** **Failure Type:** `AssertionError` in `models/utils.py:242` during logprob comparison **Error Pattern:** ``` hf: ' ...' {0: nan, 1: nan, 2: nan, ...} vllm: '2.) . . . .The...' {1050: Logprob(logprob=-2.72, rank=1, ...)} ``` **Configuration:** - Models: kimi_vl, pixtral_hf, glm4_1v, glm4v, gemma3 - Test types: Single/multi-image inputs, custom video inputs - Various size factors and parameters **Likely Cause:** HuggingFace runner initialization failure - The HF models are producing all ` ` tokens with NaN logprobs, indicating the model/processor is not properly init...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [CI Failure]: mi325_1: Multi-Modal Models Test (Extended) 3 ci-failure ### Name of failing test `pip install git+https://github.com/TIGER-AI-Lab/Mantis.git && pytest -v -s models/multimodal/generation/test_common.py -m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: mi325_1: Multi-Modal Models Test (Extended) 3 ci-failure ### Name of failing test `pip install git+https://github.com/TIGER-AI-Lab/Mantis.git && pytest -v -s models/multimodal/generation/test_common.py -m '
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: and not core_model'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Multiple tests in `test_common.py`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: failing test Multiple tests in `test_common.py` across different model architectures: - `test_single_image_models` (kimi_vl, pixtral_hf, glm4_1v, glm4v) - `test_multi_image_models` (gemma3, kimi_vl, pixtral_hf, glm4_1v)...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: dels` (kimi_vl, pixtral_hf, glm4_1v, glm4v) - `test_multi_image_models` (gemma3, kimi_vl, pixtral_hf, glm4_1v) - `test_custom_inputs_models` (glm4_1v-video) **Total: 23 failed tests** **Failure Type:** `AssertionError`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
