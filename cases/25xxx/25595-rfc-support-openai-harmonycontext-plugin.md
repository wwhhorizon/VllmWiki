# vllm-project/vllm#25595: [RFC]: Support openai HarmonyContext plugin

| 字段 | 值 |
| --- | --- |
| Issue | [#25595](https://github.com/vllm-project/vllm/issues/25595) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support openai HarmonyContext plugin

### Issue 正文摘录

### Motivation. In some gpt-oss use cases, especially internal scenarios, we need to customize the HarmonyContext class. However, the current implementation does not allow this in OSS. I believe other users may also want similar flexibility to define their own class methods. This PR introduces custom plugin registration for HarmonyContext, making it more extensible by allowing users to register and load their own implementations. Example: from vllm.entrypoints.harmony_utils import register_context_loader @register_context_loader("HarmonyContextFB") class HarmonyContextFB(HarmonyContext): def __init__(self, *args, **kwargs): super().__init__(*args, **kwargs) async def call_tool(self) -> list[Message]: pass async def call_search_tool( self, tool_session: Union["ClientSession", Tool], last_msg: Message ) -> list[Message] pass async def call_python_tool( self, tool_session: Union["ClientSession", Tool], last_msg: Message ) -> list[Message]: pass async def call_container_tool( self, tool_session: Union["ClientSession", Tool], last_msg: Message ) -> list[Message]: pass ### Proposed Change. https://github.com/vllm-project/vllm/pull/25594 ### Feedback Period. _No response_ ### CC List. @y...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Context plugin RFC;stale ### Motivation. In some gpt-oss use cases, especially internal scenarios, we need to customize the HarmonyContext class. However, the current implementation does not allow this in OSS. I believe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: def call_tool(self) -> list[Message]: pass async def call_search_tool( self, tool_session: Union["ClientSession", Tool], last_msg: Message ) -> list[Message] pass async def call_python_tool( self, tool_session: Union["C...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Support openai HarmonyContext plugin RFC;stale ### Motivation. In some gpt-oss use cases, especially internal scenarios, we need to customize the HarmonyContext class. However, the current implementation does not allow...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: Support openai HarmonyContext plugin RFC;stale ### Motivation. In some gpt-oss use cases, especially internal scenarios, we need to customize the HarmonyContext class. However, the current implementation does not...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
