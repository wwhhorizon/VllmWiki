# vllm-project/vllm#31170: [Bug]: Torch.AcceleratorError: CUDA error: no kernel image is available for execution on the device

| 字段 | 值 |
| --- | --- |
| Issue | [#31170](https://github.com/vllm-project/vllm/issues/31170) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Torch.AcceleratorError: CUDA error: no kernel image is available for execution on the device

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello, I followed the instructions below to install vLLM on an NVIDIA Jetson Thor, but model inference is not working. ``` export TORCH_CUDA_ARCH_LIST=11.0a export CUDA_HOME=/usr/local/cuda-13 export TRITON_PTXAS_PATH=/usr/local/cuda/bin/ptxas export PATH="${CUDA_HOME}/bin:$PATH" uv venv .vllm --python 3.12 source .vllm/bin/activate uv pip install vllm --extra-index-url https://wheels.vllm.ai/0.13.0/cu130 --extra-index-url https://download.pytorch.org/whl/cu130 --index-strategy unsafe-best-match VLLM_ATTENTION_BACKEND=FLASHINFER vllm serve --model Qwen/Qwen3-4B --gpu-memory-utilization 0.85 ``` Full error log: ``` Loading safetensors checkpoint shards: 0% Completed | 0/13 [00:00 .60", line 170, in forward (EngineCore_DP0 pid=14334) ERROR 12-22 23:15:10 [core.py:866] submod_2 = self.submod_2(getitem_2, s72, getitem_1, l_self_modules_layers_modules_0_modules_mixer_modules_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_mixer_modules_out_proj_parameters_weight_, l_self_modules_layers_modules_1_modules_norm_parameters_weight_, getitem_3, l_self_modules_layers_modules_1_modules_mixer_modules_gate_parameters_weight_, l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ### 🐛 Describe the bug Hello, I followed the instructions below to install vLLM on an NVIDIA Jetson Thor, but model inference is not working. ``` export TORCH_CUDA_ARCH_LIST=11.0a export CUDA_HOME=/usr/local/cuda-13 exp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: rt TORCH_CUDA_ARCH_LIST=11.0a export CUDA_HOME=/usr/local/cuda-13 export TRITON_PTXAS_PATH=/usr/local/cuda/bin/ptxas export PATH="${CUDA_HOME}/bin:$PATH" uv venv .vllm --python 3.12 source .vllm/bin/activate uv pip inst...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Torch.AcceleratorError: CUDA error: no kernel image is available for execution on the device bug ### Your current environment ### 🐛 Describe the bug Hello, I followed the instructions below to install vLLM on an...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: wed the instructions below to install vLLM on an NVIDIA Jetson Thor, but model inference is not working. ``` export TORCH_CUDA_ARCH_LIST=11.0a export CUDA_HOME=/usr/local/cuda-13 export TRITON_PTXAS_PATH=/usr/local/cuda...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: pid=14334) ERROR 12-22 23:15:10 [core.py:866] buf7 = torch.ops.vllm.moe_forward_shared.default(buf6, buf5, 'model.layers.1.mixer.experts') (EngineCore_DP0 pid=14334) ERROR 12-22 23:15:10 [core.py:866] ^^^^^^^^^^^^^^^^^^...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
