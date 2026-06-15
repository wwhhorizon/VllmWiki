# vllm-project/vllm#15031: [Usage]: There is no module or parameter named 'language_model' in Gemma3ForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#15031](https://github.com/vllm-project/vllm/issues/15031) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: There is no module or parameter named 'language_model' in Gemma3ForCausalLM

### Issue 正文摘录

**Description:** I'm encountering an error when serving a merged model with vLLM. The merged model was created using the following command: ```python model.save_pretrained_merged("/home/mata/llm/data/models/tuned/unsloth/gemma-3-12b-it-bnb-4bit-17-03-2025/checkpoint-625/merged_16bit", tokenizer) ``` I then start the vLLM server with: ```bash vllm serve /home/mata/llm/data/models/tuned/unsloth/gemma-3-12b-it-bnb-4bit-17-03-2025/checkpoint-625/merged_16bit --chat-template /home/mata/llm/data/models/chat_temp/google--gemma-3-12b-it.jinja --gpu-memory-utilization 0.9 --max_model_len 8192 ``` However, the server fails to load the model and returns the following error: ``` ValueError: There is no module or parameter named 'language_model' in Gemma3ForCausalLM ``` The stack trace indicates that during the weight loading process, vLLM attempts to locate a submodule or parameter called `language_model` in the model class `Gemma3ForCausalLM`, but it isn’t found. **Steps to Reproduce:** 1. Merge the model using `model.save_pretrained_merged(...)` as shown above. 2. Run the vLLM server with the provided command. 3. Observe the error during model loading. **Expected Behavior:** The merged mode...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: pancy between the saved merged model structure and what vLLM expects. Specifically, vLLM is looking for a `language_model` module within `Gemma3ForCausalLM` that is not present in the merged checkpoint. A possible worka...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=8192, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: There is no module or parameter named 'language_model' in Gemma3ForCausalLM usage **Description:** I'm encountering an error when serving a merged model with vLLM. The merged model was created using the followi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: rrectly reference the appropriate module names from the merged model. **Request:** Could you please investigate if the issue is with the merging process (i.e., `save_pretrained_merged`) or with vLLM's model loading logi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dtype='auto', kv_cache_dtype='auto', max_model_len=8192, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
