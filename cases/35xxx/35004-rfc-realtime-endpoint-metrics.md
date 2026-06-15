# vllm-project/vllm#35004: [RFC]: Realtime Endpoint Metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#35004](https://github.com/vllm-project/vllm/issues/35004) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Realtime Endpoint Metrics

### Issue 正文摘录

### Motivation. With the recent pre-release of v0.16.0, vLLM now exposes a /v1/realtime endpoint that allows clients to progressively submit prompts without having to make separate HTTP requests to the /chatcompletions endpoint. This endpoint requires clients to establish a websocket connection to vLLM to stream the prompts over. The /chatcompletions HTTP endpoint currently benefits out-of-the-box metrics provided by the prometheus client that part of the stack relies on. No such metrics are currently surfaced for /v1/realtime and this means that anyone wishing to use it is essentially operating “in the dark”. ### Proposed Change. #### Proposed metrics With this in mind, I'm proposing only the basic following metrics for starters: | Metric | Type | Labels | Description | |---|---|---|---| | vllm:realtime_active_sessions | Gauge | - | Current open WebSocket connections | | vllm:realtime_sessions_total | Counter | - | Cumulative WebSocket connections | | vllm:realtime_session_duration_seconds | Histogram | - | Connection duration (buckets: 0.5s to 30 min) | My reasoning for these specific metrics is that they answer basic questions regarding the endpoint itself for anyone looking to...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nts to progressively submit prompts without having to make separate HTTP requests to the /chatcompletions endpoint. This endpoint requires clients to establish a websocket connection to vLLM to stream the prompts over....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ection duration (buckets: 0.5s to 30 min) | My reasoning for these specific metrics is that they answer basic questions regarding the endpoint itself for anyone looking to expose it in production: - How many sessions am...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ics ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: the first model!) @joshuadeng @DarkLight1337 @NickLucche And anyone else that is interested in this. ### Any Other Things. Draft PR for visibility: https://github.com/vllm-project/vllm/compare/main...pougetat:vllm:users...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: on production level usability here since you folks contributed the first model!) @joshuadeng @DarkLight1337 @NickLucche And anyone else that is interested in this. ### Any Other Things. Draft PR for visibility: https://...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
