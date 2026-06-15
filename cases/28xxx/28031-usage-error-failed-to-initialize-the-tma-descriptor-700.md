# vllm-project/vllm#28031: [Usage]: Error: Failed to initialize the TMA descriptor 700

| 字段 | 值 |
| --- | --- |
| Issue | [#28031](https://github.com/vllm-project/vllm/issues/28031) |
| 状态 | open |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Usage]: Error: Failed to initialize the TMA descriptor 700

### Issue 正文摘录

### Your current environment vllm0.11.0 to train Qwen3-vl-8B The following error message appears intermittently during training. ``` [36m(WorkerDict pid=82555)[0m TMA Desc Addr: 0x7f4e2736b080 [36m(WorkerDict pid=82555)[0m format 9 [36m(WorkerDict pid=82555)[0m dim 4 [36m(WorkerDict pid=82555)[0m gmem_address 0xa9bdcd0000 [36m(WorkerDict pid=82555)[0m globalDim (128,415,2,1,1) [36m(WorkerDict pid=82555)[0m globalStrides (2,2048,1024,0,0) [36m(WorkerDict pid=82555)[0m boxDim (64,128,1,1,1) [36m(WorkerDict pid=82555)[0m elementStrides (1,1,1,1,1) [36m(WorkerDict pid=82555)[0m interleave 0 [36m(WorkerDict pid=82555)[0m swizzle 3 [36m(WorkerDict pid=82555)[0m l2Promotion 2 [36m(WorkerDict pid=82555)[0m oobFill 0 [36m(WorkerDict pid=82555)[0m Error: Failed to initialize the TMA descriptor 700 [36m(WorkerDict pid=82555)[0m TMA Desc Addr: 0x7f4e2736b080 [36m(WorkerDict pid=82555)[0m format 9 [36m(WorkerDict pid=82555)[0m dim 4 [36m(WorkerDict pid=82555)[0m gmem_address 0xa46a000000 [36m(WorkerDict pid=82555)[0m globalDim (128,16,2,61647,1) [36m(WorkerDict pid=82555)[0m globalStrides (2,512,256,8192,0) [36m(WorkerDict pid=82555)[0m boxDim (64,128,1,1...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: led to initialize the TMA descriptor 700 [36m(WorkerDict pid=82555)[0m CUDA error (/workspace/.deps/vllm-flash-attn-src/hopper/flash_fwd_launch_template.h:191): an illegal memory access was encountered [36m(WorkerDic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: descriptor 700 usage ### Your current environment vllm0.11.0 to train Qwen3-vl-8B The following error message appears intermittently during training. ``` [36m(WorkerDict pid=82555)[0m TMA Desc Addr: 0x7f4e2736b080 [36...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _porting;model_support;scheduler_memory cuda env_dependency;shape #4 Use FlashAttention for `multi_query_kv_attention` Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [0m globalDim (128,415,2,1,1) [36m(WorkerDict pid=82555)[0m globalStrides (2,2048,1024,0,0) [36m(WorkerDict pid=82555)[0m boxDim (64,128,1,1,1) [36m(WorkerDict pid=82555)[0m elementStrides (1,1,1,1,1) [36m(Worker...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | eated 210x across cluster][0m [36m(workerdict pid=134580)[0m frame #4: c10d::tcpstore::check(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
