# vllm-project/vllm#8066: [Bug]: TPU InternVL2 Model Error Graph break due to unsupported builtin _XLAC.PyCapsule._xla_get_replication_devices_count

| 字段 | 值 |
| --- | --- |
| Issue | [#8066](https://github.com/vllm-project/vllm/issues/8066) |
| 状态 | closed |
| 标签 | bug;tpu;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TPU InternVL2 Model Error Graph break due to unsupported builtin _XLAC.PyCapsule._xla_get_replication_devices_count

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` from transformers import AutoTokenizer from vllm.assets.image import ImageAsset from vllm import LLM, SamplingParams # Input image and question image = ImageAsset("cherry_blossom").pil_image.convert("RGB") question = "Describe the image in detail." # InternVL def run_internvl(question): model_name = "OpenGVLab/InternVL2-8B" llm = LLM( model=model_name, trust_remote_code=True, gpu_memory_utilization=0.9, tensor_parallel_size=4, max_num_batched_tokens=8192, max_model_len=4096, ) tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True) messages = [{"role": "user", "content": f" \n{question}"}] prompt = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) stop_tokens = [" ", " ", " ", " "] stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i in stop_tokens] return llm, prompt, stop_token_ids model_example_map = { "internvl_chat": run_internvl, } def main(): model = "internvl_chat" if model not in model_example_map: raise ValueError(f"Model type {model} is not supported.") llm, prompt, stop_token_ids = model_example_map[model](question) sampling_params = SamplingParams( t...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: orted builtin _XLAC.PyCapsule._xla_get_replication_devices_count bug;tpu;stale ### Your current environment ### 🐛 Describe the bug ``` from transformers import AutoTokenizer from vllm.assets.image import ImageAsset from...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: =None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, pipeline_parallel_size=1, disable_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: TPU InternVL2 Model Error Graph break due to unsupported builtin _XLAC.PyCapsule._xla_get_replication_devices_count bug;tpu;stale ### Your current environment ### 🐛 Describe the bug ``` from transformers import A...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: None, device_config=None, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ur current environment ### 🐛 Describe the bug ``` from transformers import AutoTokenizer from vllm.assets.image import ImageAsset from vllm import LLM, SamplingParams # Input image and question image = ImageAsset("cherr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
