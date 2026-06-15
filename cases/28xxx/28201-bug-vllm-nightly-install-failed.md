# vllm-project/vllm#28201: [Bug]: vllm nightly install failed

| 字段 | 值 |
| --- | --- |
| Issue | [#28201](https://github.com/vllm-project/vllm/issues/28201) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm nightly install failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Fail to install vllm nightly ```shell uv pip install 'triton-kernels @ git+https://github.com/triton-lang/triton.git@v3.5.0#subdirectory=python/triton_kernels' vllm --extra-index-url https://wheels.vllm.ai/nightly --prerelease=allow ``` failed with output below: ``` × No solution found when resolving dependencies: ╰─▶ Because there is no version of xformers{platform_machine == 'x86_64' and sys_platform == 'linux'}==0.0.33+5d4b92a5.d20251029 and vllm==0.11.1rc6.dev158+gc3ee80a01.cu129 depends on xformers{platform_machine == 'x86_64' and sys_platform == 'linux'}==0.0.33+5d4b92a5.d20251029, we can conclude that vllm==0.11.1rc6.dev158+gc3ee80a01.cu129 cannot be used. And because only vllm==0.11.1rc6.dev158+gc3ee80a01.cu129 is available and you require vllm, we can conclude that your requirements are unsatisfiable. hint: `vllm` was found on https://wheels.vllm.ai/nightly, but not at the requested version (all of: vllm 0.11.1rc6.dev158+gc3ee80a01.cu129 ). A compatible version may be available on a subsequent index (e.g., https://pypi.org/simple). By default, uv will only consider versions that are published on the first index that cont...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: vllm nightly install failed bug ### Your current environment ### 🐛 Describe the bug Fail to install vllm nightly ```shell uv pip install 'triton-kernels @ git+https://github.com/triton-lang/triton.git@v3.5.0#subd...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: escribe the bug Fail to install vllm nightly ```shell uv pip install 'triton-kernels @ git+https://github.com/triton-lang/triton.git@v3.5.0#subdirectory=python/triton_kernels' vllm --extra-index-url https://wheels.vllm....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: hint: `vllm` was found on https://wheels.vllm.ai/nightly, but not at the requested version (all of: vllm 0.11.1rc6.dev158+gc3ee80a01.cu129 ). A compatible version may be available on a subsequent index (e.g., https://py...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
