# vllm-project/vllm#14964: [Feature] [ROCm]: AITER Kernel Integration

| 字段 | 值 |
| --- | --- |
| Issue | [#14964](https://github.com/vllm-project/vllm/issues/14964) |
| 状态 | closed |
| 标签 | feature request;rocm;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | activation;attention;fp8;gemm;kernel;moe;operator;quantization;sampling |
| 症状 |  |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature] [ROCm]: AITER Kernel Integration

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This is an issue that tracks PRs related to AITER https://github.com/ROCm/aiter . _AITER is AMD’s centralized repository that support various of high performance AI operators for AI workloads acceleration, where a good, unified place for all the customer operator-level requests, which can match different customers' needs. Developers can focus on operators, and let the customers integrate this op collection into their own private/public/whatever framework._ *Note*: This issue tracker description has been reorganized from the latest to the oldest ## Based on AITER commit (20 Aug 2025): `5ee37dced6f1bde0229b2c77ce079433549aa25f549aa25f` * [ ] https://github.com/vllm-project/vllm/pull/23336 ## Based on AITER commit (12 July 2025): `916bf3c` * [x] https://github.com/vllm-project/vllm/pull/20880 * [x] https://github.com/vllm-project/vllm/pull/21242 * [x] https://github.com/vllm-project/vllm/pull/22521 * [ ] https://github.com/vllm-project/vllm/pull/22759 ## Based on AITER commit: ` ` * [x] https://github.com/vllm-project/vllm/pull/20295 ## Based on AITER commit: `636a9f0d56c202040e93b9560c296441b7f77233` * [ ] Add weight preshuffled PTPC FP8 GEMM...

## 现有链接修复摘要

#20988 [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: a9f0d56c202040e93b9560c296441b7f77233` * [ ] Add weight preshuffled PTPC FP8 GEMM (https://github.com/vllm-project/vllm/pull/19417) ## Based on AITER commit: `648764942e552a8bb5fe16026703716a81f05374 ` * [x] AITER MHA V...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: /pull/19822 * [ ] Add padding to weight to use block scaled fused moe on Qwen3-235B TP4 (https://github.com/vllm-project/vllm/pull/19234) * [x] https://github.com/vllm-project/vllm/pull/19904 ## Based on AITER commit: `...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: d56c202040e93b9560c296441b7f77233` * [ ] Add weight preshuffled PTPC FP8 GEMM (https://github.com/vllm-project/vllm/pull/19417) ## Based on AITER commit: `648764942e552a8bb5fe16026703716a81f05374 ` * [x] AITER MHA V1 (h...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature] [ROCm]: AITER Kernel Integration feature request;rocm;stale ### 🚀 The feature, motivation and pitch This is an issue that tracks PRs related to AITER https://github.com/ROCm/aiter . _AITER is AMD’s centralized...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 76e4fea7c4b70` * [x] Fix MLA Backend v0 due to AITER API change in newer version (https://github.com/vllm-project/vllm/pull/17864) * [x] It has been reverted (https://github.com/vllm-project/vllm/pull/17910) as it intro...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20988](https://github.com/vllm-project/vllm/pull/20988) | mentioned | 0.6 | [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | _ROCM_USE_AITER=1 hit device_gemm with the specif... [bug, rocm] 4. #14964: [Feature] [ROCm]: AITER Kernel Integration... [feature request, rocm] Creating issues in vllmellm/vllm.… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
