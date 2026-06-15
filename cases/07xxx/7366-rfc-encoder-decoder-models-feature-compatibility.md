# vllm-project/vllm#7366: [RFC]: Encoder/decoder models & feature compatibility

| 字段 | 值 |
| --- | --- |
| Issue | [#7366](https://github.com/vllm-project/vllm/issues/7366) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 25; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | install |
| Operator 关键词 | attention;cache;fp8;gemm;kernel;operator;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Encoder/decoder models & feature compatibility

### Issue 正文摘录

## Motivation # There is significant interest in vLLM supporting encoder/decoder models. Issues #187 and #180 , for example, request encoder/decoder model support. As a result encoder/decoder support was recently introduced to vLLM via the following three PRs: * #4837 * #4888 * #4942 These three PRs make encoder/decoder model inference possible; however, they leave more to be desired in terms of (1) parity between vLLM's decoder-only & encoder/decoder request processing pipelines with respect to feature support, and (2) the number of encoder/decoder models which are supported. The ask for the vLLM community is to contribute PRs which help bring vLLM encoder/decoder functionality to a similar level of maturity as that of vLLM's decoder-only functionality. ## Proposed changes # The support matrix below summarizes which encoder/decoder models have already been added & which features are currently compatible with the vLLM encoder/decoder pipeline, versus which features & models will require additional PRs to implement in the long-term: Model/feature Model is already available/feature is already compatible with encoder-decoder? Having this model/making this feature compatible is a long...

## 现有链接修复摘要

#3117 Add Encoder-decoder model support and T5 Model support | #4837 [Core] Cross-attention KV caching and memory-management (towards eventual encoder/decoder model support) | #4888 [Kernel] Correctly invoke prefill & decode kernels for cross-attention (towards eventual encoder/decoder model support) | #4942 [Core] Subclass ModelRunner to support cross-attention & encoder sequences (towards eventual encoder/decoder model support)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [RFC]: Encoder/decoder models & feature compatibility RFC;stale ## Motivation # There is significant interest in vLLM supporting encoder/decoder models. Issues #187 and #180 , for example, request encoder/decoder model...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: and Whisper in the same PR; that way, the Whisper model may be used to facilitate an end-to-end test with of audio multimodality. #### Add T5 model # Note: T5 depends on [custom attention bias being supported](#support-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [RFC]: Encoder/decoder models & feature compatibility RFC;stale ## Motivation # There is significant interest in vLLM supporting encoder/decoder models. Issues #187 and #180 , for example, request encoder/decoder model...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: support encoder attention and cross-attention: * The backend's `AttentionMetadata` subclass must support fields for encoder sequence lengths, encoder sequence token count, cross-attention blocktables, and cross-attentio...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: Other enc/dec models No Yes Quantization Untested Yes Multimodality No Yes Attention backends other than Xformers (esp. flash-attn, flashinfer) No Yes Cus

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#3117](https://github.com/vllm-project/vllm/pull/3117) | mentioned | 0.45 | Add Encoder-decoder model support and T5 Model support | was added to `pagedattention` in an older version of vllm as part of #3117 ; given changes in vllm since then, additional work would be required to integrate this implementation.… |
| [#4837](https://github.com/vllm-project/vllm/pull/4837) | mentioned | 0.45 | [Core] Cross-attention KV caching and memory-management (towards eventual encoder/decoder model support) | ort was recently introduced to vllm via the following three prs: * #4837 * #4888 * #4942 these three prs make encoder/decoder model inference possible; however, they leave mo |
| [#4888](https://github.com/vllm-project/vllm/pull/4888) | mentioned | 0.45 | [Kernel] Correctly invoke prefill & decode kernels for cross-attention (towards eventual encoder/decoder model support) | cently introduced to vllm via the following three prs: * #4837 * #4888 * #4942 these three prs make encoder/decoder model inference possible; however, they leave more to be d |
| [#4942](https://github.com/vllm-project/vllm/pull/4942) | mentioned | 0.45 | [Core] Subclass ModelRunner to support cross-attention & encoder sequences (towards eventual encoder/decoder model support) | roduced to vllm via the following three prs: * #4837 * #4888 * #4942 these three prs make encoder/decoder model inference possible; however, they leave more to be desired in |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
