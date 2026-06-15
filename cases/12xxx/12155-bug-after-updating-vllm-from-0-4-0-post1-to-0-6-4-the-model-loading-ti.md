# vllm-project/vllm#12155: [Bug]: After updating VLLM from 0.4.0.post1 to 0.6.4, the model loading time increased by one minute.

| 字段 | 值 |
| --- | --- |
| Issue | [#12155](https://github.com/vllm-project/vllm/issues/12155) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: After updating VLLM from 0.4.0.post1 to 0.6.4, the model loading time increased by one minute.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When my vllm version was 0.4.0.post1, it only took me 35 seconds to load Qwen2.5-7B-Instruct through the following code, but when I upgraded the vllm version to 0.6.4, this loading time increased sharply to 1 minute and 34 seconds. What is the situation here? More importantly, after the problem is solved, I also wonder if there is any way to accelerate the speed of model loading on the local, regardless of whether the vllm version is 0.4.0.post1 or 0.6.4. At present, the model loading time is normally between 30 and 60 seconds, but this is still much longer compared to the model loading using `AutoModelForCausalLM.from_pretrained()` The specific code for loading the model: ```python @ray.remote class VLLM_Qwen_Chat_Ray: def __init__(self): try: self.model_name_or_path = "/data/model/Qwen2.5-7B-Instruct" self.sampling_params = vllm.SamplingParams( temperature=0.01, top_p=0.8, repetition_penalty=1.05, max_tokens=1024 ) self.llm = vllm.LLM( model=self.model_name_or_path, tensor_parallel_size=2, gpu_memory_utilization=0.98 ) self.ready = True except Exception as e: self.ready = False logger.error(f...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: # Model Input Dumps _No response_ ### 🐛 Describe the bug When my vllm version was 0.4.0.post1, it only took me 35 seconds to load Qwen2.5-7B-Instruct through the following code, but when I upgraded the vllm version to 0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: .4.0.post1 to 0.6.4, the model loading time increased by one minute. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When my vllm version was 0.4.0.post1, it only took m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disable...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: After updating VLLM from 0.4.0.post1 to 0.6.4, the model loading time increased by one minute. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When my vllm versio...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
