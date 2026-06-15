# vllm-project/vllm#24910: [Bug]: Health endpoint not responsive while preprocessing a chat request (and other requests types too probably)

| 字段 | 值 |
| --- | --- |
| Issue | [#24910](https://github.com/vllm-project/vllm/issues/24910) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Health endpoint not responsive while preprocessing a chat request (and other requests types too probably)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Here is a software pattern problem rather than a bug per-se. I couldn't find an open issue about it. It looks like HTTP Requests handling is mono-threaded. I stumbled upon a 439KB request which takes 53 seconds to preprocess (specifically, applying a mistral chat template with `MistralTokenizer.mistral.encode_chat_completion`). Usually, the `/health` endpoint takes ~10ms max to reply so I expect most Kubernetes liveness probes will be configured with a 3x 1-10s timeout. 53 seconds of `/health` HTTP endpoint unresponsiveness is enough to have the Pod terminated under these conditions. Because preprocessing performance is not 100% under vLLM control due to 3rd party libraries, it is unclear to me what is our best option here, here are a few ideas: - make the HTTP server multithreaded: most probably very complex to implement downstream, I guess request preprocessing hasn't been coded thread-safe if there was no use for it - open a second HTTP server for health and metrics (on its own thread, provided we can easily make health/metrics code thread-safe) - work with 3rd party library providers so they improve their code performance (th...

## 现有链接修复摘要

#36451 [CORE][V1] fix: alive-but-hung EngineCore not being detected by `/health` endpoint.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: I stumbled upon a 439KB request which takes 53 seconds to preprocess (specifically, applying a mistral chat template with `MistralTokenizer.mistral.encode_chat_completion`). Usually, the `/health` endpoint takes ~10ms m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: k ? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s ~10ms max to reply so I expect most Kubernetes liveness probes will be configured with a 3x 1-10s timeout. 53 seconds of `/health` HTTP endpoint unresponsiveness is enough to have the Pod terminated under these condit...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Health endpoint not responsive while preprocessing a chat request (and other requests types too probably) bug ### Your current environment ### 🐛 Describe the bug Here is a software pattern problem rather than a b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency #36451 [CORE][V1] fix: alive-but-hung EngineCore not being detected by `/health` endpoint. Your current...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36451](https://github.com/vllm-project/vllm/pull/36451) | mentioned | 0.6 | [CORE][V1] fix: alive-but-hung EngineCore not being detected by `/health` endpoint. | → <code>/health</code> returns 503.</p> <p>Addresses #19849. Related: #24910</p> <p><strong>Config:</strong></p> <ul> <li><code>VLLM_HEALTH_CHECK_TIMEOUT</code> (default: <code>60… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
