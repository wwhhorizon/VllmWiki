# vllm-project/vllm#16552: [Bug]: What is the differnce performance for AsyncLLMEngine in the latest VLLM 0.8.3

| 字段 | 值 |
| --- | --- |
| Issue | [#16552](https://github.com/vllm-project/vllm/issues/16552) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: What is the differnce performance for AsyncLLMEngine in the latest VLLM 0.8.3

### Issue 正文摘录

### Your current environment VLLM 0.8.3 ### 🐛 Describe the bug What used the same `AsyncLLMEngine` and the endpoint `OpenAIServingChat` of vllm using (`uvicorn main:app`) , but I checked that the TTFT is slower for the my serve than the one vllm server (`vllm serve`) although they have the exact configurations. when I checked the logged engine on the terminal I checked that they have the only difference is that the value of `use_cached_outputs` which is enabled in vllm but not in my definition of async. btw this `use_cached_outputs` arg is not exposed outside to be set from command args. Any idea please? >> Although serving the same method I used has the same performance with vllm server for the older VLLM version `0.6.6.post1`. my setup: ``` INFO 04-11 19:28:50 [llm_engine.py:242] Initializing a V0 LLM engine (v0.8.3) with config: model='NousResearch/Meta-Llama-3.1-8B-Instruct', speculative_config=None, tokenizer='NousResearch/Meta-Llama-3.1-8B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_par...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rve than the one vllm server (`vllm serve`) although they have the exact configurations. when I checked the logged engine on the terminal I checked that they have the only difference is that the value of `use_cached_out...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: he differnce performance for AsyncLLMEngine in the latest VLLM 0.8.3 bug;stale ### Your current environment VLLM 0.8.3 ### 🐛 Describe the bug What used the same `AsyncLLMEngine` and the endpoint `OpenAIServingChat` of v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: thod I used has the same performance with vllm server for the older VLLM version `0.6.6.post1`. my setup: ``` INFO 04-11 19:28:50 [llm_engine.py:242] Initializing a V0 LLM engine (v0.8.3) with config: model='NousResearc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: y:242] Initializing a V0 LLM engine (v0.8.3) with config: model='NousResearch/Meta-Llama-3.1-8B-Instruct', speculative_config=None, tokenizer='NousResearch/Meta-Llama-3.1-8B-Instruct', skip_tokenizer_init=False, tokeniz...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
