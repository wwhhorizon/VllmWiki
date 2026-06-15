# vllm-project/vllm#28199: [Bug]: vllm/vllm/_C.abi3.so: undefined symbol: _Z20cutlass_moe_mm_sm100RN2at6TensorERKS0_S3_S3_S3_S3_S3_S3_S3_S3_bb

| 字段 | 值 |
| --- | --- |
| Issue | [#28199](https://github.com/vllm-project/vllm/issues/28199) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm/vllm/_C.abi3.so: undefined symbol: _Z20cutlass_moe_mm_sm100RN2at6TensorERKS0_S3_S3_S3_S3_S3_S3_S3_S3_bb

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I keep getting the same error when running vLLM . I've tried multiple installation methods from the vLLM documentation, including building from source and installing via pip wheels. ``` CUDA_VISIBLE_DEVICES=0 vllm serve Qwen/Qwen2.5-VL-3B-Instruct --port 8001 --host 0.0.0.0 --dtype bfloat16 (APIServer pid=36082) INFO 11-06 16:17:14 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=36082) INFO 11-06 16:17:14 [utils.py:233] non-default args: {'model_tag': 'Qwen/Qwen2.5-VL-3B-Instruct', 'host': '0.0.0.0', 'port': 8001, 'model': 'Qwen/Qwen2.5-VL-3B-Instruct', 'dtype': 'bfloat16'} (APIServer pid=36082) ERROR 11-06 16:17:19 [registry.py:548] Error in inspecting model architecture 'Qwen2_5_VLForConditionalGeneration' (APIServer pid=36082) ERROR 11-06 16:17:19 [registry.py:548] Traceback (most recent call last): (APIServer pid=36082) ERROR 11-06 16:17:19 [registry.py:548] File "/data/zhangjiawei/miniforge3/envs/vllm/lib/python3.12/site-packages/vllm/model_executor/models/registry.py", line 966, in _run_in_subprocess (APIServer pid=36082) ERROR 11-06 16:17:19 [registry.py:548] returned.check_returncode() (APIServer pid=36...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: vllm/vllm/_C.abi3.so: undefined symbol: _Z20cutlass_moe_mm_sm100RN2at6TensorERKS0_S3_S3_S3_S3_S3_S3_S3_S3_bb bug ### Your current environment ### 🐛 Describe the bug I keep getting the same error when running vLLM...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ES=0 vllm serve Qwen/Qwen2.5-VL-3B-Instruct --port 8001 --host 0.0.0.0 --dtype bfloat16 (APIServer pid=36082) INFO 11-06 16:17:14 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=36082) INFO 11-06 16:1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: vllm/vllm/_C.abi3.so: undefined symbol: _Z20cutlass_moe_mm_sm100RN2at6TensorERKS0_S3_S3_S3_S3_S3_S3_S3_S3_bb bug ### Your current environment ### 🐛 Describe the bug I keep getting the same error when running vLLM...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: vllm/vllm/_C.abi3.so: undefined symbol: _Z20cutlass_moe_mm_sm100RN2at6TensorERKS0_S3_S3_S3_S3_S3_S3_S3_S3_bb bug ### Your current environment ### 🐛 Describe the bug I keep getting the same error when running vLLM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rce and installing via pip wheels. ``` CUDA_VISIBLE_DEVICES=0 vllm serve Qwen/Qwen2.5-VL-3B-Instruct --port 8001 --host 0.0.0.0 --dtype bfloat16 (APIServer pid=36082) INFO 11-06 16:17:14 [api_server.py:1839] vLLM API se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
