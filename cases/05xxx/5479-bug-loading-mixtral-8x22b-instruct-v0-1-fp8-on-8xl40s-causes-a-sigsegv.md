# vllm-project/vllm#5479: [Bug]: Loading Mixtral-8x22B-Instruct-v0.1-FP8 on 8xL40S causes a SIGSEGV 

| 字段 | 值 |
| --- | --- |
| Issue | [#5479](https://github.com/vllm-project/vllm/issues/5479) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Loading Mixtral-8x22B-Instruct-v0.1-FP8 on 8xL40S causes a SIGSEGV 

### Issue 正文摘录

### Your current environment For setup, I am using the version 0.5 and the vllm_openai target as part of the Dockerfile with these arguments: ``` environment: - NCCL_SOCKET_IFNAME=eth0 restart: unless-stopped ulimits: memlock: -1 stack: -1 ports: - "3010:8000" ipc: host command: - "--model" - "/models/Mixtral-8x22B-Instruct-v0.1-FP8" - "--gpu-memory-utilization" - "0.95" - "--tensor-parallel-size" - "8" - "--host" - "0.0.0.0" - "--max-num-seqs" - "70" - "--quantization" - "fp8" - "--download-dir" - "/models" ``` ### 🐛 Describe the bug When I load [Mixtral-8x22B-Instruct-v0.1-FP8](https://huggingface.co/nm-testing/Mixtral-8x22B-Instruct-v0.1-FP8) onto 8 L40S it causes this error: ``` Attaching to vllm1-1 vllm1-1 | (VllmWorkerProcess pid=14207) INFO 06-13 00:51:33 multiproc_worker_utils.py:215] Worker ready; awaiting tasks vllm1-1 | (VllmWorkerProcess pid=14205) INFO 06-13 00:51:33 multiproc_worker_utils.py:215] Worker ready; awaiting tasks vllm1-1 | (VllmWorkerProcess pid=14206) INFO 06-13 00:51:33 multiproc_worker_utils.py:215] Worker ready; awaiting tasks vllm1-1 | (VllmWorkerProcess pid=14210) INFO 06-13 00:51:33 multiproc_worker_utils.py:215] Worker ready; awaiting tasks vllm1-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: GSEGV bug;stale ### Your current environment For setup, I am using the version 0.5 and the vllm_openai target as part of the Dockerfile with these arguments: ``` environment: - NCCL_SOCKET_IFNAME=eth0 restart: unless-st...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Loading Mixtral-8x22B-Instruct-v0.1-FP8 on 8xL40S causes a SIGSEGV bug;stale ### Your current environment For setup, I am using the version 0.5 and the vllm_openai target as part of the Dockerfile with these argu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 0 vllm1-1 | vllm1-1 | UNREACHABLE executed at /project/lib/Conversion/TritonGPUToLLVM/ElementwiseOpToLLVM.cpp:823! vllm1-1 | Conversion from/to f8e4m3nv is only supported on compute capability >= 90 vllm1-1 | vllm1-1 |...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: in main vllm1-1 | cache[rtype].remove(name) vllm1-1 | KeyError: '/psm_38be8863' vllm1-1 | Traceback (most recent call last): vllm1-1 | File "/usr/lib/python3.10/multiprocessing/resource_tracker.py", line 209, in main vl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: -1 ports: - "3010:8000" ipc: host command: - "--model" - "/models/Mixtral-8x22B-Instruct-v0.1-FP8" - "--gpu-memory-utilization" - "0.95" - "--tensor-parallel-size" - "8" - "--host" - "0.0.0.0" - "--max-num-seqs"

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
