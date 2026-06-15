# vllm-project/vllm#4387: [Usage]: How to decrease VRAM Usage when specifying FP8 arguments

| 字段 | 值 |
| --- | --- |
| Issue | [#4387](https://github.com/vllm-project/vllm/issues/4387) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to decrease VRAM Usage when specifying FP8 arguments

### Issue 正文摘录

### Your current environment Thank you for the teamwork on FP8 quantization. However, I am currently loading FP16 using the arguments --quantization fp8 --kv-cache-dtype fp8, and it appears that the VRAM usage is the same as with FP16. How can we decrease VRAM usage when specifying FP8 arguments? ### How would you like to use vllm I believe that FP8 should require less than 50% of the VRAM usage compared to FP16.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Usage]: How to decrease VRAM Usage when specifying FP8 arguments usage ### Your current environment Thank you for the teamwork on FP8 quantization. However, I am currently loading FP16 using the arguments --quantizatio...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: How to decrease VRAM Usage when specifying FP8 arguments usage ### Your current environment Thank you for the teamwork on FP8 quantization. However, I am currently loading FP16 using the arguments --quantizatio...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: er, I am currently loading FP16 using the arguments --quantization fp8 --kv-cache-dtype fp8, and it appears that the VRAM usage is the same as with FP16. How can we decrease VRAM usage when specifying FP8 arguments? ###...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
