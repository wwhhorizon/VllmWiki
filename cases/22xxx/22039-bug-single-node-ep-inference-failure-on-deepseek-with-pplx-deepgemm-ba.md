# vllm-project/vllm#22039: [Bug]: Single-Node EP Inference Failure on DeepSeek with PPLX/DeepGEMM Backend

| 字段 | 值 |
| --- | --- |
| Issue | [#22039](https://github.com/vllm-project/vllm/issues/22039) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;operator;quantization |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Single-Node EP Inference Failure on DeepSeek with PPLX/DeepGEMM Backend

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi Team, I have installed the gdrcopy, and have followed the instruction [here](https://github.com/vllm-project/vllm/blob/f12d9256b39f058b93c201cedc7ffd9e605e9db8/tools/ep_kernels/install_python_libraries.sh) to install the NVSHMEM and PPLX kernel. (One change I made to the script is that, since I only want to start testing in single node situation, and the server I used is with EFA instead of Infiniband, so I changed the environment variable: `export NVSHMEM_IBGDA_SUPPORT=0` and `export NVSHMEM_USE_GDRCOPY=1` I used the pytest provided in PPLX Kernel to ensure the PPLX kernel is successfully installed: ```bash tests/test_nvshmem.py::test_nvshmem_1_gpu PASSED tests/test_nvshmem.py::test_nvshmem_4_gpu PASSED tests/test_nvshmem.py::test_all_to_all PASSED tests/test_nvshmem.py::test_all_to_all_multi_node SKIPPED (Requires multi-node environment) ======================================================== 27 passed, 7 skipped in 543.53s (0:09:03) ``` The starting server command is as follows: ```bash VLLM_ALL2ALL_BACKEND=pplx vllm serve deepseek-ai/DeepSeek-R1-0528 --tensor-parallel-size 1 --data-parallel-size 8 --enable-expert-parallel...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 2 17:13:35 [core.py:683] self.impl.process_weights_after_loading(act_dtype) (EngineCore_6 pid=108587) ERROR 08-02 17:13:35 [core.py:683] File "/root/vllm/vllm/v1/attention/backends/mla/common.py", line 988, in process_w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ## Your current environment ### 🐛 Describe the bug Hi Team, I have installed the gdrcopy, and have followed the instruction [here](https://github.com/vllm-project/vllm/blob/f12d9256b39f058b93c201cedc7ffd9e605e9db8/tools...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: gle-Node EP Inference Failure on DeepSeek with PPLX/DeepGEMM Backend bug;stale ### Your current environment ### 🐛 Describe the bug Hi Team, I have installed the gdrcopy, and have followed the instruction [here](https://...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Single-Node EP Inference Failure on DeepSeek with PPLX/DeepGEMM Backend bug;stale ### Your current environment ### 🐛 Describe the bug Hi Team, I have installed the gdrcopy, and have followed the instruction [here...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Single-Node EP Inference Failure on DeepSeek with PPLX/DeepGEMM Backend bug;stale ### Your current environment ### 🐛 Describe the bug Hi Team, I have installed the gdrcopy, and have followed the instruction [here...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
