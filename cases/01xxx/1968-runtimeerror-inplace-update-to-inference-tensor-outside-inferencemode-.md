# vllm-project/vllm#1968: RuntimeError: Inplace update to inference tensor outside InferenceMode is not allowed.You can make a clone to get a normal tensor before doing inplace update.See https://github.com/pytorch/rfcs/pull/17 for more details.

| 字段 | 值 |
| --- | --- |
| Issue | [#1968](https://github.com/vllm-project/vllm/issues/1968) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 | crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> RuntimeError: Inplace update to inference tensor outside InferenceMode is not allowed.You can make a clone to get a normal tensor before doing inplace update.See https://github.com/pytorch/rfcs/pull/17 for more details.

### Issue 正文摘录

1*8H100 DGX BOX Torch version: 2.1.1 CUDA version: 12.1 VLLM: 0.2.3 The inference works just fine in tensor parallel 1 but when using **tp > 1** I am getting this error below: WARNING 12-07 18:20:11 tokenizer.py:79] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast tokenizer instead. Traceback (most recent call last): File "/usr/local/bin/lm_eval", line 33, in sys.exit(load_entry_point('lm-eval', 'console_scripts', 'lm_eval')()) File "/data/users/ravi/experiments/summarization-research/FastChat/lm-evaluation-harness/lm_eval/__main__.py", line 207, in cli_evaluate results = evaluator.simple_evaluate( File "/data/users/ravi/experiments/summarization-research/FastChat/lm-evaluation-harness/lm_eval/utils.py", line 402, in _wrapper return fn(*args, **kwargs) File "/data/users/ravi/experiments/summarization-research/FastChat/lm-evaluation-harness/lm_eval/evaluator.py", line 102, in simple_evaluate lm = lm_eval.api.registry.get_model(model).create_from_arg_string( File "/data/users/ravi/experiments/summarization-research/FastChat/lm-evaluation-harness/lm_eval/api/model.py", line 136, in create_from_arg_string return cls(**args, **args2) File "/data/us...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e.See https://github.com/pytorch/rfcs/pull/17 for more details. stale 1*8H100 DGX BOX Torch version: 2.1.1 CUDA version: 12.1 VLLM: 0.2.3 The inference works just fine in tensor parallel 1 but when using **tp > 1** I am...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ator.py", line 102, in simple_evaluate lm = lm_eval.api.registry.get_model(model).create_from_arg_string( File "/data/users/ravi/experiments/summarization-research/FastChat/lm-evaluation-harness/lm_eval/api/model.py", l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: b.com/pytorch/rfcs/pull/17 for more details. stale 1*8H100 DGX BOX Torch version: 2.1.1 CUDA version: 12.1 VLLM: 0.2.3 The inference works just fine in tensor parallel 1 but when using **tp > 1** I am getting this error...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: er instead. Traceback (most recent call last): File "/usr/local/bin/lm_eval", line 33, in sys.exit(load_entry_point('lm-eval', 'console_scripts', 'lm_eval')()) File "/data/users/ravi/experiments/summarization-research/F...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: search/vllm/vllm/engine/llm_engine.py", line 208, in _init_cache num_blocks = self._run_workers( File "/data/users/ravi/experiments/summarization-research/vllm/vllm/engine/llm_engine.py", line 750, in _run_workers self....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
