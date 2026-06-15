# vllm-project/vllm#26369: [Performance]: Use int over list[int] as output_tokens to reduce GC overhead

| 字段 | 值 |
| --- | --- |
| Issue | [#26369](https://github.com/vllm-project/vllm/issues/26369) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Use int over list[int] as output_tokens to reduce GC overhead

### Issue 正文摘录

### Proposal to improve performance Currently, we're consistently using list[int] to represent output_tokens in ModelRunnerOutput which is very inefficient from GC prospective. The default setup of GC is (700, 10, 10) which means - if allocated_obj-deallocated_obj>=700 in generation 0, GC0 will be triggered - GC1 is triggered after 10 GC0 - GC2 is triggered after 10 GC1 In this scenario, large batch size scenarios (small models) each batch could be as large as 1024, which means GC0 will be triggered per decode cycle, GC1 will triggered per 10 decode cycle and GC2 per 100 decode cycle, which is very inefficient! max_batch_size of list will be created here https://github.com/vllm-project/vllm/blob/a38c1bfe09f487cb61b4eddb10d71a8d81cd6f11/vllm/v1/worker/gpu_model_runner.py#L4504-L4517 ## Proposal #1 (Change OutputToken from list[int] to Union[int, list[int]]) https://github.com/vllm-project/vllm/pull/26368 shows very promising results of this proposal - **19%** throughput boost in infinite request rate scenario for facebook-125m ## Proposal #2 (Semi-Hacky but simple) Increase the GC0 threshold by max_batch_size which ensured GC0 won't be triggered right after the sample output tensor...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: se int over list[int] as output_tokens to reduce GC overhead performance;stale ### Proposal to improve performance Currently, we're consistently using list[int] to represent output_tokens in ModelRunnerOutput which is v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: /vllm/pull/26368 shows very promising results of this proposal - **19%** throughput boost in infinite request rate scenario for facebook-125m ## Proposal #2 (Semi-Hacky but simple) Increase the GC0 threshold by max_batc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: int] to represent output_tokens in ModelRunnerOutput which is very inefficient from GC prospective. The default setup of GC is (700, 10, 10) which means - if allocated_obj-deallocated_obj>=700 in generation 0, GC0 will...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: is triggered after 10 GC1 In this scenario, large batch size scenarios (small models) each batch could be as large as 1024, which means GC0 will be triggered per decode cycle, GC1 will triggered per 10 decode cycle and...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rently, we're consistently using list[int] to represent output_tokens in ModelRunnerOutput which is very inefficient from GC prospective. The default setup of GC is (700, 10, 10) which means - if allocated_obj-deallocat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
