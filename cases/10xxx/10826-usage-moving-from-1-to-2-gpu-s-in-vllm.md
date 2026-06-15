# vllm-project/vllm#10826: [Usage]: Moving from 1 to 2 GPU's in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#10826](https://github.com/vllm-project/vllm/issues/10826) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Moving from 1 to 2 GPU's in vLLM

### Issue 正文摘录

### Your current environment ```text k8s 1.31 using vllm-openai:latest ``` ### How would you like to use vllm I am currently running the QWEN model with 1 GPU with the below manifest ``` apiVersion: apps/v1 kind: Deployment metadata: name: q2q-7b namespace: nmlp labels: app: q2q-7b spec: replicas: 1 selector: matchLabels: app: q2q-7b template: metadata: labels: app: q2q-7b spec: volumes: - name: cache-volume persistentVolumeClaim: claimName: q2q-7b # vLLM needs to access the host's shared memory for tensor parallel inference. - name: shm emptyDir: medium: Memory sizeLimit: "2Gi" runtimeClassName: nvidia containers: - name: q2q-7b image: vllm/vllm-openai:latest command: ["/bin/sh", "-c"] args: [ "vllm serve Qwen/QwQ-32B-Preview --gpu-memory-utilization 0.9 --max_model_len 13680" ] env: - name: HUGGING_FACE_HUB_TOKEN valueFrom: secretKeyRef: name: hf-token-secret key: token ports: - containerPort: 8000 resources: limits: cpu: "10" memory: 100G nvidia.com/gpu: "1" requests: cpu: "10" memory: 100G nvidia.com/gpu: "1" volumeMounts: - mountPath: /root/.cache/huggingface name: cache-volume - name: shm mountPath: /dev/shm ``` This works perfectly. The trouble starts when i try to use 2 GP...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: test ``` ### How would you like to use vllm I am currently running the QWEN model with 1 GPU with the below manifest ``` apiVersion: apps/v1 kind: Deployment metadata: name: q2q-7b namespace: nmlp labels: app: q2q-7b sp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Moving from 1 to 2 GPU's in vLLM usage;stale ### Your current environment ```text k8s 1.31 using vllm-openai:latest ``` ### How would you like to use vllm I am currently running the QWEN model with 1 GPU with t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rently running the QWEN model with 1 GPU with the below manifest ``` apiVersion: apps/v1 kind: Deployment metadata: name: q2q-7b namespace: nmlp labels: app: q2q-7b spec: replicas: 1 selector: matchLabels: app: q2q-7b t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 1 GPU with the below manifest ``` apiVersion: apps/v1 kind: Deployment metadata: name: q2q-7b namespace: nmlp labels: app: q2q-7b spec: replicas: 1 selector: matchLabels: app: q2q-7b template: metadata: labels: app: q2q...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
