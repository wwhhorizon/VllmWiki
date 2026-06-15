# vllm-project/vllm#27442: [CI Failure][AMD] Encoder-Decoder Models Fail on AMD CI

| 字段 | 值 |
| --- | --- |
| Issue | [#27442](https://github.com/vllm-project/vllm/issues/27442) |
| 状态 | closed |
| 标签 | rocm;multi-modality;ci-failure |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | install |
| Operator 关键词 | attention |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure][AMD] Encoder-Decoder Models Fail on AMD CI

### Issue 正文摘录

### Name of failing test entrypoints/openai/test_transcription_validation.py::test_basic_audio[openai/whisper-large-v3-turbo] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ## Summary Encoder-decoder models (Whisper, T5, BART, vision-language models) fail on AMD ROCm with `NotImplementedError` because **all ROCm-specific attention backends only support decoder-only models**. Therefore, all the tests using these models will fail on AMD CI([example](https://buildkite.com/vllm/ci/builds/35670#019a04ed-a2f7-4e7e-85ad-4e2118f76898)), mainly in `Entrypoints Integration Test (API Server)` and `Entrypoints Integration Test (Pooling)`. ### Affected Models - **Speech-to-Text**: Whisper family (`openai/whisper-large-v3-turbo`, `mistralai/Voxtral-Mini-3B-2507`) - **Vision-Language**: `microsoft/Phi-3.5-vision-instruct` - **Translation**: T5, BART, MarianMT models - **Any model with cross-attention**: Encoder-decoder architectures ### Failure Mode **Error**: ``` NotImplementedError: Encoder self-attention and encoder/decoder cross-attention are not implemented for TritonAttention...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [CI Failure][AMD] Encoder-Decoder Models Fail on AMD CI rocm;multi-modality;ci-failure ### Name of failing test entrypoints/openai/test_transcription_validation.py::test_basic_audio[openai/whisper-large-v3-turbo] ### Ba...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: MD ROCm with `NotImplementedError` because **all ROCm-specific attention backends only support decoder-only models**. Therefore, all the tests using these models will fail on AMD CI([example](https://buildkite.com/vllm/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure][AMD] Encoder-Decoder Models Fail on AMD CI rocm;multi-modality;ci-failure ### Name of failing test entrypoints/openai/test_transcription_validation.py::test_basic_audio[openai/whisper-large-v3-turbo] ### Ba
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure][AMD] Encoder-Decoder Models Fail on AMD CI rocm;multi-modality;ci-failure ### Name of failing test entrypoints/openai/test_transcription_validation.py::test_basic_audio[openai/whisper-large-v3-turbo] ### Ba...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: isper-large-v3-turbo] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ## Summary Encoder-decoder models...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
