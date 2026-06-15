# vllm-project/vllm#1354: Vicuna-7b-v1.3 OOM with vLLM but working with Fastchat

| 字段 | 值 |
| --- | --- |
| Issue | [#1354](https://github.com/vllm-project/vllm/issues/1354) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Vicuna-7b-v1.3 OOM with vLLM but working with Fastchat

### Issue 正文摘录

I am using WSL2 and trying to start OpenAI server with `lmsys/vicuna-7b-v1.3` model using the following command: ```{shell} python -m vllm.entrypoints.openai.api_server --model lmsys/vicuna-7b-v1.3 --gpu-memory-utilization 0.98 --dtype half ``` After loading the model it takes ~5-6 min of waiting until I get the **ValueError: No available memory for the cache blocks**: ``` $ python -m vllm.entrypoints.openai.api_server --model lmsys/vicuna-7b-v1.3 --gpu-memory-utilization 0.98 --dtype half INFO 10-14 21:32:44 llm_engine.py:72] Initializing an LLM engine with config: model='lmsys/vicuna-7b-v1.3', tokenizer='lmsys/vicuna-7b-v1.3', tokenizer_mode=auto, revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, seed=0) You are using the default legacy behaviour of the . This is expected, and simply means that the `legacy` (previous) behavior will be used so nothing changes for you. If you want to use the new behaviour, set `legacy=False`. This should only be set if you understand what it means, and thouroughly read the reason why this was added as explained in https://github.com/hugging...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: :00<00:00, 103kB/s] USER: Hi! How are you? ASSISTANT: Hello! As an artificial intelligence language model, I don't have... ``` Same with staring the OpenAI server with Fastchat, everything works correctly. I am using NV...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: using WSL2 and trying to start OpenAI server with `lmsys/vicuna-7b-v1.3` model using the following command: ```{shell} python -m vllm.entrypoints.openai.api_server --model lmsys/vicuna-7b-v1.3 --gpu-memory-utilization 0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: .api_server --model lmsys/vicuna-7b-v1.3 --gpu-memory-utilization 0.98 --dtype half ``` After loading the model it takes ~5-6 min of waiting until I get the **ValueError: No available memory for the cache blocks**: ```...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ython3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.3 --device cuda You are using the default legacy behaviour of the . This is expected, and simply means that the `legacy` (previous) behavior will be used so n...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: Vicuna-7b-v1.3 OOM with vLLM but working with Fastchat I am using WSL2 and trying to start OpenAI server with `lmsys/vicuna-7b-v1.3` model using the following command: ```{shell} python -m vllm.entrypoints.openai.api_se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
