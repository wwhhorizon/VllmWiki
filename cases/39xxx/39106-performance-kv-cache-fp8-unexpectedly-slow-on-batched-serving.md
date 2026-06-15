# vllm-project/vllm#39106: [Performance]: KV Cache FP8 unexpectedly slow on batched serving

| 字段 | 值 |
| --- | --- |
| Issue | [#39106](https://github.com/vllm-project/vllm/issues/39106) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cache;fp8;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: KV Cache FP8 unexpectedly slow on batched serving

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression ### Summary When benchmarking FP8 vs BF16 on `gpt-oss-20b` with vLLM on a single H100, FP8 performs as expected (equal or slightly better) for single-concurrency workloads, but is **~10% slower** than BF16 under a concurrent mixed-length workload (concurrency 8, 150 requests, ~20K input tokens). ### Environment - Model: `openai/gpt-oss-20b` - vLLM version: 0.19.0 - GPU: 1x H100 FP8: ``` python3 -m vllm.entrypoints.openai.api_server \ --model openai/gpt-oss-20b \ --kv-cache-dtype "fp8" \ --no-enable-prefix-caching ``` BF16: ``` python3 -m vllm.entrypoints.openai.api_server \ --model openai/gpt-oss-20b \ --no-enable-prefix-caching ``` ### Benchmark Setup **Short context** (concurrency 1, 10 requests, 512 in / 512 out): `vllm bench serve --dataset-name sonnet --sonnet-input-len 512 --sonnet-output-len 512 --max-concurrency 1 --num-prompts 10` **Long context** (concurrency 1, 10 requests, 130K in / 512 out): `vllm bench serve --dataset-name sonnet --sonnet-input-len 130000 --sonnet-output-len 512 --max-concurrency 1 --num-prompts 10` **Concurrent mixed** (concurrency 8, 150 requests, ~20K in / ~2K o...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: roposal to improve performance _No response_ ### Report of performance regression ### Summary When benchmarking FP8 vs BF16 on `gpt-oss-20b` with vLLM on a single H100, FP8 performs as expected (equal or slightly better...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Performance]: KV Cache FP8 unexpectedly slow on batched serving performance ### Proposal to improve performance _No response_ ### Report of performance regression ### Summary When benchmarking FP8 vs BF16 on `gpt-oss-2...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 0K input tokens). ### Environment - Model: `openai/gpt-oss-20b` - vLLM version: 0.19.0 - GPU: 1x H100 FP8: ``` python3 -m vllm.entrypoints.openai.api_server \ --model openai/gpt-oss-20b \ --kv-cache-dtype "fp8" \ --no-e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ry When benchmarking FP8 vs BF16 on `gpt-oss-20b` with vLLM on a single H100, FP8 performs as expected (equal or slightly better) for single-concurrency workloads, but is **~10% slower** than BF16 under a concurrent mix...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Performance]: KV Cache FP8 unexpectedly slow on batched serving performance ### Proposal to improve performance _No response_ ### Report of performance regression ### Summary When benchmarking FP8 vs BF16 on `gpt-oss-2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
