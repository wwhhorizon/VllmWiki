# vllm-project/vllm#15631: [Bug]: Can't load any LLM with v0.8.*

| 字段 | 值 |
| --- | --- |
| Issue | [#15631](https://github.com/vllm-project/vllm/issues/15631) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't load any LLM with v0.8.*

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The simple code i run: ```python # built on nvidia/cuda:12.6.2-base-ubuntu22.04 from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="google/gemma-3-1b-it") # or any gemma model ``` Here is the output. Right after "Model loading took" pod is dying with status code 139. When i run these codes in notebook kernel dies immidiately. I don't know how can i track any other error. I couldn't catch but the setup was very simple. ``` Fetching 10 files: 0%| | 0/10 [00:00<?, ?it/s] Fetching 10 files: 100%|██████████| 10/10 [00:00<00:00, 3725.29it/s] INFO 03-27 15:53:05 [config.py:585] This model supports multiple tasks: {'classify', 'generate', 'embed', 'reward', 'score'}. Defaulting to 'generate'. INFO 03-27 15:53:05 [llm_engine.py:241] Initializing a V0 LLM engine (v0.8.2) with config: model='google/gemma-3-1b-it', speculative_config=None, tokenizer='google/gemma-3-1b-it', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_con...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: run: ```python # built on nvidia/cuda:12.6.2-base-ubuntu22.04 from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="google/gemma-3-1b-it") # or any gemma model ``` Here is the output. Right after "Model loading took" pod is dying with status code 139. When...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: zing a V0 LLM engine (v0.8.2) with config: model='google/gemma-3-1b-it', speculative_config=None, tokenizer='google/gemma-3-1b-it', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
