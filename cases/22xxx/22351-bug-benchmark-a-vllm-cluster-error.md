# vllm-project/vllm#22351: [Bug]: benchmark a vllm cluster error

| 字段 | 值 |
| --- | --- |
| Issue | [#22351](https://github.com/vllm-project/vllm/issues/22351) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling |
| 症状 | crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: benchmark a vllm cluster error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug (venv) root@kf-gpu-node003:/vllm/benchmarks# python3 benchmark_serving.py \ --backend vllm \ --base-url "http://oai-vllm.traefik.osip.cc" \ --num-prompts 100 \ --model Qwen/Qwen3-14B \ --tokenizer Qwen/Qwen3-14B \ --dataset-name sharegpt \ --max-concurrency 1 \ --trust-remote-code \ --dataset-path ShareGPT_V3_unfiltered_cleaned_split.json INFO 08-06 17:54:56 [__init__.py:235] Automatically detected platform cuda. /vllm/benchmarks/benchmark_serving.py:1298: DeprecationWarning: benchmark_serving.py is deprecated and will be removed in a future version. Please use 'vllm bench serve' instead. main(args) Namespace(backend='vllm', base_url='http://oai-vllm.traefik.osip.cc', host='127.0.0.1', port=8000, endpoint='/v1/completions', dataset_name='sharegpt', dataset_path='ShareGPT_V3_unfiltered_cleaned_split.json', no_stream=False, max_concurrency=1, model='Qwen/Qwen3-14B', tokenizer='Qwen/Qwen3-14B', use_beam_search=False, num_prompts=100, logprobs=None, request_rate=inf, burstiness=1.0, seed=0, trust_remote_code=True, disable_tqdm=False, profile=False, save_result=False, save_detailed=False, append_result=False, metadata=None, result_dir...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: benchmark a vllm cluster error bug ### Your current environment ### 🐛 Describe the bug (venv) root@kf-gpu-node003:/vllm/benchmarks# python3 benchmark_serving.py \ --backend vllm \ --base-url "http://oai-vllm
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ning: benchmark_serving.py is deprecated and will be removed in a future version. Please use 'vllm bench serve' instead. main(args) Namespace(backend='vllm', base_url='http://oai-vllm.traefik.osip.cc', host='127.0.0.1',...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: se-url "http://oai-vllm.traefik.osip.cc" \ --num-prompts 100 \ --model Qwen/Qwen3-14B \ --tokenizer Qwen/Qwen3-14B \ --dataset-name sharegpt \ --max-concurrency 1 \ --trust-remote-code \ --dataset-path ShareGPT_V3_unfil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: on INFO 08-06 17:54:56 [__init__.py:235] Automatically detected platform cuda. /vllm/benchmarks/benchmark_serving.py:1298: DeprecationWarning: benchmark_serving.py is deprecated and will be removed in a future version....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ', dataset_path='ShareGPT_V3_unfiltered_cleaned_split.json', no_stream=False, max_concurrency=1, model='Qwen/Qwen3-14B', tokenizer='Qwen/Qwen3-14B', use_beam_search=False, num_prompts=100, logprobs=None, request_rate=in...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
