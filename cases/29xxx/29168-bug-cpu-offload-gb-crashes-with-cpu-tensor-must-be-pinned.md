# vllm-project/vllm#29168: [Bug]: cpu-offload-gb crashes with "CPU tensor must be pinned"

| 字段 | 值 |
| --- | --- |
| Issue | [#29168](https://github.com/vllm-project/vllm/issues/29168) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: cpu-offload-gb crashes with "CPU tensor must be pinned"

### Issue 正文摘录

### Your current environment My enironment include k8s and rtx4090 equipped nodes. My GGUF Gemma3-12b is working well with `maxModelLen : 8192` I would like to increase maxModelLen, so the model need to be offloaded to CPU AFAIN it can be obtained using ["--cpu-offload-gb", "2"] as `extraArgs`, but engine pod crashes with: `assert cpu_tensor.is_pinned(), "CPU tensor must be pinned"` Below are the k8 helm manifests: `servingEngineSpec: modelSpec: - name: "gemma3-12b" repository: "vllm/vllm-openai" tag: "nightly" modelURL: "/data/google/gemma-3-12b-it-q4_0.gguf" imagePullPolicy: "IfNotPresent" replicaCount: 1 requestCPU: "8" requestMemory: "40Gi" requestGPU: 1 pvcStorage: "50Gi" pvcMatchLabels: model: "vllm" env: - name: VLLM_LOGGING_LEVEL value: "DEBUG" vllmConfig: cpu-offload-gb: 2 gpuMemoryUtilization: 0.85 dtype: "bfloat16" maxModelLen: 8192 offload: true # extraArgs: ["--tokenizer", "google/gemma-3-12b-it", "--cpu-offload-gb", "1"] extraArgs: ["--tokenizer", "google/gemma-3-12b-it"] resources: requests: memory: 20000Mi limits: memory: 40000Mi runtimeClassName: "" startupProbe: initialDelaySeconds: 180 periodSeconds: 30 failureThreshold: 3 livenessProbe: httpGet: path: /health p...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ig: cpu-offload-gb: 2 gpuMemoryUtilization: 0.85 dtype: "bfloat16" maxModelLen: 8192 offload: true # extraArgs: ["--tokenizer", "google/gemma-3-12b-it", "--cpu-offload-gb", "1"] extraArgs: ["--tokenizer", "google/gemma-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ironment My enironment include k8s and rtx4090 equipped nodes. My GGUF Gemma3-12b is working well with `maxModelLen : 8192` I would like to increase maxModelLen, so the model need to be offloaded to CPU AFAIN it can be...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ironment My enironment include k8s and rtx4090 equipped nodes. My GGUF Gemma3-12b is working well with `maxModelLen : 8192` I would like to increase maxModelLen, so the model need to be offloaded to CPU AFAIN it can be...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: cpu-offload-gb crashes with "CPU tensor must be pinned" bug;stale ### Your current environment My enironment include k8s and rtx4090 equipped nodes. My GGUF Gemma3-12b is working well with `maxModelLen : 8192` I...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: /vllm(/|$)(.*) pathType: ImplementationSpecific backend: service: name: vllm-router-service port: number: 80 tls: - hosts: - ai-lab.rt-solar.ru secretName: ailab-tls nodeSele

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
