# vllm-project/vllm#7074: run llama 3.1 405B has error[Usage]: 

| 字段 | 值 |
| --- | --- |
| Issue | [#7074](https://github.com/vllm-project/vllm/issues/7074) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> run llama 3.1 405B has error[Usage]: 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` environment two node,node1 and node2,every node eth set is eth0 is the controller network eth1 to eth8 is the GPU RoCe network vllm version：vLLM API server version 0.5.3.post1 the start command is： GLOO_SOCKET_IFNAME=eth0 NCCL_SOCKET_IFNAME=eth0 TP_SOCKET_IFNAME="eth0" vllm serve /models --tensor-parallel-size 16 the error is： DEBUG 08-02 08:50:03 parallel_state.py:803] world_size=16 rank=0 local_rank=0 distributed_init_method=tcp://10.41.0.7:34773 backend=nccl (RayWorkerWrapper pid=1978, ip=10.41.0.8) [rank9]:[W ProcessGroupGloo.cpp:721] **Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with** GLOO_SOCKET_IFNAME. (function operator()) (RayWorkerWrapper pid=1890, ip=10.41.0.8) [rank8]:[E ProcessGroupGloo.cpp:144] Gloo connectFullMesh failed with [../third_party/gloo/gloo/transport/tcp/pair.cc:144] no error (RayWorkerWrapper pid=1890, ip=10.41.0.8) ERROR 08-02 08:50:03 worker_base.py:382] Error executing method init_device. This might cause deadlock in distributed execution. (RayWorkerWrapper pid=1890, ip=10.4...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: th0 is the controller network eth1 to eth8 is the GPU RoCe network vllm version：vLLM API server version 0.5.3.post1 the start command is： GLOO_SOCKET_IFNAME=eth0 NCCL_SOCKET_IFNAME=eth0 TP_SOCKET_IFNAME="eth0" vllm serv...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: run llama 3.1 405B has error[Usage]: usage ### Your current environment ```text The output of `python collect_env.py` ``` environment two node,node1 and node2,every node eth set is eth0 is the controller network eth1 to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ize=16 rank=0 local_rank=0 distributed_init_method=tcp://10.41.0.7:34773 backend=nccl (RayWorkerWrapper pid=1978, ip=10.41.0.8) [rank9]:[W ProcessGroupGloo.cpp:721] **Warning: Unable to resolve hostname to a (local) add...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: worker_base.py:382] Error executing method init_device. This might cause deadlock in distributed execution. (RayWorkerWrapper pid=1890, ip=10.41.0.8) ERROR 08-02 08:50:03 worker_base.py:382] Traceback (most recent call...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
