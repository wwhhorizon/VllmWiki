# vllm-project/vllm#21768: [Bug]: vLLM v0.10.0 docker image missing flashinfer AoT compiled files

| 字段 | 值 |
| --- | --- |
| Issue | [#21768](https://github.com/vllm-project/vllm/issues/21768) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM v0.10.0 docker image missing flashinfer AoT compiled files

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It is a [known issue on flashinfer side](https://github.com/flashinfer-ai/flashinfer/issues/1256) that flashinfer AoT build script requires a GPU on the building machine. As a result, all the vLLM CI build pipelines with `flashinfer>=0.2.8` silently fails at the `python3 -m flashinfer.aot` command line, resulting an empty `flashinfer/datra/aot/` directory. (For the official vLLM image it is under `/usr/local/lib/python3.12/dist-packages/flashinfer/data/aot`) The first major release version with this regression is `vllm==0.10.0`. I don't know if this is intended, but it feels like AoT compiled flashinfer is a big performance merit of the officia docker image, so I'd wonder if we can build flashinfer separately into a wheel (just as before when we have `flashinfer_python==0.2.6.post1` pre-compiled and uploaded on vllm wheel repository) and just pip install it on vllm CI side. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked quest...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: vLLM v0.10.0 docker image missing flashinfer AoT compiled files bug;stale ### Your current environment ### 🐛 Describe the bug It is a [known issue on flashinfer side](https://github.com/flashinfer-ai/flashinfer/i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ackages/flashinfer/data/aot`) The first major release version with this regression is `vllm==0.10.0`. I don't know if this is intended, but it feels like AoT compiled flashinfer is a big performance merit of the officia...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: vLLM v0.10.0 docker image missing flashinfer AoT compiled files bug;stale ### Your current environment ### 🐛 Describe the bug It is a [known issue on flashinfer side](https://github.com/flashinfer-ai/flashinfer/i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: de. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ug]: vLLM v0.10.0 docker image missing flashinfer AoT compiled files bug;stale ### Your current environment ### 🐛 Describe the bug It is a [known issue on flashinfer side](https://github.com/flashinfer-ai/flashinfer/iss...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
