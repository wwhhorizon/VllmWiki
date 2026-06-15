# vllm-project/vllm#2084: Unable to run any model with tensor_parallel_size>1 on AWS sagemaker notebooks

| 字段 | 值 |
| --- | --- |
| Issue | [#2084](https://github.com/vllm-project/vllm/issues/2084) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Unable to run any model with tensor_parallel_size>1 on AWS sagemaker notebooks

### Issue 正文摘录

I am running my code on AWS Sagemaker notebooks and I have machine with 4 GPUs. Whenever I set the tensor_parallel_size>1 it shows me the following error. NFO 12-13 13:07:31 llm_engine.py:72] Initializing an LLM engine with config: model='mistralai/Mistral-7B-Instruct-v0.1', tokenizer='mistralai/Mistral-7B-Instruct-v0.1', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=4, quantization=None, seed=0) (RayWorker pid=14391) pytorch-2-0-1-gpu-ml-g4dn-12xlarge-a1771cff5b2706f02b86883798ff:14391:14391 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^lo,docker,veth (RayWorker pid=14391) (RayWorker pid=14391) pytorch-2-0-1-gpu-ml-g4dn-12xlarge-a1771cff5b2706f02b86883798ff:14391:14391 [0] bootstrap.cc:45 NCCL WARN Bootstrap : no socket interface found (RayWorker pid=14391) pytorch-2-0-1-gpu-ml-g4dn-12xlarge-a1771cff5b2706f02b86883798ff:14391:14391 [0] NCCL INFO init.cc:82 -> 3 (RayWorker pid=14391) pytorch-2-0-1-gpu-ml-g4dn-12xlarge-a1771cff5b2706f02b86883798ff:14391:14391 [0] NCCL INFO init.cc:101 -> 3 -----------------------------------------------...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: f:14391:14391 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^lo,docker,veth (RayWorker pid=14391) (RayWorker pid=14391) pytorch-2-0-1-gpu-ml-g4dn-12xlarge-a1771cff5b2706f02b86883798ff:14391:14391 [0] bootstrap....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=4, quantization=None, seed=0) (RayWorker pid=143...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Unable to run any model with tensor_parallel_size>1 on AWS sagemaker notebooks stale I am running my code on AWS Sagemaker notebooks and I have machine with 4 GPUs. Whenever I set the tensor_parallel_size>1 it shows me...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: to run any model with tensor_parallel_size>1 on AWS sagemaker notebooks stale I am running my code on AWS Sagemaker notebooks and I have machine with 4 GPUs. Whenever I set the tensor_parallel_size>1 it shows me the fol...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ------------------------------------------------------- RayTaskError(DistBackendError) Traceback (most recent call last) Cell In[1], line 3 1 from vllm import LLM 2 import torch ----> 3 llm = LLM(model="mistralai/Mistra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
