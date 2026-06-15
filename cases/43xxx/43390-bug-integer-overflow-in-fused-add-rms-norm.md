# vllm-project/vllm#43390: [Bug]: integer overflow in fused_add_rms_norm

| 字段 | 值 |
| --- | --- |
| Issue | [#43390](https://github.com/vllm-project/vllm/issues/43390) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: integer overflow in fused_add_rms_norm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There is a potential integer overflow in fused_add_rms_norm in layernorm_kernels.cu when handling long sequences. The expression: `blockIdx.x * vec_hidden_size + idx` can exceed 2^31-1 for sufficiently large values of blockIdx.x and hidden_size. https://github.com/vllm-project/vllm/blob/8c8b1825eb26c1ffae776baaab16f2eebf92b7d3/csrc/layernorm_kernels.cu#L117-L118 For example, for model "royokong/e5-v", hidden_size is 4096, vec_hidden_size is 512, when batch_size is 1000 and seq_len=4195, `blockIdx.x * vec_hidden_size + idx` overflows. log: ``` fused_add_rms_norm x 554942179328 shape torch.Size([4195000, 4096]) dtype torch.float16 residual 336402025984 shape torch.Size([4195000, 4096]) dtype torch.float16 weight 12919196672 shape torch.Size([4096]) dtype torch.float16 [rank0]: Traceback (most recent call last): [rank0]: File "/workspace/./run_vllm.py", line 115, in [rank0]: llm = LLM(model=modelId, trust_remote_code=True, hf_token=HF_TOKEN, [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/usr/local/lib/python3.11/site-packages/vllm/entrypoints/llm.py", line 382, in __init__ [rank0]: self.llm_en...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: baaab16f2eebf92b7d3/csrc/layernorm_kernels.cu#L117-L118 For example, for model "royokong/e5-v", hidden_size is 4096, vec_hidden_size is 512, when batch_size is 1000 and seq_len=4195, `blockIdx.x * vec_hidden_size + idx`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ression: `blockIdx.x * vec_hidden_size + idx` can exceed 2^31-1 for sufficiently large values of blockIdx.x and hidden_size. https://github.com/vllm-project/vllm/blob/8c8b1825eb26c1ffae776baaab16f2eebf92b7d3/csrc/layern...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ``` fused_add_rms_norm x 554942179328 shape torch.Size([4195000, 4096]) dtype torch.float16 residual 336402025984 shape torch.Size([4195000, 4096]) dtype torch.float16 weight 12919196672 shape torch.Size([4096]) dtype t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: model_executor/layers/linear.py", line 228, in apply [rank0]: return dispatch_unquantized_gemm()(layer, x, layer.weight, bias) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/usr/local...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: torch.AcceleratorError: CUDA error: an illegal memory access was encountered [rank0]: Search for `cudaErrorIllegalAddress' in https://docs.nvidia.com/cuda/cuda-runtime-ap...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
