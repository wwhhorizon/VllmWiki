# vllm-project/vllm#8553: [Bug]: Online serving failing for Phi-3-vision-128k-instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#8553](https://github.com/vllm-project/vllm/issues/8553) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Online serving failing for Phi-3-vision-128k-instruct

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug online inference falls for this model ```bash vllm serve microsoft/Phi-3-vision-128k-instruct --trust-remote-code --max-num-seqs 5 --disable_sliding_window ... _pickle.PicklingError: Can't pickle : it's not the same object as transformers_modules.microsoft.Phi-3-vision-128k-instruct.c45209e90a4c4f7d16b2e9d48503c7f3e83623ed.configuration_phi3_v.Phi3VConfig ``` Doesn't seem to be transformers (4.44.2) or weights issue I did clear hf cache and redownloaded Also doesn't seem to support TP same params for the [offline inference ](https://github.com/vllm-project/vllm/blob/95965d31b6ac2c9557816a6ffabe4a3117a5ccb2/examples/offline_inference_vision_language.py#L54) works ```python # Phi-3-Vision def run_phi3v(question): prompt = f" \n \n{question} \n \n" # noqa: E501 # Note: The default setting of max_num_seqs (256) and # max_model_len (128k) for this model may cause OOM. # You may lower either to run this example on lower-end GPUs. # In this example, we override max_num_seqs to 5 while # keeping the original context length of 128k. llm = LLM( model="microsoft/Phi-3-vision-128k-instruct", trust_remote_code=True, max_num_seqs=5, disable_sl...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: =None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disabl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: environment ### 🐛 Describe the bug online inference falls for this model ```bash vllm serve microsoft/Phi-3-vision-128k-instruct --trust-remote-code --max-num-seqs 5 --disable_sliding_window ... _pickle.PicklingError: C...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ning out of memory, consider decreasing `gpu_memory_utilization` or enforcing eager mode. You can also reduce the `max_num_seqs` as needed to decrease memory usage. INFO 09-18 04:50:41 model_runner.py:1430] Graph captur...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: =False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, coll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
