# vllm-project/vllm#38382: [Transformers v5] Mistral multimodal models

| 字段 | 值 |
| --- | --- |
| Issue | [#38382](https://github.com/vllm-project/vllm/issues/38382) |
| 状态 | closed |
| 标签 | help wanted;good first issue |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Transformers v5] Mistral multimodal models

### Issue 正文摘录

This is a sub-issue forming part of the work in https://github.com/vllm-project/vllm/issues/38379, please read the description of this issue before beginning to work on this one. ## Which test is failing? ```console $ pytest tests/entrypoints/openai/speech_to_text/test_transcription_validation.py::test_basic_audio[mistralai/Voxtral-Mini-3B-2507] ... (EngineCore pid=1621824) File "/home/harry/vllm/vllm/multimodal/processing/processor.py", line 1374, in _merge_mm_kwargs (EngineCore pid=1621824) missing_kwargs_item = missing_kwargs[missing_next_idx] (EngineCore pid=1621824) ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^ (EngineCore pid=1621824) IndexError: list index out of range ``` Appears to have been caused by the refacor in https://github.com/vllm-project/vllm/pull/38018, which was made using v5.3, but processors were refactored in v5.4, which was just released. Related test failures: ``` [2026-03-27T01:26:17Z] FAILED entrypoints/openai/realtime/test_realtime_validation.py::test_multi_chunk_streaming[mistralai/Voxtral-Mini-4B-Realtime-2602] - RuntimeError: Server exited unexpectedly. [2026-03-27T01:26:17Z] FAILED entrypoints/openai/realtime/test_realtime_validation.py::test_empty_commit_does_...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Transformers v5] Mistral multimodal models help wanted;good first issue This is a sub-issue forming part of the work in https://github.com/vllm-project/vllm/issues/38379, please read the description of this issue befor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: _mm_fields_config`). ``` ## How to configure my environment? It's very important that you install both vLLM and Transformers from source so that your test results reflect the current state of both libraries. ```console...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: y::test_model_tensor_schema[mistralai/Mistral-Large-3-675B-Instruct-2512-NVFP4] - RuntimeError: Expected there to be 3 image items in keyword arguments corresponding to 3 image data items, but only found 0! There is lik...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: essing/test_tensor_schema.py::test_model_tensor_schema[mistralai/Mistral-Small-3.1-24B-Instruct-2503] - RuntimeError: Expected there to be 3 image items in keyword arguments corresponding to 3 image data items, but only...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: escription of this issue before beginning to work on this one. ## Which test is failing? ```console $ pytest tests/entrypoints/openai/speech_to_text/test_transcription_validation.py::test_basic_audio[mistralai/Voxtral-M...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
