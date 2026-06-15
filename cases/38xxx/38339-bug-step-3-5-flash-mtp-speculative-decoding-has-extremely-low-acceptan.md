# vllm-project/vllm#38339: [Bug] Step-3.5-Flash MTP Speculative Decoding Has Extremely Low Acceptance Rate (2.4%-4.6%)

| 字段 | 值 |
| --- | --- |
| Issue | [#38339](https://github.com/vllm-project/vllm/issues/38339) |
| 状态 | open |
| 标签 | bug;speculative-decoding |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] Step-3.5-Flash MTP Speculative Decoding Has Extremely Low Acceptance Rate (2.4%-4.6%)

### Issue 正文摘录

## Problem Description Step-3.5-Flash MTP (Multi-Token Prediction) speculative decoding has extremely low acceptance rate in current vLLM versions, rendering the feature practically unusable. | Version | Acceptance Rate (mtp=1) | Acceptance Rate (mtp=3) | |---------|------------------------|------------------------| | Current vLLM (main) | 2.4%-4.6% | N/A | | v0.15.1 + Step-AI patch | 97%-100% | 58%-83% | | sglang | N/A | ~50% | ## Reproduction ### Server Command ```bash vllm serve /path/to/Step-3.5-Flash/ \ --served-model-name step3p5-flash \ --max-model-len 4096 \ --trust-remote-code \ --gpu-memory-utilization 0.8 \ --max-num-seqs 32 \ --disable-cascade-attn \ --reasoning-parser step3p5 \ --enable-auto-tool-choice \ --tool-call-parser step3p5 \ --no-enable-prefix-caching \ --tensor-parallel-size 8 \ --port 18111 \ --hf-overrides '{"num_nextn_predict_layers": 1}' \ --speculative-config '{"method": "step3p5_mtp", "num_speculative_tokens": 1}' \ --enable-expert-parallel ``` ### Client Command ```bash curl -X POST http://127.0.0.1:18111/v1/completions -H "Content-Type: application/json" \ -d '{ "model": "step3p5-flash", "prompt": "Hangzhou is a", "max_tokens": 2048, "temperature": 0...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: erver Command ```bash vllm serve /path/to/Step-3.5-Flash/ \ --served-model-name step3p5-flash \ --max-model-len 4096 \ --trust-remote-code \ --gpu-memory-utilization 0.8 \ --max-num-seqs 32 \ --disable-cascade-attn \ --...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug] Step-3.5-Flash MTP Speculative Decoding Has Extremely Low Acceptance Rate (2.4%-4.6%) bug;speculative-decoding ## Problem Description Step-3.5-Flash MTP (Multi-Token Prediction) speculative decoding has extremely...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ) speculative decoding has extremely low acceptance rate in current vLLM versions, rendering the feature practically unusable. | Version | Acceptance Rate (mtp=1) | Acceptance Rate (mtp=3) | |---------|-----------------...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: '{"method": "step3p5_mtp", "num_speculative_tokens": 1}' \ --enable-expert-parallel ``` ### Client Command ```bash curl -X POST http://127.0.0.1:18111/v1/completions -H "Content-Type: application/json" \ -d '{ "model":...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Output ``` SpecDecoding metrics: Mean acceptance length: 1.03, Accepted throughput: 0.57 tokens/s, Drafted throughput: 18.50 tokens/s, Accepted: 23 tokens, Drafted: 740 tokens, Per-position acceptance rate: 0.031, Avg D...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
