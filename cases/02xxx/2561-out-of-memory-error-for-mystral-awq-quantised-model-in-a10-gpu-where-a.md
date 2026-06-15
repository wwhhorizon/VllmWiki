# vllm-project/vllm#2561: Out of memory error for Mystral AWQ quantised model in A10 GPU where as non-quantised model is easily loaded in the memory.

| 字段 | 值 |
| --- | --- |
| Issue | [#2561](https://github.com/vllm-project/vllm/issues/2561) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Out of memory error for Mystral AWQ quantised model in A10 GPU where as non-quantised model is easily loaded in the memory.

### Issue 正文摘录

When I am trying to load AWQ quantised version of Mystral-7b, I am facing OOM issues. AWQ config : "q_group_size": 128, "w_bit": 4, "version": "GEMM" But when I try to load non-quantised mystral, it is loaded. What is the issue here?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: l is easily loaded in the memory. When I am trying to load AWQ quantised version of Mystral-7b, I am facing OOM issues. AWQ config : "q_group_size": 128, "w_bit": 4, "version": "GEMM" But when I try to load non-quantise...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Out of memory error for Mystral AWQ quantised model in A10 GPU where as non-quantised model is easily loaded in the memory. When I am trying to load AWQ quantised version of Mystral-7b, I am facing OOM issues. AWQ confi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Out of memory error for Mystral AWQ quantised model in A10 GPU where as non-quantised model is easily loaded in the memory. When I am trying to load AWQ quantised version of Mystral-7b, I am facing OOM issues. AWQ confi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: hen I am trying to load AWQ quantised version of Mystral-7b, I am facing OOM issues. AWQ config : "q_group_size": 128, "w_bit": 4, "version": "GEMM" But when I try to load non-quantised mystral, it is loaded. What is th...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: OOM issues. AWQ config : "q_group_size": 128, "w_bit": 4, "version": "GEMM" But when I try to load non-quantised mystral, it is loaded. What is the issue here?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
