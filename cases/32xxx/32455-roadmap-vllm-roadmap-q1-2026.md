# vllm-project/vllm#32455: [Roadmap] vLLM Roadmap Q1 2026

| 字段 | 值 |
| --- | --- |
| Issue | [#32455](https://github.com/vllm-project/vllm/issues/32455) |
| 状态 | closed |
| 标签 | rocm |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;gemm;kernel;moe;operator;quantization |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Roadmap] vLLM Roadmap Q1 2026

### Issue 正文摘录

*Hi vLLM Community,* *We are tackling the roadmap a bit differently this year. In this roadmap, the planned objectives and milestones are captured by different areas. For each area, you will find more detailed tracking issues and lead committers to discuss with. Please continue to send feedback here\!* ### Core Engine Meeting Time/Link: Channel: #sig-core Members: @WoosukKwon The team focuses on the vLLM Engine Core including Scheduler, KV Cache Manager, Distributed, Model Runner, KV Connector code path. - [x] Turn async scheduling on by default @njhill - [ ] Turn model runner V2 on by default @WoosukKwon - [ ] dual batch overlap - [x] piecewise cg - [x] pipeline parallelism - [ ] more attention backends (right now it’s only flash attention) - [ ] more testing - [ ] CPU KV cache production ready: performance optimized, HMA support @orozery - [ ] Process structure simplification/flattening prototype @zhuohan123 - [ ] Data structure clean up: improve efficiently for data structures that grow with number of tokens and number of requests (e.g., list\[int\] \-\> numpy arrays, removing dictionaries). @njhill - [ ] Attention backend re-design One goal this SIG will work on is interface s...

## 现有链接修复摘要

#33960 [Core] Pipeline Parallel support for Model Runner V2

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 9: the vLLM Engine Core including Scheduler, KV Cache Manager, Distributed, Model Runner, KV Connector code path. - [x] Turn async scheduling on by default @njhill - [ ] Turn model runner V2 on by default @WoosukKwon - [ ]...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Please continue to send feedback here\!* ### Core Engine Meeting Time/Link: Channel: #sig-core Members: @WoosukKwon The team focuses on the vLLM Engine Core including Scheduler, KV Cache Manager, Distributed, Model Runn...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: ] Clean up - [ ] Weight Loading - [ ] Distributed Linear - [x] Quantization @robertgshaw2-redhat Finally, low latency serving with spec decoding is in scope as well, led by @benchislett - [x] Stable support MTP (one lay...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: re attention backends (right now it’s only flash attention) - [ ] more testing - [ ] CPU KV cache production ready: performance optimized, HMA support @orozery - [ ] Process structure simplification/flattening prototype...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Roadmap] vLLM Roadmap Q1 2026 rocm *Hi vLLM Community,* *We are tackling the roadmap a bit differently this year. In this roadmap, the planned objectives and milestones are captured by different areas. For each area, y...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33960](https://github.com/vllm-project/vllm/pull/33960) | mentioned | 0.6 | [Core] Pipeline Parallel support for Model Runner V2 | output and competitive throughput against the V1 baseline. Related: #32455 (Q1 2026 Roadmap) — PP is listed as a missing feature for Model Runner V2. ## Changes ### In Model Runner |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
