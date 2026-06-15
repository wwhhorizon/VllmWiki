# vllm-project/vllm#7896: [Bug]:  RuntimeError: NCCL error: unhandled cuda error (run with NCCL_DEBUG=INFO for details) [repeated 6x across cluster]

| 字段 | 值 |
| --- | --- |
| Issue | [#7896](https://github.com/vllm-project/vllm/issues/7896) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  RuntimeError: NCCL error: unhandled cuda error (run with NCCL_DEBUG=INFO for details) [repeated 6x across cluster]

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am running a 8 node Kubernetes cluster with vllm and deploying llama 3.1 405b BF16 model as 4 replicas. 3 of the replicas are running in stable state, the 4th repics keeps restarting with the following error. Here are my start up commands for leader and worker. leader command ``` /vllm-workspace/ray_init.sh leader --ray_cluster_size=$RAY_CLUSTER_SIZE; python3 -m vllm.entrypoints.openai.api_server --port 8080 --model meta-llama/Meta-Llama-3.1-405B-Instruct \ --tensor-parallel-size 8 --pipeline_parallel_size 2 --max-logprobs 1000 --max-num-batched-tokens 16384 \ --enable-chunked-prefill --kv-cache-dtype fp8 --disable-log-stats --gpu-memory-utilization 0.95 \ --device cuda --quantization fp8 ``` Worker Command - ``` /vllm-workspace/ray_init.sh worker --ray_address=$(LEADER_NAME).$(LWS_NAME).$(NAMESPACE).svc.cluster.local ``` Error Trace : ```(RayWorkerWrapper pid=1181, ip=192.168.145.194) INFO 08-27 05:11:55 pynccl.py:63] vLLM is using nccl==2.20.5 [repeated 14x across cluster] ERROR 08-27 05:12:18 worker_base.py:382] Error executing method init_device. This might cause deadlock in distributed execution. ERROR 08-27 05:12:18 worke...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: nning a 8 node Kubernetes cluster with vllm and deploying llama 3.1 405b BF16 model as 4 replicas. 3 of the replicas are running in stable state, the 4th repics keeps restarting with the following error. Here are my sta...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;operator;quantization;samp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: he bug I am running a 8 node Kubernetes cluster with vllm and deploying llama 3.1 405b BF16 model as 4 replicas. 3 of the replicas are running in stable state, the 4th repics keeps restarting with the following error. H...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 1000 --max-num-batched-tokens 16384 \ --enable-chunked-prefill --kv-cache-dtype fp8 --disable-log-stats --gpu-memory-utilization 0.95 \ --device cuda --quantization fp8 ``` Worker Command - ``` /vllm-workspace/ray_init....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: RuntimeError: NCCL error: unhandled cuda error (run with NCCL_DEBUG=INFO for details) [repeated 6x across cluster] bug ### Your current environment ### 🐛 Describe the bug I am running a 8 node Kubernetes cluster...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
