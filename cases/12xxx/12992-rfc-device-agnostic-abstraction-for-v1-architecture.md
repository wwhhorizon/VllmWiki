# vllm-project/vllm#12992: [RFC]: Device-agnostic Abstraction for V1 Architecture

| 字段 | 值 |
| --- | --- |
| Issue | [#12992](https://github.com/vllm-project/vllm/issues/12992) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;model_support;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;operator |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Device-agnostic Abstraction for V1 Architecture

### Issue 正文摘录

### Motivation. vLLM V1 Engine architecture (https://github.com/vllm-project/vllm/issues/8779) takes chunked-prefill and prefix-caching as first-class feature, and simplifies multi-step scheduling via async process. The effort in trying to extend device support (e.g. https://github.com/vllm-project/vllm/issues/12480) brings the challenges in reusing existing code structure. ### Purpose This RFC is intent to discuss how to extend device support for V1 architecture, **with explicit assumption that the device backend is able to support both chunked-prefill and prefix caching**. **Goal**: * Safely assume the device backend support both chunked-prefill and prefix-caching * Simplify the device-agnostic design and encourage code-reuse * GPUModelRunner class * Encourage code-reuse among devices that support openxla backend in torch.compile * Abstract out device-incompatibility code in helper function, instead of adding if-else conditions for handling device-specific optimizations (or bugs). * Keep attention backend structure similar to V0 **Non-goal**: * multi-modality with cross-attention in V1: https://github.com/vllm-project/vllm/issues/12761 * migrating hardware plugable capablity to...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: to discuss how to extend device support for V1 architecture, **with explicit assumption that the device backend is able to support both chunked-prefill and prefix caching**. **Goal**: * Safely assume the device backend...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: support for V1 architecture, **with explicit assumption that the device backend is able to support both chunked-prefill and prefix caching**. **Goal**: * Safely assume the device backend support both chunked-prefill and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [RFC]: Device-agnostic Abstraction for V1 Architecture RFC ### Motivation. vLLM V1 Engine architecture (https://github.com/vllm-project/vllm/issues/8779) takes chunked-prefill and prefix-caching as first-class feature,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tecture (https://github.com/vllm-project/vllm/issues/8779) takes chunked-prefill and prefix-caching as first-class feature, and simplifies multi-step scheduling via async process. The effort in trying to extend device s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ment. These will include `_cache_device_properties`(), `load_model()` , `profiler_run()`, `capture_model()` function. (See Appendix for details) * The `_cache_device_properties`() function is called in ModelRunnerBase.`...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
