# vllm-project/vllm#27304: [Feature]: Allow custom stat_loggers in V1 engine initialization

| 字段 | 值 |
| --- | --- |
| Issue | [#27304](https://github.com/vllm-project/vllm/issues/27304) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow custom stat_loggers in V1 engine initialization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Contribution PR: https://github.com/vllm-project/vllm/pull/27302 Our metrics tests rely on passing custom `stat_loggers` to `engine.add_logger` in V0. After moving to V1, we pass it to `build_async_engine_client`->`build_async_engine_client_from_engine_args`->`AsyncLLM.from_vllm_config` now. In the example below, "build_async_engine_client_from_engine_args" calls AsyncLLM.from_vllm_config but did not pass "stat_loggers" parameter. ```python # vllm/entrypoints/openai/api_server.pyclass @asynccontextmanager async def build_async_engine_client( args: Namespace, *, usage_context: UsageContext = UsageContext.OPENAI_API_SERVER, disable_frontend_multiprocessing: Optional[bool] = None, client_config: Optional[dict[str, Any]] = None, ) -> AsyncIterator[EngineClient]: ... async with build_async_engine_client_from_engine_args( engine_args, usage_context=usage_context, disable_frontend_multiprocessing=disable_frontend_multiprocessing, client_config=client_config, ) as engine: yield engine @asynccontextmanager async def build_async_engine_client_from_engine_args( engine_args: AsyncEngineArgs, *, usage_context: UsageContext = UsageContext.OPENAI_API_SERVE...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: oggers` to `engine.add_logger` in V0. After moving to V1, we pass it to `build_async_engine_client`->`build_async_engine_client_from_engine_args`->`AsyncLLM.from_vllm_config` now. In the example below, "build_async_engi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Allow custom stat_loggers in V1 engine initialization feature request;stale ### 🚀 The feature, motivation and pitch Contribution PR: https://github.com/vllm-project/vllm/pull/27302 Our metrics tests rely on p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ontext.OPENAI_API_SERVER, disable_frontend_multiprocessing: bool = False, client_config: Optional[dict[str, Any]] = None, ) -> AsyncIterator[EngineClient]: ... try: async_llm = AsyncLLM.from_vllm_config( vllm_config=vll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ient`->`build_async_engine_client_from_engine_args`->`AsyncLLM.from_vllm_config` now. In the example below, "build_async_engine_client_from_engine_args" calls AsyncLLM.from_vllm_config but did not pass "stat_loggers" pa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
