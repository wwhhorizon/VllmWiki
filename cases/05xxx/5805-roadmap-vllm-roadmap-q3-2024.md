# vllm-project/vllm#5805: [Roadmap] vLLM Roadmap Q3 2024

| 字段 | 值 |
| --- | --- |
| Issue | [#5805](https://github.com/vllm-project/vllm/issues/5805) |
| 状态 | closed |
| 标签 |  |
| 评论 | 42; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | attention;cache;fp8;gemm;quantization;sampling |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Roadmap] vLLM Roadmap Q3 2024

### Issue 正文摘录

Update: * Please see #6801 for major items in performance sprint. * Please see #8779 for major items in a new architecture aim at simplicity and performance. * We are in the feedback gathering phase for Q4 roadmap! --- This document includes the features in vLLM's roadmap for Q3 2024. Please feel free to discuss and contribute, as this roadmap is shaped by the vLLM community. ### Themes. As before, we categorized our roadmap into 6 broad themes: * **Broad model support**: vLLM should support a wide range of transformer based models. It should be kept up to date as much as possible. This includes new auto-regressive decoder models, encoder-decoder models, hybrid architectures, and models supporting multi-modal inputs. * **Excellent hardware coverage**: vLLM should run on a wide range of accelerators for production AI workload. This includes GPUs, tensor accelerators, and CPUs. We will work closely with hardware vendors to ensure vLLM utilizes the greatest performance out of the chip. * **Performance optimization**:vLLM should be kept up to date with the latest performance optimization techniques. Users of vLLM can trust its performance to be competitive and strong. * **Production l...

## 现有链接修复摘要

#4412 [Core] Pipeline Parallel Support | #4837 [Core] Cross-attention KV caching and memory-management (towards eventual encoder/decoder model support) | #4888 [Kernel] Correctly invoke prefill & decode kernels for cross-attention (towards eventual encoder/decoder model support) | #4942 [Core] Subclass ModelRunner to support cross-attention & encoder sequences (towards eventual encoder/decoder model support) | #5447 [Model] Bert Embedding Model | #5770 [Model] Initial Support for Chameleon

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: e kept up to date as much as possible. This includes new auto-regressive decoder models, encoder-decoder models, hybrid architectures, and models supporting multi-modal inputs. * **Excellent hardware coverage**: vLLM sh...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 400B+ when released) - [x] Via Pipeline Parallelism #4412 - [x] Via FP8 - [x] New Attention Mechanism (Jamba, Phi3-Small, etc) - [x] Encoder Decoder (#4837, #4888, #4942) - [x] Multi-Modal #4194 Help wanted: - [ ] Whisp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tems in performance sprint. * Please see #8779 for major items in a new architecture aim at simplicity and performance. * We are in the feedback gathering phase for Q4 roadmap! --- This document includes the features in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: As before, we categorized our roadmap into 6 broad themes: * **Broad model support**: vLLM should support a wide range of transformer based models. It should be kept up to date as much as possible. This includes new aut...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: . * Please see #8779 for major items in a new architecture aim at simplicity and performance. * We are in the feedback gathering phase for Q4 roadmap! --- This document includes the features in vLLM's roadmap for Q3 202...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4412](https://github.com/vllm-project/vllm/pull/4412) | mentioned | 0.45 | [Core] Pipeline Parallel Support | otron4, llama3 400b+ when released) - [x] via pipeline parallelism #4412 - [x] via fp8 - [x] new attention mechanism (jamba, phi3-small, etc) - [x] encoder decoder (#4837, #488 |
| [#4837](https://github.com/vllm-project/vllm/pull/4837) | mentioned | 0.45 | [Core] Cross-attention KV caching and memory-management (towards eventual encoder/decoder model support) | attention mechanism (jamba, phi3-small, etc) - [x] encoder decoder (#4837, #4888, #4942) - [x] multi-modal #4194 help wanted: - [ ] whisper and the audio api - [ ] arbitrary h |
| [#4888](https://github.com/vllm-project/vllm/pull/4888) | mentioned | 0.45 | [Kernel] Correctly invoke prefill & decode kernels for cross-attention (towards eventual encoder/decoder model support) | ion mechanism (jamba, phi3-small, etc) - [x] encoder decoder (#4837, #4888, #4942) - [x] multi-modal #4194 help wanted: - [ ] whisper and the audio api - [ ] arbitrary hf model |
| [#4942](https://github.com/vllm-project/vllm/pull/4942) | mentioned | 0.45 | [Core] Subclass ModelRunner to support cross-attention & encoder sequences (towards eventual encoder/decoder model support) | hanism (jamba, phi3-small, etc) - [x] encoder decoder (#4837, #4888, #4942) - [x] multi-modal #4194 help wanted: - [ ] whisper and the audio api - [ ] arbitrary hf model - [x] |
| [#5447](https://github.com/vllm-project/vllm/pull/5447) | mentioned | 0.45 | [Model] Bert Embedding Model | reward model api - [ ] embedding model expansion (bert, xlmroberta) (#5447) ### hardware support - [ ] a feature matrix for all the hardware that vllm supports, and their maturity |
| [#5770](https://github.com/vllm-project/vllm/pull/5770) | mentioned | 0.45 | [Model] Initial Support for Chameleon | whisper and the audio api - [ ] arbitrary hf model - [x] chameleon (#5770) - [ ] multi token prediction - [ ] reward model api - [ ] embedding model expansion (bert, xlmroberta) (# |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
