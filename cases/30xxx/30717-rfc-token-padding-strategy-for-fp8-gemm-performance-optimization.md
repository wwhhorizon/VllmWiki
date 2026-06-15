# vllm-project/vllm#30717: [RFC]: Token Padding Strategy for FP8 GEMM Performance Optimization

| 字段 | 值 |
| --- | --- |
| Issue | [#30717](https://github.com/vllm-project/vllm/issues/30717) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | shape_align |
| Operator 关键词 | cuda;fp8;gemm;kernel;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Token Padding Strategy for FP8 GEMM Performance Optimization

### Issue 正文摘录

### Motivation. This RFC proposes implementing a token padding mechanism in the vLLM execution loop to ensure the number of tokens (batch size M) is a multiple of 4 when running FP8 models. This alignment significantly improves performance on NVIDIA B200/H200 GPUs. FP8 GEMM kernels (both DeepGEMM and CUTLASS-based implementations) exhibit distinct performance characteristics based on input dimensions. Benchmarks on B200 hardware demonstrate substantial throughput degradation when the number of tokens (M) is not aligned to specific boundaries. ### Benchmark Data - End-to-End serving `vllm serve` and `vllm bench serve --backend vllm --dataset-name sharegpt --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json --base-url http://localhost:8000 --endpoint /v1/completions --model [model] --tokenizer [model] --num-prompts 2000 --max-concurrency 100` | GPU | model | Total Token throughput (tok/s) Before | Total Token throughput (tok/s) After | Speedup | | -- | -- | -- | -- | -- | | B200 | Qwen/Qwen3-8B-FP8 | 15455.37 | 17350.65 | 10.9% | | B200 | Qwen/Qwen3-32B-FP8 | 6350.89 | 8016.02 | 26.2% | | H200 | Qwen/Qwen3-8B-FP8 | 15810.43 | 16136.04 | 2.0% | | H200 | Qwen/Qwen3-32B-FP8 | 60...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: e ### Motivation. This RFC proposes implementing a token padding mechanism in the vLLM execution loop to ensure the number of tokens (batch size M) is a multiple of 4 when running FP8 models. This alignment significantl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: exhibit distinct performance characteristics based on input dimensions. Benchmarks on B200 hardware demonstrate substantial throughput degradation when the number of tokens (M) is not aligned to specific boundaries. ###...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [RFC]: Token Padding Strategy for FP8 GEMM Performance Optimization RFC;stale ### Motivation. This RFC proposes implementing a token padding mechanism in the vLLM execution loop to ensure the number of tokens (batch siz...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: | - GEMM only (B200) `python3 benchmarks/kernels/deepgemm/benchmark_fp8_block_dense_gemm.py` with shape modifications | m | n | k | Time DeepGEMM (μs) | TFLOPS DeepGEMM | GB/s DeepGEMM | Time vLLM CUTLASS (μs) | TFLOPS...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rformance on NVIDIA B200/H200 GPUs. FP8 GEMM kernels (both DeepGEMM and CUTLASS-based implementations) exhibit distinct performance characteristics based on input dimensions. Benchmarks on B200 hardware demonstrate subs...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
