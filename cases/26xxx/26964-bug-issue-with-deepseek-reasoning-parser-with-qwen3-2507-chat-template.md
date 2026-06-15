# vllm-project/vllm#26964: [Bug]: Issue with Deepseek Reasoning parser with Qwen3 2507 chat templates

| 字段 | 值 |
| --- | --- |
| Issue | [#26964](https://github.com/vllm-project/vllm/issues/26964) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Issue with Deepseek Reasoning parser with Qwen3 2507 chat templates

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm running vLLM as a docker container on an Unraid server. It is a backend to Open WebUI chat interface. The issue I see is that the reasoning block for Open WebUI is closing too early. According to this discussion on the Open WebUI git, I think it is because of the deepseek parser used as recommended by the model card. See this link: https://github.com/open-webui/open-webui/pull/16687 Here is an example of the issue that I face: I think this is the place to raise this issue. Thanks so much! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ur current environment ### 🐛 Describe the bug I'm running vLLM as a docker container on an Unraid server. It is a backend to Open WebUI chat interface. The issue I see is that the reasoning block for Open WebUI is closi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Issue with Deepseek Reasoning parser with Qwen3 2507 chat templates bug;stale ### Your current environment ### 🐛 Describe the bug I'm running vLLM as a docker container on an Unraid server. It is a backend to Ope...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: bug I'm running vLLM as a docker container on an Unraid server. It is a backend to Open WebUI chat interface. The issue I see is that the reasoning block for Open WebUI is closing too early. According to this discussion...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ch! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: kend to Open WebUI chat interface. The issue I see is that the reasoning block for Open WebUI is closing too early. According to this discussion on the Open WebUI git, I think it is because of the deepseek parser used a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
