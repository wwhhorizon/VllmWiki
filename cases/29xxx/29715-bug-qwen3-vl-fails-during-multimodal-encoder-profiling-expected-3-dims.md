# vllm-project/vllm#29715: [Bug]: Qwen3-VL fails during multimodal encoder profiling (expected 3 dims, got 2) on Blackwell + NVFP4 (FlashInfer) even after CUDA header fix

| 字段 | 值 |
| --- | --- |
| Issue | [#29715](https://github.com/vllm-project/vllm/issues/29715) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL fails during multimodal encoder profiling (expected 3 dims, got 2) on Blackwell + NVFP4 (FlashInfer) even after CUDA header fix

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving an NVFP4-quantized Qwen3-VL model on a Blackwell GPU using the `vllm-openai:nightly` image, engine initialization fails during the multimodal encoder profiling step with: `> ValueError: not enough values to unpack (expected 3, got 2)` This happens after weights load successfully. The failure occurs inside the Qwen2.5-VL attention block where it expects a `[seq_len, batch_size, hidden_dim]` tensor but receives a 2D tensor instead. This is my command to reproduce the issue: docker run --runtime nvidia --gpus all --ipc=host -p 8000:8000 \ -e TORCH_ALLOW_TF32_CUBLAS_OVERRIDE=1 \ -v /usr/local/cuda-12.8/targets/x86_64-linux/include:/usr/local/cuda/include:ro \ vllm/vllm-openai:nightly \ Firworks/Qwen3-VL-32B-Thinking-nvfp4 \ --dtype auto \ --max-model-len 32768 \ --gpu-memory-utilization 0.9 \ --limit-mm-per-prompt.video 0 Model downloads and loads successfully. Failure happens during engine startup, before any client request. --limit-mm-per-prompt.video 0 is set; I was getting an additional error about the video profiler but I set this to try to get past that. There may be an issue there but if I could at least test text...

## 现有链接修复摘要

#29742 [Bugfix] Fix mismatched nvfp4 gemm output shape

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: eceives a 2D tensor instead. This is my command to reproduce the issue: docker run --runtime nvidia --gpus all --ipc=host -p 8000:8000 \ -e TORCH_ALLOW_TF32_CUBLAS_OVERRIDE=1 \ -v /usr/local/cuda-12.8/targets/x86_64-lin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ing multimodal encoder profiling (expected 3 dims, got 2) on Blackwell + NVFP4 (FlashInfer) even after CUDA header fix bug ### Your current environment ### 🐛 Describe the bug When serving an NVFP4-quantized Qwen3-VL mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: VL fails during multimodal encoder profiling (expected 3 dims, got 2) on Blackwell + NVFP4 (FlashInfer) even after CUDA header fix bug ### Your current environment ### 🐛 Describe the bug When serving an NVFP4-quantized...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-VL fails during multimodal encoder profiling (expected 3 dims, got 2) on Blackwell + NVFP4 (FlashInfer) even after CUDA header fix bug ### Your current environment ### 🐛 Describe the bug When serving an NVF...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Qwen3-VL fails during multimodal encoder profiling (expected 3 dims, got 2) on Blackwell + NVFP4 (FlashInfer) even after CUDA header fix bug ### Your current environment ### 🐛 Describe the bug When serving an NVF...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29742](https://github.com/vllm-project/vllm/pull/29742) | closes_keyword | 0.95 | [Bugfix] Fix mismatched nvfp4 gemm output shape | Fix #29715 - Currently, `CompressedTensorsW4A4Fp4` always output 2d gemm hidden states, which will cause shape mismatch for ViT whose inputs are 3d. ## Test Plan ## Test Result |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
