# vllm-project/vllm#14456: [Bug]: No Cuda GPUs are available when running vLLM on Ray (Qwen 2.5 VL AWQ)

| 字段 | 值 |
| --- | --- |
| Issue | [#14456](https://github.com/vllm-project/vllm/issues/14456) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: No Cuda GPUs are available when running vLLM on Ray (Qwen 2.5 VL AWQ)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi all, I am hosting vLLM on Ray Serve on a Kubernetes cluster (AWS EKS) and I run into a strange issue when trying to host the AWQ quantized [Qwen2.5-VL-7B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct-AWQ) models. The stack trace implies that there is no CUDA GPU available, but I can detect my GPUs when I SSH into the pod and run `nvidia-smi`. This error seems specific to the AWQ quantized model versions. When I run the same configs using the non-quantized QWEN models, it is successful. I will share the stack trace below: nvidia-smi output Here are my Ray Serve configs and entrypoint script: ``` - name: qwen2-vl-7b-instruct route_prefix: /qwen2-vl-7b-instruct import_path: vllm_florence2_prototype.api_server:build_app runtime_env: pip: - "git+https://github.com/huggingface/transformers.git@11afab19c0e4b652855f9ed7f82aa010c4f14754" - "vllm[video]==0.7.2" - "qwen-vl-utils[decord]" - "ninja" deployments: - name: VLLMDeployment max_ongoing_requests: 1000 autoscaling_config: min_replicas: 1 max_replicas: 5 args: model: "Qwen/Qwen2.5-VL-7B-Instruct-AWQ" tensor_parallel_size: 4 max_model_len: 32768 trust_remote_code:...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: No Cuda GPUs are available when running vLLM on Ray (Qwen 2.5 VL AWQ) bug;ray;stale ### Your current environment ### 🐛 Describe the bug Hi all, I am hosting vLLM on Ray Serve on a Kubernetes cluster (AWS EKS) and...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: GPUs when I SSH into the pod and run `nvidia-smi`. This error seems specific to the AWQ quantized model versions. When I run the same configs using the non-quantized QWEN models, it is successful. I will share the stack...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: No Cuda GPUs are available when running vLLM on Ray (Qwen 2.5 VL AWQ) bug;ray;stale ### Your current environment ### 🐛 Describe the bug Hi all, I am hosting vLLM on Ray Serve on a Kubernetes cluster (AWS EKS) and...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ter (AWS EKS) and I run into a strange issue when trying to host the AWQ quantized [Qwen2.5-VL-7B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct-AWQ) models. The stack trace implies that there is no CU...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: da GPUs are available when running vLLM on Ray (Qwen 2.5 VL AWQ) bug;ray;stale ### Your current environment ### 🐛 Describe the bug Hi all, I am hosting vLLM on Ray Serve on a Kubernetes cluster (AWS EKS) and I run into...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
