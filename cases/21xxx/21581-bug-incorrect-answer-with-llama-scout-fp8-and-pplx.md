# vllm-project/vllm#21581: [Bug]: Incorrect Answer with Llama-Scout-Fp8 and PPLX

| 字段 | 值 |
| --- | --- |
| Issue | [#21581](https://github.com/vllm-project/vllm/issues/21581) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;moe |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incorrect Answer with Llama-Scout-Fp8 and PPLX

### Issue 正文摘录

### Your current environment - 2 8xH200 node setup - infiniband networking the following llm-d config: ```yaml multinode: false modelArtifacts: uri: "hf://RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic" size: 300Gi authSecretName: "llm-d-hf-token" routing: modelName: RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic servicePort: 8000 parentRefs: - group: gateway.networking.k8s.io kind: Gateway name: infra-pd-inference-gateway proxy: image: ghcr.io/llm-d/llm-d-routing-sidecar:v0.2.0 connector: nixlv2 secure: false inferenceModel: criticality: Critical create: true inferencePool: create: false name: gaie-pd httpRoute: create: true epp: create: false decode: create: true replicas: 1 containers: - name: "vllm" image: "quay.io/wseaton/vllm:llmd-multistage-6" modelCommand: vllmServe args: - "--enable-expert-parallel" - "--data-parallel-size" - "8" - "--block-size" - "128" - "--kv-transfer-config" - '{"kv_connector":"NixlConnector", "kv_role":"kv_both"}' - "--disable-log-requests" - "--disable-uvicorn-access-log" - "--max-model-len" - "32000" env: - name: VLLM_NIXL_SIDE_CHANNEL_HOST valueFrom: fieldRef: fieldPath: status.podIP - name: VLLM_ALL2ALL_BACKEND value: "pplx" resources:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: th: /.config - name: shm mountPath: /dev/shm - name: torch-compile-cache mountPath: /.cache volumes: - name: metrics-volume emptyDir: {} - name: shm emptyDir: medium: Memory sizeLimit: "16Gi" - name: torch-compile-cache...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Incorrect Answer with Llama-Scout-Fp8 and PPLX bug;stale ### Your current environment - 2 8xH200 node setup - infiniband networking the following llm-d config: ```yaml multinode: false modelArtifacts: uri: "hf://...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Incorrect Answer with Llama-Scout-Fp8 and PPLX bug;stale ### Your current environment - 2 8xH200 node setup - infiniband networking the following llm-d config: ```yaml multinode: false modelArtifacts: uri: "hf://...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Incorrect Answer with Llama-Scout-Fp8 and PPLX bug;stale ### Your current environment - 2 8xH200 node setup - infiniband networking the following llm-d config: ```yaml multinode: false modelArtifacts: uri: "hf://...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: infiniband networking the following llm-d config: ```yaml multinode: false modelArtifacts: uri: "hf://RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic" size: 300Gi authSecretName: "llm-d-hf-token" routing: modelName:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
