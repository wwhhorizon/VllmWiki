# vllm-project/vllm#34210: [Bug]: Enable DBO on Qwen3-VL-235B-A22B raise TypeError: 'NoneType' object is not subscriptable

| 字段 | 值 |
| --- | --- |
| Issue | [#34210](https://github.com/vllm-project/vllm/issues/34210) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;gemm;moe;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Enable DBO on Qwen3-VL-235B-A22B raise TypeError: 'NoneType' object is not subscriptable

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug start script ```bash export CUDA_VISIBLE_DEVICES=0,1,2,3 export VLLM_SERVER_DEV_MODE=1 export VLLM_USE_FLASHINFER_MOE_FP8=0 export VLLM_USE_FLASHINFER_SAMPLER=0 export VLLM_USE_DEEP_GEMM_E8M0=0 MODEL_PATH=Qwen/Qwen3-VL-235B-A22B-Instruct-FP8 export SERVER_PORT=8822 export TP=2 export DP=2 export OMP_NUM_THREADS=1 vllm serve $MODEL_PATH --host 0.0.0.0 \ --tensor-parallel-size $TP \ --data-parallel-size $DP \ --enable-expert-parallel \ --all2all-backend deepep_low_latency \ --enable-dbo \ --port $SERVER_PORT \ --trust_remote_code \ --mm-encoder-tp-mode data \ --limit-mm-per-prompt.video 0 \ --gpu-memory-utilization 0.8 \ --max-num-seqs 256 \ --max-model-len 32768 \ --mm-processor-cache-gb 0 \ --no-async-scheduling ``` error log ``` (Worker_DP0_TP0_EP0 pid=208907) ERROR 02-10 13:36:23 [multiproc_executor.py:852] File "/mnt/data/conda-env/vllm-0.15.1/lib/python3.12/site-packages/vllm/v1/worker/gpu_ubatch_wrapper.py", line 369, in _slice_model_inputs (Worker_DP0_TP0_EP0 pid=208907) ERROR 02-10 13:36:23 [multiproc_executor.py:852] sliced_input_ids = input_ids[tokens_slice] (Worker_DP0_TP0_EP0 pid=208907) ERROR 02-10 13:36:23 [multiproc...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: DA_VISIBLE_DEVICES=0,1,2,3 export VLLM_SERVER_DEV_MODE=1 export VLLM_USE_FLASHINFER_MOE_FP8=0 export VLLM_USE_FLASHINFER_SAMPLER=0 export VLLM_USE_DEEP_GEMM_E8M0=0 MODEL_PATH=Qwen/Qwen3-VL-235B-A22B-Instruct-FP8 export...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory cuda;fp8;gemm;moe;operator...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: CES=0,1,2,3 export VLLM_SERVER_DEV_MODE=1 export VLLM_USE_FLASHINFER_MOE_FP8=0 export VLLM_USE_FLASHINFER_SAMPLER=0 export VLLM_USE_DEEP_GEMM_E8M0=0 MODEL_PATH=Qwen/Qwen3-VL-235B-A22B-Instruct-FP8 export SERVER_PORT=882...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: DEVICES=0,1,2,3 export VLLM_SERVER_DEV_MODE=1 export VLLM_USE_FLASHINFER_MOE_FP8=0 export VLLM_USE_FLASHINFER_SAMPLER=0 export VLLM_USE_DEEP_GEMM_E8M0=0 MODEL_PATH=Qwen/Qwen3-VL-235B-A22B-Instruct-FP8 export SERVER_PORT...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nt environment ### 🐛 Describe the bug start script ```bash export CUDA_VISIBLE_DEVICES=0,1,2,3 export VLLM_SERVER_DEV_MODE=1 export VLLM_USE_FLASHINFER_MOE_FP8=0 export VLLM_USE_FLASHINFER_SAMPLER=0 export VLLM_USE_DEEP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
