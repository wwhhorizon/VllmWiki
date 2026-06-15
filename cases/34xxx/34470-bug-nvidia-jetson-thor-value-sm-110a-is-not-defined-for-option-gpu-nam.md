# vllm-project/vllm#34470: [Bug]: NVIDIA Jetson Thor: Value 'sm_110a' is not defined for option 'gpu-name'

| 字段 | 值 |
| --- | --- |
| Issue | [#34470](https://github.com/vllm-project/vllm/issues/34470) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NVIDIA Jetson Thor: Value 'sm_110a' is not defined for option 'gpu-name'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug [Repository for reproducibility purposes](https://github.com/Kaweees/thor_inference) Running these commands: ```bash export TORCH_CUDA_ARCH_LIST=11.0f export TRITON_PTXAS_PATH=/usr/local/cuda/bin/ptxas export PATH=/usr/local/cuda/bin:$PATH export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH uv run vllm serve "Qwen/Qwen2.5-1.5B-Instruct" \ --port 8000 \ --host 0.0.0.0 \ --trust-remote-code \ --max-model-len 8192 \ --gpu-memory-utilization 0.7 ``` Results in [the attached error logs](https://github.com/user-attachments/files/25275680/error.txt). ```txt # core log ... (EngineCore_DP0 pid=133799) ERROR 02-12 14:03:17 [core.py:1006] raise RuntimeError(f"Failed to run autotuning code block: {e}") from e (EngineCore_DP0 pid=133799) ERROR 02-12 14:03:17 [core.py:1006] torch._inductor.exc.InductorError: RuntimeError: Failed to run autotuning code block: No valid triton configs. PTXASError: PTXAS error: Internal Triton PTX codegen error (EngineCore_DP0 pid=133799) ERROR 02-12 14:03:17 [core.py:1006] `ptxas` stderr: (EngineCore_DP0 pid=133799) ERROR 02-12 14:03:17 [core.py:1006] ptxas-blackwell fatal : Value 'sm_110a' is not defin...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: NVIDIA Jetson Thor: Value 'sm_110a' is not defined for option 'gpu-name' bug ### Your current environment ### 🐛 Describe the bug [Repository for reproducibility purposes](https://github.com/Kaweees/thor_inference...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: r current environment ### 🐛 Describe the bug [Repository for reproducibility purposes](https://github.com/Kaweees/thor_inference) Running these commands: ```bash export TORCH_CUDA_ARCH_LIST=11.0f export TRITON_PTXAS_PAT...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: _LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH uv run vllm serve "Qwen/Qwen2.5-1.5B-Instruct" \ --port 8000 \ --host 0.0.0.0 \ --trust-remote-code \ --max-model-len 8192 \ --gpu-memory-utilization 0.7 ``` Results...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Running these commands: ```bash export TORCH_CUDA_ARCH_LIST=11.0f export TRITON_PTXAS_PATH=/usr/local/cuda/bin/ptxas export PATH=/usr/local/cuda/bin:$PATH export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH uv...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 17 [core.py:1006] raise RuntimeError(f"Failed to run autotuning code block: {e}") from e (EngineCore_DP0 pid=133799) ERROR 02-12 14:03:17 [core.py:1006] torch._inductor.exc.InductorError: RuntimeError: Failed to run aut...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
