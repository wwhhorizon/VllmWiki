# vllm-project/vllm#35028: [Bug]: RuntimeError: CUDA error: CUBLAS_STATUS_INVALID_VALUE when calling `cublasGemmEx

| 字段 | 值 |
| --- | --- |
| Issue | [#35028](https://github.com/vllm-project/vllm/issues/35028) |
| 状态 | open |
| 标签 | bug |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: CUBLAS_STATUS_INVALID_VALUE when calling `cublasGemmEx

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello, When I try to serve the model using `vllm serve` I encounter the issue below. It fails on the x86 machine and on Jetson Thor, but it works on DGX Spark. Is this expected behavior? ``` #x86 machine with cuda 13.0 uv pip install https://github.com/vllm-project/vllm/releases/download/v0.16.0/vllm-0.16.0+cu130-cp38-abi3-manylinux_2_35_x86_64.whl \ --extra-index-url https://download.pytorch.org/whl/cu130 \ --index-strategy unsafe-best-match #DGX spark and Jetson Thor cuda 13.0 uv pip install https://github.com/vllm-project/vllm/releases/download/v0.16.0/vllm-0.16.0+cu130-cp38-abi3-manylinux_2_35_aarch64.whl \ --extra-index-url https://download.pytorch.org/whl/cu130 \ --index-strategy unsafe-best-match ``` Full error log: ``` (EngineCore_DP0 pid=348607) INFO 02-21 22:45:28 [cuda.py:367] Using FLASH_ATTN attention backend out of potential backends: ['FLASH_ATTN', 'FLASHINFER', 'TRITON_ATTN', 'FLEX_ATTENTION']. Loading safetensors checkpoint shards: 0% Completed | 0/3 [00:00 .74", line 298, in forward (EngineCore_DP0 pid=348607) ERROR 02-21 22:45:36 [core.py:1006] submod_0 = self.submod_0(l_input_ids_, s72, l_self_modules_embed_to...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ark. Is this expected behavior? ``` #x86 machine with cuda 13.0 uv pip install https://github.com/vllm-project/vllm/releases/download/v0.16.0/vllm-0.16.0+cu130-cp38-abi3-manylinux_2_35_x86_64.whl \ --extra-index-url htt...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: pid=348607) INFO 02-21 22:45:28 [cuda.py:367] Using FLASH_ATTN attention backend out of potential backends: ['FLASH_ATTN', 'FLASHINFER', 'TRITON_ATTN', 'FLEX_ATTENTION']. Loading safetensors checkpoint shards: 0% Comple...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: environment ### 🐛 Describe the bug Hello, When I try to serve the model using `vllm serve` I encounter the issue below. It fails on the x86 machine and on Jetson Thor, but it works on DGX Spark. Is this expected behavio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 6] File "/home/admin2/.vllm/lib/python3.12/site-packages/torch/_dynamo/eval_frame.py", line 1181, in _fn (EngineCore_DP0 pid=348607) ERROR 02-21 22:45:36 [core.py:1006] return fn(*args, **kwargs) (EngineCore_DP0 pid=348...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: RuntimeError: CUDA error: CUBLAS_STATUS_INVALID_VALUE when calling `cublasGemmEx bug ### Your current environment ### 🐛 Describe the bug Hello, When I try to serve the model using `vllm serve` I encounter the iss...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
