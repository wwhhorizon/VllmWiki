# vllm-project/vllm#25371: [Feature]: Distribute API servers across multiple nodes

| 字段 | 值 |
| --- | --- |
| Issue | [#25371](https://github.com/vllm-project/vllm/issues/25371) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Distribute API servers across multiple nodes

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The current --api-server-count parameter scales the API servers on a single node. _from utils.py, APIServerProcessManager_ ``` ... for i, in_addr, out_addr in zip(range(num_servers), input_addresses, output_addresses): client_config = { "input_address": in_addr, "output_address": out_addr, "client_count": num_servers, "client_index": i } if stats_update_address is not None: client_config["stats_update_address"] = stats_update_address proc = spawn_context.Process(target=target_server_fn, name=f"ApiServer_{i}", args=(listen_address, sock, args, client_config)) self.processes.append(proc) proc.start() logger.info("Started %d API server processes", len(self.processes)) ... ``` A potential improvement is to distribute the API servers across available nodes to balance load. For example, in a two-node, DP-16 configuration, half the API servers (0-7) would run on Node 0 and the other half (8-15) on Node 1, with each server managing one DP rank. An external load balancer can be applied to route client requests to the appropriate API server based on its assigned rank. This strategy relieves the computational burden on Node 0 by offloading half of the...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cales the API servers on a single node. _from utils.py, APIServerProcessManager_ ``` ... for i, in_addr, out_addr in zip(range(num_servers), input_addresses, output_addresses): client_config = { "input_address": in_addr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Distribute API servers across multiple nodes feature request;stale ### 🚀 The feature, motivation and pitch The current --api-server-count parameter scales the API servers on a single node. _from utils.py, API...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: reprocessing/postprocessing workload to Node 1, improving overall system throughput and resilience. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sur...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: feature, motivation and pitch The current --api-server-count parameter scales the API servers on a single node. _from utils.py, APIServerProcessManager_ ``` ... for i, in_addr, out_addr in zip(range(num_servers), input_...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: gned rank. This strategy relieves the computational burden on Node 0 by offloading half of the preprocessing/postprocessing workload to Node 1, improving overall system throughput and resilience. ### Alternatives _No re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
