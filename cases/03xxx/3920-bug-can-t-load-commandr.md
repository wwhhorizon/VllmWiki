# vllm-project/vllm#3920: [Bug]: Can´t load CommandR+

| 字段 | 值 |
| --- | --- |
| Issue | [#3920](https://github.com/vllm-project/vllm/issues/3920) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support |
| 子分类 | debug |
| Operator 关键词 | attention |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can´t load CommandR+

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug When loading Command R + I get the following error, however I can load and run the model using Huggingface with `device_map="auto"`, also I can use vLLM with other large models, e.g. LLama 70b and Mixtral and it works fine. I am running on a Node with 4x64Gb A100, the GPU might seem strange, these are from the Leonardo Super computer. Is this a known bug or can I somehow fix it? I am runnign with `tensor-parallel-size=4` in lm-eval-harness. ``` vLLM is using nccl==2.18.1 (RayWorkerVllm pid=282131) INFO 04-08 16:24:58 pynccl_utils.py:45] vLLM is using nccl==2.18.1 Traceback (most recent call last): File "/leonardo_scratch/large/userexternal/gpuccett/Repos/llm_newest/conda_venv/bin/lm_eval", line 8, in sys.exit(cli_evaluate()) ^^^^^^^^^^^^^^ File "/leonardo_scratch/large/userexternal/gpuccett/Repos/llm_newest/lm-evaluation-harness/lm_eval/__main__.py", line 341, in cli_evaluate results = evaluator.simple_evaluate( ^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/leonardo_scratch/large/userexternal/gpuccett/Repos/llm_newest/lm-evaluation-harness/lm_eval/utils.py", line 288, in _wrapper return fn(*a...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ng Command R + I get the following error, however I can load and run the model using Huggingface with `device_map="auto"`, also I can use vLLM with other large models, e.g. LLama 70b and Mixtral and it works fine. I am...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ht' (RayWorkerVllm pid=282294) INFO 04-08 16:24:57 selector.py:16] Using FlashAttention backend. [repeated 2x across cluster] (Ray deduplicates logs by default. Set RAY_DEDUP_LOGS=0 to disable log deduplication, or see...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ache;distributed_parallel;frontend_api;model_support attention crash env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ma 70b and Mixtral and it works fine. I am running on a Node with 4x64Gb A100, the GPU might seem strange, these are from the Leonardo Super computer. Is this a known bug or can I somehow fix it? I am runnign with `tens...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: r can I somehow fix it? I am runnign with `tensor-parallel-size=4` in lm-eval-harness. ``` vLLM is using nccl==2.18.1 (RayWorkerVllm pid=282131) INFO 04-08 16:24:58 pynccl_utils.py:45] vLLM is using nccl==2.18.1 Traceba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
