# vllm-project/vllm#8453: [RFC]: Support encode only models by Workflow Defined Engine

| 字段 | 值 |
| --- | --- |
| Issue | [#8453](https://github.com/vllm-project/vllm/issues/8453) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;quantization |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Support encode only models by Workflow Defined Engine

### Issue 正文摘录

### Motivation. As vllm supports more and more models and functions, they require different attention, scheduler, executor, and input output processor. . These modules are becoming increasingly complex, and sometimes new features must be compromised for compatibility. ultimately leading to suboptimal results Take support for encode only models as an example Although the encode only models is much simpler than the decode model, they are very different. The simplest way to support the encode only models is to implement different modules for models of different architectures and load the required modules on demand. I call this architecture Workflow Defined Engine, or WDE for short. ### Terminology. The scope of discussion is slightly larger than encode only models, and is roughly divided into three categories： - Encode only models. (Bidirectional Transformers, causal=False), Often fine-tuned as retriever and reranker etc. - Decode only models. (masked multi-head attention, causal=True). There are two interesting uses: - Output last hidden states as a feature extractor - Decode only retriever （I don't know of a better name），E.g. e5-mistral-7b （The only Embed model currently supported...

## 现有链接修复摘要

#5447 [Model] Bert Embedding Model | #7496 add causal parameter for flash attention | #8462 [Core]: Support encode only models (xlm-roberta、bge-m3...) by Workflow Defined Engine | #9124 [Core]: (2/N) Support prefill only models by Workflow Defined Engine - Prefill only attention

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [RFC]: Support encode only models by Workflow Defined Engine RFC;stale ### Motivation. As vllm supports more and more models and functions, they require different attention, scheduler, executor, and input output process...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: here is only the prefill stage. In order to make the terminology more precise, prefill only is used below. You can think of prefill only as encode only fancy writing. add more: Natural language processing (NLP) can be d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: de only models is to implement different modules for models of different architectures and load the required modules on demand. I call this architecture Workflow Defined Engine, or WDE for short. ### Terminology. The sc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC]: Support encode only models by Workflow Defined Engine RFC;stale ### Motivation. As vllm supports more and more models and functions, they require different attention, scheduler, executor, and input output process...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ble bidirectional Features supported and tested: - WDE core - Attention Backend for prefill only models - Flash Attention Backend - Torch SDPA Backend - XFormers Backend - FlashInfer Backend (Because prefill only models...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5447](https://github.com/vllm-project/vllm/pull/5447) | mentioned | 0.45 | [Model] Bert Embedding Model | #3187 #5737 #6498 #7969） - bge-reranker-v2-m3 (#8022) - bert (#5179 #5447 #7496) - bge v1.5 family which rely on bert ( #7506 #5502) - snowflake arctic embed (family) (#7792) (the |
| [#7496](https://github.com/vllm-project/vllm/pull/7496) | mentioned | 0.45 | add causal parameter for flash attention | #5737 #6498 #7969） - bge-reranker-v2-m3 (#8022) - bert (#5179 #5447 #7496) - bge v1.5 family which rely on bert ( #7506 #5502) - snowflake arctic embed (family) (#7792) (the archit |
| [#8462](https://github.com/vllm-project/vllm/pull/8462) | mentioned | 0.6 | [Core]: Support encode only models (xlm-roberta、bge-m3...) by Workflow Defined Engine | -m3...) by Workflow Defined Engine FILL IN THE PR DESCRIPTION HERE #8453 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <detail |
| [#9124](https://github.com/vllm-project/vllm/pull/9124) | mentioned | 0.6 | [Core]: (2/N) Support prefill only models by Workflow Defined Engine - Prefill only attention | ncoder only) models. Motivatio\Terminology\Proposed Change etc. PTAL #8453 - Proof of Concept, most features and all models are already supported and tested in #8452 - Discuss how |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
