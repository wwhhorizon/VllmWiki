# vllm-project/vllm#20043: [Bug]: Benchmarking using sonnet dataset isn't working for different input and output lens

| 字段 | 值 |
| --- | --- |
| Issue | [#20043](https://github.com/vllm-project/vllm/issues/20043) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Benchmarking using sonnet dataset isn't working for different input and output lens

### Issue 正文摘录

### Your current environment I've created a conda env with py 3.10 and followed the steps from documentation [here](https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html#build-wheel-from-source) to install vLLM venv without compilation. ### 🐛 Describe the bug The output of the following command using default input/output lens for sonnet works ```python benchmarks/benchmark_serving.py --backend openai-chat --base-url="https://api.sambanova.ai/" --dataset-name="sonnet" --dataset_path="./benchmarks/sonnet.txt" --endpoint="v1/chat/completions" --model="meta-llama/Llama-3.3-70B-Instruct" --served_model_name="Meta-Llama-3.3-70B-Instruct" --request-rate=inf --num-prompts=2 --max_concurrency=2 --sonnet-input-len=500 --sonnet-output-len=100``` However, if I change the input/output tokens to other values like the the following, then it doens't work ```python benchmarks/benchmark_serving.py --backend openai-chat --base-url="https://api.sambanova.ai/" --dataset-name="sonnet" --dataset_path="./benchmarks/sonnet.txt" --endpoint="v1/chat/completions" --model="meta-llama/Llama-3.3-70B-Instruct" --served_model_name="Meta-Llama-3.3-70B-Instruct" --request-rate=inf --num-prompts=2 --m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: from documentation [here](https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html#build-wheel-from-source) to install vLLM venv without compilation. ### 🐛 Describe the bug The output of the following comman...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Benchmarking using sonnet dataset isn't working for different input and output lens bug;stale ### Your current environment I've created a conda env with py 3.10 and followed the steps from documentation [here](ht...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ataset_path="./benchmarks/sonnet.txt" --endpoint="v1/chat/completions" --model="meta-llama/Llama-3.3-70B-Instruct" --served_model_name="Meta-Llama-3.3-70B-Instruct" --request-rate=inf --num-prompts=2 --max_concurrency=2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `` INFO 06-24 19:34:21 [__init__.py:244] Automatically detected platform cuda. Namespace(backend='openai-chat', base_url='https://api.sambanova.ai/', host='127.0.0.1', port=8000, endpoint='v1/chat/completions', dataset_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: l='meta-llama/Llama-3.3-70B-Instruct', tokenizer=None, use_beam_search=False, num_prompts=2, logprobs=None, request_rate=inf, burstiness=1.0, seed=0, trust_remote_code=False, disable_tqdm=False, profile=False, save_resu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
