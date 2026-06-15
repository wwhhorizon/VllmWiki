# vllm-project/vllm#37933: [Bug]: v0.18.0 fails to run pipeline parallel across nodes

| 字段 | 值 |
| --- | --- |
| Issue | [#37933](https://github.com/vllm-project/vllm/issues/37933) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.18.0 fails to run pipeline parallel across nodes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Launching PP on 2 CPU-only nodes ```python vllm serve meta-llama/Llama-3.1-8B-Instruct --pipeline-parallel-size 2 --nnodes 2 --node-rank 0 --master-addr vllm serve meta-llama/Llama-3.1-8B-Instruct --pipeline-parallel-size 2 --nnodes 2 --node-rank 1 --master-addr --headless ``` After sending the first request, it gives following error message: ``` (Worker_PP1 pid=42781) ERROR 03-23 21:23:08 [multiproc_executor.py:932] File "/root/venv/lib/python3.12/site-packages/vllm/distributed/device_communicators/cpu_communicator.py", line 152, in recv_tensor_dict (Worker_PP1 pid=42781) ERROR 03-23 21:23:08 [multiproc_executor.py:932] return self.dist_module.recv_tensor_dict(src) (Worker_PP1 pid=42781) ERROR 03-23 21:23:08 [multiproc_executor.py:932] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_PP1 pid=42781) ERROR 03-23 21:23:08 [multiproc_executor.py:932] AttributeError: module 'torch.distributed' has no attribute 'recv_tensor_dict' ``` When ranks are not on the same node, it uses `torch.distributed` as the backend, rather than `_CPUSHMDistributed`. `_CPUSHMDistributed` has a function named `recv_tensor_dict()`, but `torch.distributed` doesn't....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: stributed` doesn't. Not sure why this issue was not revealed in previous versions, but there should be a more robust way to check whether `send_tensor_dict()` and `recv_tensor_dict()` can be called. ### Before submittin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ribe the bug Launching PP on 2 CPU-only nodes ```python vllm serve meta-llama/Llama-3.1-8B-Instruct --pipeline-parallel-size 2 --nnodes 2 --node-rank 0 --master-addr vllm serve meta-llama/Llama-3.1-8B-Instruct --pipelin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: s 2 --node-rank 1 --master-addr --headless ``` After sending the first request, it gives following error message: ``` (Worker_PP1 pid=42781) ERROR 03-23 21:23:08 [multiproc_executor.py:932] File "/root/venv/lib/python3....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: When ranks are not on the same node, it uses `torch.distributed` as the backend, rather than `_CPUSHMDistributed`. `_CPUSHMDistributed` has a function named `recv_tensor_dict()`, but `torch.distributed` doesn't. Not sur...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
