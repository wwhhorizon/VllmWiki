# vllm-project/vllm#19332: [Bug]: [ROCm] DeepSeek-R1 fails to start with V1 engine with TP=4

| 字段 | 值 |
| --- | --- |
| Issue | [#19332](https://github.com/vllm-project/vllm/issues/19332) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [ROCm] DeepSeek-R1 fails to start with V1 engine with TP=4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I try to get DeepSeek-R1 (or R1-0528) running on 4x AMD MI325X, using the image `rocm/vllm-dev:nightly_main_20250606` I can start successfully with V0 engine, via ``` VLLM_USE_V1=0 vllm serve "deepseek-ai/DeepSeek-R1" --max-model-len 30000 --gpu-memory-utilization 0.90 --tensor-parallel-size 4 ``` However, when I set `VLLM_USE_V1=1`, the same command fails eventually with > RuntimeError: Worker failed with error 'Dynamo failed to run FX node with fake tensors: call_function (*(FakeTensor(..., device='cuda:0', size=(32*s0, 32, 64), dtype=torch.bfloat16), FakeTensor(..., device='cuda:0', size=(s0, 1, 64), dtype=torch.bfloat16)), **{}): got RuntimeError('The size of tensor a (32*s0) must match the size of tensor b (s0) at non-singleton dimension 0)') The Ask-vLLM-Bot suggests to set `VLLM_ATTENTION_BACKEND=ROCM_AITER_MLA`, which seems to work only in combination with `--block-size 1`. Unfortunately, that leads to > AssertionError: Aiter MLA only supports 16 or 128 number of heads. Provided 32 number of heads. Try adjusting tensor_parallel_size value. This is quite a pity since DeepSeek runs fine on 4 GPUs with V0 engine, but seems t...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: call_function (*(FakeTensor(..., device='cuda:0', size=(32*s0, 32, 64), dtype=torch.bfloat16), FakeTensor(..., device='cuda:0', size=(s0, 1, 64), dtype=torch.bfloat16)), **{}): got RuntimeError('The size of tensor a (32...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: [ROCm] DeepSeek-R1 fails to start with V1 engine with TP=4 bug;rocm;stale ### Your current environment ### 🐛 Describe the bug I try to get DeepSeek-R1 (or R1-0528) running on 4x AMD MI325X, using the image `rocm/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: eton dimension 0)') The Ask-vLLM-Bot suggests to set `VLLM_ATTENTION_BACKEND=ROCM_AITER_MLA`, which seems to work only in combination with `--block-size 1`. Unfortunately, that leads to > AssertionError: Aiter MLA only...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: equently asked questions. correctness activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding attention;cuda;fp8...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: BACKEND=ROCM_AITER_MLA`, which seems to work only in combination with `--block-size 1`. Unfortunately, that leads to > AssertionError: Aiter MLA only supports 16 or 128 number of heads. Provided 32 number of heads. Try...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
