# vllm-project/vllm#27094: [RFC]: Remove redundant multi-modal input preprocessing during disaggregated inference

| 字段 | 值 |
| --- | --- |
| Issue | [#27094](https://github.com/vllm-project/vllm/issues/27094) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support;multimodal_vlm;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | gemm |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Remove redundant multi-modal input preprocessing during disaggregated inference

### Issue 正文摘录

### Motivation. E/P/D disaggregation is actively in development from #25233, but the preprocessing of multi-modal inputs is repeated among all workers in the inference path. Following "Multimodal processing simplification" in the Q4 2025 roadmap #26376, I propose to add something like`image_embeds_dummy` in the content type of the input of LLM.chat and LLM.generate. Currently, LLM.generate can take `multi_modal_data` with preprocessed raw tensors like the Qwen2-VL example in the [official document page](https://docs.vllm.ai/en/latest/features/multimodal_inputs.html#embedding-inputs), but still it requires to send image values or preprocessed tokens between E-P workers. We may want the request only contain the metadata (e.g. image size, hash value) of the input after the encoding stage. ## Profiler result To measure the impact of the preprocessor, I ran PyTorch profilers and breakdown each steps of a single request of an 1024x1024px image with a single text token by the E-P-D disaggregation of #25233. - Model: Qwen/Qwen2.5-VL-3B-Instruct - Device: 3x RTX3090, AMD EPYC 7F52 16-core - Interconnection: PCIe (E -> P), NVLink (P -> D) **CPU - entrypoint** **GPU - model runner** - End-to...

## 现有链接修复摘要

#25233 [Core] Encoder separation for Encode-Prefill-Decode Disaggregation

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: inputs is repeated among all workers in the inference path. Following "Multimodal processing simplification" in the Q4 2025 roadmap #26376, I propose to add something like`image_embeds_dummy` in the content type of the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ndant multi-modal input preprocessing during disaggregated inference RFC;stale ### Motivation. E/P/D disaggregation is actively in development from #25233, but the preprocessing of multi-modal inputs is repeated among a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ata` with preprocessed raw tensors like the Qwen2-VL example in the [official document page](https://docs.vllm.ai/en/latest/features/multimodal_inputs.html#embedding-inputs), but still it requires to send image values o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: "pixel_values": {"type": "tensor", "shape": [16, 1176], "dtype": "torch.float32"}, "image_grid_thw": {"type": "tensor", "value": [[1, 4, 4]], "dtype": "torch.int64"} }, }, { "type": "text", "text": "What's i
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: aggregation of #25233. - Model: Qwen/Qwen2.5-VL-3B-Instruct - Device: 3x RTX3090, AMD EPYC 7F52 16-core - Interconnection: PCIe (E -> P), NVLink (P -> D) **CPU - entrypoint** **GPU - model runner** - End-to-end Mean TTF...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#25233](https://github.com/vllm-project/vllm/pull/25233) | mentioned | 0.45 | [Core] Encoder separation for Encode-Prefill-Decode Disaggregation | x1024px image with a single text token by the e-p-d disaggregation of #25233. - model: qwen/qwen2.5-vl-3b-instruct - device: 3x rtx3090, amd epyc 7f52 16-core - interconnection: p… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
