# vllm-project/vllm#15124: [Bug]: AssertionError - assert loaded_weight.shape[output_dim] == self.org_vocab_size

| 字段 | 值 |
| --- | --- |
| Issue | [#15124](https://github.com/vllm-project/vllm/issues/15124) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError - assert loaded_weight.shape[output_dim] == self.org_vocab_size

### Issue 正文摘录

When I use trl's GRPOTrainer + vllm for training, I encounter the above error and am unable to resolve it. ```python training_args = GRPOConfig( ...... use_vllm=True, vllm_gpu_memory_utilization=0.3, vllm_device="cuda:7", vllm_dtype="bfloat16", vllm_max_model_len=4096, ) ``` ```bash [rank0]: Traceback (most recent call last): [rank0]: File "/xxxxxx/code/GRPO/train_gpro.py", line 80, in [rank0]: trainer.train() [rank0]: File "/opt/conda/lib/python3.10/site-packages/transformers/trainer.py", line 2171, in train [rank0]: return inner_training_loop( [rank0]: File "/opt/conda/lib/python3.10/site-packages/transformers/trainer.py", line 2531, in _inner_training_loop [rank0]: tr_loss_step = self.training_step(model, inputs, num_items_in_batch) [rank0]: File "/opt/conda/lib/python3.10/site-packages/transformers/trainer.py", line 3669, in training_step [rank0]: inputs = self._prepare_inputs(inputs) [rank0]: File "/opt/conda/lib/python3.10/site-packages/trl/trainer/grpo_trainer.py", line 538, in _prepare_inputs [rank0]: self._move_model_to_vllm() [rank0]: File "/opt/conda/lib/python3.10/site-packages/trl/trainer/grpo_trainer.py", line 514, in _move_model_to_vllm [rank0]: llm_model.load_weigh...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;model_support cuda crash dtype;env_dependency;shape When I use trl's GRPOTrainer + vllm for training, I encounter the above error and am...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: vllm_gpu_memory_utilization=0.3, vllm_device="cuda:7", vllm_dtype="bfloat16", vllm_max_model_len=4096, ) ``` ```bash [rank0]: Traceback (most recent call last): [rank0]: File "/xxxxxx/code/GRPO/train_gpro.py", line 80,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e above error and am unable to resolve it. ```python training_args = GRPOConfig( ...... use_vllm=True, vllm_gpu_memory_utilization=0.3, vllm_device="cuda:7", vllm_dtype="bfloat16", vllm_max_model_len=4096, ) ``` ```bash...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: use_vllm=True, vllm_gpu_memory_utilization=0.3, vllm_device="cuda:7", vllm_dtype="bfloat16", vllm_max_model_len=4096, ) ``` ```bash [rank0]: Traceback (most recent call last): [rank0]: File "/xxxxxx/code/GRPO/train_gpro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: rror - assert loaded_weight.shape[output_dim] == self.org_vocab_size bug;stale When I use trl's GRPOTrainer + vllm for training, I encounter the above error and am unable to resolve it. ```python training_args = GRPOCon...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
