# vllm-project/vllm#24850: [Bug]: How to Use the VLLM_USE_NVFP4_CT_EMULATIONS=1 Flag on Non-Blackwell GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#24850](https://github.com/vllm-project/vllm/issues/24850) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: How to Use the VLLM_USE_NVFP4_CT_EMULATIONS=1 Flag on Non-Blackwell GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello, I am currently attempting to perform quantization with NVFP4 using llmcompressor and then run inference. The GPU I have available is an A6000, but since NVFP4 is not natively supported on the A6000, I was searching for alternatives and came across the VLLM_USE_NVFP4_CT_EMULATIONS flag. It seems that this flag allows fake quantization for activations on non-Blackwell GPUs, enabling inference. However, I encounter errors. Specifically, an error occurs during the CUDA graph capture process, and it appears to originate at the Triton kernel level. When I bypass the CUDA graph capturing process by enabling the enforce_eager option, inference does work, but it becomes extremely slow. Could you please let me know how to properly use the VLLM_USE_NVFP4_CT_EMULATIONS flag on an A6000? Thank you. [Running script] ```sh export VLLM_USE_NVFP4_CT_EMULATIONS=1 python evaluation.py --model \ --tensor_parallel_size 1 ``` ```python llm = LLM( model = model_path, tensor_parallel_size = tensor_parallel_size, trust_remote_code=True, max_model_len=32768, enforce_eager=False, -> True of False gpu_memory_utilization=0.9 ) ``` ```sh (EngineCore_DP...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: How to Use the VLLM_USE_NVFP4_CT_EMULATIONS=1 Flag on Non-Blackwell GPUs bug;stale ### Your current environment ### 🐛 Describe the bug Hello, I am currently attempting to perform quantization with NVFP4 using llm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: non-Blackwell GPUs, enabling inference. However, I encounter errors. Specifically, an error occurs during the CUDA graph capture process, and it appears to originate at the Triton kernel level. When I bypass the CUDA gr...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: _remote_code=True, max_model_len=32768, enforce_eager=False, -> True of False gpu_memory_utilization=0.9 ) ``` ```sh (EngineCore_DP0 pid=2660106) [rank0]:E0915 03:59:15.531000 2660106 site-packages/torch/_inductor/runti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: How to Use the VLLM_USE_NVFP4_CT_EMULATIONS=1 Flag on Non-Blackwell GPUs bug;stale ### Your current environment ### 🐛 Describe the bug Hello, I am currently attempting to perform quantization with NVFP4 using llm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ript] ```sh export VLLM_USE_NVFP4_CT_EMULATIONS=1 python evaluation.py --model \ --tensor_parallel_size 1 ``` ```python llm = LLM( model = model_path, tensor_parallel_size = tensor_parallel_size, trust_remote_code=True,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
