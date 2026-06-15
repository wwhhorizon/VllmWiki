# vllm-project/vllm#33549: [RFC]: Dynamic Expert Load Balance optimization

| 字段 | 值 |
| --- | --- |
| Issue | [#33549](https://github.com/vllm-project/vllm/issues/33549) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Dynamic Expert Load Balance optimization

### Issue 正文摘录

### Motivation. Optimize dynamic expert load balance 1. The current EPLB algorithm is executed in serial mode, which incurs certain overheads. 2. The current moe_load_view requires complex calculation, instead of being directly output from modular_kernel.py. 3. Currently, the shared expert and routing expert are calculated in serial mode. We now consider the shared expert as the routing expert and calculate the number of copies and the deployment mode of the shared expert. Record experts distribution during forward. We using expert_token_num after disptach instead of topk_ids, thus we got much smaller tensor shape to reduce cost of hbm recording and add-operator. Do all-gather for experts distribution. Using all-gather instead of all-reduce as less traffic volume. Wake up eplb worker process with experts distribution when num_iterations comes. Run eplb algorithm in eplb worker. Generate p2p send/recv ops and other operator such as log2phy would cost long cpu time. Lanch ibatch_send_recv in async_stream before forward. After forward, wait for the ibatch_send_recv finish, then do uapte expert map and expert weights. ### Proposed Change. 1. We also add the process of the algorithm ca...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: [RFC]: Dynamic Expert Load Balance optimization RFC ### Motivation. Optimize dynamic expert load balance 1. The current EPLB algorithm is executed in serial mode, which incurs certain overheads. 2. The current moe_load_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng expert_token_num after disptach instead of topk_ids, thus we got much smaller tensor shape to reduce cost of hbm recording and add-operator. Do all-gather for experts distribution. Using all-gather instead of all-red...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ectly output from modular_kernel.py. 3. Currently, the shared expert and routing expert are calculated in serial mode. We now consider the shared expert as the routing expert and calculate the number of copies and the d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: w maps into the asynchronous stream. 2. We offer a variety of load balancing algorithms. https://github.com/vllm-project/vllm/pull/24069 3. We eliminate the scttar_add_ operator for heat collection. https://github.com/v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
