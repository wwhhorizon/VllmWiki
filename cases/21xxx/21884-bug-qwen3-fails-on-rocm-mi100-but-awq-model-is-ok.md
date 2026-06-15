# vllm-project/vllm#21884: [Bug]: Qwen3 fails on ROCM MI100, but awq model is OK

| 字段 | 值 |
| --- | --- |
| Issue | [#21884](https://github.com/vllm-project/vllm/issues/21884) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3 fails on ROCM MI100, but awq model is OK

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to serve the Qwen3 8B model on a Mi100 card, vllm fails and repeatedly outputs the following error. What's weird is that serving Qwen3 AWQ model is fine, if VLLM_USE_TRITON_AWQ=1 is set. /app/vllm/build/temp.linux-x86_64-cpython-312/csrc/rocm/skinny_gemms.hip:497: void wvSplitK_hf_sml_(const int, const int, const scalar_t *, const scalar_t *__restrict, scalar_t *, const int, const int) [scalar_t = __hip_bfloat16, THRDS = 64, YTILE = 2, WvPrGrp = 16, A_CHUNK = 8, UNRL = 2, N = 2]: Device-side assertion `false' failed. The command to start vllm is: vllm serve /models/Qwen3-8B/ --max-model-len 8192 --dtype auto --served-model-name zz-model --api-key xxxx --port 8080 INFO 07-30 02:10:47 [__init__.py:239] Automatically detected platform rocm. INFO 07-30 02:11:09 [api_server.py:1043] vLLM API server version 0.8.5.dev137+gacba33a0f.d20250429 INFO 07-30 02:11:09 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='/models/Qwen3-8B/', config='', host=None, port=8080, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=[...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ing Qwen3 AWQ model is fine, if VLLM_USE_TRITON_AWQ=1 is set. /app/vllm/build/temp.linux-x86_64-cpython-312/csrc/rocm/skinny_gemms.hip:497: void wvSplitK_hf_sml_(const int, const int, const scalar_t *, const scalar_t *_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: calar_t *__restrict, scalar_t *, const int, const int) [scalar_t = __hip_bfloat16, THRDS = 64, YTILE = 2, WvPrGrp = 16, A_CHUNK = 8, UNRL = 2, N = 2]: Device-side assertion `false' failed. The command to start vllm is:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Qwen3 fails on ROCM MI100, but awq model is OK bug ### Your current environment ### 🐛 Describe the bug When trying to serve the Qwen3 8B model on a Mi100 card, vllm fails and repeatedly outputs the following erro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3 fails on ROCM MI100, but awq model is OK bug ### Your current environment ### 🐛 Describe the bug When trying to serve the Qwen3 8B model on a Mi100 card, vllm fails and repeatedly outputs the following erro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: error. What's weird is that serving Qwen3 AWQ model is fine, if VLLM_USE_TRITON_AWQ=1 is set. /app/vllm/build/temp.linux-x86_64-cpython-312/csrc/rocm/skinny_gemms.hip:497: void wvSplitK_hf_sml_(const int, const int, con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
