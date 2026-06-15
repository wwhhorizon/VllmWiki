# vllm-project/vllm#3910: [Doc]: Question about the timing of prefix caches release for multiples requests with long time interval. 

| 字段 | 值 |
| --- | --- |
| Issue | [#3910](https://github.com/vllm-project/vllm/issues/3910) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Question about the timing of prefix caches release for multiples requests with long time interval. 

### Issue 正文摘录

### 📚 The doc issue It's there has any docs about the timing of prefix caches release ? specific for multiples requests with long time interval. ```bash 1rd req [+ long prompt_0] -> after 10 mins -> 2rd req [+ long prompt_0] -> after 5 mins -> 3rd req [+ long prompt_0] -> ... | | | | ------ cached ---------> will cache release here? ------> .... ``` ### Suggest a potential alternative/fix _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: It's there has any docs about the timing of prefix caches release ? specific for multiples requests with long time interval. ```bash 1rd req [+ long prompt_0] -> after 10 mins -> 2rd req [+ long prompt_0] -> after 5 min...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Doc]: Question about the timing of prefix caches release for multiples requests with long time interval. documentation ### 📚 The doc issue It's there has any docs about the timing of prefix caches release ? specific fo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: Question about the timing of prefix caches release for multiples requests with long time interval. documentation ### 📚 The doc issue It's there has any docs about the timing of prefix caches release ? specific fo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
