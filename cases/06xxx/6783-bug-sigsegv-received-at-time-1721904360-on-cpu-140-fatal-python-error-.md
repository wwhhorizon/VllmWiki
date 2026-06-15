# vllm-project/vllm#6783: [Bug]: SIGSEGV received at time=1721904360 on cpu 140, Fatal Python error: Segmentation fault

| 字段 | 值 |
| --- | --- |
| Issue | [#6783](https://github.com/vllm-project/vllm/issues/6783) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;gemm_linear;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: SIGSEGV received at time=1721904360 on cpu 140, Fatal Python error: Segmentation fault

### Issue 正文摘录

### Your current environment My environment setup involving two 8xH100 nodes is detailed in https://github.com/vllm-project/vllm/issues/6775; therefore, I will omit it here for brevity. ### 🐛 Describe the bug I am trying to run `lm-evaluation-harness` with `vllm` as the backend. The evaluation should run either with TP=16 or with TP=8 + PP=2. The problem I am facing happens after I run this command: ```bash lm_eval \ --model vllm \ --model_args pretrained="meta-llama/Meta-Llama-3.1-8B-Instruct",dtype=auto,gpu_memory_utilization=0.8,add_bos_token=True,max_model_len=2048,tensor_parallel_size=16,distributed_executor_backend="ray" \ --tasks winogrande \ --num_fewshot 5 \ --batch_size auto \ --device cuda ``` and it looks like this: ```bash INFO 07-25 10:44:52 llm_engine.py:176] Initializing an LLM engine (v0.5.3.post1) with config: model='/home/meta-llama/Meta-Llama-3-8B-Instruct', speculative_config=None, tokenizer='/home/meta-llama/Meta-Llama-3-8B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=2048, download_dir=None, load_format=LoadForm...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: vllm \ --model_args pretrained="meta-llama/Meta-Llama-3.1-8B-Instruct",dtype=auto,gpu_memory_utilization=0.8,add_bos_token=True,max_model_len=2048,tensor_parallel_size=16,distributed_executor_backend="ray" \ --tasks win...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: blem I am facing happens after I run this command: ```bash lm_eval \ --model vllm \ --model_args pretrained="meta-llama/Meta-Llama-3.1-8B-Instruct",dtype=auto,gpu_memory_utilization=0.8,add_bos_token=True,max_model_len=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: t time=1721904360 on cpu 140, Fatal Python error: Segmentation fault bug;stale ### Your current environment My environment setup involving two 8xH100 nodes is detailed in https://github.com/vllm-project/vllm/issues/6775...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: n should run either with TP=16 or with TP=8 + PP=2. The problem I am facing happens after I run this command: ```bash lm_eval \ --model vllm \ --model_args pretrained="meta-llama/Meta-Llama-3.1-8B-Instruct",dtype=auto,g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: stale ### Your current environment My environment setup involving two 8xH100 nodes is detailed in https://github.com/vllm-project/vllm/issues/6775; therefore, I will omit it here for brevity. ### 🐛 Describe the bug I am...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
