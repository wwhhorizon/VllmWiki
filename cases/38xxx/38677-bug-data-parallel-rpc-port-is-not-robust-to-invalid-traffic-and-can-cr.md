# vllm-project/vllm#38677: [Bug]: data_parallel_rpc_port is not robust to invalid traffic and can crash multi-node startup

| 字段 | 值 |
| --- | --- |
| Issue | [#38677](https://github.com/vllm-project/vllm/issues/38677) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: data_parallel_rpc_port is not robust to invalid traffic and can crash multi-node startup

### Issue 正文摘录

### Your current environment vLLM: current main Deployment: Kubernetes + LWS, Nodes: 2 DP: 16,Local DP per node: 8,TP: 1,EP enabled,all2all backend: deepep_low_latency ``` yaml vllm serve /??? \ --served-model-name /??? \ --tensor-parallel-size 1 \ --data-parallel-size 16 \ --data-parallel-size-local 8 \ --enable-expert-parallel \ --all2all-backend deepep_low_latency \ --data-parallel-address ${LWS_LEADER_ADDRESS} \ --data-parallel-rpc-port 13345 \ --data-parallel-hybrid-lb \ --api-server-count 8 \ --trust-remote-code \ --port 8000 \ --nnodes ${LWS_GROUP_SIZE} \ --node-rank ${LWS_WORKER_INDEX} ``` ### 🐛 Describe the bug In multi-node DP serving, vLLM crashes during engine startup if the DP handshake port (`--data-parallel-rpc-port`) receives a non-engine TCP connection such as an HTTP metrics scrape. Instead of ignoring or rejecting invalid traffic, the launcher interprets the incoming bytes as an engine identity and raises: ```text RuntimeError: Message from engine with unexpected data parallel rank: ``` During startup, the leader pod fails with logs like: ```plaintext Traceback (most recent call last): File "/usr/local/bin/vllm", line 10, in sys.exit(main()) ^^^^^^ File "/usr/lo...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: es + LWS, Nodes: 2 DP: 16,Local DP per node: 8,TP: 1,EP enabled,all2all backend: deepep_low_latency ``` yaml vllm serve /??? \ --served-model-name /??? \ --tensor-parallel-size 1 \ --data-parallel-size 16 \ --data-paral...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 9286026737070985330274755728732960911242422067284 ``` The large integer decodes to the bytes of an HTTP request sent to the DP RPC port, for example: ``` T /metrics HTTP/1.1 Host: 172.26.43.196:13345 User-Agent: vm_prom...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: DP: 16,Local DP per node: 8,TP: 1,EP enabled,all2all backend: deepep_low_latency ``` yaml vllm serve /??? \ --served-model-name /??? \ --tensor-parallel-size 1 \ --data-parallel-size 16 \ --data-parallel-size-local 8 \...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: l backend: deepep_low_latency ``` yaml vllm serve /??? \ --served-model-name /??? \ --tensor-parallel-size 1 \ --data-parallel-size 16 \ --data-parallel-size-local 8 \ --enable-expert-parallel \ --all2all-backend deepep...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
