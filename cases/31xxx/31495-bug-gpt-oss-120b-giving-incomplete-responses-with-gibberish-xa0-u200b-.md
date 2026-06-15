# vllm-project/vllm#31495: [Bug]: GPT-OSS-120b giving incomplete responses with gibberish \xa0\u200b ending characters

| 字段 | 值 |
| --- | --- |
| Issue | [#31495](https://github.com/vllm-project/vllm/issues/31495) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | operator;sampling |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPT-OSS-120b giving incomplete responses with gibberish \xa0\u200b ending characters

### Issue 正文摘录

### Your current environment I deployed GPT-oss-120b on 2 H200 GPUs with the following config: ```` apiVersion: apps/v1 kind: Deployment metadata: name: gpt-oss-120b-2gpu namespace: my-namespace spec: replicas: 1 selector: matchLabels: { app: gpt-oss-120b-2gpu } template: metadata: labels: { app: gpt-oss-120b-2gpu } annotations: prometheus.io/scrape: "true" prometheus.io/port: "8000" spec: nodeSelector: nvidia.com/gpu.present: "true" tolerations: - key: nvidia.com/gpu operator: Exists effect: NoSchedule containers: - name: vllm image: vllm/vllm-openai:v0.12.0 imagePullPolicy: IfNotPresent env: - name: CLUSTER_HOSTNAME value: "gptoss-120b-0" - name: VLLM_LOGGING_LEVEL value: "INFO" - name: VLLM_DEBUG_LOG_API_SERVER_RESPONSE value: "TRUE" - name: VLLM_TRACE_FUNCTION value: "0" ports: - containerPort: 8000 args: - "--host" - "0.0.0.0" - "--port" - "8000" - "--model" - "/models/gpt-oss-120b" # <- replace with the exact HF repo - "--served-model-name" - "openai/gpt-oss-120b" - "--tensor-parallel-size" - "2" # <- match GPU count per pod - "--async-scheduling" - "--max-cudagraph-capture-size" - "2048" - "--max-num-batched-tokens" - "8192" - "--stream-interval" - "1" - "--tool-call-parser...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: GPT-OSS-120b giving incomplete responses with gibberish \xa0\u200b ending characters bug;stale ### Your current environment I deployed GPT-oss-120b on 2 H200 GPUs with the following config: ```` apiVersion: apps/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ing incomplete responses with gibberish \xa0\u200b ending characters bug;stale ### Your current environment I deployed GPT-oss-120b on 2 H200 GPUs with the following config: ```` apiVersion: apps/v1 kind: Deployment met...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: n=None, regex=None, choice=None, grammar=None, json_object=None, disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, whitespace_pattern=None, structural_tag=None, _backend=None, _b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: deployed GPT-oss-120b on 2 H200 GPUs with the following config: ```` apiVersion: apps/v1 kind: Deployment metadata: name: gpt-oss-120b-2gpu namespace: my-namespace spec: replicas: 1 selector: matchLabels: { app: gpt-oss...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: PU count per pod - "--async-scheduling" - "--max-cudagraph-capture-size" - "2048" - "--max-num-batched-tokens" - "8192" - "--stream-interval" - "1" - "--tool-call-parser" - "openai"

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
