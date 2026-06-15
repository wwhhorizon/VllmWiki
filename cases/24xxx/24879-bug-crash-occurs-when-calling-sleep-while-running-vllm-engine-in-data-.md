# vllm-project/vllm#24879: [Bug]: Crash occurs when calling sleep while running vLLM engine in data parallel mode

| 字段 | 值 |
| --- | --- |
| Issue | [#24879](https://github.com/vllm-project/vllm/issues/24879) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crash occurs when calling sleep while running vLLM engine in data parallel mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug During RLHF, the generative reward model needs to release GPU memory using the sleep function after a rollout. However, when using data parallelism, calling sleep immediately after the rollout causes the vLLM engine to crash. run engine ```bash VLLM_SERVER_DEV_MODE=1 vllm serve ~/huggingface/Qwen2-1.5B-Instruct --enable-sleep-mode --gpu-memory-utilization 0.7 -dp 2 --port 8199 --served-model-name Qwen2-1.5B-Instruct ``` rollout and sleep ```python import requests from openai import OpenAI port = 8199 def chat(): openai_api_key = "EMPTY" openai_api_base = f"http://localhost:{port}/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) models = client.models.list() model_name = models.data[0].id completion = client.completions.create(model=model_name, prompt="San Francisco is a") print("Completion result:", completion) return completion def model_sleep(): requests.post(f'http://localhost:{port}/sleep?level=1') if __name__ == "__main__": resp = chat() model_sleep() ``` crash ``` INFO 09-15 09:24:14 [__init__.py:216] Automatically detected platform cuda. WARNING 09-15 09:24:17 [api_server.py:1051] SECURITY WARNING:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: --served-model-name Qwen2-1.5B-Instruct ``` rollout and sleep ```python import requests from openai import OpenAI port = 8199 def chat(): openai_api_key = "EMPTY" openai_api_base = f"http://localhost:{port}/v1" client =...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ;stale ### Your current environment ### 🐛 Describe the bug During RLHF, the generative reward model needs to release GPU memory using the sleep function after a rollout. However, when using data parallelism, calling sle...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: s when calling sleep while running vLLM engine in data parallel mode bug;stale ### Your current environment ### 🐛 Describe the bug During RLHF, the generative reward model needs to release GPU memory using the sleep fun...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
