# vllm-project/vllm#18743: [Bug]: Dockerfile.cpu missing libtbb-dev

| 字段 | 值 |
| --- | --- |
| Issue | [#18743](https://github.com/vllm-project/vllm/issues/18743) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Dockerfile.cpu missing libtbb-dev

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I build the image using `docker/Dockerfile.cpu` and run it, I get the following message: `[FATAL UMF] utils_open_library: dlopen(libtbbmalloc.so.2) failed with error: libtbbmalloc.so.2: cannot open shared object file: No such file or directory` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Dockerfile.cpu missing libtbb-dev bug ### Your current environment ### 🐛 Describe the bug When I build the image using `docker/Dockerfile.cpu` and run it, I get the following message: `[FATAL UMF] utils_open_libr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ry` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
