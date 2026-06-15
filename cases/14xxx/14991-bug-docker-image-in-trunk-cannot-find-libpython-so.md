# vllm-project/vllm#14991: [Bug]: Docker image in trunk cannot find libpython.so

| 字段 | 值 |
| --- | --- |
| Issue | [#14991](https://github.com/vllm-project/vllm/issues/14991) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Docker image in trunk cannot find libpython.so

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```text py-spy dump -p 30 Error: Failed to find python version from target process /vllm-workspace# ldd /opt/venv/bin/python3 linux-vdso.so.1 (0x00007fffa436e000) /opt/venv/bin/../lib/libpython3.12.so.1.0 => not found libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f551ffd1000) libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f551ffcc000) libutil.so.1 => /lib/x86_64-linux-gnu/libutil.so.1 (0x00007f551ffc7000) libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f551fee0000) librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f551fed9000) libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f551fcb0000) /lib64/ld-linux-x86-64.so.2 (0x00007f551ffe0000) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Docker image in trunk cannot find libpython.so bug ### Your current environment ### 🐛 Describe the bug ```text py-spy dump -p 30 Error: Failed to find python version from target process /vllm-workspace# ldd /opt/v
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed questions. development ci_build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support cuda;operato...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
