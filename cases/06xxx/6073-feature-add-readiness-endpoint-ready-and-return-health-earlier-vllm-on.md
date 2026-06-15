# vllm-project/vllm#6073: [Feature]: Add readiness endpoint /ready and return /health earlier (vLLM on Kubernetes)

| 字段 | 值 |
| --- | --- |
| Issue | [#6073](https://github.com/vllm-project/vllm/issues/6073) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Add readiness endpoint /ready and return /health earlier (vLLM on Kubernetes)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am running vLLM instances on Kubernetes, as likely are others. Currently there only is the `/health` endpoint https://github.com/vllm-project/vllm/blob/15aba081f33e6d048422df6dcdb94301d08d13e6/vllm/entrypoints/openai/api_server.py#L88 When defining health checks for workload on Kubernetes there are Liveness and Readiness probes (https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes). While the liveness check determines if a process is still alive (extending on taking only the sheer existence of a process as health indication), the readiness check is used to determine if a pod is ready to receive requests. The first issue with the health endpoint in the case of vLLM is that it only becomes available and returns HTTP 200 after the API server is started up. If you look at the example in the additional section, this is ~16 seconds after the vLLM was spawned, even without a model download and with a relatively small model only using one small GPU. A liveness check is hard to configure properly with an unknown time it takes for a service to start providing the corresponding endpoint. If the timeouts...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: here are Liveness and Readiness probes (https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes). While the liveness check determines if a process is still alive (extending o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: endpoint /ready and return /health earlier (vLLM on Kubernetes) feature request ### 🚀 The feature, motivation and pitch I am running vLLM instances on Kubernetes, as likely are others. Currently there only is the `/heal...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: onal context ``` INFO 07-02 15:27:33 api_server.py:177] vLLM API server version 0.5.0.post1
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: INFO 07-02 15:27:34 config.py:1197] Casting torch.float32 to torch.float16.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: he vLLM was spawned, even without a model download and with a relatively small model only using one small GPU. A liveness check is hard to configure properly with an unknown time it takes for a service to start providin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
