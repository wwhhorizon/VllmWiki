# vllm-project/vllm#38991: [Bug]: runai_safetensors_weights_iterator yields tensors in nondeterministic order, breaking FP8 inference on some platforms

| 字段 | 值 |
| --- | --- |
| Issue | [#38991](https://github.com/vllm-project/vllm/issues/38991) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: runai_safetensors_weights_iterator yields tensors in nondeterministic order, breaking FP8 inference on some platforms

### Issue 正文摘录

### Your current environment - vLLM 0.18.1 / 0.18.2rc1 (upstream nightly, `vllm/vllm-openai:cu130-nightly`) - Platforms tested: DGX Spark (GB10, arm64), AGX Thor (arm64), DGX H100 (x86), GB200 NVL (arm64), GB300 NVL (arm64) - Models: nemotron-edge-4b (FP8, NVFP4), nemotron-super-v1.5-49b (NVFP4) ### Describe the bug `runai_safetensors_weights_iterator` yields tensors that are **views into a shared numpy buffer** from the runai-model-streamer library. When these tensors are loaded into model parameters via `param.data.copy_(loaded_weight)`, the copy is a **cross-device operation** (CPU tensor → CUDA parameter) because `BaseModelLoader.load_model()` creates model parameters on CUDA inside a `with target_device:` context. On **unified memory** platforms (DGX Spark, AGX Thor), this cross-device `copy_()` is **asynchronous** — it goes through the CUDA copy engine but both source and destination are in the same physical memory. The Python generator advances before the copy completes, and subsequent streamer I/O can modify the shared buffer while earlier copies are still in-flight, causing data corruption. On **discrete GPU** platforms (H100, GB200, GB300), the same `copy_()` is a DMA tr...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: sors_weights_iterator yields tensors in nondeterministic order, breaking FP8 inference on some platforms ### Your current environment - vLLM 0.18.1 / 0.18.2rc1 (upstream nightly, `vllm/vllm-openai:cu130-nightly`) - Plat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: tly`) - Platforms tested: DGX Spark (GB10, arm64), AGX Thor (arm64), DGX H100 (x86), GB200 NVL (arm64), GB300 NVL (arm64) - Models: nemotron-edge-4b (FP8, NVFP4), nemotron-super-v1.5-49b (NVFP4) ### Describe the bug `ru...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: [Bug]: runai_safetensors_weights_iterator yields tensors in nondeterministic order, breaking FP8 inference on some platforms ### Your current environment - vLLM 0.18.1 / 0.18.2rc1 (upstream nightly, `vllm/vllm-openai:cu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: weight loading and post-processing — one barrier after all loads is sufficient - **Clone** proves the shared buffer is the source of the race — detaching tensors eliminates it entirely ### Platform impact | Platform | A...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: AGX Thor (arm64), DGX H100 (x86), GB200 NVL (arm64), GB300 NVL (arm64) - Models: nemotron-edge-4b (FP8, NVFP4), nemotron-super-v1.5-49b (NVFP4) ### Describe the bug `runai_safetensors_weights_iterator` yields tensors th...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
