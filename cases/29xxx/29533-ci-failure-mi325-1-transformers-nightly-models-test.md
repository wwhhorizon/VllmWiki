# vllm-project/vllm#29533: [CI Failure]: mi325_1: Transformers Nightly Models Test

| 字段 | 值 |
| --- | --- |
| Issue | [#29533](https://github.com/vllm-project/vllm/issues/29533) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 | install |
| Operator 关键词 | attention;kernel;quantization |
| 症状 | build_error |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Transformers Nightly Models Test

### Issue 正文摘录

### Name of failing test `pip install --upgrade git+https://github.com/huggingface/transformers && pytest -v -s tests/models/test_initialization.py -k 'not (Gemma3 or ModernBert or Qwen2_5_VL or Qwen2_5vl or Qwen2VL or TransformersMultiModalEmbeddingModel or TransformersMultiModalForSequenceClassification or Ultravox or Phi4Multimodal or LlavaNextVideo or MiniCPMO or Lfm2Moe or PaliGemma or RobertaForSequenceClassification or Ovis2_5 or Fuyu or DeepseekOCR or KimiVL)' && pytest -v -s tests/models/test_transformers.py && pytest -v -s tests/models/multimodal/test_mapping.py -k 'not (Gemma3 or Qwen2VL or Qwen2_5_VL)' && python3 examples/offline_inference/basic/chat.py && VLLM_WORKER_MULTIPROC_METHOD=spawn python3 examples/offline_inference/audio_language.py --model-type whisper` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests:** 3 failures in `test_transformers.py` - Transformers backend functionality tests **Tests:** 1. `test_quantization[5-32-TheBloke/TinyLlama-1.1B-Chat-v0.3-GPTQ-quantization_kwargs1]` - GPTQ quantization with Transformers backend 2. `...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 10: [CI Failure]: mi325_1: Transformers Nightly Models Test ci-failure ### Name of failing test `pip install --upgrade git+https://github.com/huggingface/transformers && pytest -v -s tests/models/test_initialization.py -k '...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_1: Transformers Nightly Models Test ci-failure ### Name of failing test `pip install --upgrade git+https://github.com/huggingface/transformers && pytest -v -s tests/models/test_initialization.py -k 'n
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: mers.py` - Transformers backend functionality tests **Tests:** 1. `test_quantization[5-32-TheBloke/TinyLlama-1.1B-Chat-v0.3-GPTQ-quantization_kwargs1]` - GPTQ quantization with Transformers backend 2. `test_pooling[Tran...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Gemma3 or ModernBert or Qwen2_5_VL or Qwen2_5vl or Qwen2VL or TransformersMultiModalEmbeddingModel or TransformersMultiModalForSequenceClassification or Ultravox or Phi4Multimodal or LlavaNextVideo or MiniCPMO or Lfm2Mo...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ransformers && pytest -v -s tests/models/test_initialization.py -k 'not (Gemma3 or ModernBert or Qwen2_5_VL or Qwen2_5vl or Qwen2VL or TransformersMultiModalEmbeddingModel or TransformersMultiModalForSequenceClassificat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
