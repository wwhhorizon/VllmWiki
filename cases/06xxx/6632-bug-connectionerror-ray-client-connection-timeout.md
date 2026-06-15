# vllm-project/vllm#6632: [Bug]: ConnectionError: ray client connection timeout

| 字段 | 值 |
| --- | --- |
| Issue | [#6632](https://github.com/vllm-project/vllm/issues/6632) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ConnectionError: ray client connection timeout

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` vllm 0.5.2 ray 2.32.0 python 3.10 ======== Autoscaler status: 2024-07-22 11:48:35.722861 ======== Node status --------------------------------------------------------------- Active: 1 node_9184feb3690b1aef0da4ec0b9b7a32c642111f8c4a33b968d5bdac59 1 node_3d712c9cfd35feacee5ead596945de4a7cb65d2eca3073431397c25e Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------------------------- Usage: 0.0/176.0 CPU 0.0/8.0 GPU 0B/613.29GiB memory 0B/266.83GiB object_store_memory Demands: (no resource demands) ### 🐛 Describe the bug from vllm import LLM, SamplingParams import os os.environ["GLOO_SOCKET_IFNAME"]='eth0' os.environ["TP_SOCKET_IFNAME"]='eth0' os.environ["NCCL_SOCKET_IFNAME"]='eth0' import ray ray.init("ray://10.157.148.2:6379") # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model="./qwen",trust_remote_code=True,gpu_memory_utiliza...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model="./qwen",trust_remote_code=True,gpu_memory_utilization=0.8,tensor_parallel_size=8,enforce_eager=True) # Generate texts from the prompts. The o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: ConnectionError: ray client connection timeout bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` vllm 0.5.2 ray 2.32.0 python 3.10 ======== Autoscaler status: 2024-07-22 1
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: mory Demands: (no resource demands) ### 🐛 Describe the bug from vllm import LLM, SamplingParams import os os.environ["GLOO_SOCKET_IFNAME"]='eth0' os.environ["TP_SOCKET_IFNAME"]='eth0' os.environ["NCCL_SOCKET_IFNAME"]='e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 0.5.2 ray 2.32.0 python 3.10 ======== Autoscaler status: 2024-07-22 11:48:35.722861 ======== Node status --------------------------------------------------------------- Active: 1 node_9184feb3690b1aef0da4ec0b9b7a32c6421...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
