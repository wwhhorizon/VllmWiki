# vllm-project/vllm#3589: [Usage]: run fastchat.serve.vllm_worker in WSL ubuntu2204 ,It exited the system

| 字段 | 值 |
| --- | --- |
| Issue | [#3589](https://github.com/vllm-project/vllm/issues/3589) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: run fastchat.serve.vllm_worker in WSL ubuntu2204 ,It exited the system

### Issue 正文摘录

### Your current environment ![image](https://github.com/vllm-project/vllm/assets/122587001/0ad1016d-fbd7-484b-80bb-d8ebf2132a87) ![image](https://github.com/vllm-project/vllm/assets/122587001/f9cc44a2-768f-47c8-8547-f51d7e25381d) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: d) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: fastchat.serve.vllm_worker in WSL ubuntu2204 ,It exited the system usage;stale ### Your current environment ![image](https://github.com/vllm-project/vllm/assets/122587001/0ad1016d-fbd7-484b-80bb-d8ebf2132a87) ![image](h...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
