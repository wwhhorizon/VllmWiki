# vllm-project/vllm#43700: [Doc]: INT8 weight-only quantization causes 4x throughput regression at batch=1 on memory-bandwidth-bound GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#43700](https://github.com/vllm-project/vllm/issues/43700) |
| 状态 | open |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;gemm_linear;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;gemm;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: INT8 weight-only quantization causes 4x throughput regression at batch=1 on memory-bandwidth-bound GPUs

### Issue 正文摘录

### 📚 The doc issue The quantization page at https://docs.vllm.ai/en/latest/features/quantization/ lists bitsandbytes INT8 as a supported format without noting a critical batch-size dependency that causes catastrophic throughput regression in production latency-sensitive endpoints. Using Qwen2.5-3B-Instruct with bitsandbytes INT8 quantization (load_in_8bit=True, threshold=6.0) at batch=1, I measured 22,288ms mean latency versus 5,275ms for FP32 a 4.2x slowdown. This is counterintuitive because INT8 reduces memory footprint from 12.4GB to 3.4GB, yet throughput degrades by 4x at small batch sizes. Root cause: bitsandbytes emits the warning MatMul8bitLt: inputs will be cast from torch.bfloat16 to float16 at each layer. The dequantization pass adds a separate memory movement step before each matmul. On a memory-bandwidth-bound workload like single-request serving, this overhead dominates entirely. PyTorch CUDA profiling confirmed linear and matmul operations consume 34% of total CUDA execution time while attention consumes only 0.2%, so any extra memory movement in the linear path is expensive. At batch=16 the regression disappears. The problem is specifically small batch sizes, which...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: [Doc]: INT8 weight-only quantization causes 4x throughput regression at batch=1 on memory-bandwidth-bound GPUs documentation ### 📚 The doc issue The quantization page at https://docs.vllm.ai/en/latest/features/quantizat...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Doc]: INT8 weight-only quantization causes 4x throughput regression at batch=1 on memory-bandwidth-bound GPUs documentation ### 📚 The doc issue The quantization page at https://docs.vllm.ai/en/latest/features/quantizat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: en/latest/features/quantization/ lists bitsandbytes INT8 as a supported format without noting a critical batch-size dependency that causes catastrophic throughput regression in production latency-sensitive endpoints. Us...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ndbytes INT8 as a supported format without noting a critical batch-size dependency that causes catastrophic throughput regression in production latency-sensitive endpoints. Using Qwen2.5-3B-Instruct with bitsandbytes IN...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: memory footprint from 12.4GB to 3.4GB, yet throughput degrades by 4x at small batch sizes. Root cause: bitsandbytes emits the warning MatMul8bitLt: inputs will be cast from torch.bfloat16 to float16 at each layer. The d...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
