# vllm-project/vllm#12429: Flash Attention 3 (FA3) Support

| 字段 | 值 |
| --- | --- |
| Issue | [#12429](https://github.com/vllm-project/vllm/issues/12429) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;hardware_porting;quantization |
| 子分类 |  |
| Operator 关键词 | attention;fp8 |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Flash Attention 3 (FA3) Support

### Issue 正文摘录

As of https://github.com/vllm-project/vllm/pull/12093 Flash Attention 3 is now supported in vLLM for Hopper GPUs (SM 9.0). It can also be enabled for SM 8.0 and 8.7 using `VLLM_FLASH_ATTN_VERSION=3`. For 8.6 and 8.9 its fully disabled since they don't have enough shared memory for the current implementation, some work needs to be done here. This issue tracks the remaining features that have yet to be implemented ### Hardware Support - [ ] SM 8.9 Ada Lovelace (L4, L40s) Support - [ ] SM 8.6 Ampere (A6000) Support ### Optimizations - [x] FP8 Attention

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: s) Support - [ ] SM 8.6 Ampere (A6000) Support ### Optimizations - [x] FP8 Attention performance attention_kv_cache;hardware_porting;quantization attention;fp8 dtype As of https://github.com/vllm-project/vllm/pull/12093...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: m-project/vllm/pull/12093 Flash Attention 3 is now supported in vLLM for Hopper GPUs (SM 9.0). It can also be enabled for SM 8.0 and 8.7 using `VLLM_FLASH_ATTN_VERSION=3`. For 8.6 and 8.9 its fully disabled since they d...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Flash Attention 3 (FA3) Support stale As of https://github.com/vllm-project/vllm/pull/12093 Flash Attention 3 is now supported in vLLM for Hopper GPUs (SM 9.0). It can also be enabled for SM 8.0 and 8.7 using `VLLM_FLAS
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 9.0). It can also be enabled for SM 8.0 and 8.7 using `VLLM_FLASH_ATTN_VERSION=3`. For 8.6 and 8.9 its fully disabled since they don't have enough shared memory for the current implementation, some work needs to be done...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Flash Attention 3 (FA3) Support stale As of https://github.com/vllm-project/vllm/pull/12093 Flash Attention 3 is now supported in vLLM for Hopper GPUs (SM 9.0). It can also be enabled for SM 8.0 and 8.7 using `VLLM_FLAS...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
