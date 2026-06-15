# vllm-project/vllm#38868: Gemma 4 support: model_type `gemma4` not recognized

| 字段 | 值 |
| --- | --- |
| Issue | [#38868](https://github.com/vllm-project/vllm/issues/38868) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Gemma 4 support: model_type `gemma4` not recognized

### Issue 正文摘录

## Summary Google released the Gemma 4 model family ([gemma-4-E2B-it](https://huggingface.co/google/gemma-4-E2B-it), [gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)) which introduces a new `model_type: gemma4`. This model type was added in `transformers >= 5.5.0`, but vLLM currently ships with an older version. ## Error ``` The checkpoint you are trying to load has model type `gemma4` but Transformers does not recognize this architecture. ``` ## Steps to reproduce ```bash vllm serve 2imi9/gemma-4-E2B-it-NVFP4A16 ``` Or with any Gemma 4 model (e.g. `google/gemma-4-E2B-it`, `google/gemma-4-E4B-it`). ## Key details - Gemma 4 is a multimodal model (vision + audio + text) using `AutoModelForImageTextToText` - Architecture includes `vision_tower`, `audio_tower`, `embed_vision`, `embed_audio` modules - Requires `transformers >= 5.5.0` for `gemma4` model type registration ## Related - vllm-project/llm-compressor#2562 — same transformers version issue in llm-compressor - vllm-project/llm-compressor#2561 — Gemma 4 NVFP4A16 quantization example

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Gemma 4 support: model_type `gemma4` not recognized ## Summary Google released the Gemma 4 model family ([gemma-4-E2B-it](https://huggingface.co/google/gemma-4-E2B-it), [gemma-4-E4B-it](https://huggingface.co/google/gem
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ure. ``` ## Steps to reproduce ```bash vllm serve 2imi9/gemma-4-E2B-it-NVFP4A16 ``` Or with any Gemma 4 model (e.g. `google/gemma-4-E2B-it`, `google/gemma-4-E4B-it`). ## Key details - Gemma 4 is a multimodal model (visi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: his model type was added in `transformers >= 5.5.0`, but vLLM currently ships with an older version. ## Error ``` The checkpoint you are trying to load has model type `gemma4` but Transformers does not recognize this ar...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: but Transformers does not recognize this architecture. ``` ## Steps to reproduce ```bash vllm serve 2imi9/gemma-4-E2B-it-NVFP4A16 ``` Or with any Gemma 4 model (e.g. `google/gemma-4-E2B-it`, `google/gemma-4-E4B-it`). ##...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: added in `transformers >= 5.5.0`, but vLLM currently ships with an older version. ## Error ``` The checkpoint you are trying to load has model type `gemma4` but Transformers does not recognize this architecture. ``` ##...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
