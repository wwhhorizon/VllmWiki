# vllm-project/vllm#33913: [Usage]: Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.

| 字段 | 值 |
| --- | --- |
| Issue | [#33913](https://github.com/vllm-project/vllm/issues/33913) |
| 状态 | open |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.

### Issue 正文摘录

### Your current environment 请替我分析一下：Traceback (most recent call last): File "/mnt/bn/liweilai-dct1201/miniconda3/envs/infer/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop output = func(*args, **kwargs) File "/mnt/bn/liweilai-dct1201/miniconda3/envs/infer/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context return func(*args, **kwargs) File "/mnt/bn/liweilai-dct1201/miniconda3/envs/infer/lib/python3.10/site-packages/vllm/v1/worker/gpu_worker.py", line 263, in determine_available_memory self.model_runner.profile_run() File "/mnt/bn/liweilai-dct1201/miniconda3/envs/infer/lib/python3.10/site-packages/vllm/v1/worker/gpu_model_runner.py", line 3361, in profile_run self.model.get_multimodal_embeddings( File "/mnt/bn/liweilai-dct1201/miniconda3/envs/infer/lib/python3.10/site-packages/vllm/model_executor/models/qwen3_vl.py", line 1381, in get_multimodal_embeddings video_embeddings = self._process_video_input(multimodal_input) File "/mnt/bn/liweilai-dct1201/miniconda3/envs/infer/lib/python3.10/site-packages/vllm/model_executor/models/qwen3_vl.py", line 1335, in _process_video_input video_embeds = self.v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Usage]: Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. usage ### Your current environment 请替我分析一下：Traceback (most recent call last): File "/mnt/bn/liweilai-dct1201/miniconda3/envs/infer/lib/python3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Usage]: Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. usage ### Your current environment 请替我分析一下：Traceback (most recent call last): File "/mnt/bn/liweilai-dct1201/miniconda3/envs/infer/lib/python3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: /worker/gpu_worker.py", line 263, in determine_available_memory self.model_runner.profile_run() File "/mnt/bn/liweilai-dct1201/miniconda3/envs/infer/lib/python3.10/site-packages/vllm/v1/worker/gpu_model_runner.py", line...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: attn_interface.py", line 233, in flash_attn_varlen_func out, softmax_lse = torch.ops._vllm_fa2_C.varlen_fwd( File "/mnt/bn/liweilai-dct1201/miniconda3/envs/infer/lib/python3.10/site-packages/torch/_ops.py", line 1243, i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: orker.py", line 263, in determine_available_memory self.model_runner.profile_run() File "/mnt/bn/liweilai-dct1201/miniconda3/envs/infer/lib/python3.10/site-packages/vllm/v1/worker/gpu_model_runner.py", line 3361, in pro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
