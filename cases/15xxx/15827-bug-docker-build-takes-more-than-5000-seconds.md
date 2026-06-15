# vllm-project/vllm#15827: [Bug]: Docker build takes more than 5000 seconds

| 字段 | 值 |
| --- | --- |
| Issue | [#15827](https://github.com/vllm-project/vllm/issues/15827) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Docker build takes more than 5000 seconds

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried to build my own image following the steps from https://docs.vllm.ai/en/latest/deployment/docker.html#use-the-custom-built-vllm-docker-image However, at this step, the build takes over 5000 seconds (and counting) ``` ENV CCACHE_DIR=/root/.cache/ccache RUN --mount=type=cache,target=/root/.cache/ccache \ --mount=type=cache,target=/root/.cache/uv \ --mount=type=bind,source=.git,target=.git \ if [ "$USE_SCCACHE" != "1" ]; then \ # Clean any existing CMake artifacts rm -rf .deps && \ mkdir -p .deps && \ python3 setup.py bdist_wheel --dist-dir=dist --py-limited-api=cp38; \ fi ``` Not sure what is wrong. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Docker build takes more than 5000 seconds bug;stale ### Your current environment ### 🐛 Describe the bug I tried to build my own image following the steps from https://docs.vllm.ai/en/latest/deployment/docker.html...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Docker build takes more than 5000 seconds bug;stale ### Your current environment ### 🐛 Describe the bug I tried to build my own image following the steps from https://docs.vllm.ai/en/latest/deployment/docker.html...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: to build my own image following the steps from https://docs.vllm.ai/en/latest/deployment/docker.html#use-the-custom-built-vllm-docker-image However, at this step, the build takes over 5000 seconds (and counting) ``` ENV...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
