# vllm-project/vllm#39761: [Bug]:CUDA illegal instruction during decode (V1 Engine + NVFP4) on aarch64 (NVIDIA GB10)

| 字段 | 值 |
| --- | --- |
| Issue | [#39761](https://github.com/vllm-project/vllm/issues/39761) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;kernel;moe;operator;quantization |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:CUDA illegal instruction during decode (V1 Engine + NVFP4) on aarch64 (NVIDIA GB10)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 🐛 Describe the bug When running an NVFP4 quantized MoE model (qwen3.5-35b-a3b-nvfp4) on an ARM64 server equipped with an NVIDIA GB10 (Grace Blackwell) GPU (which natively supports NVFP4), the vLLM V1 engine crashes with a torch.AcceleratorError: CUDA error: an illegal instruction was encountered. The prefill phase successfully processes tokens (in my case, processing 57,260 prompt tokens with an 84% prefix cache hit rate), but the engine crashes specifically during the decode phase (around output token 45) inside GPUModelRunner.get_output(). Since the Blackwell hardware natively supports NVFP4 instructions, this strongly suggests a JIT compilation bug (torch.compile / Inductor) or CUDA graph issue generating invalid PTX/SASS instructions for aarch64 under the V1 Engine. Workaround: Appending --enforce-eager to the docker run command bypasses the crash entirely, which further confirms it is a compilation issue rather than a hardware limitation. To Reproduce Run the following command on a GB10 (aarch64) node: Bash docker run --runtime nvidia --gpus all \ -v /home/admin/models:/workspace/models \ -p 8081:8000 \ --ipc=host \ vllm/vll...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]:CUDA illegal instruction during decode (V1 Engine + NVFP4) on aarch64 (NVIDIA GB10) bug ### Your current environment ### 🐛 Describe the bug 🐛 Describe the bug When running an NVFP4 quantized MoE model (qwen3.5-35b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: mpt tokens with an 84% prefix cache hit rate), but the engine crashes specifically during the decode phase (around output token 45) inside GPUModelRunner.get_output(). Since the Blackwell hardware natively supports NVFP...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]:CUDA illegal instruction during decode (V1 Engine + NVFP4) on aarch64 (NVIDIA GB10) bug ### Your current environment ### 🐛 Describe the bug 🐛 Describe the bug When running an NVFP4 quantized MoE model (qwen3.5-35b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]:CUDA illegal instruction during decode (V1 Engine + NVFP4) on aarch64 (NVIDIA GB10) bug ### Your current environment ### 🐛 Describe the bug 🐛 Describe the bug When running an NVFP4 quantized MoE model (qwen3.5-35b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Describe the bug 🐛 Describe the bug When running an NVFP4 quantized MoE model (qwen3.5-35b-a3b-nvfp4) on an ARM64 server equipped with an NVIDIA GB10 (Grace Blackwell) GPU (which natively supports NVFP4), the vLLM V1 en...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
