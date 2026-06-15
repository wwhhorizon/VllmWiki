# vllm-project/vllm#7216: [Bug]: Dynamic FP8 Marlin quantization fails on `0.5.4` 

| 字段 | 值 |
| --- | --- |
| Issue | [#7216](https://github.com/vllm-project/vllm/issues/7216) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Dynamic FP8 Marlin quantization fails on `0.5.4` 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Dynamic FP8 works fine on H100 but fails on A100. This is an issue with the dynamic FP8 Marlin backend. ``` vllm serve meta-llama/Meta-Llama-3-8B-Instruct --quantization="fp8" --port 9000 ... File "/home/mgoin/venvs/vllm-rel/lib/python3.10/site-packages/vllm/model_executor/layers/quantization/utils/marlin_utils.py", line 172, in marlin_permute_scales s = s.reshape((-1, len(scale_perm_single)))[:, scale_perm_single] RuntimeError: shape '[-1, 32]' is invalid for input of size 1 ``` It does work fine with models that are already quantized to FP8 on A100: ``` vllm serve neuralmagic/Meta-Llama-3-8B-Instruct-FP8 --quantization="fp8" --port 9000 ... INFO: Uvicorn running on http://0.0.0.0:9000 (Press CTRL+C to quit) ``` Full command and output/stacktrace: ``` vllm serve meta-llama/Meta-Llama-3-8B-Instruct --quantization="fp8" --port 9000 INFO 08-06 19:27:35 api_server.py:339] vLLM API server version 0.5.4 INFO 08-06 19:27:35 api_server.py:340] args: Namespace(model_tag='meta-llama/Meta-Llama-3-8B-Instruct', host=None, port=9000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_head...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Dynamic FP8 Marlin quantization fails on `0.5.4` bug ### Your current environment ### 🐛 Describe the bug Dynamic FP8 works fine on H100 but fails on A100. This is an issue with the dynamic FP8 Marlin backend. ```...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, num_speculative_tokens=None, speculative_draft_tensor_parallel_si...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: --port 9000 INFO 08-06 19:27:35 api_server.py:339] vLLM API server version 0.5.4 INFO 08-06 19:27:35 api_server.py:340] args: Namespace(model_tag='meta-llama/Meta-Llama-3-8B-Instruct', host=None, port=9000, uvicorn_log_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: his is an issue with the dynamic FP8 Marlin backend. ``` vllm serve meta-llama/Meta-Llama-3-8B-Instruct --quantization="fp8" --port 9000 ... File "/home/mgoin/venvs/vllm-rel/lib/python3.10/site-packages/vllm/model_execu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: on H100 but fails on A100. This is an issue with the dynamic FP8 Marlin backend. ``` vllm serve meta-llama/Meta-Llama-3-8B-Instruct --quantization="fp8" --port 9000 ... File "/home/mgoin/venvs/vllm-rel/lib/python3.10/si...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
