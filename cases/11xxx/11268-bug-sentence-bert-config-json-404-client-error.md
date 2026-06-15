# vllm-project/vllm#11268: [Bug]: sentence_bert_config.json 404 Client Error

| 字段 | 值 |
| --- | --- |
| Issue | [#11268](https://github.com/vllm-project/vllm/issues/11268) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: sentence_bert_config.json 404 Client Error

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This PR (https://github.com/vllm-project/vllm/pull/9506/files) introduce a default loading for sentence transformer config whenever the model config is created regardless the actual model type (sentence transformer vs regular CLMs). ``` from vllm import LLM model = LLM("meta-llama/Llama-3.1-70B-Instruct") ### { "name": "HfHubHTTPError", "message": "404 Client Error: Not Found for url: https://hfproxy/meta-llama/Llama-3.1-70B-Instruct/resolve/main/sentence_bert_config.json", "stack": "--------------------------------------------------------------------------- HTTPError Traceback (most recent call last) File ~/.airconda-environments/production--ml_infra--ray--vllm--v0.0.9/lib/python3.11/site-packages/huggingface_hub/utils/_http.py:406, in hf_raise_for_status(response, endpoint_name) 405 try: --> 406 response.raise_for_status() 407 except HTTPError as e: File ~/.airconda-environments/production--ml_infra--ray--vllm--v0.0.9/lib/python3.11/site-packages/requests/models.py:1024, in Response.raise_for_status(self) 1023 if http_error_msg: -> 1024 raise HTTPError(http_error_msg, response=self) HTTPError...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: sentence_bert_config.json 404 Client Error bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This PR (https://github.com/vllm-project/vllm/pull/9506/files) introduc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: actual model type (sentence transformer vs regular CLMs). ``` from vllm import LLM model = LLM("meta-llama/Llama-3.1-70B-Instruct") ### { "name": "HfHubHTTPError", "message": "404 Client Error: Not Found for url: https:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: n(*args, **kwargs) 111 if check_use_auth_token: 112 kwargs = smoothly_deprecate_use_auth_token(fn_name=fn.__name__, has_token=has_token, kwargs=kwargs) --> 114 return fn(*args, **kwargs) File ~/.airconda-environments/pr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: sentence_bert_config.json 404 Client Error bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This PR (https://github.com/vllm-project/vllm/pull/9506/files) introduc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: init, trust_remote_code, allowed_local_media_path, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, cpu_offload_gb, enforce_eager, max_seq_len_to_capture...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
