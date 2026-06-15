# vllm-project/vllm#3292: lm-evaluation-harness broken on master

| 字段 | 值 |
| --- | --- |
| Issue | [#3292](https://github.com/vllm-project/vllm/issues/3292) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> lm-evaluation-harness broken on master

### Issue 正文摘录

Since https://github.com/vllm-project/vllm/pull/3065, the eval suite https://github.com/EleutherAI/lm-evaluation-harness is broken. Repro (this should be run on 2 A100s or H100s to make sure the Mixtral model fits into GPU memory): ```shell # First install vllm from master via https://docs.vllm.ai/en/latest/getting_started/installation.html#build-from-source # Then clone an install https://github.com/EleutherAI/lm-evaluation-harness git clone https://github.com/EleutherAI/lm-evaluation-harness cd lm-evaluation-harness pip install -e . # Now run the evaluation harness lm_eval --model vllm --model_args pretrained=mistralai/Mixtral-8x7B-Instruct-v0.1,tensor_parallel_size=2 --tasks mmlu --num_fewshot 5 ``` This fails with ```python File "/home/ray/anaconda3/bin/lm_eval", line 8, in sys.exit(cli_evaluate()) File "/home/ray/default/lm-evaluation-harness/lm_eval/__main__.py", line 318, in cli_evaluate results = evaluator.simple_evaluate( File "/home/ray/default/lm-evaluation-harness/lm_eval/utils.py", line 288, in _wrapper return fn(*args, **kwargs) File "/home/ray/default/lm-evaluation-harness/lm_eval/evaluator.py", line 230, in simple_evaluate results = evaluate( File "/home/ray/defaul...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: to make sure the Mixtral model fits into GPU memory): ```shell # First install vllm from master via https://docs.vllm.ai/en/latest/getting_started/installation.html#build-from-source # Then clone an install https://gith...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: utherAI/lm-evaluation-harness is broken. Repro (this should be run on 2 A100s or H100s to make sure the Mixtral model fits into GPU memory): ```shell # First install vllm from master via https://docs.vllm.ai/en/latest/g...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: lm-evaluation-harness broken on master stale Since https://github.com/vllm-project/vllm/pull/3065, the eval suite https://github.com/EleutherAI/lm-evaluation-harness is broken. Repro (this should be run on 2 A100s or H1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: lm-evaluation-harness broken on master stale Since https://github.com/vllm-project/vllm/pull/3065, the eval suite https://github.com/EleutherAI/lm-evaluation-harness is broken. Repro (this should be run on 2 A100s or H1...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ould be run on 2 A100s or H100s to make sure the Mixtral model fits into GPU memory): ```shell # First install vllm from master via https://docs.vllm.ai/en/latest/getting_started/installation.html#build-from-source # Th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
