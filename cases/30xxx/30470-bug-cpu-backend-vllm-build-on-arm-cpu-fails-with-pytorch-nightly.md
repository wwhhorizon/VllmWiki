# vllm-project/vllm#30470: [Bug] [CPU Backend]: vLLM build on Arm CPU fails with pytorch nightly

| 字段 | 值 |
| --- | --- |
| Issue | [#30470](https://github.com/vllm-project/vllm/issues/30470) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] [CPU Backend]: vLLM build on Arm CPU fails with pytorch nightly

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried to build vLLM with PyTorch nightly - version: `2.10.0.dev20251210+cpu` on Arm CPU. I got this error: ``` CMake Error at cmake/cpu_extension.cmake:225 (find_library): Could not find OPEN_MP using the following names: gomp Call Stack (most recent call first): CMakeLists.txt:111 (include) ``` It's caused by a recent change in PyTorch where they stopped shipping versioned/hash-suffixed libgomp (e.g. `libgomp-1dd373e6.so.1.0.0`) and now just ship `libgomp.so.1`. They also now ship it under `torch/libs` instead of `torch.libs` Our [cmake util func ](https://github.com/vllm-project/vllm/blob/main/cmake/utils.cmake#L148) which searches for PyTorch's libgomp needs to be updated to support these patterns: - `./lib/python3.10/site-packages/torch.libs/libgomp-a49a47f9.so.1.0.0` - the case with PyTorch 2.9 - `./lib/python3.10/site-packages/torch/lib/libgomp.so.1` - the case with PyTorch nightly (`2.10.0.dev20251210+cpu`) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug] [CPU Backend]: vLLM build on Arm CPU fails with pytorch nightly bug;cpu ### Your current environment ### 🐛 Describe the bug I tried to build vLLM with PyTorch nightly - version: `2.10.0.dev20251210+cpu` on Arm CPU...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lude) ``` It's caused by a recent change in PyTorch where they stopped shipping versioned/hash-suffixed libgomp (e.g. `libgomp-1dd373e6.so.1.0.0`) and now just ship `libgomp.so.1`. They also now ship it under `torch/lib...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug] [CPU Backend]: vLLM build on Arm CPU fails with pytorch nightly bug;cpu ### Your current environment ### 🐛 Describe the bug I tried to build vLLM with PyTorch nightly - version: `2.10.0.dev20251210+cpu` on Arm CPU...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
