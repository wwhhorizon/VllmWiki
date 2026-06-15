# vllm-project/vllm#23645: [Bug]: Qwen2.5-VL GPTQ W4A16 quantized with llm-compressor breaks with 0.10.1/0.10.1.1 (was working with 0.10.0)

| 字段 | 值 |
| --- | --- |
| Issue | [#23645](https://github.com/vllm-project/vllm/issues/23645) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-VL GPTQ W4A16 quantized with llm-compressor breaks with 0.10.1/0.10.1.1 (was working with 0.10.0)

### Issue 正文摘录

### Your current environment I tried to run on 2 servers, 1 with 2 H100 and the other with 2 A100 (both GCP) ### 🐛 Describe the bug My model is a GPTQ int4 W4A16 Qwen2.5-VL-3B compressed with the script provided by the documentation of llm-compressor https://github.com/vllm-project/llm-compressor/blob/main/examples/multimodal_vision/qwen_2_5_vl_example.py (I only changed from a 7B to a 3B for easier replication). I have publicly uploaded the model https://huggingface.co/NM-dev/Qwen2.5-VL-3B-Instruct-W4A16-G128 This configuration (llm-compressor + Qwen2.5-VL) was just added in 0.10.0 (was not supported before that version) and it works perfectly. However, it cannot be loaded anymore in 0.10.1 and 0.10.1.1, even when using the exact same command. As I did not see any depreciation notice in the patch note or a change in the default configuration, I assume it is a bug, especially since the GPUs as I using (at least the H100) are fairly recent and quite common. With vllm==0.10.1, if I use --dtype float16 the error is ```text KeyError: 'blocks.0.mlp.gate_up_proj.weight' ``` and if I don't it's (on the A100) ```text (EngineCore_0 pid=14506) ValueError: Failed to find a kernel that can im...

## 现有链接修复摘要

#20988 [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: tale ### Your current environment I tried to run on 2 servers, 1 with 2 H100 and the other with 2 A100 (both GCP) ### 🐛 Describe the bug My model is a GPTQ int4 W4A16 Qwen2.5-VL-3B compressed with the script provided by...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Qwen2.5-VL GPTQ W4A16 quantized with llm-compressor breaks with 0.10.1/0.10.1.1 (was working with 0.10.0) bug;stale ### Your current environment I tried to run on 2 servers, 1 with 2 H100 and the other with 2 A10...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: or + Qwen2.5-VL) was just added in 0.10.0 (was not supported before that version) and it works perfectly. However, it cannot be loaded anymore in 0.10.1 and 0.10.1.1, even when using the exact same command. As I did not...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Qwen2.5-VL GPTQ W4A16 quantized with llm-compressor breaks with 0.10.1/0.10.1.1 (was working with 0.10.0) bug;stale ### Your current environment I tried to run on 2 servers, 1 with 2 H100 and the other with 2 A10...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ngineCore_0 pid=14506) ConchLinearKernel cannot implement due to: conch-triton-kernels is not installed, please install it via `pip install conch-triton-kernels` and try again! (EngineCore_0 pid=14506) ExllamaLinearKern...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20988](https://github.com/vllm-project/vllm/pull/20988) | mentioned | 0.6 | [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | : RuntimeError: Unexpected error from cudaGetDeviceCo... [usage] 2. #23645: [Bug]: Qwen2.5-VL GPTQ W4A16 quantized with llm-compressor b... [bug] 3. #23641: [Feature]: Frequency a… |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23655: Should have ROCm label: NO (0 matches) #23645: Should have ROCm label: NO (0 matches) #23641: Should have ROCm label: NO (0 matches) #23638: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
