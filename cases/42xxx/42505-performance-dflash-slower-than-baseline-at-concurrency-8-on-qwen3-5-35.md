# vllm-project/vllm#42505: [Performance] DFlash slower than baseline at concurrency > 8 on Qwen3.5-35B-A3B

| 字段 | 值 |
| --- | --- |
| Issue | [#42505](https://github.com/vllm-project/vllm/issues/42505) |
| 状态 | open |
| 标签 | performance |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;moe;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | attention;moe;triton |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance] DFlash slower than baseline at concurrency > 8 on Qwen3.5-35B-A3B

### Issue 正文摘录

**Description:** We are testing DFlash speculative decoding with Qwen3.5-35B-A3B on vLLM 0.20.1 and observed two performance issues: 1. **At concurrency=1**, the speedup is much lower than reported in the DFlash paper. 2. **At concurrency>8**, DFlash becomes slower than the baseline (no speculative decoding). **Environment:** - vLLM version: 0.20.1 - Model: Qwen3.5-35B-A3B - Draft model: z-lab/Qwen3.5-35B-A3B-DFlash - GPU: RTX PRO 6000 * 1 - Attention backend: flash_attn - MoE backend: triton **Reproduction:** Baseline (no DFlash): ```bash vllm serve /parent-dir/Qwen3.5-35B-A3B \ --attention-backend flash_attn \ --max-num-batched-tokens 32768 \ --max-num-seqs 16 \ --moe-backend triton \ --safetensors-load-strategy=prefetch \ --max-model-len 183872 ``` DFlash: ```bash vllm serve /parent-dir/Qwen3.5-35B-A3B \ --speculative-config '{"method": "dflash", "model": "/parent-dir/Qwen3.5-35B-A3B-DFlash/", "num_speculative_tokens": 4}' \ --attention-backend flash_attn \ --max-num-batched-tokens 32768 \ --max-num-seqs 16 \ --moe-backend triton \ --safetensors-load-strategy=prefetch \ --max-model-len 183872 ``` Benchmark: ```bash evalscope perf \ --model /parent-dir/Qwen3.5-35B-A3B \ --url ht...

## 现有链接修复摘要

#42704 [Bugfix] Fix DFlash target layer index offset for auxiliary hidden states | #42728 [Bugfix] Avoid FULL cudagraph dispatch for DFlash

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Performance] DFlash slower than baseline at concurrency > 8 on Qwen3.5-35B-A3B performance **Description:** We are testing DFlash speculative decoding with Qwen3.5-35B-A3B on vLLM 0.20.1 and observed two performance is...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: model: z-lab/Qwen3.5-35B-A3B-DFlash - GPU: RTX PRO 6000 * 1 - Attention backend: flash_attn - MoE backend: triton **Reproduction:** Baseline (no DFlash): ```bash vllm serve /parent-dir/Qwen3.5-35B-A3B \ --attention-back...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: del: Qwen3.5-35B-A3B - Draft model: z-lab/Qwen3.5-35B-A3B-DFlash - GPU: RTX PRO 6000 * 1 - Attention backend: flash_attn - MoE backend: triton **Reproduction:** Baseline (no DFlash): ```bash vllm serve /parent-dir/Qwen3...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: t concurrency > 8 on Qwen3.5-35B-A3B performance **Description:** We are testing DFlash speculative decoding with Qwen3.5-35B-A3B on vLLM 0.20.1 and observed two performance issues: 1. **At concurrency=1**, the speedup...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 8 on Qwen3.5-35B-A3B performance **Description:** We are testing DFlash speculative decoding with Qwen3.5-35B-A3B on vLLM 0.20.1 and observed two performance issues: 1. **At concurrency=1**, the speedup is much lower th...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42704](https://github.com/vllm-project/vllm/pull/42704) | closes_keyword | 0.95 | [Bugfix] Fix DFlash target layer index offset for auxiliary hidden states | Fix #42505, which reports the low draft acceptance rate and limited DFlash speculative decoding speedup on Qwen3.5-35B-A3B. During reproduction, I found that the low acceptance |
| [#42728](https://github.com/vllm-project/vllm/pull/42728) | mentioned | 0.6 | [Bugfix] Avoid FULL cudagraph dispatch for DFlash | e and piecewise graphs intact (no regression to eager). Relates to #42505 ("DFlash slower than baseline at concurrency > 8 on Qwen3.5-35B-A3B"): that issue tracks the high-concurr… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
