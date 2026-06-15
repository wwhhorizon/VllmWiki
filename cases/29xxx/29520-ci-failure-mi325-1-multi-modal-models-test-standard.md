# vllm-project/vllm#29520: [CI Failure]: mi325_1: Multi-Modal Models Test (Standard)

| 字段 | 值 |
| --- | --- |
| Issue | [#29520](https://github.com/vllm-project/vllm/issues/29520) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;model_support;multimodal_vlm;sampling_logits |
| 子分类 |  |
| Operator 关键词 | sampling |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Multi-Modal Models Test (Standard)

### Issue 正文摘录

### Name of failing test ` pip install git+https://github.com/TIGER-AI-Lab/Mantis.git && pip freeze | grep -E 'torch' && pytest -v -s models/multimodal -m core_model --ignore models/multimodal/generation/test_whisper.py --ignore models/multimodal/processing && cd .. && VLLM_WORKER_MULTIPROC_METHOD=spawn pytest -v -s tests/models/multimodal/generation/test_whisper.py -m core_model` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests Summary:** **test_single_image_models** in `test_common.py` (6 failures) - Tests: qwen2_5_vl (test_case60-62), qwen3_vl (test_case65-67) - Failure: Engine process crash during multimodal generation - Configuration: Single image input with various size factors and dtypes - Likely cause: Memory or compute instability in Qwen vision models during image encoding, possibly related to EVS (Efficient Video Sampling) or vision tower processing differences between vLLM and HF implementations. **test_multi_image_models** in `test_common.py` (1 failure) - Tests: qwen3_vl (test_case66) - Failure: Engine core process died unexpectedly - Conf...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [CI Failure]: mi325_1: Multi-Modal Models Test (Standard) ci-failure ### Name of failing test ` pip install git+https://github.com/TIGER-AI-Lab/Mantis.git && pip freeze | grep -E 'torch' && pytest -v -s models/multimoda...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: mi325_1: Multi-Modal Models Test (Standard) ci-failure ### Name of failing test ` pip install git+https://github.com/TIGER-AI-Lab/Mantis.git && pip freeze | grep -E 'torch' && pytest -v -s models/multimodal
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: per.py -m core_model` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests Summary:** **test_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ration - Configuration: Single image input with various size factors and dtypes - Likely cause: Memory or compute instability in Qwen vision models during image encoding, possibly related to EVS (Efficient Video Samplin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi325_1: Multi-Modal Models Test (Standard) ci-failure ### Name of failing test ` pip install git+https://github.com/TIGER-AI-Lab/Mantis.git && pip freeze | grep -E 'torch' && pytest -v -s models/multimoda...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
