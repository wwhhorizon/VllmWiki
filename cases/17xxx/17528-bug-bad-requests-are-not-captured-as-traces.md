# vllm-project/vllm#17528: [Bug]: Bad requests are not captured as traces

| 字段 | 值 |
| --- | --- |
| Issue | [#17528](https://github.com/vllm-project/vllm/issues/17528) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Bad requests are not captured as traces

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I run the following: ```bash pip install \ 'opentelemetry-sdk>=1.26.0, =1.26.0, =1.26.0, =0.4.1, Optional: false OTEL_EXPORTER_OTLP_TRACES_INSECURE: true OTEL_SERVICE_NAME: vllm OTEL_EXPORTER_OTLP_ENDPOINT: http://backend.observability.svc.cluster.local:4317 OTEL_RESOURCE_ATTRIBUTES_POD_NAME: vllm-58d8d665b7-mh5v5 (v1:metadata.name) OTEL_RESOURCE_ATTRIBUTES_NODE_NAME: (v1:spec.nodeName) OTEL_PROPAGATORS: tracecontext,baggage OTEL_RESOURCE_ATTRIBUTES: k8s.container.name=vllm,k8s.deployment.name=vllm,k8s.namespace.name=llm,k8s.node.name=$(OTEL_RESOURCE_ATTRIBUTES_NODE_NAME),k8s.pod.name=$(OTEL_RESOURCE_ATTRIBUTES_POD_NAME),k8s.replicaset.name=vllm-58d8d665b7,service.instance.id=llm.$(OTEL_RESOURCE_ATTRIBUTES_POD_NAME).vllm,service.namespace=llm,service.version=2.2.0-b17 ``` Afterwards I am able to see all my requests getting captured: ![Image](https://github.com/user-attachments/assets/a691fd4b-1096-41f1-b6e4-2e70dcd802d4) But when I send a request with to much context and the api endpoint fails with `400`, its not captured. ``` ERROR 05-01 18:48:22 serving_chat.py:175] Error in preprocessing prompt inputs ERROR 05-01 18:48:22 serv...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ### 🐛 Describe the bug I run the following: ```bash pip install \ 'opentelemetry-sdk>=1.26.0, =1.26.0, =1.26.0, =0.4.1, Optional: false OTEL_EXPORTER_OTLP_TRACES_INSECURE: true OTEL_SERVICE_NAME: vllm
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: 'opentelemetry-sdk>=1.26.0, =1.26.0, =1.26.0, =0.4.1, Optional: false OTEL_EXPORTER_OTLP_TRACES_INSECURE: true OTEL_SERVICE_NAME: vllm OTEL_EXPORTER_OTLP_ENDPOINT: http://backend.observability.svc.cluster.loc
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Bad requests are not captured as traces bug;stale ### Your current environment ### 🐛 Describe the bug I run the following: ```bash pip install \ 'opentelemetry-sdk>=1.26.0, =1.26.0, =1.26.0, =0
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: vllm OTEL_EXPORTER_OTLP_ENDPOINT: http://backend.observability.svc.cluster.local:4317 OTEL_RESOURCE_ATTRIBUTES_POD_NAME: vllm-58d8d665b7-mh5v5 (v1:metadata.name) OTEL_RESOURCE_ATTRIBUTES_NODE_NAME: (v1:spec.nodeName)
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 344 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
