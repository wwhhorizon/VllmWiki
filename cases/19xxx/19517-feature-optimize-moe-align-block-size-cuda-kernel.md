# vllm-project/vllm#19517: [Feature]: Optimize `moe_align_block_size` CUDA kernel

| 字段 | 值 |
| --- | --- |
| Issue | [#19517](https://github.com/vllm-project/vllm/issues/19517) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cuda;fp8;kernel;moe;sampling |
| 症状 | slowdown |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Optimize `moe_align_block_size` CUDA kernel

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently `moe_align_block_size` is a performance bottleneck, even slower than `fused_moe_kernel` I think we can reuse the kernel from SGL to optimize it as the first step (as the default one). I will have a pr for this later Benchmark test ```bash moe-align-block-size-performance: num_tokens num_experts topk VLLM SGL 0 1.0 16.0 1.0 20.064000 21.663999 1 1.0 16.0 2.0 19.616000 22.272000 2 1.0 16.0 8.0 19.616000 21.695999 3 1.0 64.0 1.0 25.632000 27.680000 4 1.0 64.0 2.0 26.384000 27.680000 5 1.0 64.0 8.0 26.368000 27.680000 6 1.0 224.0 1.0 62.463999 32.768000 7 1.0 224.0 2.0 62.463999 32.864001 8 1.0 224.0 8.0 62.463999 32.896001 9 1.0 256.0 1.0 71.872003 31.744000 10 1.0 256.0 2.0 71.744002 31.776000 11 1.0 256.0 8.0 71.744002 31.808000 12 16.0 16.0 1.0 21.344000 23.615999 13 16.0 16.0 2.0 21.376001 23.584001 14 16.0 16.0 8.0 21.344000 23.712000 15 16.0 64.0 1.0 25.632000 28.720001 16 16.0 64.0 2.0 25.632000 28.672000 17 16.0 64.0 8.0 26.400000 29.792000 18 16.0 224.0 1.0 62.463999 32.800000 19 16.0 224.0 2.0 62.463999 32.864001 20 16.0 224.0 8.0 62.463999 32.800000 21 16.0 256.0 1.0 72.704002 33.856001 22 16.0 256.0 2.0 72.704002 33.824001...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 4762.52 output tokens/s(B200 sgl moe_align_block_size) #### Throughput(fp8) `vllm bench throughput --model Qwen/Qwen3-30B-A3B-FP8 --load-format dummy --input-len 1000 --output-len 100` Throughput: 42.28 requests/s, 4642...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: Optimize `moe_align_block_size` CUDA kernel feature request ### 🚀 The feature, motivation and pitch Currently `moe_align_block_size` is a performance bottleneck, even slower than `fused_moe_kernel` I think we...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 1.007999 52.223999 ``` #### Throughput(fp16) `vllm bench throughput --model Qwen/Qwen3-30B-A3B --load-format dummy --input-len 1000 --output-len 100` Throughput: 46.03 requests/s, 50547.85 total tokens/s, 4603.43 output...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Feature]: Optimize `moe_align_block_size` CUDA kernel feature request ### 🚀 The feature, motivation and pitch Currently `moe_align_block_size` is a performance bottleneck, even slower than `fused_moe_kernel` I think we...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: as the first step (as the default one). I will have a pr for this later Benchmark test ```bash moe-align-block-size-performance: num_tokens num_experts topk VLLM SGL 0 1.0 16.0 1.0 20.064000 21.663999 1 1.0 16.0 2.0 19....

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
