# vllm-project/vllm#10360: [Bug]: v0.6.4 requires more GPU memory than v0.6.3

| 字段 | 值 |
| --- | --- |
| Issue | [#10360](https://github.com/vllm-project/vllm/issues/10360) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v0.6.4 requires more GPU memory than v0.6.3

### Issue 正文摘录

### Your current environment docker image 0.6.4 ### 🐛 Describe the bug docker run 0.6.4 image requires more GPU memory than version 0.6.3 to trigger OOM with the same settings. The model being used is Qwen 2.5 1.5B, with the following Docker launch settings: --model Qwen2.5-1.5B-Instruct --max-model-len 4096 --gpu-memory-utilization 0.15 --enable-prefix-caching

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ires more GPU memory than v0.6.3 bug;stale ### Your current environment docker image 0.6.4 ### 🐛 Describe the bug docker run 0.6.4 image requires more GPU memory than version 0.6.3 to trigger OOM with the same settings....
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: v0.6.4 requires more GPU memory than v0.6.3 bug;stale ### Your current environment docker image 0.6.4 ### 🐛 Describe the bug docker run 0.6.4 image requires more GPU memory than version 0.6.3 to trigger OOM with...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: GPU memory than version 0.6.3 to trigger OOM with the same settings. The model being used is Qwen 2.5 1.5B, with the following Docker launch settings: --model Qwen2.5-1.5B-Instruct --max-model-len 4096 --gpu-memory-util...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: v0.6.4 requires more GPU memory than v0.6.3 bug;stale ### Your current environment docker image 0.6.4 ### 🐛 Describe the bug docker run 0.6.4 image requires more GPU memory than version 0.6.3 to trigger OOM with...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
