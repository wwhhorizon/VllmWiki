# vllm-project/vllm#9369: [Bug]: cannot run model when TP>1 (already run debug file)

| 字段 | 值 |
| --- | --- |
| Issue | [#9369](https://github.com/vllm-project/vllm/issues/9369) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;operator |
| 症状 | crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: cannot run model when TP>1 (already run debug file)

### Issue 正文摘录

### Your current environment ### Model Input Dumps model = LLM("DeepSeek-Coder-V2-Lite-Base-Autofp8", trust_remote_code=True, max_model_len=4096, tensor_parallel_size=4) ### 🐛 Describe the bug $NCCL_DEBUG=TRACE torchrun --nproc-per-node=4 vLLM_debug.py kmaker-54-033138205093:44710:44710 [0] NCCL INFO Bootstrap : Using eth0:33.138.205.93 kmaker-54-033138205093:44710:44710 [0] NCCL INFO NET/Plugin : dlerror=libnccl-net.so: cannot open shared object file: No such file or directory No plugin found (libnccl-net.so), using internal implementation kmaker-54-033138205093:44710:44710 [0] NCCL INFO cudaDriverVersion 12010 kmaker-54-033138205093:44710:44710 [0] misc/cudawrap.cc:36 NCCL WARN Cuda failure 3 'initialization error' NCCL version 2.20.5+cuda12.4 kmaker-54-033138205093:44713:44713 [3] NCCL INFO cudaDriverVersion 12010 kmaker-54-033138205093:44711:44711 [1] NCCL INFO cudaDriverVersion 12010 kmaker-54-033138205093:44712:44712 [2] NCCL INFO cudaDriverVersion 12010 kmaker-54-033138205093:44713:44713 [3] misc/cudawrap.cc:36 NCCL WARN Cuda failure 3 'initialization error' kmaker-54-033138205093:44711:44711 [1] misc/cudawrap.cc:36 NCCL WARN Cuda failure 3 'initialization error' kmaker-54-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: mplementation kmaker-54-033138205093:44710:44710 [0] NCCL INFO cudaDriverVersion 12010 kmaker-54-033138205093:44710:44710 [0] misc/cudawrap.cc:36 NCCL WARN Cuda failure 3 'initialization error' NCCL version 2.20.5+cuda1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: internal implementation kmaker-54-033138205093:44710:44710 [0] NCCL INFO cudaDriverVersion 12010 kmaker-54-033138205093:44710:44710 [0] misc/cudawrap.cc:36 NCCL WARN Cuda failure 3 'initialization error' NCCL version 2....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: this process. In rare cases this process can exit before this point and block the progress of another member of the process group. This constraint has always been present, but this warning has only been added since PyTo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: cannot run model when TP>1 (already run debug file) bug;stale ### Your current environment ### Model Input Dumps model = LLM("DeepSeek-Coder-V2-Lite-Base-Autofp8", trust_remote_code=True, max_model_len=4096, tens...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: work = group.allreduce([tensor], opts) [rank2]: torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/NCCLUtils.hpp:275, unhandled cuda error (run with NCCL_DEBUG=INFO for details), NCCL vers...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
