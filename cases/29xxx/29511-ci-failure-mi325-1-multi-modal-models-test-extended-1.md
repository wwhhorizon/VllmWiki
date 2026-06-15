# vllm-project/vllm#29511: [CI Failure]: mi325_1: Multi-Modal Models Test (Extended) 1

| 字段 | 值 |
| --- | --- |
| Issue | [#29511](https://github.com/vllm-project/vllm/issues/29511) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;multimodal_vlm |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel |
| 症状 | build_error;mismatch |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Multi-Modal Models Test (Extended) 1

### Issue 正文摘录

### Name of failing test `pip install git+https://github.com/TIGER-AI-Lab/Mantis.git && pytest -v -s models/multimodal -m 'not core_model' --ignore models/multimodal/generation/test_common.py --ignore models/multimodal/processing` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test # Failing Tests Summary - Multimodal Models #### 1. **test_granite_speech.py::test_models** Tests IBM Granite Speech model with audio LoRA adapter. **Failure:** Test execution failure (specific error not shown in truncated output) **Configuration:** Model: ibm-granite/granite-speech-3.3-2b, bfloat16, max_model_len=2048, num_logprobs=10 **Likely cause:** Audio encoder or LoRA adapter implementation incompatible with ROCm; audio processing pipeline may use CUDA-specific kernels not properly translated for ROCm. #### 2. **test_pixtral.py::test_chat** (2 failures - different max_model_len) Tests Mistral Pixtral/Small multimodal chat with vision. **Failure:** Logprobs mismatch - numerical differences in output probabilities **Configuration:** Models: Pixtral-12B, Mistral-Small-3.1-24B; max_model_len...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 6: ultimodal/processing` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test # Failing Tests Summary - Multimod...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [CI Failure]: mi325_1: Multi-Modal Models Test (Extended) 1 ci-failure ### Name of failing test `pip install git+https://github.com/TIGER-AI-Lab/Mantis.git && pytest -v -s models/multimodal -m 'not core_model' --ignore...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: cause:** Audio encoder or LoRA adapter implementation incompatible with ROCm; audio processing pipeline may use CUDA-specific kernels not properly translated for ROCm. #### 2. **test_pixtral.py::test_chat** (2 failures...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_1: Multi-Modal Models Test (Extended) 1 ci-failure ### Name of failing test `pip install git+https://github.com/TIGER-AI-Lab/Mantis.git && pytest -v -s models/multimodal -m 'not core_model' --ignore m
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: d output) **Configuration:** Model: ibm-granite/granite-speech-3.3-2b, bfloat16, max_model_len=2048, num_logprobs=10 **Likely cause:** Audio encoder or LoRA adapter implementation incompatible with ROCm; audio processin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
