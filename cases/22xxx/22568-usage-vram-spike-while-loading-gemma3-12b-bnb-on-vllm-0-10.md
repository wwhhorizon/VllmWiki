# vllm-project/vllm#22568: [Usage]: VRAM spike while loading gemma3-12b bnb on vllm-0.10

| 字段 | 值 |
| --- | --- |
| Issue | [#22568](https://github.com/vllm-project/vllm/issues/22568) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: VRAM spike while loading gemma3-12b bnb on vllm-0.10

### Issue 正文摘录

### Your current environment When loading the gemma3 bnb model, VRM usage spikes and generates OOM errors if I raise batched tokens to over 42k After the model is loaded, VRAM usage almost halves, and I think it's not being used for inference. See this nvtop chart: https://i.imgur.com/febfE0d.png Is this observation correct? The vllm command line is: `vllm serve unsloth/gemma-3-12b-it-qat-int4-unsloth-bnb-4bit --api-key none --port 6666 --max-model-len 16384 --max_num_batched_tokens 43000 --max_num_seqs 32 --disable-log-requests --gpu_memory_utilization 0.95 --served-model-name google/gemma-3-12b-it` Is there anything I should be adding to that? My goal in using the 4bit quant is to conserve VRAM. ```text ============================== [77/197] System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ==============================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: VRAM spike while loading gemma3-12b bnb on vllm-0.10 usage;stale ### Your current environment When loading the gemma3 bnb model, VRM usage spikes and generates OOM errors if I raise batched tokens to over 42k A...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rect? The vllm command line is: `vllm serve unsloth/gemma-3-12b-it-qat-int4-unsloth-bnb-4bit --api-key none --port 6666 --max-model-len 16384 --max_num_batched_tokens 43000 --max_num_seqs 32 --disable-log-requests --gpu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: VRAM spike while loading gemma3-12b bnb on vllm-0.10 usage;stale ### Your current environment When loading the gemma3 bnb model, VRM usage spikes and generates OOM errors if I raise batched tokens to over 42k A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
