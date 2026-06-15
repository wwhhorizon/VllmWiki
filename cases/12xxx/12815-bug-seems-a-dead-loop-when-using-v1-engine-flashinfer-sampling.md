# vllm-project/vllm#12815: [Bug]: Seems a dead loop when using v1 engine + flashinfer sampling

| 字段 | 值 |
| --- | --- |
| Issue | [#12815](https://github.com/vllm-project/vllm/issues/12815) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Seems a dead loop when using v1 engine + flashinfer sampling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The GPU utilization keeps 100%, and cpu process keeps 100%. ![Image](https://github.com/user-attachments/assets/5194c78d-57b5-46e4-b4ae-fe5ae828c741) ![Image](https://github.com/user-attachments/assets/0bd66ca7-8674-48e1-97ae-62878744d63f) ``` [Thread debugging using libthread_db enabled] Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1". 0x00007fed8de6c3a1 in ?? () from /usr/local/cuda/compat/lib/libcuda.so.1 [New Thread 0x7fed8f5e4480 (LWP 32250)] [New Thread 0x7fdc47fff640 (LWP 32251)] [Detaching after fork from child process 32252] [Thread 0x7fed8f5e4480 (LWP 32250) exited] Thread 1 "python3" received signal SIGURG, Urgent I/O condition. [Switching focus to CUDA kernel 0, grid 4670577, block (16,0,0), thread (0,0,0), device 0, sm 34, warp 3, lane 0] 0x00007fdd72f04bc0 in void flashinfer::sampling::TopKRenormProbKernel (float*, float*, int*, unsigned int, unsigned int) >> () (cuda-gdb) bt #0 0x00007fdd72f04bc0 in void flashinfer::sampling::TopKRenormProbKernel (float*, float*, int*, unsigned int, unsigned int) >> () (cuda-gdb) ``` I run the code using ``` import os port = 10010 model_path = "/data/bench...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: int, unsigned int) >> () (cuda-gdb) ``` I run the code using ``` import os port = 10010 model_path = "/data/benchmark-vllm-v1/models/qwen2.5-32b-task32_311phbrtw-static-fp8" cmd = f"CUDA_VISIBLE_DEVICES=0 VLLM_USE_V1=1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: th = "/data/benchmark-vllm-v1/models/qwen2.5-32b-task32_311phbrtw-static-fp8" cmd = f"CUDA_VISIBLE_DEVICES=0 VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server \ --port {port} \ --model {model_path} \ --dtype a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Seems a dead loop when using v1 engine + flashinfer sampling bug;stale ### Your current environment ### 🐛 Describe the bug The GPU utilization keeps 100%, and cpu process keeps 100%. ![Image](https://github.com/u...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: >> () (cuda-gdb) ``` I run the code using ``` import os port = 10010 model_path = "/data/benchmark-vllm-v1/models/qwen2.5-32b-task32_311phbrtw-static-fp8" cmd = f"CUDA_VISIBLE_DEVICES=0 VLLM_USE_V1=1 python3 -m vllm.ent...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: Seems a dead loop when using v1 engine + flashinfer sampling bug;stale ### Your current environment ### 🐛 Describe the bug The GPU utilization keeps 100%, and cpu process keeps 100%. ![Image](https://github.com/u...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
