# vllm-project/vllm#7466: [Usage]: Got nccl error when deploy vllm in k8s with multiple GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#7466](https://github.com/vllm-project/vllm/issues/7466) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Got nccl error when deploy vllm in k8s with multiple GPUs

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I trying to deploy a Qwen2-72b model in k8s, with 4 GPUs in one node. Accroding to the log it seems can't enable NCCL P2P in k8s pod, even the GPUs are in the same node. Or is there a way to enable it? Here is my k8s deployment file: ` apiVersion: apps/v1 kind: Deployment metadata: name: vllm-deployment namespace: model spec: replicas: 1 # You can scale this up to 10 selector: matchLabels: app: vllm template: metadata: labels: app: vllm spec: volumes: - name: dshm emptyDir: medium: Memory containers: - name: vllm-container image: vllm/vllm-openai:latest env: - name: NCCL_DEBUG value: INFO args: ["--model", "Qwen/Qwen2-72B-Instruct-GPTQ-Int4", "--download-dir", "/models", "--served-model-name", "qwen2-72b", "--kv-cache-dtype", "fp8_e4m3", "--tensor-parallel-size", "4", "--gpu-memory-utilization", "0.8", "--max-model-len", "14336", "--port", "11434"] # check the health of the container by hitting port 8000/health endpoint readinessProbe: httpGet: path: /health port: 11434 initialDelaySeconds: 5 periodSeconds: 1 ports: - containerPort: 11434 name: vllm-port resources: req...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: name: vllm-deployment namespace: model spec: replicas: 1 # You can scale this up to 10 selector: matchLabels: app: vllm template: metadata: labels: app: vllm spec: volumes: - name: dshm emptyDir: medium: Memory cont
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ct_env.py` ``` ### How would you like to use vllm I trying to deploy a Qwen2-72b model in k8s, with 4 GPUs in one node. Accroding to the log it seems can't enable NCCL P2P in k8s pod, even the GPUs are in the same node....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: de. Or is there a way to enable it? Here is my k8s deployment file: ` apiVersion: apps/v1 kind: Deployment metadata: name: vllm-deployment namespace: model spec: replicas: 1 # You can scale this up to 10 selector: match...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Got nccl error when deploy vllm in k8s with multiple GPUs usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I trying to deploy a Qwen2...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: t4", "--download-dir", "/models", "--served-model-name", "qwen2-72b", "--kv-cache-dtype", "fp8_e4m3", "--tensor-parallel-size", "4", "--gpu-memory-utilization", "0.8", "--max-model-len", "14336", "--port", "11434"] # ch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
