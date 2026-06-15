# vllm-project/vllm#24289: [Bug]: module 'triton.language' has no attribute 'constexpr_function'

| 字段 | 值 |
| --- | --- |
| Issue | [#24289](https://github.com/vllm-project/vllm/issues/24289) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: module 'triton.language' has no attribute 'constexpr_function'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve MiniCPM-V-4_5-AWQ --dtype auto --max-model-len 16384 --gpu_memory_utilization 0.9 --trust-remote-code error message ``` INFO 09-04 16:17:23 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=948082) INFO 09-04 16:17:26 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=948082) INFO 09-04 16:17:26 [utils.py:326] non-default args: {'model_tag': 'MiniCPM-V-4_5-AWQ', 'model': 'MiniCPM-V-4_5-AWQ', 'trust_remote_code': True, 'max_model_len': 16384} (APIServer pid=948082) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=948082) INFO 09-04 16:17:35 [__init__.py:711] Resolved architecture: MiniCPMV (APIServer pid=948082) `torch_dtype` is deprecated! Use `dtype` instead! (APIServer pid=948082) WARNING 09-04 16:17:35 [__init__.py:2768] Your device 'NVIDIA GeForce RTX 2080 Ti' (with compute capability 7.5) doesn't support torch.bfloat16. Falling back to torch.float16 for compatibility. (APIServer pid=948082) WARNING 09-04 16:17:35 [__init__.py:2819] Casting torch.bfloat16 to torch.float16. (APIServer pid=948082) INFO 09-04 1...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: environment ### 🐛 Describe the bug vllm serve MiniCPM-V-4_5-AWQ --dtype auto --max-model-len 16384 --gpu_memory_utilization 0.9 --trust-remote-code error message ``` INFO 09-04 16:17:23 [__init__.py:241] Automatically d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ver pid=948082) INFO 09-04 16:17:26 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=948082) INFO 09-04 16:17:26 [utils.py:326] non-default args: {'model_tag': 'MiniCPM-V-4_5-AWQ', 'model': 'MiniCPM-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: `` INFO 09-04 16:17:23 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=948082) INFO 09-04 16:17:26 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=948082) INFO 09-04 16:17:26...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### 🐛 Describe the bug vllm serve MiniCPM-V-4_5-AWQ --dtype auto --max-model-len 16384 --gpu_memory_utilization 0.9 --trust-remote-code error message ``` INFO 09-04 16:17:23 [__init__.py:241] Automatically detected plat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: module 'triton.language' has no attribute 'constexpr_function' bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve MiniCPM-V-4_5-AWQ --dtype auto --max-model-len 16384 --gpu_memory_utilizatio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
