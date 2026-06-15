# vllm-project/vllm#24199: [Feature][gpt-oss] Python Tool Test Enhancement

| 字段 | 值 |
| --- | --- |
| Issue | [#24199](https://github.com/vllm-project/vllm/issues/24199) |
| 状态 | closed |
| 标签 | feature request;gpt-oss |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][gpt-oss] Python Tool Test Enhancement

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Python tool is disabled in CI now because it needs to run in docker but we can't do it as CI is already inside a docker. https://github.com/vllm-project/vllm/blob/36c260dad604ccc845150753f2530b5b2ba9d7e6/tests/entrypoints/openai/test_response_api_with_harmony.py#L343 https://github.com/vllm-project/vllm/blob/36c260dad604ccc845150753f2530b5b2ba9d7e6/tests/entrypoints/openai/test_response_api_with_harmony.py#L282 Please also find a way to make sure the python tool is called and gives reasonable output. To enable the test, you can use uv to execute the python tool with `PYTHON_EXECUTION_BACKEND=dangerously_use_uv` (https://github.com/vllm-project/recipes/blob/46a7a1c57ec04f6118e2fdc47e78f0b858f3180e/OpenAI/GPT-OSS.md?plain=1#L154C323-L154C365) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: -oss ### 🚀 The feature, motivation and pitch Python tool is disabled in CI now because it needs to run in docker but we can't do it as CI is already inside a docker. https://github.com/vllm-project/vllm/blob/36c260dad60...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e test, you can use uv to execute the python tool with `PYTHON_EXECUTION_BACKEND=dangerously_use_uv` (https://github.com/vllm-project/recipes/blob/46a7a1c57ec04f6118e2fdc47e78f0b858f3180e/OpenAI/GPT-OSS.md?plain=1#L154C...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature][gpt-oss] Python Tool Test Enhancement feature request;gpt-oss ### 🚀 The feature, motivation and pitch Python tool is disabled in CI now because it needs to run in docker but we can't do it as CI is already ins...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature][gpt-oss] Python Tool Test Enhancement feature request;gpt-oss ### 🚀 The feature, motivation and pitch Python tool is disabled in CI now because it needs to run in docker but we can't do it as CI is already ins...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
