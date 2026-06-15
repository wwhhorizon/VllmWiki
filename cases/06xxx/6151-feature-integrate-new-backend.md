# vllm-project/vllm#6151: [Feature]: Integrate new backend

| 字段 | 值 |
| --- | --- |
| Issue | [#6151](https://github.com/vllm-project/vllm/issues/6151) |
| 状态 | closed |
| 标签 | feature request;unstale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Integrate new backend

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, vLLM supports TPU and XPU. We would like to use vLLM on new backend. What are the community's suggestions or plans for integrating new devices? ### Alternatives There may be the following two methods: #### 1. Add new backend by modify codebase Such as XPU, Added XPUExecutor, XPUWorker, XPUModelRunner to isolate XPU backend with others. How the community reviews new backend integrations? #### 2. Provide Out-of-Tree backend registration Integrate a backend without modifying the vLLM codebase. We use PrivateUse1 to integrate new backend in PyTorch, and expected to integrate new backend in vllm in the similar way. maybe need to do: * Add privateuse1 in DeviceConfig * Provide ExecutorRegistry register CustomExecutor, and create instances of CustomWorker and CustomModelRunner in CustomExecutor. * Provide forward register in CustomOp, and dispatch_forward in forward_privateuse1 if use new backend. * Provide AttentionBackend register, and add new branch for new backend. ### Additional context _No response_

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: Integrate new backend feature request;unstale ### 🚀 The feature, motivation and pitch Currently, vLLM supports TPU and XPU. We would like to use vLLM on new backend. What are the community's suggestions or pl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: backend by modify codebase Such as XPU, Added XPUExecutor, XPUWorker, XPUModelRunner to isolate XPU backend with others. How the community reviews new backend integrations? #### 2. Provide Out-of-Tree backend registrati...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Integrate new backend feature request;unstale ### 🚀 The feature, motivation and pitch Currently, vLLM supports TPU and XPU. We would like to use vLLM on new backend. What are the community's suggestions or pl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
