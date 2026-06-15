# vllm-project/vllm#28947: [Tracking Issue][Performance]: Speculative decoding performance/QoL improvements

| 字段 | 值 |
| --- | --- |
| Issue | [#28947](https://github.com/vllm-project/vllm/issues/28947) |
| 状态 | open |
| 标签 | performance;stale;nvidia |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | kernel;sampling;triton |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Tracking Issue][Performance]: Speculative decoding performance/QoL improvements

### Issue 正文摘录

Below are some of the items that help improve the usability and performance of speculative decoding in vLLM. Please feel free to review, suggest and collaborate if you are interested! Point of Contact: @benchislett, drafted/maintained by @benchislett ## New Drafting Styles - [x] Draft-model support (Merged #24322) - [x] Parallel Drafting (PARD, P-EAGLE) (Merged #32887) - [ ] DFlash Parallel Drafting (WIP #32206) - [ ] NGram-GPU support (In Review https://github.com/vllm-project/vllm/pull/29184) - [ ] Hybrid ngram-eagle drafting (In Review https://github.com/vllm-project/vllm/pull/24344) ## Extending Model Support - [ ] Support more than 1 spec token for DeepSeek V3.2 (Tracking Issue https://github.com/vllm-project/vllm/issues/31845) ## Performance Improvements - [ ] Full CudaGraph for the drafter (Tracking Issue #33341) - [ ] Reduce number of kernels issued in EAGLE drafting - [x] Task 1: optimize prepare_inputs_padded (Merged https://github.com/vllm-project/vllm/pull/28597) - [ ] Task 2: clean up and optimize work done between iterations of the drafter (Tracking Issue #33455) - - [ ] Fuse the slot mapping update into a triton kernel (In Review https://github.com/vllm-project/vllm...

## 现有链接修复摘要

#24322 feat: spec decode with draft models | #29957 [Perf][Async] Implement zero-bubble async speculative decoding | #32887 [Spec Decode] Unified Parallel Drafting

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Tracking Issue][Performance]: Speculative decoding performance/QoL improvements performance;stale;nvidia Below are some of the items that help improve the usability and performance of speculative decoding in vLLM. Plea...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: will save a few redundant copies] (Tracking Issue #33456) - [ ] Misc: Compile the drafter (What exactly does this do?) (In Review https://github.com/vllm-project/vllm/pull/26179) - [ ] First-class support for multimodal...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: drafted/maintained by @benchislett ## New Drafting Styles - [x] Draft-model support (Merged #24322) - [x] Parallel Drafting (PARD, P-EAGLE) (Merged #32887) - [ ] DFlash Parallel Drafting (WIP #32206) - [ ] NGram-GPU sup...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: een iterations of the drafter (Tracking Issue #33455) - - [ ] Fuse the slot mapping update into a triton kernel (In Review https://github.com/vllm-project/vllm/pull/33503) - [ ] Task 3: make eagle’s prepare_inputs metho...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: er (Tracking Issue #33455) - - [ ] Fuse the slot mapping update into a triton kernel (In Review https://github.com/vllm-project/vllm/pull/33503) - [ ] Task 3: make eagle’s prepare_inputs methods stateful [cleaner implem...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24322](https://github.com/vllm-project/vllm/pull/24322) | mentioned | 0.45 | feat: spec decode with draft models | nchislett ## new drafting styles - [x] draft-model support (merged #24322) - [x] parallel drafting (pard, p-eagle) (merged #32887) - [ ] dflash parallel drafting (wip #32206) - [… |
| [#29957](https://github.com/vllm-project/vllm/pull/29957) | mentioned | 0.6 | [Perf][Async] Implement zero-bubble async speculative decoding | om/user-attachments/assets/d6c8e199-8288-4e00-854b-a598cb113798" /> #28947 mention: Improved overlapping beyond drafting time (todo, discussion https://github.com/vllm-project/vll… |
| [#32887](https://github.com/vllm-project/vllm/pull/32887) | mentioned | 0.45 | [Spec Decode] Unified Parallel Drafting | pport (merged #24322) - [x] parallel drafting (pard, p-eagle) (merged #32887) - [ ] dflash parallel drafting (wip #32206) - [ ] ngram-gpu support (in review https://github.com/vll… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
