# vllm-project/vllm#470: Specify GPUs bug (torch.distributed.all_reduce(torch.zeros(1).cuda()))

| 字段 | 值 |
| --- | --- |
| Issue | [#470](https://github.com/vllm-project/vllm/issues/470) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Specify GPUs bug (torch.distributed.all_reduce(torch.zeros(1).cuda()))

### Issue 正文摘录

On my server, when the cuda:0 is full, then I face with this issue each time, when I specify other GPus with CUDA_VISIBLE_DEVICES..

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Specify GPUs bug (torch.distributed.all_reduce(torch.zeros(1).cuda())) feature request On my server, when the cuda:0 is full, then I face with this issue each time, when I specify other GPus with CUDA_VISIBLE_DEVICES..
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Specify GPUs bug (torch.distributed.all_reduce(torch.zeros(1).cuda())) feature request On my server, when the cuda:0 is full, then I face with this issue each time, when I specify other GPus with CUDA_VISIBLE_DEVICES..
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: y GPUs bug (torch.distributed.all_reduce(torch.zeros(1).cuda())) feature request On my server, when the cuda:0 is full, then I face with this issue each time, when I specify other GPus with CUDA_VISIBLE_DEVICES..

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
