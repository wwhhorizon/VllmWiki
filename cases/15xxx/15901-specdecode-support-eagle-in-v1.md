# vllm-project/vllm#15901: [SpecDecode] Support EAGLE in V1

| 字段 | 值 |
| --- | --- |
| Issue | [#15901](https://github.com/vllm-project/vllm/issues/15901) |
| 状态 | closed |
| 标签 | speculative-decoding;stale;v1 |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cache;cuda;sampling |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [SpecDecode] Support EAGLE in V1

### Issue 正文摘录

- [x] 1. Correctly initializing and loading the EAGLE draft model - [x] 2. Consider the lookahead slots in the KV cache manager - [x] 3. Cache `draft_probs` inside the model runner and correctly feed it to the rejection sampler in the next step (temporarily workaround: #16899) - [x] 4. Handle the edge cases like when the draft model generates beyond `max_pos_embeddings` - [ ] 5. Handle the seeds correctly - [ ] 6. Do E2E correctness and performance tests - [x] 7. Support prefix caching. Eagle requires special handling because Eagle's i-th KV cache is coupled with the i+1-th token ID. (@LiuXiaoxuanPKU) - [ ] 8. Properly handle the sampling parameters that are not (currently) compatible with spec decoding (e.g., min_p). - [x] 9. Use CUDA graphs for draft model. (@luyuzhe111) - [x] 10. Support Eagle 3 (https://github.com/vllm-project/vllm/pull/16937) _Originally posted by @WoosukKwon in https://github.com/vllm-project/vllm/issues/15729#issuecomment-2765192455_

## 现有链接修复摘要

#17560 [WIP][V1][Spec Decode] EAGLE tree-attention

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [SpecDecode] Support EAGLE in V1 speculative-decoding;stale;v1 - [x] 1. Correctly initializing and loading the EAGLE draft model - [x] 2. Consider the lookahead slots in the KV cache manager - [x] 3. Cache `draft_probs`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: and performance tests - [x] 7. Support prefix caching. Eagle requires special handling because Eagle's i-th KV cache is coupled with the i+1-th token ID. (@LiuXiaoxuanPKU) - [ ] 8. Properly handle the sampling parameter...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ot (currently) compatible with spec decoding (e.g., min_p). - [x] 9. Use CUDA graphs for draft model. (@luyuzhe111) - [x] 10. Support Eagle 3 (https://github.com/vllm-project/vllm/pull/16937) _Originally posted by @Woos...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ading the EAGLE draft model - [x] 2. Consider the lookahead slots in the KV cache manager - [x] 3. Cache `draft_probs` inside the model runner and correctly feed it to the rejection sampler in the next step (temporarily...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: lizing and loading the EAGLE draft model - [x] 2. Consider the lookahead slots in the KV cache manager - [x] 3. Cache `draft_probs` inside the model runner and correctly feed it to the rejection sampler in the next step...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#17560](https://github.com/vllm-project/vllm/pull/17560) | mentioned | 0.6 | [WIP][V1][Spec Decode] EAGLE tree-attention | [WIP][V1][Spec Decode] EAGLE tree-attention As mentioned in #15901, currently we only support top-1 selection from the candidates from the EAGLE model (we call it chain-draft), |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
