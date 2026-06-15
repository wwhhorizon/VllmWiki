# vllm-project/vllm#1607: What happens when GPU KV cache usage reaching 100%?

| 字段 | 值 |
| --- | --- |
| Issue | [#1607](https://github.com/vllm-project/vllm/issues/1607) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> What happens when GPU KV cache usage reaching 100%?

### Issue 正文摘录

As the question showed, I meet some case that the output may be so long and the GPU KV cache usage keeps increasing， and reaches 100%，then model don't genearate anything and don't recieve other request. Finally, I only restart it

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: easing， and reaches 100%，then model don't genearate anything and don't recieve other request. Finally, I only restart it
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: What happens when GPU KV cache usage reaching 100%? As the question showed, I meet some case that the output may be so long and the GPU KV cache usage keeps increasing， and reaches 100%，then model don't genearate anythi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: long and the GPU KV cache usage keeps increasing， and reaches 100%，then model don't genearate anything and don't recieve other request. Finally, I only restart it
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: reaches 100%，then model don't genearate anything and don't recieve other request. Finally, I only restart it

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
