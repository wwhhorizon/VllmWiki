# vllm-project/vllm#5023: [Bug]: Mistral 7b inst v0.3 fails to run

| 字段 | 值 |
| --- | --- |
| Issue | [#5023](https://github.com/vllm-project/vllm/issues/5023) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral 7b inst v0.3 fails to run

### Issue 正文摘录

### Your current environment Using official Docker image. ### 🐛 Describe the bug Using Docker image: vllm/vllm-openai:latest Params: ``` --model=mistralai/Mistral-7B-Instruct-v0.3 --gpu-memory-utilization=0.9 --trust-remote-code --max-model-len=16000 ``` Same params for Mistral-7b-Instruct-v0.2 work well, no errors. /usr/local/lib/python3.10/dist-packages/huggingface_hub/file_download.py:1132: FutureWarning: `resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`. warnings.warn( INFO 05-24 08:02:13 llm_engine.py:100] Initializing an LLM engine (v0.4.2) with config: model='mistralai/Mistral-7B-Instruct-v0.3', speculative_config=None, tokenizer='mistralai/Mistral-7B-Instruct-v0.3', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=16000, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingC...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: al 7b inst v0.3 fails to run bug ### Your current environment Using official Docker image. ### 🐛 Describe the bug Using Docker image: vllm/vllm-openai:latest Params: ``` --model=mistralai/Mistral-7B-Instruct-v0.3 --gpu-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: cribe the bug Using Docker image: vllm/vllm-openai:latest Params: ``` --model=mistralai/Mistral-7B-Instruct-v0.3 --gpu-memory-utilization=0.9 --trust-remote-code --max-model-len=16000 ``` Same params for Mistral-7b-Inst...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=16000, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, disable_custom_all_reduce=False,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=0, served_model_name=mistralai/Mistral-7B-Instruct-v0.3) You set `add_prefix_space`. The tokenizer needs to be converted...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: =False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=0, served_model_name=mistralai/Mistral-7B-Instruct-v0.3) You set `a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
