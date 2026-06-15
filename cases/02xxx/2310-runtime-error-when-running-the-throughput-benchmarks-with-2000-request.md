# vllm-project/vllm#2310: Runtime Error When Running the Throughput Benchmarks WIth 2000 Requests (Invalid Token Generated) (Model: OPT-2.7B, Dataset: SharedGPT)

| 字段 | 值 |
| --- | --- |
| Issue | [#2310](https://github.com/vllm-project/vllm/issues/2310) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Runtime Error When Running the Throughput Benchmarks WIth 2000 Requests (Invalid Token Generated) (Model: OPT-2.7B, Dataset: SharedGPT)

### Issue 正文摘录

When running the throughput benchmark on the OPT-2.7B model on the SharedGPT dataset (2000 requests), a None token is generated, incurring a runtime error within the de-tokenizer. The ID of the problematic token is 50265 while the vocab size of the OPT tokenizer is only 50265. Reproduce the bug: ```bash python benchmark_throughput.py --backend vllm --dataset ../ShareGPT_V3_unfiltered_cleaned_split.json --model facebook/opt-2.7b --num-prompts 2000 ``` The logging output: ```bash Namespace(backend='vllm', dataset='../ShareGPT_V3_unfiltered_cleaned_split.json', dtype='auto', enforce_eager=False, hf_max_batch_size=None, input_len=None, max_model_len=None, model='facebook/opt-2.7b', n=1, num_prompts=2000, output_len=None, quantization=None, seed=0, tensor_parallel_size=1, tokenizer='facebook/opt-2.7b', trust_remote_code=False, use_beam_search=False) INFO 12-30 22:13:01 llm_engine.py:73] Initializing an LLM engine with config: model='facebook/opt-2.7b', tokenizer='facebook/opt-2.7b', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, e...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: the Throughput Benchmarks WIth 2000 Requests (Invalid Token Generated) (Model: OPT-2.7B, Dataset: SharedGPT) When running the throughput benchmark on the OPT-2.7B model on the SharedGPT dataset (2000 requests), a None t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Runtime Error When Running the Throughput Benchmarks WIth 2000 Requests (Invalid Token Generated) (Model: OPT-2.7B, Dataset: SharedGPT) When running the throughput benchmark on the OPT-2.7B model on the SharedGPT datase...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: (backend='vllm', dataset='../ShareGPT_V3_unfiltered_cleaned_split.json', dtype='auto', enforce_eager=False, hf_max_batch_size=None, input_len=None, max_model_len=None, model='facebook/opt-2.7b', n=1, num_prompts=2000, o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ze=1, tokenizer='facebook/opt-2.7b', trust_remote_code=False, use_beam_search=False) INFO 12-30 22:13:01 llm_engine.py:73] Initializing an LLM engine with config: model='facebook/opt-2.7b', tokenizer='facebook/opt-2.7b'...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: either: - Avoid using `tokenizers` before the fork if possible - Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false) huggingface/tokenizers: The current process just got forked, after paralleli...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
