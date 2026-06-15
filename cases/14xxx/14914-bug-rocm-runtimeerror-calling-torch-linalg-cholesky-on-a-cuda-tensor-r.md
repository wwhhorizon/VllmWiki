# vllm-project/vllm#14914: [Bug] [ROCm]: RuntimeError: Calling `torch.linalg.cholesky` on a CUDA tensor requires compiling PyTorch with MAGMA. Please use PyTorch built with MAGMA support.

| 字段 | 值 |
| --- | --- |
| Issue | [#14914](https://github.com/vllm-project/vllm/issues/14914) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] [ROCm]: RuntimeError: Calling `torch.linalg.cholesky` on a CUDA tensor requires compiling PyTorch with MAGMA. Please use PyTorch built with MAGMA support.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug To support vision language embedding model (llava model) on vLLM for ROCm. When I am trying to enable vision_language embedding model support on vLLM for ROCm, I encounter this issue. ``` tests/models/embedding/vision_language/test_llava_next.py:134: _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ tests/models/embedding/vision_language/test_llava_next.py:63: in _run_test hf_model.model.resize_token_embeddings( /usr/local/lib/python3.12/dist-packages/transformers/modeling_utils.py:2109: in resize_token_embeddings model_embeds = self._resize_token_embeddings(new_num_tokens, pad_to_multiple_of, mean_resizing) /usr/local/lib/python3.12/dist-packages/transformers/modeling_utils.py:2134: in _resize_token_embeddings new_embeddings = self._get_resized_embeddings( /usr/local/lib/python3.12/dist-packages/transformers/modeling_utils.py:2291: in _get_resized_embeddings self._init_added_embeddings_weights_with_mean( /usr/local/lib/python3.12/dist-packages/transformers/modeling_utils.py:2470: in _init_added_embeddings_weights_with_mean is_covariance_psd = constraints.positive_definite.check(epsilon * covariance)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: y does not support this feature as the PyTorch is built from scratch in `Dockerfile.rocm_base` and in the build process, MAGMA is not compiled and PyTorch is also not compiled with `USE_MAGMA` flag on. ### Before submit...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ronment ### 🐛 Describe the bug To support vision language embedding model (llava model) on vLLM for ROCm. When I am trying to enable vision_language embedding model support on vLLM for ROCm, I encounter this issue. ```...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug] [ROCm]: RuntimeError: Calling `torch.linalg.cholesky` on a CUDA tensor requires compiling PyTorch with MAGMA. Please use PyTorch built with MAGMA support. bug;rocm;stale ### Your current environment ### 🐛 Describe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ware_porting;model_support;multimodal_vlm;quantization cuda;quantization;triton build_error env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: uted_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization cuda;quantization;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
