# vllm-project/vllm#34500: [Bug]: AMD 7900 running GLM-4.7-Flash crash

| 字段 | 值 |
| --- | --- |
| Issue | [#34500](https://github.com/vllm-project/vllm/issues/34500) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AMD 7900 running GLM-4.7-Flash crash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve /data-nvm1/GLM-4.7-Flash/ -tp 2 --tool-call-parser glm47 --reasoning-parser glm45 --enable-auto-tool-choice --served-model-name GLM-4.7-Flash --max-model-len 32768 (APIServer pid=400594) DEBUG 02-13 15:31:17 [v1/sample/logits_processor/__init__.py:63] No logitsprocs plugins installed (group vllm.logits_processors). (APIServer pid=400594) DEBUG 02-13 15:31:17 [utils/torch_utils.py:119] OMP_NUM_THREADS is not set; defaulting Torch threads to 1. (EngineCore_DP0 pid=400806) DEBUG 02-13 15:31:17 [v1/engine/core.py:1049] EngineCore loop active. (Worker_TP0 pid=401013) DEBUG 02-13 15:31:17 [v1/worker/gpu_model_runner.py:3413] Running batch with cudagraph_mode: PIECEWISE, batch_descriptor: BatchDescriptor(num_tokens=8, num_reqs=None, uniform=False, has_lora=False, num_active_loras=0), should_ubatch: False, num_tokens_across_dp: None (Worker_TP1 pid=401014) DEBUG 02-13 15:31:17 [v1/worker/gpu_model_runner.py:3413] Running batch with cudagraph_mode: PIECEWISE, batch_descriptor: BatchDescriptor(num_tokens=8, num_reqs=None, uniform=False, has_lora=False, num_active_loras=0), should_ubatch: False, num_tokens_across_dp: None (Worker...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0% (EngineCore_DP0 pid=400806) ERROR 02-13 15:31:17 [v1/executor/multiproc_exec...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: 31:17 [v1/sample/logits_processor/__init__.py:63] No logitsprocs plugins installed (group vllm.logits_processors). (APIServer pid=400594) DEBUG 02-13 15:31:17 [utils/torch_utils.py:119] OMP_NUM_THREADS is not set; defau...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: parser glm47 --reasoning-parser glm45 --enable-auto-tool-choice --served-model-name GLM-4.7-Flash --max-model-len 32768 (APIServer pid=400594) DEBUG 02-13 15:31:17 [v1/sample/logits_processor/__init__.py:63] No logitspr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='glm45', reasoning_par...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, data_parallel_size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
