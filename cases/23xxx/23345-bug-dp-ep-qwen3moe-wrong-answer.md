# vllm-project/vllm#23345: [Bug][DP/EP]: Qwen3MoE Wrong Answer

| 字段 | 值 |
| --- | --- |
| Issue | [#23345](https://github.com/vllm-project/vllm/issues/23345) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | fp8;moe |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][DP/EP]: Qwen3MoE Wrong Answer

### Issue 正文摘录

### Your current environment - llm-d 0.2 (vllm==0.10.0) (`ghcr.io/llm-d/llm-d:v0.2.0`) - 4x8xH200 Cluster (w/ IB) - Qwen3-MoE, EP32 DP32 ```yaml ```yaml multinode: true modelArtifacts: uri: "hf://Qwen/Qwen3-235B-A22B-Thinking-2507-FP8" size: 100Gi authSecretName: "llm-d-hf-token" routing: modelName: Qwen/Qwen3-235B-A22B-Thinking-2507-FP8 servicePort: 8000 parentRefs: - group: gateway.networking.k8s.io kind: Gateway name: infra-wide-ep-inference-gateway proxy: image: "ghcr.io/llm-d/llm-d-routing-sidecar:v0.2.0" secure: false debugLevel: 1 connector: nixlv2 inferenceModel: criticality: Critical create: true inferencePool: create: false name: gaie-wide-ep httpRoute: create: true epp: create: false decode: create: true replicas: 1 acceleratorTypes: labelKey: gpu.nvidia.com/model labelValues: - H200 parallelism: # TODO: The value for parallelism.data is a hack to get the pod-per-node case working. # This must equal the number of nodes rather than the dp_size. data: 4 tensor: 1 # these will be derived based performance testing monitoring: podmonitor: enabled: false portName: "metrics" # decode vLLM service port (from routing.proxy.targetPort) path: "/metrics" interval: "30s" containers:...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug][DP/EP]: Qwen3MoE Wrong Answer bug;stale ### Your current environment - llm-d 0.2 (vllm==0.10.0) (`ghcr.io/llm-d/llm-d:v0.2.0`) - 4x8xH200 Cluster (w/ IB) - Qwen3-MoE, EP32 DP32 ```yaml ```yaml multinode: true mode...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug][DP/EP]: Qwen3MoE Wrong Answer bug;stale ### Your current environment - llm-d 0.2 (vllm==0.10.0) (`ghcr.io/llm-d/llm-d:v0.2.0`) - 4x8xH200 Cluster (w/ IB) - Qwen3-MoE, EP32 DP32 ```yaml ```yaml multinode: true mode...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug][DP/EP]: Qwen3MoE Wrong Answer bug;stale ### Your current environment - llm-d 0.2 (vllm==0.10.0) (`ghcr.io/llm-d/llm-d:v0.2.0`) - 4x8xH200 Cluster (w/ IB) - Qwen3-MoE, EP32 DP32 ```yaml ```yaml multinode: true mode...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 22B-Thinking-2507-FP8" size: 100Gi authSecretName: "llm-d-hf-token" routing: modelName: Qwen/Qwen3-235B-A22B-Thinking-2507-FP8 servicePort: 8000 parentRefs: - group: gateway.networking.k8s.io kind: Gateway name: infra-w...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e: true modelArtifacts: uri: "hf://Qwen/Qwen3-235B-A22B-Thinking-2507-FP8" size: 100Gi authSecretName: "llm-d-hf-token" routing: modelName: Qwen/Qwen3-235B-A22B-Thinking-2507-FP8 servicePort: 8000 parentRefs: - group: g...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
