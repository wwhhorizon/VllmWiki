# vllm-project/vllm#17348: [Bug]:  h unknown: block: [487,0,0], thread: [31,0,0] Assertion `index out of bounds: 0 <= tl.broadcast_to(tmp34, [XBLOCK]) < 131072` failed.

| 字段 | 值 |
| --- | --- |
| Issue | [#17348](https://github.com/vllm-project/vllm/issues/17348) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  h unknown: block: [487,0,0], thread: [31,0,0] Assertion `index out of bounds: 0 <= tl.broadcast_to(tmp34, [XBLOCK]) < 131072` failed.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I run in termine and when model start the error occurs (VllmWorker rank=3 pid=24287) INFO 04-29 11:48:08 [backends.py:430] Dynamo bytecode transform time: 14.77 s (VllmWorker rank=1 pid=24285) INFO 04-29 11:48:11 [backends.py:136] Cache the graph of shape None for later use (VllmWorker rank=0 pid=24284) INFO 04-29 11:48:11 [backends.py:136] Cache the graph of shape None for later use (VllmWorker rank=5 pid=24289) INFO 04-29 11:48:11 [backends.py:136] Cache the graph of shape None for later use (VllmWorker rank=2 pid=24286) INFO 04-29 11:48:12 [backends.py:136] Cache the graph of shape None for later use (VllmWorker rank=4 pid=24288) INFO 04-29 11:48:12 [backends.py:136] Cache the graph of shape None for later use (VllmWorker rank=7 pid=24291) INFO 04-29 11:48:12 [backends.py:136] Cache the graph of shape None for later use (VllmWorker rank=6 pid=24290) INFO 04-29 11:48:12 [backends.py:136] Cache the graph of shape None for later use (VllmWorker rank=3 pid=24287) INFO 04-29 11:48:12 [backends.py:136] Cache the graph of shape None for later use (VllmWorker rank=1 pid=24285) INFO 04-29 11:49:01 [backends.py:148] Compiling a graph fo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ounds: 0 <= tl.broadcast_to(tmp34, [XBLOCK]) < 131072` failed. bug;torch.compile ### Your current environment ### 🐛 Describe the bug I run in termine and when model start the error occurs (VllmWorker rank=3 pid=24287) I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Rank 0 Group 0 Pid 20836 on 6000gpu device 0 [0000:4f:00] NVIDIA RTX A6000 # Rank 1 Group 0 Pid 20836 on 6000gpu device 1 [0000:52:00] NVIDIA RTX A6000 # Rank 2 Group 0 Pid 20836 on 6000gpu device 2 [0000:56:00] NVIDIA...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: art the error occurs (VllmWorker rank=3 pid=24287) INFO 04-29 11:48:08 [backends.py:430] Dynamo bytecode transform time: 14.77 s (VllmWorker rank=1 pid=24285) INFO 04-29 11:48:11 [backends.py:136] Cache the graph of sha...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: h unknown: block: [487,0,0], thread: [31,0,0] Assertion `index out of bounds: 0 <= tl.broadcast_to(tmp34, [XBLOCK]) < 131072` failed. bug;torch.compile ### Your current environment ### 🐛 Describe the bug I run in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: urrent environment ### 🐛 Describe the bug I run in termine and when model start the error occurs (VllmWorker rank=3 pid=24287) INFO 04-29 11:48:08 [backends.py:430] Dynamo bytecode transform time: 14.77 s (VllmWorker ra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
