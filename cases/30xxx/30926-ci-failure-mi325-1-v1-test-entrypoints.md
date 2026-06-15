# vllm-project/vllm#30926: [CI Failure]: mi325_1: V1 Test entrypoints

| 字段 | 值 |
| --- | --- |
| Issue | [#30926](https://github.com/vllm-project/vllm/issues/30926) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build |
| 子分类 |  |
| Operator 关键词 | attention |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: V1 Test entrypoints

### Issue 正文摘录

### Name of failing test `pytest -v -s v1/entrypoints` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` =========================== short test summary info ============================ 2025-12-17 21:06:17 UTC FAILED v1/entrypoints/llm/test_struct_output_generate.py::test_structured_output_auto_mode[Qwen/Qwen2.5-1.5B-Instruct-auto] 2025-12-17 21:06:17 UTC FAILED v1/entrypoints/llm/test_struct_output_generate.py::test_guidance_no_additional_properties 2025-12-17 21:06:17 UTC ERROR v1/entrypoints/openai/serving_responses/test_image.py::test_single_chat_session_image[2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg-Qwen/Qwen2.5-VL-3B-Instruct] 2025-12-17 21:06:17 UTC ERROR v1/entrypoints/openai/serving_responses/test_image.py::test_single_chat_session_image[Grayscale_8bits_palette_sample_image.png-Qwen/Qwen2.5-VL-3B-Instruct] 2025-12-17 21:06:17 UTC ERROR v1/entrypoints/openai/serving_responses/test_image.py::test_single_chat_session_image[1280px-Venn_diagram_rgb.svg.png-Qwen/Qwen2.5-VL-3B-Instruct] 2025-12-17 21:06:17 UTC ERROR v1/entrypoints/openai/serving_respo...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: This test is failing for two reasons: 1. xgrammar falls back to guidance backend for structured decoding and guidance fails on AMD. However this is not an AMD specific reason, this is a general bug in guidance where the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_1: V1 Test entrypoints ci-failure ### Name of failing test `pytest -v -s v1/entrypoints` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. b
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ure ### Name of failing test `pytest -v -s v1/entrypoints` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: -v -s v1/entrypoints` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` =========================== sh...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: enai/serving_responses/test_image.py::test_single_chat_session_image[Grayscale_8bits_palette_sample_image.png-Qwen/Qwen2.5-VL-3B-Instruct] 2025-12-17 21:06:17 UTC ERROR v1/entrypoints/openai/serving_responses/test_image...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
