# vllm-project/vllm#25154: [Bug]: AttributeError: 'Parameter' object has no attribute 'load_column_parallel_weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#25154](https://github.com/vllm-project/vllm/issues/25154) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | gemm_linear;model_support |
| 子分类 | wrong_output |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'Parameter' object has no attribute 'load_column_parallel_weight'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python in update_weight [rank4]: self.model_runner.model.load_weights(weights=[(name, weight)]) [rank4]: File "/root/miniconda3/lib/python3.11/site-packages/flash_rl/vllm_patch.py", line 701, in hacked_load_weights [rank4]: updated_params = original_load_weights( [rank4]: ^^^^^^^^^^^^^^^^^^^^^^ [rank4]: File "/root/miniconda3/lib/python3.11/site-packages/vllm/model_executor/models/qwen2_5_vl.py", line 1115, in load_weights [rank4]: return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper) [rank4]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank4]: File "/root/miniconda3/lib/python3.11/site-packages/vllm/model_executor/models/utils.py", line 261, in load_weights [rank4]: autoloaded_weights = set(self._load_module("", self.module, weights)) [rank4]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank4]: File "/root/miniconda3/lib/python3.11/site-packages/vllm/model_executor/models/utils.py", line 222, in _load_module [rank4]: yield from self._load_module(prefix, [rank4]: File "/root/miniconda3/lib/python3.11/site-packages/vllm/model_executor/models/utils.py", line 195, in _load_module [rank4]: loade...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### 🐛 Describe the bug ```python in update_weight [rank4]: self.model_runner.model.load_weights(weights=[(name, weight)]) [rank4]: File "/root/miniconda3/lib/python3.11/site-packages/flash_rl/vllm_patch.py", line 701, i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: t' ``` The code is as follows: ```python from vllm.v1.worker.gpu_worker import Worker as WorkerV1 class WorkerWrapV1(WorkerV1): def update_weight(self, name, dtype, shape, weight, empty_cache=False): # pylint: disable=R...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: WorkerV1 class WorkerWrapV1(WorkerV1): def update_weight(self, name, dtype, shape, weight, empty_cache=False): # pylint: disable=R0917, W0613 assert dtype == self.model_config.dtype, f"mismatch dtype: src {dtype}, dst {...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: isable=R0917, W0613 assert dtype == self.model_config.dtype, f"mismatch dtype: src {dtype}, dst {self.model_config.dtype}" self.model_runner.model.load_weights(weights=[(name, weight)]) del weight if empty_cache: torch....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: disable=R0917, W0613 assert dtype == self.model_config.dtype, f"mismatch dtype: src {dtype}, dst {self.model_config.dtype}" self.model_runner.model.load_weights(weights=[(name, weight)]) del weight if empty_cache: torch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
