# vllm-project/vllm#8821: [issue tracker] make vllm compatible with dynamo

| 字段 | 值 |
| --- | --- |
| Issue | [#8821](https://github.com/vllm-project/vllm/issues/8821) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | shape_align |
| Operator 关键词 | cuda |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [issue tracker] make vllm compatible with dynamo

### Issue 正文摘录

### Anything you want to discuss about vllm. The first step to enable `torch.compile`, is to use dynamo to capture the graph. while dynamo can handle many python features, every time there is a python side change, dynamo will try to re-compile the code. for example: ```python # test.py import torch @torch.compile def f(x, i): return (x + i) * i x = torch.randn(5, 5).cuda() f(x, 1) f(x, 2) f(x, 3) ``` running the code with `TORCH_LOGS=recompiles_verbose python test.py` , we can get: ```text V0925 13:16:45.714159 140477991954240 torch/_dynamo/guards.py:2609] [0/1] [__recompiles_verbose] Recompiling function f in /data/youkaichao/vllm/testb.py:3 V0925 13:16:45.714159 140477991954240 torch/_dynamo/guards.py:2609] [0/1] [__recompiles_verbose] triggered by the following guard failure(s): V0925 13:16:45.714159 140477991954240 torch/_dynamo/guards.py:2609] [0/1] [__recompiles_verbose] guard 0 failures: V0925 13:16:45.714159 140477991954240 torch/_dynamo/guards.py:2609] [0/1] [__recompiles_verbose] - L['i'] == 1 V0925 13:16:45.882663 140477991954240 torch/_dynamo/guards.py:2609] [0/2] [__recompiles_verbose] Recompiling function f in /data/youkaichao/vllm/testb.py:3 V0925 13:16:45.882663 14...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: nything you want to discuss about vllm. The first step to enable `torch.compile`, is to use dynamo to capture the graph. while dynamo can handle many python features, every time there is a python side change, dynamo wil...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: to a tensor, so that pytorch will re-use the graph as long as the tensor metadata (device, shape, dtype, etc) matches, the graph can be re-used: ```python # test.py import torch @torch.compile def f(x, i): i = i.cuda()...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: torch.compile def f(x, i): return (x + i) * i x = torch.randn(5, 5).cuda() f(x, 1) f(x, 2) f(x, 3) ``` running the code with `TORCH_LOGS=recompiles_verbose python test.py` , we can get: ```text V0925 13:16:45.714159 140...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: l use cases, and future run will not trigger compilation. (if a new user request triggers compilation, the TTFT will be several seconds because of compilation). our first goal, is to remove unnecessary Python side chang...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ards.py:2609] [0/7] [__recompiles_verbose] - tensor 'L['input_ids']' dispatch key set mismatch. expected DispatchKeySet(CUDA, BackendSelect), actual DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView) [rank0]:V0925 13:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
