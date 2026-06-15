# vllm-project/vllm#35638: [Question][XPU]: Best practices and optimized arguments for running 30B+ models on Intel Arc B580 (Dual GPU) via vLLM-XPU

| 字段 | 值 |
| --- | --- |
| Issue | [#35638](https://github.com/vllm-project/vllm/issues/35638) |
| 状态 | open |
| 标签 | usage;intel-gpu;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Question][XPU]: Best practices and optimized arguments for running 30B+ models on Intel Arc B580 (Dual GPU) via vLLM-XPU

### Issue 正文摘录

Hi vLLM-XPU Team, First of all, thank you for your incredible work on bringing vLLM to the Intel GPU ecosystem. I’ve been following the progress of the XPU backend closely, especially since the transition of IPEX and IPEX-LLM features into the upstream PyTorch and vLLM projects. It is exciting to see a more unified and native experience for Intel hardware. I am currently building a high-performance inference backend using the latest Intel Core Ultra 9 285K (Arrow Lake) paired with dual Intel Arc B580 (12GB each, 24GB total VRAM). I am using a custom Docker image built from the vLLM v0.16.0 release. I have a few detailed questions regarding the optimal startup arguments and model recommendations for this specific hardware tier. Your patience and guidance would be greatly appreciated. ## Current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : Could not collect CMake version : version 4.2.1 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch ve...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: system. I’ve been following the progress of the XPU backend closely, especially since the transition of IPEX and IPEX-LLM features into the upstream PyTorch and vLLM projects. It is exciting to see a more unified and na...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: h version : 2.10.0+xpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Question][XPU]: Best practices and optimized arguments for running 30B+ models on Intel Arc B580 (Dual GPU) via vLLM-XPU usage;intel-gpu;stale Hi vLLM-XPU Team, First of all, thank you for your incredible work on bring...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ng 30B+ models on Intel Arc B580 (Dual GPU) via vLLM-XPU usage;intel-gpu;stale Hi vLLM-XPU Team, First of all, thank you for your incredible work on bringing vLLM to the Intel GPU ecosystem. I’ve been following the prog...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: B+) model on a dual B580 setup. Given the model weight takes up ~20GB in INT4, I only have ~4GB left for KV Cache and activation. I have experimented with several parameters (e.g., varying --gpu-memory-utilization and -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
