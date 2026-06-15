# vllm-project/vllm#11238: [New Model]: Support Phi-4

| 字段 | 值 |
| --- | --- |
| Issue | [#11238](https://github.com/vllm-project/vllm/issues/11238) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Support Phi-4

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The upcoming Phi-4 is already available: https://huggingface.co/matteogeniaccio/phi-4/tree/main/phi-4 The benchmarks are great. ### Alternatives _No response_ ### Additional context Currently, it fails with the latest vllm: ``` [rank0]: Traceback (most recent call last): [rank0]: File "/root/mcts_methods/entropy-evals/eval_vanila.py", line 211, in [rank0]: fire.Fire(AnswerPredictor) [rank0]: File "/root/miniconda3/envs/blueberry/lib/python3.11/site-packages/fire/core.py", line 135, in Fire [rank0]: component_trace = _Fire(component, args, parsed_flag_args, context, name) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/root/miniconda3/envs/blueberry/lib/python3.11/site-packages/fire/core.py", line 468, in _Fire [rank0]: component, remaining_args = _CallAndUpdateTrace( [rank0]: ^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/root/miniconda3/envs/blueberry/lib/python3.11/site-packages/fire/core.py", line 684, in _CallAndUpdateTrace [rank0]: component = fn(*varargs, **kwargs) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/root/mcts_methods/entropy-evals/eval_vanila.py", line 51, in __init__ [rank0]: model = PiecewiseSampli...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: Support Phi-4 new-model ### 🚀 The feature, motivation and pitch The upcoming Phi-4 is already available: https://huggingface.co/matteogeniaccio/phi-4/tree/main/phi-4 The benchmarks are great. ### Alternativ...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: lable: https://huggingface.co/matteogeniaccio/phi-4/tree/main/phi-4 The benchmarks are great. ### Alternatives _No response_ ### Additional context Currently, it fails with the latest vllm: ``` [rank0]: Traceback (most...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: upcoming Phi-4 is already available: https://huggingface.co/matteogeniaccio/phi-4/tree/main/phi-4 The benchmarks are great. ### Alternatives _No response_ ### Additional context Currently, it fails with the latest vllm:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: /vllm/model_executor/models/utils.py", line 510, in [rank0]: maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}")) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/root/miniconda3/envs/blueberry/lib/python...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
