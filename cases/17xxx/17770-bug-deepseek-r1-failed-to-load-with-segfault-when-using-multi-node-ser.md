# vllm-project/vllm#17770: [Bug]: Deepseek R1 failed to load with segfault when using multi-node serving in V1

| 字段 | 值 |
| --- | --- |
| Issue | [#17770](https://github.com/vllm-project/vllm/issues/17770) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Deepseek R1 failed to load with segfault when using multi-node serving in V1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug With vLLM image in docker hub `vllm/vllm-openai:v0.8.4`, attempt to run deepseek R1 model in V1 engine fail with segfault, while changing back to V0 using `export VLLM_USE_V1=0` can start successfully. To reproduce, use 2 nodes and create a ray cluster according to vLLM's multi-node guide and run below command on one of the node ``` vllm serve deepseek-ai/DeepSeek-R1 --block-size 128 --max-model-len 3500 --max-num-batched-tokens 3500 --tensor-parallel-size 16 --disable-log-requests ``` Below segfault will be observed ``` (RayWorkerWrapper pid=2191173, ip=10.52.51.232) *** SIGSEGV received at time=1746566409 on cpu 131 *** (RayWorkerWrapper pid=2191173, ip=10.52.51.232) PC: @ 0x7fcfcd849b8a (unknown) addProxyOpIfNeeded() (RayWorkerWrapper pid=2191173, ip=10.52.51.232) @ 0x7ffff7c9e520 267994832 (unknown) (RayWorkerWrapper pid=2191173, ip=10.52.51.232) @ 0x80000 (unknown) (unknown) (RayWorkerWrapper pid=2191173, ip=10.52.51.232) [2025-05-06 14:20:09,187 E 2191173 2191173] logging.cc:484: *** SIGSEGV received at time=1746566409 on cpu 131 *** (RayWorkerWrapper pid=2191173, ip=10.52.51.232) [2025-05-06 14:20:09,187 E 2191173 2191173]...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 51.232) File "/usr/local/lib/python3.12/dist-packages/vllm/compilation/backends.py", line 649 in __call__ (RayWorkerWrapper pid=2191173, ip=10.52.51.232) File " .162", line 817 in forward (RayWorkerWrapper pid=2191173,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Your current environment ### 🐛 Describe the bug With vLLM image in docker hub `vllm/vllm-openai:v0.8.4`, attempt to run deepseek R1 model in V1 engine fail with segfault, while changing back to V0 using `export VLLM_USE...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: mage in docker hub `vllm/vllm-openai:v0.8.4`, attempt to run deepseek R1 model in V1 engine fail with segfault, while changing back to V0 using `export VLLM_USE_V1=0` can start successfully. To reproduce, use 2 nodes an...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: local/lib/python3.12/dist-packages/vllm/distributed/device_communicators/cuda_communicator.py", line 63 in all_reduce (RayWorkerWrapper pid=2191173, ip=10.52.51.232) File "/usr/local/lib/python3.12/dist-packages/vllm/di...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: failed to load with segfault when using multi-node serving in V1 bug;ray;stale ### Your current environment ### 🐛 Describe the bug With vLLM image in docker hub `vllm/vllm-openai:v0.8.4`, attempt to run deepseek R1 mode...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
