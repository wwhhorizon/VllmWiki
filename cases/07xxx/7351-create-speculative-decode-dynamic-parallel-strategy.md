# vllm-project/vllm#7351: Create speculative decode dynamic parallel strategy

| 字段 | 值 |
| --- | --- |
| Issue | [#7351](https://github.com/vllm-project/vllm/issues/7351) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Create speculative decode dynamic parallel strategy

### Issue 正文摘录

## Motivation Create new speculative decode dynamic parallel strategy for our team needs ## Features Here we briefly describe features that we will implement in order to implement speculative decode dynamic parallel strategy. Each feature has high level description as a part of request for change with more description provided inside pull request for particular feature #### Save speculative decoding states #7358 Allow users to optionally receive speculative decoding artifacts such as history of draft token indices for each step of speculative decode algorithm #### Create draft from random tokens from promt #7359 Implement speculative proposers that enrich previous draft with tokens randomly sampled from current prompt #### Allow model executor to return many next tokens #7361 Current implementation of model executor and model runner produce one last next token in decode stage. This feature would allow inner model runners to return next tokens for a range of tokens #### Create parallel scorer #7362 Implement scorer that uses feature that allows to get next tokens in single forward request. Runs target model and returns scores for next tokens #### Create speculative decode dynamic p...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Create speculative decode dynamic parallel strategy RFC ## Motivation Create new speculative decode dynamic parallel strategy for our team needs ## Features Here we briefly describe features that we will implement in or...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vious draft with tokens randomly sampled from current prompt #### Allow model executor to return many next tokens #7361 Current implementation of model executor and model runner produce one last next token in decode sta...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
