# vllm-project/vllm#17160: [Bug]: failed to run distribute Inference with vllm 0.8.2

| 字段 | 值 |
| --- | --- |
| Issue | [#17160](https://github.com/vllm-project/vllm/issues/17160) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: failed to run distribute Inference with vllm 0.8.2

### Issue 正文摘录

### Your current environment I am trying to run the distribute inference in ray with vllm 0.8.2 and failed with the following errors, here are the steps: 1. I followed this link to do the sanity check, and it passed: https://docs.vllm.ai/en/latest/getting_started/troubleshooting.html#incorrect-hardware-driver ray head node ``` ======== Autoscaler status: 2025-04-25 13:23:43.124555 ======== Node status --------------------------------------------------------------- Active: 1 node_1331c5c771898a75caaaeed528c77d9a10132b3f6f57a46bd444980d 1 node_f9fee740f9505a910fa99a16799e10a4fad360251146be8297486b49 Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------------------------- Usage: 0.0/32.0 CPU 0.0/4.0 GPU 0B/30.14GiB memory 0B/12.92GiB object_store_memory Demands: (no resource demands) NCCL_SOCKET_IFNAME=ens4 GLOO_SOCKET_IFNAME=ens4 NCCL_DEBUG=TRACE torchrun --nnodes 2 --nproc-per-node=2 --node-rank 0 --master_addr 172.21.151.99 test.py ``` ray worker node ``` NCCL_SOCKET_IFNAME=ens4 GLOO_SOCKET_IFNAME=ens4 NCCL_DEBUG=TRACE torchrun --nnodes 2 --nproc-per-node=2 --node-rank 1 --master_addr 172.21.151.99 test.py ``` 2. I ran th...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: failed to run distribute Inference with vllm 0.8.2 bug;stale ### Your current environment I am trying to run the distribute inference in ray with vllm 0.8.2 and failed with the following errors, here are the step...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ailed with the following errors, here are the steps: 1. I followed this link to do the sanity check, and it passed: https://docs.vllm.ai/en/latest/getting_started/troubleshooting.html#incorrect-hardware-driver ray head...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: eshooting.html#incorrect-hardware-driver ray head node ``` ======== Autoscaler status: 2025-04-25 13:23:43.124555 ======== Node status --------------------------------------------------------------- Active: 1 node_1331c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: M_DISABLE=1 export NCCL_NET=Socket export NCCL_DEBUG=TRACE vllm serve /models/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B \ --served-model-name DeepSeek-R1-Distill-Qwen-14B \ --gpu-memory-utilization 0.95 \ --dtype half \...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dtype='half', kv_cache_dtype='auto', max_model_len=2048, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=2, tensor_parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
