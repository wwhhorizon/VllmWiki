# vllm-project/vllm#34524: [Bug]: Error saving sharded state for GPT-OSS-120B - safetensors KeyError for torch.float8_e8m0fnu

| 字段 | 值 |
| --- | --- |
| Issue | [#34524](https://github.com/vllm-project/vllm/issues/34524) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error saving sharded state for GPT-OSS-120B - safetensors KeyError for torch.float8_e8m0fnu

### Issue 正文摘录

### 🐛 Description of the bug Functionally the failure is triggered by this call: `llm.llm_engine.engine_core.save_sharded_state` Details: When running examples/offline_inference/save_sharded_state.py with a GPT-OSS-120B model, saving fails with: `KeyError: torch.float8_e8m0fnu` This happens inside safetensors/torch.py because safetensors attempts to look up the size of torch.float8_e8m0fnu in _SIZE, but that dtype is not supported yet. Because GPT-OSS-120B uses MXFP4 quantization, some tensors are materialized with dtype float8_e8m0fnu. ``` KeyError: torch.float8_e8m0fnu ... File ".../site-packages/safetensors/torch.py", line 431, in _tobytes bytes_per_item = _SIZE[tensor.dtype] ``` Steps to reproduce 1. Load GPT-OSS-120B with vLLM 2. Run save_sharded_state.py 3. Observe crash during safetensors serialization Environment details: ``` ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.10 (...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: attempts to look up the size of torch.float8_e8m0fnu in _SIZE, but that dtype is not supported yet. Because GPT-OSS-120B uses MXFP4 quantization, some tensors are materialized with dtype float8_e8m0fnu. ``` KeyError: to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Error saving sharded state for GPT-OSS-120B - safetensors KeyError for torch.float8_e8m0fnu bug ### 🐛 Description of the bug Functionally the failure is triggered by this call: `llm.llm_engine.engine_core.save_sh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.1 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
