# vllm-project/vllm#33797: [Performance][CPU Backend]: 40% Performance drop observed on AWQ models from version 0.12.0 vs version 0.11.2

| 字段 | 值 |
| --- | --- |
| Issue | [#33797](https://github.com/vllm-project/vllm/issues/33797) |
| 状态 | closed |
| 标签 | performance;cpu |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance][CPU Backend]: 40% Performance drop observed on AWQ models from version 0.12.0 vs version 0.11.2

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression compared benchmark results for version 0.11.2 and version 0.15 Using benchmark: https://github.com/opea-project/Enterprise-RAG/tree/main/src/tests/e2e/benchmarks/chatqa for model: casperhansen/llama-3-8b-instruct-awq modelConfigs: generic-base-cpu: &generic_base_cpu configMapValues: VLLM_SKIP_WARMUP: "false" VLLM_CPU_KVCACHE_SPACE: "40" VLLM_DTYPE: "bfloat16" VLLM_MAX_NUM_SEQS: "256" VLLM_TP_SIZE: "1" OMP_NUM_THREADS: "32" VLLM_PP_SIZE: "1" VLLM_MAX_MODEL_LEN: "4096" extraCmdArgs: ["--pipeline-parallel-size", "$(VLLM_PP_SIZE)", "--dtype", "$(VLLM_DTYPE)", "--max_model_len", "$(VLLM_MAX_MODEL_LEN)", "--max-num-seqs", "$(VLLM_MAX_NUM_SEQS)", "--disable-log-requests", "--download-dir", "/data"] tensor_parallel_size: "1" # not applied on CPU generic-base-awq-cpu: &generic_base_awq_cpu configMapValues: VLLM_SKIP_WARMUP: "false" VLLM_CPU_KVCACHE_SPACE: "40" VLLM_DTYPE: "bfloat16" VLLM_MAX_NUM_SEQS: "256" VLLM_TP_SIZE: "1" OMP_NUM_THREADS: "32" VLLM_PP_SIZE: "1" VLLM_MAX_MODEL_LEN: "4096" extraCmdArgs: ["--pipeline-parallel-size", "$(VLLM_PP_SIZE)", "--dtype", "$(VLLM_DTYPE)", "--max_model_len", "$(VLL...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: VLLM_SKIP_WARMUP: "false" VLLM_CPU_KVCACHE_SPACE: "40" VLLM_DTYPE: "bfloat16" VLLM_MAX_NUM_SEQS: "256" VLLM_TP_SIZE: "1" OMP_NUM_THREADS: "32" VLLM_PP_SIZE: "1" VLLM_MAX_MODEL_LEN: "4096" extraCmdArgs: ["--pipeline-para...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance][CPU Backend]: 40% Performance drop observed on AWQ models from version 0.12.0 vs version 0.11.2 performance;cpu ### Proposal to improve performance _No response_ ### Report of performance regression compar...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: roposal to improve performance _No response_ ### Report of performance regression compared benchmark results for version 0.11.2 and version 0.15 Using benchmark: https://github.com/opea-project/Enterprise-RAG/tree/main/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Performance][CPU Backend]: 40% Performance drop observed on AWQ models from version 0.12.0 vs version 0.11.2 performance;cpu ### Proposal to improve performance _No response_ ### Report of performance regression compar...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: formance][CPU Backend]: 40% Performance drop observed on AWQ models from version 0.12.0 vs version 0.11.2 performance;cpu ### Proposal to improve performance _No response_ ### Report of performance regression compared b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
