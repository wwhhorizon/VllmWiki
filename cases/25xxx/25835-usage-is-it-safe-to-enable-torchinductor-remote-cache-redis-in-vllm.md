# vllm-project/vllm#25835: [Usage]: Is it safe to enable TorchInductor remote cache (Redis) in vLLM?

| 字段 | 值 |
| --- | --- |
| Issue | [#25835](https://github.com/vllm-project/vllm/issues/25835) |
| 状态 | open |
| 标签 | usage;torch.compile;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Is it safe to enable TorchInductor remote cache (Redis) in vLLM?

### Issue 正文摘录

### Your current environment os version: Ubuntu 22.04.5 LTS (x86_64) vllm version: 0.10.2 PyTorch version: 2.8.0+cu128 gpu: NVIDIA L4 ### How would you like to use vllm We deploy vLLM on Kubernetes and are working to reduce cold-start latency. In our measurements, torch.compile’s compile time is a significant portion of startup, so we’re exploring ways to reuse TorchInductor compile artifacts via a remote cache. According to the [PyTorch docs](https://docs.pytorch.org/tutorials/recipes/torch_compile_caching_configuration_tutorial.html#torchinductor-fx-graph-remote-cache), TorchInductor supports a Redis-backed remote cache. If that’s usable in vLLM, it should be possible to enable it by setting environment variables (e.g., TORCHINDUCTOR_REDIS_HOST, etc.). What we observed - vLLM 0.9.2: during compilation vLLM uses InductorAdaptor, and remote cache appears to be forcibly disabled, so Redis is not used. [code](https://github.com/vllm-project/vllm/blob/e017120ed146cc3069d18428322d67881cb95e67/vllm/compilation/compiler_interface.py#L295-L297) - vLLM 0.10.2 + PyTorch 2.8.0: vLLM uses InductorStandaloneAdaptor. We don’t see the code path that disables remote cache, and Redis remote cache...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: t safe to enable TorchInductor remote cache (Redis) in vLLM? usage;torch.compile;stale ### Your current environment os version: Ubuntu 22.04.5 LTS (x86_64) vllm version: 0.10.2 PyTorch version: 2.8.0+cu128 gpu: NVIDIA L...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: vllm We deploy vLLM on Kubernetes and are working to reduce cold-start latency. In our measurements, torch.compile’s compile time is a significant portion of startup, so we’re exploring ways to reuse TorchInductor compi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: h docs](https://docs.pytorch.org/tutorials/recipes/torch_compile_caching_configuration_tutorial.html#torchinductor-fx-graph-remote-cache), TorchInductor supports a Redis-backed remote cache. If that’s usable in vLLM, it...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: o enable TorchInductor remote cache (Redis) in vLLM? usage;torch.compile;stale ### Your current environment os version: Ubuntu 22.04.5 LTS (x86_64) vllm version: 0.10.2 PyTorch version: 2.8.0+cu128 gpu: NVIDIA L4 ### Ho...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
