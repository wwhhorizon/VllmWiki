# vllm-project/vllm#29860: [Bug]:  VLLM  没有正确处理Function Call信息

| 字段 | 值 |
| --- | --- |
| Issue | [#29860](https://github.com/vllm-project/vllm/issues/29860) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  VLLM  没有正确处理Function Call信息

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug VLLM Version ：0.11.0 Chat-Model：qwen2.5-coder-14b 我用的是Spring-AI V1.1.0 USE Frameworker Is Spring AI Version:1.1.0 Java Code: ``` OpenAiApi openAiApi = OpenAiApi.builder() .apiKey("Empty") .baseUrl("https://127.0.0.1:8000") .build(); OpenAiChatOptions options = OpenAiChatOptions.builder() .model("qwen2.5-coder-14b") .build(); OpenAiChatModel openAiChatModel= OpenAiChatModel.builder() .openAiApi(openAiApi) .defaultOptions(options) .build(); ChatClient.Builder builder = ChatClient.builder(openAiChatModel); builder.defaultTools(new DemoTools()); System.out.println(builder.build().prompt("今天天气怎么样？").call().content()); public class DemoTools { @Tool(description = "获取天气情况") public String weatherTool(@ToolParam(description = "城市名称") String city) { // 这里可以集成实际的天气查询逻辑 return city+"天气不太行"; } } ``` {"messages":[{"content":"无锡今天天气怎么样？你可以调用工具，并且以兼容Openai的方式返回给我","role":"user"}],"model":"qwen2.5-coder-14b","stream":false,"temperature":0.7,"tools":[{"type":"function","function":{"description":"文件读取","name":"readCobolContent","parameters":{"$schema":"https://json-schema.org/draft/2020-12/schema","additionalProperties":false,"type":"object","prope...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Call信息 bug ### Your current environment ### 🐛 Describe the bug VLLM Version ：0.11.0 Chat-Model：qwen2.5-coder-14b 我用的是Spring-AI V1.1.0 USE Frameworker Is Spring AI Version:1.1.0 Java Code: ``` OpenAiApi openAiApi = OpenA...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 以兼容Openai的方式返回给我","role":"user"}],"model":"qwen2.5-coder-14b","stream":false,"temperature":0.7,"tools":[{"type":"function","function":{"description":"文件读取","name":"readCobolContent","parameters":{"$schema":"https://json...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rrent environment ### 🐛 Describe the bug VLLM Version ：0.11.0 Chat-Model：qwen2.5-coder-14b 我用的是Spring-AI V1.1.0 USE Frameworker Is Spring AI Version:1.1.0 Java Code: ``` OpenAiApi openAiApi = OpenAiApi.builder() .apiKey...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 的信息 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ame":"readCobolContent","parameters":{"$schema":"https://json-schema.org/draft/2020-12/schema","additionalProperties":false,"type":"object","properties":{"path":{"type":"string","description":"文件路径"}},"required":["path"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
