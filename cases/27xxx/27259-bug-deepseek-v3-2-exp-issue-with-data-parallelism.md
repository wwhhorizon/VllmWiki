# vllm-project/vllm#27259: [Bug]: DeepSeek v3.2 Exp Issue with Data Parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#27259](https://github.com/vllm-project/vllm/issues/27259) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;moe |
| 子分类 |  |
| Operator 关键词 | cuda;moe |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek v3.2 Exp Issue with Data Parallelism

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using the below k8s deployment on 8xB200 GPUs, single node. apiVersion: apps/v1 kind: Deployment ... spec: replicas: 1 ... spec: volumes: - name: vllm-prod-stack-v3-storage persistentVolumeClaim: claimName: vllm-prod-stack-v3-deepseek-v32-exp-storage-claim - name: shm emptyDir: medium: Memory sizeLimit: 64Gi containers: - name: vllm image: IMAGE command: - /opt/venv/bin/vllm - serve - deepseek-ai/DeepSeek-V3.2-Exp - '--host' - 0.0.0.0 - '--port' - '8000' - '--tensor-parallel-size' - '1' - '--enable-auto-tool-choice' - '--data-parallel-size' - '8' - '--enable-expert-parallel' - '--tool-call-parser' - deepseek_v31 ports: - name: container-port containerPort: 8000 protocol: TCP - name: zmq-port containerPort: 55555 protocol: TCP - name: ucx-port containerPort: 9999 protocol: TCP env: - name: HF_HOME value: /data - name: POD_IP valueFrom: fieldRef: apiVersion: v1 fieldPath: status.podIP - name: HF_TOKEN valueFrom: secretKeyRef: name: hf-token-secret key: HF_TOKEN - name: VLLM_LOGGING_LEVEL value: DEBUG - name: DO_NOT_TRACK value: '1' - name: VLLM_USE_DEEP_GEMM value: '1' resources: limits: nvidia.com/gpu: '8' requests: cpu: '180' mem...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: bug Using the below k8s deployment on 8xB200 GPUs, single node. apiVersion: apps/v1 kind: Deployment ... spec: replicas: 1 ... spec: volumes: - name: vllm-prod-stack-v3-storage persistentVolumeClaim: claimName: vllm-pro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: DeepSeek v3.2 Exp Issue with Data Parallelism bug;stale ### Your current environment ### 🐛 Describe the bug Using the below k8s deployment on 8xB200 GPUs, single node. apiVersion: apps/v1 kind: Deployment ... spe...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: - '--data-parallel-size' - '8' - '--enable-expert-parallel' - '--tool-call-parser' - deepseek_v31 ports: - name: container-port containerPort: 8000 protocol: TCP - name: zmq-por
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ort: 9999 protocol: TCP env: - name: HF_HOME value: /data - name: POD_IP valueFrom: fieldRef: apiVersion: v1 fieldPath: status.podIP - name: HF_TOKEN
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: DeepSeek v3.2 Exp Issue with Data Parallelism bug;stale ### Your current environment ### 🐛 Describe the bug Using the below k8s deployment on 8xB200 GPUs, single node. apiVersion: apps/v1 kind: Deployment ... spe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
