# vllm-project/vllm#22246: [RFC]: Dynamic Expert Load Balance with Zero-like-overhead

| 字段 | 值 |
| --- | --- |
| Issue | [#22246](https://github.com/vllm-project/vllm/issues/22246) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Dynamic Expert Load Balance with Zero-like-overhead

### Issue 正文摘录

### Motivation Currently dynamically experts balancing would stop-the-world. Asynchronously expert load balancing would be better without flowing problems: 1. Host-bound latency: There are many cpu operations during EPLB such as eplb-algorithm、creating p2p ops、and log2phy expert converting would spend long cpu time, as ~1s. 3. Communication latency: The transfer time would cost much in the situation without nvlink. As the weight of an expert maybe transfer to multiple new positions, thus N times send/recv for one expert, with result long latency. We had tested that batch_isend_irecv cost more 100ms for 16 experts weight transmission in A2 server of ascend. We have finished SwiftBalancer -- Dynamic Expert Load Balance with Zero-like-overhead on vllm-ascend 1943(https://github.com/vllm-project/vllm-ascend/pull/2186) and it is well tested. SwiftBalancer would not stop-the-world anymore, in out test on NPU 1~2ms cost for each layer while benefit 5ms-8ms decode latency with ep_size = 64. The following updates have been made: 1、expert distribution recording with lower cost. 2、async cpu computing for eplb algo and other python operator. 3、new eplb algo with less expert rebalancing while...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [RFC]: Dynamic Expert Load Balance with Zero-like-overhead RFC;stale ### Motivation Currently dynamically experts balancing would stop-the-world. Asynchronously expert load balancing would be better without flowing prob...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ke-overhead RFC;stale ### Motivation Currently dynamically experts balancing would stop-the-world. Asynchronously expert load balancing would be better without flowing problems: 1. Host-bound latency: There are many cpu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tested that batch_isend_irecv cost more 100ms for 16 experts weight transmission in A2 server of ascend. We have finished SwiftBalancer -- Dynamic Expert Load Balance with Zero-like-overhead on vllm-ascend 1943(https://...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Dynamic Expert Load Balance with Zero-like-overhead RFC;stale ### Motivation Currently dynamically experts balancing would stop-the-world. Asynchronously expert load balancing would be better without flowing prob...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: load balancing would be better without flowing problems: 1. Host-bound latency: There are many cpu operations during EPLB such as eplb-algorithm、creating p2p ops、and log2phy expert converting would spend long cpu time,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
