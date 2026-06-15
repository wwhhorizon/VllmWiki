# vllm-project/vllm#14947: [Bug]: macOS launch fails with `--tensor-parallel-size 2`

| 字段 | 值 |
| --- | --- |
| Issue | [#14947](https://github.com/vllm-project/vllm/issues/14947) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: macOS launch fails with `--tensor-parallel-size 2`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There are actually two errors here. When you try it for the first time, you will get an `AssertionError`. This is because under macOS, the size of shm allocation is related to the page size and cannot be completely equal to the buffer size. Ref: [Python doc](https://docs.python.org/3.13/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory) After solving the first problem, the second problem will arise: the worker process will be blocked by the macOS security policy: ``` ------------------------------------- Translated Report (Full Report Below) ------------------------------------- Process: Python [60747] Path: /Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python Identifier: com.apple.python3 Version: 3.9.6 (3.9.6) Build Info: python3-141000000000000~2624 Code Type: ARM-64 (Native) Parent Process: python [60648] Responsible: pycharm [38310] User ID: 501 Date/Time: 2025-03-17 17:49:59.4696 +0800 OS Version: macOS 15.3.1 (24D70) Report Version: 12 Anonymous UUID: 38F79004-CE3C-C2A6-5357-18A1C7925C39 Sleep/Wake UUID: 9...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ations/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python Identifier: com.apple.python3 Version: 3.9.6 (3.9.6) Build Info: python3-141000000000000~2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: cally isn’t run on macOS, it’s still useful for developing and debugging small features. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: his is because under macOS, the size of shm allocation is related to the page size and cannot be completely equal to the buffer size. Ref: [Python doc](https://docs.python.org/3.13/library/multiprocessing.shared_memory....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: System Integrity Protection: enabled Crashed Thread: 0 Dispatch queue: com.apple.main-thread Exception Type: EXC_GUARD (SIGKILL) Exception Codes: GUARD_TYPE_MACH_PORT Exception Codes: 0x0000000000000000, 0x0000000000000...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: seconds System Integrity Protection: enabled Crashed Thread: 0 Dispatch queue: com.apple.main-thread Exception Type: EXC_GUARD (SIGKILL) Exception Codes: GUARD_TYPE_MACH_PORT Exception Codes: 0x0000000000000000, 0x00000...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
