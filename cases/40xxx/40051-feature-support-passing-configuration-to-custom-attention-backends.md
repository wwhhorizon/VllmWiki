# vllm-project/vllm#40051: [Feature] Support passing configuration to custom attention backends

| 字段 | 值 |
| --- | --- |
| Issue | [#40051](https://github.com/vllm-project/vllm/issues/40051) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature] Support passing configuration to custom attention backends

### Issue 正文摘录

### Motivation We're building [glassbox](https://github.com/dmaniloff/glassbox), an observability tool that is implemented as a custom attention backend, and registered via `vllm.general_plugins` and `register_backend(AttentionBackendEnum.CUSTOM, ...)`. There's some configuration that we need to pass to the custom backend, but as far as we can tell, there's no mechanism to do so: - **Plugin side:** `vllm.general_plugins` entry points are zero-argument callables — no config, context, or kwargs are passed in when they're loaded ([source](https://github.com/vllm-project/vllm/blob/main/vllm/plugins/__init__.py)). - **Backend side:** `register_backend()` maps an enum to a class path string. The backend `Impl` class is instantiated by vLLM with a fixed constructor signature (`num_heads`, `head_size`, etc.) — no user-config parameter ([source](https://github.com/vllm-project/vllm/blob/main/vllm/v1/attention/backends/registry.py)). - **Subprocess behavior:** The plugin docs note that plugins "can be loaded multiple times in different processes" but there's no mechanism to coordinate state or configuration across those loads. At the moment, we're using class-level attributes as a workaroun...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: passing configuration to custom attention backends ### Motivation We're building [glassbox](https://github.com/dmaniloff/glassbox), an observability tool that is implemented as a custom attention backend, and registered...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature] Support passing configuration to custom attention backends ### Motivation We're building [glassbox](https://github.com/dmaniloff/glassbox), an observability tool that is implemented as a custom attention backe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: pass to the custom backend, but as far as we can tell, there's no mechanism to do so: - **Plugin side:** `vllm.general_plugins` entry points are zero-argument callables — no config, context, or kwargs are passed in when...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature] Support passing configuration to custom attention backends ### Motivation We're building [glassbox](https://github.com/dmaniloff/glassbox), an observability tool that is implemented as a custom attention backe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
