# vllm-project/vllm#2773: Error with vLLM docker container `vllm/vllm-openai:v0.3.0`

| 字段 | 值 |
| --- | --- |
| Issue | [#2773](https://github.com/vllm-project/vllm/issues/2773) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;moe |
| 子分类 |  |
| Operator 关键词 | operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Error with vLLM docker container `vllm/vllm-openai:v0.3.0`

### Issue 正文摘录

I am trying to deploy vLLM on k8 with the following deployment YAML ``` apiVersion: apps/v1 kind: Deployment metadata: name: vllm-deployment spec: replicas: 1 # You can scale this up to 10 selector: matchLabels: app: vllm template: metadata: labels: app: vllm spec: tolerations: - key: cloud.google.com/gke-spot operator: Equal value: "true" effect: NoSchedule nodeSelector: cloud.google.com/gke-spot: "true" volumes: - name: dshm emptyDir: medium: Memory containers: - name: vllm-container image: vllm/vllm-openai:latest args: ["--model", "ehartford/dolphin-2.5-mixtral-8x7b", "--host", "0.0.0.0", "--tensor-parallel-size", "8"] # check the health of the container by hitting port 8000/health endpoint readinessProbe: httpGet: path: /health port: 8000 initialDelaySeconds: 5 periodSeconds: 1 ports: - containerPort: 8000 name: vllm-port env: - name: HUGGING_FACE_HUB_TOKEN value: ${HUGGING_FACE_HUB_TOKEN} resources: limits: nvidia.com/gpu: 8 # Requesting one GPU per pod volumeMounts: - mountPath: /dev/shm name: dshm ``` Although this deployment worked fine with previous versions of the vLLM docker container, on the latest version, the following error occurs after the model is finished loading...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Error with vLLM docker container `vllm/vllm-openai:v0.3.0` I am trying to deploy vLLM on k8 with the following deployment YAML ``` apiVersion: apps/v1 kind: Deployment metadata: name: vllm-deployment spec: replicas: 1 #...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: the following deployment YAML ``` apiVersion: apps/v1 kind: Deployment metadata: name: vllm-deployment spec: replicas: 1 # You can scale this up to 10 selector: matchLabels: app: vllm template: metadata: labels: app: vl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vllm-container image: vllm/vllm-openai:latest args: ["--model", "ehartford/dolphin-2.5-mixtral-8x7b", "--host", "0.0.0.0", "--tensor-parallel-size", "8"] # check the health of the container by hitting port 8000/health e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ntainers: - name: vllm-container image: vllm/vllm-openai:latest args: ["--model", "ehartford/dolphin-2.5-mixtral-8x7b", "--host", "0.0.0.0", "--tensor-parallel-size", "8"] # check the health of the container by hitting...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 63, in fused_moe_kernel File "/usr/local/lib/python3.10/dist-packages/triton/compiler/compiler.py", line 425, in compile so_path = make_stub(name, signature, constants) File "/usr/local/lib/python3.10/dist-packages/trit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
