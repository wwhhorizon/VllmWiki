# vllm-project/vllm#24198: [Feature][gpt-oss]: Browser Tool Test Enhancement

| 字段 | 值 |
| --- | --- |
| Issue | [#24198](https://github.com/vllm-project/vllm/issues/24198) |
| 状态 | closed |
| 标签 | feature request;stale;gpt-oss |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][gpt-oss]: Browser Tool Test Enhancement

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Browser tool is disabled in CI now. To enable it, we need to create a dummy browser backend to interact with. https://github.com/vllm-project/vllm/blob/36c260dad604ccc845150753f2530b5b2ba9d7e6/tests/entrypoints/openai/test_response_api_with_harmony.py#L329 https://github.com/vllm-project/vllm/blob/36c260dad604ccc845150753f2530b5b2ba9d7e6/tests/entrypoints/openai/test_response_api_with_harmony.py#L283 The current browser tool is at https://github.com/vllm-project/vllm/blob/36c260dad604ccc845150753f2530b5b2ba9d7e6/vllm/entrypoints/tool.py#L47 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature][gpt-oss]: Browser Tool Test Enhancement feature request;stale;gpt-oss ### 🚀 The feature, motivation and pitch Browser tool is disabled in CI now. To enable it, we need to create a dummy browser backend to inte...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: l is disabled in CI now. To enable it, we need to create a dummy browser backend to interact with. https://github.com/vllm-project/vllm/blob/36c260dad604ccc845150753f2530b5b2ba9d7e6/tests/entrypoints/openai/test_respons...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: oss ### 🚀 The feature, motivation and pitch Browser tool is disabled in CI now. To enable it, we need to create a dummy browser backend to interact with. https://github.com/vllm-project/vllm/blob/36c260dad604ccc84515075...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature][gpt-oss]: Browser Tool Test Enhancement feature request;stale;gpt-oss ### 🚀 The feature, motivation and pitch Browser tool is disabled in CI now. To enable it, we need to create a dummy browser backend to inte...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
