# vllm-project/vllm#38729: [Bug] All models hang on GB300 (SM103) with FlashInfer 0.6.7

| 字段 | 值 |
| --- | --- |
| Issue | [#38729](https://github.com/vllm-project/vllm/issues/38729) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] All models hang on GB300 (SM103) with FlashInfer 0.6.7

### Issue 正文摘录

## Bug Description Multiple models hang indefinitely on GB300 (SM103, CC 10.3) during inference with large batch sizes. The GPU shows 99% SM utilization and 0% memory bandwidth. This is a regression introduced by the FlashInfer 0.6.6 to 0.6.7 upgrade, where TRTLLM attention kernels are no longer forward-compatible with SM103. Correctness tests with small batches (4 prompts) pass. Throughput benchmarks with 768 prompts hang. GB200 (SM100) is not affected. Related FlashInfer issue: [flashinfer-ai/flashinfer#2939](https://github.com/flashinfer-ai/flashinfer/issues/2939) (fix in progress on the FlashInfer side) ## Reproduction ```bash # GB300 (SM103), FlashInfer 0.6.7 # Hangs at "Processed prompts: 0%" vllm bench throughput \ --tensor-parallel-size=1 --model=nvidia/Qwen3-8B-FP8 \ --load-format=dummy --num-prompts=768 --output-len=256 --input-len=256 \ --kv-cache-dtype=auto --gpu-memory-utilization=0.90 \ --max-num-batched-tokens=2048 --max-num-seqs=768 --max-model-len=2048 \ --trust-remote-code --quantization=modelopt ``` ## Affected Configuration - **Hardware**: GB300 (SM103, CC 10.3). GB200 (SM100, CC 10.0) is **not** affected. - **Models**: Multiple models tested hang, including FP...

## 现有链接修复摘要

#38730 [Bugfix] Restrict TRTLLM attention to SM100, fixing GB300 (SM103) hang

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: lm bench throughput \ --tensor-parallel-size=1 --model=nvidia/Qwen3-8B-FP8 \ --load-format=dummy --num-prompts=768 --output-len=256 --input-len=256 \ --kv-cache-dtype=auto --gpu-memory-utilization=0.90 \ --max-num-batch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug] All models hang on GB300 (SM103) with FlashInfer 0.6.7 ## Bug Description Multiple models hang indefinitely on GB300 (SM103, CC 10.3) during inference with large batch sizes. The GPU shows 99% SM utilization and 0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: zes. The GPU shows 99% SM utilization and 0% memory bandwidth. This is a regression introduced by the FlashInfer 0.6.6 to 0.6.7 upgrade, where TRTLLM attention kernels are no longer forward-compatible with SM103. Correc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug] All models hang on GB300 (SM103) with FlashInfer 0.6.7 ## Bug Description Multiple models hang indefinitely on GB300 (SM103, CC 10.3) during inference with large batch sizes. The GPU shows 99% SM utilization and 0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug] All models hang on GB300 (SM103) with FlashInfer 0.6.7 ## Bug Description Multiple models hang indefinitely on GB300 (SM103, CC 10.3) during inference with large batch sizes. The GPU shows 99% SM utilization and 0...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38730](https://github.com/vllm-project/vllm/pull/38730) | closes_keyword | 0.95 | [Bugfix] Restrict TRTLLM attention to SM100, fixing GB300 (SM103) hang | Fixes #38729 ## Change Restrict `supports_trtllm_attention()` to exact SM100 (CC 10.0) instead of the CC 10.x family. SM103 falls back to the FlashInfer default attention backend |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
