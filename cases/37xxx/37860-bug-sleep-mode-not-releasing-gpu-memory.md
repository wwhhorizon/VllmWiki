# vllm-project/vllm#37860: [Bug]: sleep mode not releasing GPU memory

| 字段 | 值 |
| --- | --- |
| Issue | [#37860](https://github.com/vllm-project/vllm/issues/37860) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: sleep mode not releasing GPU memory

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` (EngineCore_DP0 pid=1531) INFO 03-23 07:20:41 [block_pool.py:452] Successfully reset prefix cache (EngineCore_DP0 pid=1531) INFO 03-23 07:20:41 [cumem.py:213] CuMemAllocator: sleep freed 23.27 GiB memory in total, of which 0.00 GiB is backed up in CPU and the rest 23.27 GiB is discarded directly. (EngineCore_DP0 pid=1531) INFO 03-23 07:20:41 [gpu_worker.py:140] Sleep mode freed 24.69 GiB memory, 16.27 GiB memory is still in use. (EngineCore_DP0 pid=1531) INFO 03-23 07:20:41 [abstract.py:312] It took 0.060528 seconds to fall asleep. (APIServer pid=1331) INFO: 10.130.9.10:58068 - "POST /sleep?level=1 HTTP/1.1" 200 OK ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;hardware_porting;scheduler_memory cuda build_error env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: sleep mode not releasing GPU memory bug ### Your current environment ### 🐛 Describe the bug ``` (EngineCore_DP0 pid=1531) INFO 03-23 07:20:41 [block_pool.py:452] Successfully reset prefix cache (EngineCore_DP0 pi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ## 🐛 Describe the bug ``` (EngineCore_DP0 pid=1531) INFO 03-23 07:20:41 [block_pool.py:452] Successfully reset prefix cache (EngineCore_DP0 pid=1531) INFO 03-23 07:20:41 [cumem.py:213] CuMemAllocator: sleep freed 23.27...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ots of frequently asked questions. performance ci_build;hardware_porting;scheduler_memory cuda build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
