# vllm-project/vllm#914: CUDA Graph support

| 字段 | 值 |
| --- | --- |
| Issue | [#914](https://github.com/vllm-project/vllm/issues/914) |
| 状态 | closed |
| 标签 | performance;feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> CUDA Graph support

### Issue 正文摘录

Hi vLLM genius @WoosukKwon @zhuohan123 After reading the [Speed, Python: Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning](https://blog.fireworks.ai/speed-python-pick-two-how-cuda-graphs-enable-fast-python-code-for-deep-learning-353bf6241248) and the [llama-cuda-graph-example](https://github.com/fw-ai/llama-cuda-graph-example) by [Fireworks.ai](https://www.fireworks.ai/)'s @jamesr66a > CUDA graphs address all sources of CPU overhead highlighted above: user-written logic, PyTorch dispatcher logic, memory allocation overhead, and GPU driver/kernel overhead. > Thus, incremental generation can be limited by the CPU speed and thus is a good candidate for CUDA graphs. > While both the regular attention mechanism and the [PagedAttention](https://vllm.ai/) scheme undergo shape changes over iterations, the latter provides a unique advantage when integrating with CUDA graphs. And with this [benchmark](https://github.com/fw-ai/llama-cuda-graph-example/commit/d8003f59af8893837ec9834c705cfd0035d3ad37#diff-4ead05c4053ddcb00e0038dcf342af9021f87146b8a29f67248719bc3c8d1566) > We find that without CUDA graphs, LLaMA-7B inference executes at 30 tokens/sec, but with CUDA graphs ena...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: CUDA Graph support performance;feature request Hi vLLM genius @WoosukKwon @zhuohan123 After reading the [Speed, Python: Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning](https://blog.fireworks.ai/spe
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: CUDA Graph support performance;feature request Hi vLLM genius @WoosukKwon @zhuohan123 After reading the [Speed, Python: Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning](https://blog.fireworks.ai/spee...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: l sources of CPU overhead highlighted above: user-written logic, PyTorch dispatcher logic, memory allocation overhead, and GPU driver/kernel overhead. > Thus, incremental generation can be limited by the CPU speed and t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tention_kv_cache;frontend_api;scheduler_memory attention;cuda;kernel env_dependency;shape Hi vLLM genius @WoosukKwon @zhuohan123
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: -graphs-enable-fast-python-code-for-deep-learning-353bf6241248) and the [llama-cuda-graph-example](https://github.com/fw-ai/llama-cuda-graph-example) by [Fireworks.ai](https://www.fireworks.ai/)'s @jamesr66a > CUDA grap...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
