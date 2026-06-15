# vllm-project/vllm#29536: [CI Failure]: mi325_1: Multi-Modal Models Test (Extended) 2

| 字段 | 值 |
| --- | --- |
| Issue | [#29536](https://github.com/vllm-project/vllm/issues/29536) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;multimodal_vlm |
| 子分类 | precision |
| Operator 关键词 | attention |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Multi-Modal Models Test (Extended) 2

### Issue 正文摘录

### Name of failing test `pip install git+https://github.com/TIGER-AI-Lab/Mantis.git; pytest -v -s models/multimodal/generation/test_common.py -m 'split(group=0) and not core_model'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests Summary:** **ovis2_5 model (test_case8-11)** - Tests: `test_single_image_models`, `test_multi_image_models`, `test_video_models` - Failure type: Logprob comparison mismatch between vLLM and HuggingFace outputs - Configuration: dtype=half, model=AIDC-AI/Ovis2.5-2B with image/multi-image/video inputs - Likely cause: Numerical precision differences in visual encoder or attention computations between vLLM and HF implementations. **smolvlm model (test_case21-24)** - Tests: `test_single_image_models`, `test_multi_image_models` - Failure type: Logprob comparison mismatch - Configuration: dtype varies, model=HuggingFaceTB/SmolVLM2-2.2B-Instruct with image inputs - Likely cause: SmolVLM2's Idefics3-based architecture may have numerical stability issues in the vision-text fusion layers when compiled **minimax_vl_01 model (test_case29-3...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [CI Failure]: mi325_1: Multi-Modal Models Test (Extended) 2 ci-failure ### Name of failing test `pip install git+https://github.com/TIGER-AI-Lab/Mantis.git; pytest -v -s models/multimodal/generation/test_common.py -m 's...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 6: and not core_model'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests Summary:** **ovis2_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: mi325_1: Multi-Modal Models Test (Extended) 2 ci-failure ### Name of failing test `pip install git+https://github.com/TIGER-AI-Lab/Mantis.git; pytest -v -s models/multimodal/generation/test_common.py -m 'sp
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: omparison mismatch between vLLM and HuggingFace outputs - Configuration: dtype=half, model=AIDC-AI/Ovis2.5-2B with image/multi-image/video inputs - Likely cause: Numerical precision differences in visual encoder or atte...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: _image_models`, `test_video_models` - Failure type: Logprob comparison mismatch between vLLM and HuggingFace outputs - Configuration: dtype=half, model=AIDC-AI/Ovis2.5-2B with image/multi-image/video inputs - Likely cau...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
