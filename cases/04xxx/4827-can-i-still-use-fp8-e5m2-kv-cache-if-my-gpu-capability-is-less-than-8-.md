# vllm-project/vllm#4827: Can I still use FP8 E5M2 KV Cache if my GPU capability is less than 8.9?

| 字段 | 值 |
| --- | --- |
| Issue | [#4827](https://github.com/vllm-project/vllm/issues/4827) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can I still use FP8 E5M2 KV Cache if my GPU capability is less than 8.9?

### Issue 正文摘录

### Your current environment Can I still use FP8 E5M2 KV Cache if my GPU capability is less than 8.9? VLLM did not report any errors, showing the use of FP8 KV Cache, even though my GPU capability was less than 8.9 ### How would you like to use vllm use vllm in A10

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Can I still use FP8 E5M2 KV Cache if my GPU capability is less than 8.9? usage ### Your current environment Can I still use FP8 E5M2 KV Cache if my GPU capability is less than 8.9? VLLM did not report any errors, showin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Can I still use FP8 E5M2 KV Cache if my GPU capability is less than 8.9? usage ### Your current environment Can I still use FP8 E5M2 KV Cache if my GPU capability is less than 8.9? VLLM did not report any errors, showin...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Can I still use FP8 E5M2 KV Cache if my GPU capability is less than 8.9? usage ### Your current environment Can I still use FP8 E5M2 KV Cache if my GPU capability is less than 8.9? VLLM did not report any errors, showin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
