# vllm-project/vllm#9006: [Roadmap] vLLM Roadmap Q4 2024

| 字段 | 值 |
| --- | --- |
| Issue | [#9006](https://github.com/vllm-project/vllm/issues/9006) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 30; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cache;gemm;kernel;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Roadmap] vLLM Roadmap Q4 2024

### Issue 正文摘录

### Themes. As before, we categorized our roadmap into 6 broad themes: broad model support, wide hardware coverage, state of the art performance optimization, production level engine, strong OSS community, and extensible architectures. As we are seeing more ### Broad Model Support - [x] Enhance LLM Support - [x] Hybrid/Interleaved Attention (#9464) - [x] Enhance Multi-Modality in vLLM (#4194) - [x] Enhance Support for State Space Models (Mamba) - [x] Reward Model API (#8967) - [ ] Arbitrary HF model (a collaboration with Hugging Face!) - [ ] #11330 - [ ] Whisper Help wanted: - [x] Expand coverage for encoder-decoder models (Bert, XLMRoberta, BGE, T5) - #9056 - #10400 - [ ] API for streaming input (in particular for audio) ### Hardware Support - [x] A feature matrix for all the hardware that vLLM supports, and their maturity level - [ ] Expanding features support on various hardwares - [ ] Fast PagedAttention and Chunked Prefill on Inferentia - [x] Upstream of Intel Gaudi - [x] Enhancements in TPU Support - [x] Upstream enhancements in AMD MI300x - [x] Performance enhancement and measurement for NVIDIA H200 - [ ] New accelerator support: IBM Spyre Help wanted: - [x] Design for plug...

## 现有链接修复摘要

#9056 Support `BERTModel` (first `encoder-only` embedding model) | #11330 [Model]: Add `transformers` backend support | #11928 [Core] Cache policy framework

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Roadmap] vLLM Roadmap Q4 2024 stale ### Themes. As before, we categorized our roadmap into 6 broad themes: broad model support, wide hardware coverage, state of the art performance optimization, production level engine...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: IBM Spyre Help wanted: - [x] Design for pluggable, out-of-tree hardware backend similar to PyTorch’s PrivateUse API - [ ] Prototype JAX support ### Performance Optimizations - [ ] Turn on chunked prefill, prefix caching...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: , FlashInfer, FlexAttention, Triton) - [x] Native integration with torch.compile Help wanted: - [ ] A fast ngrams speculator - [ ] Sparse KV cache framework (#5751) - [ ] Long context optimizations: context parallelism,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: imization, production level engine, strong OSS community, and extensible architectures. As we are seeing more ### Broad Model Support - [x] Enhance LLM Support - [x] Hybrid/Interleaved Attention (#9464) - [x] Enhance Mu...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: torch.compile Help wanted: - [ ] A fast ngrams speculator - [ ] Sparse KV cache framework (#5751) - [ ] Long context optimizations: context parallelism, etc. ### Production Features - [x] KV cache offload to CPU and dis...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9056](https://github.com/vllm-project/vllm/pull/9056) | mentioned | 0.45 | Support `BERTModel` (first `encoder-only` embedding model) | coverage for encoder-decoder models (bert, xlmroberta, bge, t5) - #9056 - #10400 - [ ] api for streaming input (in particular for audio) ### hardware support - [x] a feature |
| [#11330](https://github.com/vllm-project/vllm/pull/11330) | mentioned | 0.45 | [Model]: Add `transformers` backend support | [ ] arbitrary hf model (a collaboration with hugging face!) - [ ] #11330 - [ ] whisper help wanted: - [x] expand coverage for encoder-decoder models (bert, xlmroberta, bge, t5) |
| [#11928](https://github.com/vllm-project/vllm/pull/11928) | mentioned | 0.6 | [Core] Cache policy framework | work on KV cache management when I read Simon posted Roadmap Q4 2024 (#9006), which listed Sparse KV cache framework. After digging it for some time, I realized that Sliding Windo… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
