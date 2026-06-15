# vllm-project/vllm#15056: [Bug]: [Minor] Forking happens after the creation of tokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#15056](https://github.com/vllm-project/vllm/issues/15056) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Minor] Forking happens after the creation of tokenizer

### Issue 正文摘录

### Your current environment When testing prefix caching on TPU, we got the following in the log: ```text huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks... To disable this warning, you can either: - Avoid using `tokenizers` before the fork if possible - Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false) … ``` ```text Command to reproduce: _VLLM_USE_V1=1 python benchmark_prefix_caching.py --model meta-llama/Llama-3.1-8B-Instruct --dataset-path ~/data/ShareGPT_V3_unfiltered_cleaned_split.json --enable-prefix-caching --num-prompts 20 --repeat-count 5 --input-length-range 128:256 --gpu-memory-utilization 0.95 --max-model-len 2048 ``` The output of `python collect_env.py` ### 🐛 Describe the bug When testing prefix caching on TPU, we got the following in the log: ```text huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks... To disable this warning, you can either: - Avoid using `tokenizers` before the fork if possible - Explicitly set the environment variable TOKENIZERS_PARAL...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: either: - Avoid using `tokenizers` before the fork if possible - Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false) … ``` ```text Command to reproduce: _VLLM_USE_V1=1 python benchmark_prefix_c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: gingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks... To disable this warning, you can either: - Avoid using `tokenizers` before t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: testing prefix caching on TPU, we got the following in the log: ```text huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks... T...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: after parallelism has already been used. Disabling parallelism to avoid deadlocks... To disable this warning, you can either: - Avoid using `tokenizers` before the fork if possible - Explicitly set the environment varia...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: s after the creation of tokenizer bug ### Your current environment When testing prefix caching on TPU, we got the following in the log: ```text huggingface/tokenizers: The current process just got forked, after parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
