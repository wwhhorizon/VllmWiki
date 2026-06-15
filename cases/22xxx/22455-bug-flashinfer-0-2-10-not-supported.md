# vllm-project/vllm#22455: [Bug]: Flashinfer 0.2.10 not supported

| 字段 | 值 |
| --- | --- |
| Issue | [#22455](https://github.com/vllm-project/vllm/issues/22455) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Flashinfer 0.2.10 not supported

### Issue 正文摘录

### Your current environment uv init vllminfer uv pip install vllm source .venv/bin/activate git clone https://github.com/flashinfer-ai/flashinfer.git --recursive cd flashinfer export TORCH_CUDA_ARCH_LIST="7.5 8.0 8.9 9.0a 10.0a" python -m flashinfer.aot # Produces AOT kernels in aot-ops/ python -m pip install --no-build-isolation --verbose . ### 🐛 Describe the bug I compiled Flashinfer 0.2.10 AOT mode in my environment. this was reported. I guess the version check thought 0.2.10 = 0.2.3 required. Falling back to default sampling implementation. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: not supported bug ### Your current environment uv init vllminfer uv pip install vllm source .venv/bin/activate git clone https://github.com/flashinfer-ai/flashinfer.git --recursive cd flashinfer export TORCH_CUDA_ARCH_L...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .com/flashinfer-ai/flashinfer.git --recursive cd flashinfer export TORCH_CUDA_ARCH_LIST="7.5 8.0 8.9 9.0a 10.0a" python -m flashinfer.aot # Produces AOT kernels in aot-ops/ python -m pip install --no-build-isolation --v...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: Flashinfer 0.2.10 not supported bug ### Your current environment uv init vllminfer uv pip install vllm source .venv/bin/activate git clone https://github.com/flashinfer-ai/flashinfer.git --recursive cd flashinfer...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
