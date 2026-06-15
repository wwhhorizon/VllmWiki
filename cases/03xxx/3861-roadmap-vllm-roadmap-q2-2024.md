# vllm-project/vllm#3861: [Roadmap] vLLM Roadmap Q2 2024

| 字段 | 值 |
| --- | --- |
| Issue | [#3861](https://github.com/vllm-project/vllm/issues/3861) |
| 状态 | closed |
| 标签 |  |
| 评论 | 39; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Roadmap] vLLM Roadmap Q2 2024

### Issue 正文摘录

This document includes the features in vLLM's roadmap for Q2 2024. Please feel free to discuss and contribute to the specific features at related RFC/Issues/PRs and add anything else you'd like to talk about in this issue. You can see our historical roadmap at #2681, #244. This roadmap contains work committed by the vLLM team from UC Berkeley, as well as the broader vLLM contributor groups including but not limited to Anyscale, IBM, NeuralMagic, Roblox, Oracle Cloud. You can also find help wanted items in this roadmap as well! Additionally, this roadmap is shaped by you, our user community! ### Themes. We categorized our roadmap into 6 broad themes: * **Broad model support**: vLLM should support a wide range of transformer based models. It should be kept up to date as much as possible. This includes new auto-regressive decoder models, encoder-decoder models, hybrid architectures, and models supporting multi-modal inputs. * **Excellent hardware coverage**: vLLM should run on a wide range of accelerators for production AI workload. This includes GPUs, tensor accelerators, and CPUs. We will work closely with hardware vendors to ensure vLLM utilizes the greatest performance out of the...

## 现有链接修复摘要

#2188 [WIP] Speculative decoding using a draft model | #2888 AI Controller Interface (AICI) integration | #3117 Add Encoder-decoder model support and T5 Model support | #3538 [2/N] Chunked prefill data update | #3734 [Model][Misc] Add e5-mistral-7b-instruct and Embedding API

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: ludes new auto-regressive decoder models, encoder-decoder models, hybrid architectures, and models supporting multi-modal inputs. * **Excellent hardware coverage**: vLLM should run on a wide range of accelerators for pr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: e kept up to date as much as possible. This includes new auto-regressive decoder models, encoder-decoder models, hybrid architectures, and models supporting multi-modal inputs. * **Excellent hardware coverage**: vLLM sh...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: oadmap for Q2 2024. Please feel free to discuss and contribute to the specific features at related RFC/Issues/PRs and add anything else you'd like to talk about in this issue. You can see our historical roadmap at #2681...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ### Themes. We categorized our roadmap into 6 broad themes: * **Broad model support**: vLLM should support a wide range of transformer based models. It should be kept up to date as much as possible. This includes new au...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: od abstractions to support a wide range of scheduling policies, hardware backends, and inference optimizations. We will work on refactoring the codebase to support that. ### Broad Model Support - [ ] Encoder Decoder Mod...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#2188](https://github.com/vllm-project/vllm/pull/2188) | mentioned | 0.45 | [WIP] Speculative decoding using a draft model | egated prefill (#2370) - [x] speculative decoding fully merged in (#2188) - [x] turn chunked prefill/sarathi/splitfuse on by default (#3538) * memory management - [x] automati |
| [#2888](https://github.com/vllm-project/vllm/pull/2888) | mentioned | 0.45 | AI Controller Interface (AICI) integration | tion) and extensibility (outlines #3715, lmformatenforcer #3713, aici #2888 ) help wanted: * sparse kv cache (h2o, compression, fastdecode) * speculative decoding - [ ] propo |
| [#3117](https://github.com/vllm-project/vllm/pull/3117) | mentioned | 0.45 | Add Encoder-decoder model support and T5 Model support | ### broad model support - [ ] encoder decoder models - [ ] t5 #3117 - [ ] whisper - [x] embedding #3187 - [ ] hybrid architecture (jamba) #3690 - [x] decoder only embe |
| [#3538](https://github.com/vllm-project/vllm/pull/3538) | mentioned | 0.45 | [2/N] Chunked prefill data update | #2188) - [x] turn chunked prefill/sarathi/splitfuse on by default (#3538) * memory management - [x] automatic prefix caching enhancement - [x] tgi feature parity (stop string ha |
| [#3734](https://github.com/vllm-project/vllm/pull/3734) | mentioned | 0.45 | [Model][Misc] Add e5-mistral-7b-instruct and Embedding API | brid architecture (jamba) #3690 - [x] decoder only embedding models #3734 - [ ] prefix tuning support help wanted: - [x] more vision transformers beyond llava - [x] support priv |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
