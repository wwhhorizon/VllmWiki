# vllm-project/vllm#27237: [Bug]: qwen3-vl-30B FSDP with 'Parameter' object has no attribute 'weight_loader'

| 字段 | 值 |
| --- | --- |
| Issue | [#27237](https://github.com/vllm-project/vllm/issues/27237) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen3-vl-30B FSDP with 'Parameter' object has no attribute 'weight_loader'

### Issue 正文摘录

### Your current environment I got the error: AttributeError: 'Parameter' object has no attribute 'weight_loader' In the line: vllm/vllm/model_executor/models/qwen3_vl_moe.py weight_loader = typing.cast(Callable[..., bool], param.weight_loader) The vllm version is: 0.11.0 Verl commit is: 53aed3eea159cdec3842f3281295e52417e77f68 ### 🐛 Describe the bug ``` File "qwen3vl/verl/verl/workers/rollout/vllm_rollout/vllm_rollout_spmd.py", line 463, in update_weights [36m(TaskRunner pid=2151633)[0m model.load_weights(weights) [36m(TaskRunner pid=2151633)[0m File "qwen3vl/vllm/vllm/model_executor/models/qwen3_vl.py", line 1603, in load_weights [36m(TaskRunner pid=2151633)[0m return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper) [36m(TaskRunner pid=2151633)[0m ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [36m(TaskRunner pid=2151633)[0m File "qwen3vl/vllm/vllm/model_executor/models/utils.py", line 294, in load_weights [36m(TaskRunner pid=2151633)[0m autoloaded_weights = set(self._load_module("", self.module, weights)) [36m(TaskRunner pid=2151633)[0m ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [36m(TaskRunner pid=2151633)[0m File "qwen3vl/vllm/vll...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: qwen3-vl-30B FSDP with 'Parameter' object has no attribute 'weight_loader' bug ### Your current environment I got the error: AttributeError: 'Parameter' object has no attribute 'weight_loader' In the line: vllm/v...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: e 'weight_loader' In the line: vllm/vllm/model_executor/models/qwen3_vl_moe.py weight_loader = typing.cast(Callable[..., bool], param.weight_loader) The vllm version is: 0.11.0 Verl commit is: 53aed3eea159cdec3842f32812...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: loader = typing.cast(Callable[..., bool], param.weight_loader) The vllm version is: 0.11.0 Verl commit is: 53aed3eea159cdec3842f3281295e52417e77f68 ### 🐛 Describe the bug ``` File "qwen3vl/verl/verl/workers/rollout/vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
