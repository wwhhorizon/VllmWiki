# vllm-project/vllm#5083: [RFC]: OpenAI Triton-only backend

| 字段 | 值 |
| --- | --- |
| Issue | [#5083](https://github.com/vllm-project/vllm/issues/5083) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;hardware_porting |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel;operator;triton |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: OpenAI Triton-only backend

### Issue 正文摘录

### Motivation. Recently, the OpenAI Triton backend for AMD hardware [PR 3643](https://github.com/vllm-project/vllm/pull/3643) was merged, which is so far the only flash attention backend with the source code part of vLLM. Some of the advantages of OpenAI Triton are superior platform and performance portability. Therefore, we (@tdoublep and myself) wanted to investigate if this code could work equally well on a different platform, i.e. NVIDIA GPUs. Our experiments show that using the code contributed by AMD on different NVIDIA hardware (A100, L40, H100) results in competitive prefill performance compared to the default option (`flash_attn`). For smaller number of heads, which may be the case when using tensor parallelism, it is even faster. ![image](https://github.com/vllm-project/vllm/assets/9336784/6f205a8f-d0af-4416-8de7-31014ab3b794) ![image](https://github.com/vllm-project/vllm/assets/9336784/f4cd07ec-2318-4f28-9501-27f0a0942a51) ![image](https://github.com/vllm-project/vllm/assets/9336784/a73e9fdb-73cc-48d3-bf83-1d46cee52676) For this experiments, we used the [code contributed by AMD](https://github.com/vllm-project/vllm/blob/main/vllm/attention/ops/triton_flash_attention.py...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: how that using the code contributed by AMD on different NVIDIA hardware (A100, L40, H100) results in competitive prefill performance compared to the default option (`flash_attn`). For smaller number of heads, which may...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [RFC]: OpenAI Triton-only backend RFC;stale ### Motivation. Recently, the OpenAI Triton backend for AMD hardware [PR 3643](https://github.com/vllm-project/vllm/pull/3643) was merged, which is so far the only flash atten...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: OpenAI Triton-only backend RFC;stale ### Motivation. Recently, the OpenAI Triton backend for AMD hardware [PR 3643](https://github.com/vllm-project/vllm/pull/3643) was merged, which is so far the only flash atten...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: technical motivations: 1. Using mainly Triton code, it would reduce the dependency on hand-written cuda code (e.g. ~3500 LoC for the [different variants of the forward kernel in flash_attn](https://github.com/Dao-AILab/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
