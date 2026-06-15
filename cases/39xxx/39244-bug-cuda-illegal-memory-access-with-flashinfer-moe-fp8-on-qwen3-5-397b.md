# vllm-project/vllm#39244: [Bug]: CUDA illegal memory access with FlashInfer MoE FP8 on Qwen3.5-397B (num_tokens > 256)

| 字段 | 值 |
| --- | --- |
| Issue | [#39244](https://github.com/vllm-project/vllm/issues/39244) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;moe;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA illegal memory access with FlashInfer MoE FP8 on Qwen3.5-397B (num_tokens > 256)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## How to reproduce ```bash export VLLM_USE_FLASHINFER_SAMPLER=1 export VLLM_USE_FLASHINFER_MOE_FP8=1 vllm serve Qwen/Qwen3.5-397B-A17B-FP8 \ --tensor-parallel-size 4 --enable-expert-parallel \ --async-scheduling --max-num-seqs 512 \ --max-num-batched-tokens 4096 --max-model-len 4096 \ --gpu-memory-utilization 0.9 --trust-remote-code --port 8001 \ --compilation-config '{"compile_sizes":[1,2,4,8,16,32,64,128,256,512],"cudagraph_capture_sizes":[1,2,4,8,16,32,64,128,256,512]}' ``` Then send 8 concurrent requests: ```bash for i in $(seq 1 8); do curl -s -o /dev/null -w "req_$i: HTTP %{http_code}\n" \ http://localhost:8001/v1/completions \ -H "Content-Type: application/json" \ -d '{"model":"Qwen/Qwen3.5-397B-A17B-FP8","prompt":"Write a detailed essay about AI.","max_tokens":600,"min_tokens":600}' & done; wait ``` Result: 5/8 HTTP 200, 3/8 HTTP 500. Server crashes. ## Standalone repro (no vLLM needed) ```python import torch from flashinfer.fused_moe import cutlass_fused_moe from flashinfer.fused_moe.core import ActivationType h, inter, ne, tk = 5120, 8960, 128, 8 device = "cuda" f1 = torch.randn(ne, 2*inter, h, dtype=torch.bfloat16, de...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: CUDA illegal memory access with FlashInfer MoE FP8 on Qwen3.5-397B (num_tokens > 256) bug ### Your current environment ### 🐛 Describe the bug ## How to reproduce ```bash export VLLM_USE_FLASHINFER_SAMPLER=1 expor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: lization 0.9 --trust-remote-code --port 8001 \ --compilation-config '{"compile_sizes":[1,2,4,8,16,32,64,128,256,512],"cudagraph_capture_sizes":[1,2,4,8,16,32,64,128,256,512]}' ``` Then send 8 concurrent requests: ```bas...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: CUDA illegal memory access with FlashInfer MoE FP8 on Qwen3.5-397B (num_tokens > 256) bug ### Your current environment ### 🐛 Describe the bug ## How to reproduce ```bash export VLLM_USE_FLASHINFER_SAMPLER=1 expor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: CUDA illegal memory access with FlashInfer MoE FP8 on Qwen3.5-397B (num_tokens > 256) bug ### Your current environment ### 🐛 Describe the bug ## How to reproduce ```bash export VLLM_USE_FLASHINFER_SAMPLER=1 expor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: CUDA illegal memory access with FlashInfer MoE FP8 on Qwen3.5-397B (num_tokens > 256) bug ### Your current environment ### 🐛 Describe the bug ## How to reproduce ```bash export VLLM_USE_FLASHINFER_SAMPLER=1 export

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
