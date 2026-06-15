# vllm-project/vllm#12772: [Usage]: How to get access to scheduler

| 字段 | 值 |
| --- | --- |
| Issue | [#12772](https://github.com/vllm-project/vllm/issues/12772) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to get access to scheduler

### Issue 正文摘录

### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Rocky Linux 8.6 (Green Obsidian) (x86_64) GCC version: (GCC) 8.5.0 20210514 (Red Hat 8.5.0-22) Clang version: Could not collect CMake version: version 3.26.5 Libc version: glibc-2.28 Python version: 3.12.8 | packaged by Anaconda, Inc. | (main, Dec 11 2024, 16:31:09) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.18.0-477.21.1.el8_8.x86_64-x86_64-with-glibc2.28 Is CUDA available: True ### How would you like to use vllm I'm using v1 engine in vllm v0.7.1. I would like to know whether I can get access to `vllm.v1.core.scheduler.Scheduler`. In particular, if I have a llm object from `llm = LLM(model=model_name`, can I get the scheduler from `llm ` object? It seems `scheduler` is a member of `vllm.v1.engine.core.EngineCore` and `EngineCore` is running in a background process. Thus I cannot directly access this object. I'd happy to do so and it will help me learn the source code of vllm. Looking forward to your kindly answer ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: et access to scheduler usage;stale ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Rocky Linux 8.6 (Green Obsidian) (x...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Rocky Linux 8.6 (Green Obsidian) (x86_64) GCC version: (GCC) 8.5.0 20210514 (Re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: How to get access to scheduler usage;stale ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Rocky Linux 8.6 (G...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Rocky Linux 8.6 (Green Obsidian) (x86_64) GCC version: (GCC) 8.5.0 2021051...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: eduler.Scheduler`. In particular, if I have a llm object from `llm = LLM(model=model_name`, can I get the scheduler from `llm ` object? It seems `scheduler` is a member of `vllm.v1.engine.core.EngineCore` and `EngineCor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
