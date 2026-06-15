# vllm-project/vllm#31848: [RFC]: Native Weight Syncing APIs

| 字段 | 值 |
| --- | --- |
| Issue | [#31848](https://github.com/vllm-project/vllm/issues/31848) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Native Weight Syncing APIs

### Issue 正文摘录

### Implementation Progress - [x] PR 1: New APIs, NCCL, new examples, quantized reloading integration https://github.com/vllm-project/vllm/pull/31943 - [x] PR 2: IPC: https://github.com/vllm-project/vllm/pull/34171 - [x] new IPC weight engine - [x] new examples (offline and http) - [ ] PR 3: Follow ups - [ ] caching metadata for NCCLWeightTransferUpdateInfo - [ ] Confirm this works okay with quantized models - [ ] investigate memory usage with layerwise reloading - [ ] qwen 30b example: https://github.com/vllm-project/vllm/pull/37334 - [ ] enable multigpu IPC examples/ optimizations https://github.com/NVIDIA-NeMo/RL/discussions/1189 - [ ] Alternative method for enabling endpoints (currently using `DEV_MODE`) - [ ] figuring out how to make this work without `VLLM_ALLOW_INSECURE_SERIALIZATION` - [ ] Make trainer side functions for each engine into separate library - [ ] APIs for dynamically adding/destroying NCCL groups - [ ] ensure create process groups works with all parallelisms - [ ] tracking weight versions https://github.com/vllm-project/vllm/pull/31943#issuecomment-3834098959 - [x] remove old weight_sync examples: https://github.com/vllm-project/vllm/pull/36188 - [x] update d...

## 现有链接修复摘要

#31943 [Feat][RL][1/2] Native Weight Syncing API: NCCL

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: C ### Implementation Progress - [x] PR 1: New APIs, NCCL, new examples, quantized reloading integration https://github.com/vllm-project/vllm/pull/31943 - [x] PR 2: IPC: https://github.com/vllm-project/vllm/pull/34171 -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ghtTransferUpdateInfo - [ ] Confirm this works okay with quantized models - [ ] investigate memory usage with layerwise reloading - [ ] qwen 30b example: https://github.com/vllm-project/vllm/pull/37334 - [ ] enable mult...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [RFC]: Native Weight Syncing APIs RFC ### Implementation Progress - [x] PR 1: New APIs, NCCL, new examples, quantized reloading integration https://github.com/vllm-project/vllm/pull/31943 - [x] PR 2: IPC: https://github...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: groups - [ ] ensure create process groups works with all parallelisms - [ ] tracking weight versions https://github.com/vllm-project/vllm/pull/31943#issuecomment-3834098959 - [x] remove old weight_sync examples: https:/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: on @SumanthRH vLLM serves not only as an inference runtime for serving requests from end users, but also as a means of serving requests for large language model post-training. The vLLM model weights must be synced perio...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31943](https://github.com/vllm-project/vllm/pull/31943) | mentioned | 0.6 | [Feat][RL][1/2] Native Weight Syncing API: NCCL | requires users to version-lock to specific implementations. See [RFC #31848](https://github.com/vllm-project/vllm/issues/31848) for full motivation. ### New APIs Three new endpoin… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
