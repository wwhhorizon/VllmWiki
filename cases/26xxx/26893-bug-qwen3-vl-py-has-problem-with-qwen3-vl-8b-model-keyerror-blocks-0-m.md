# vllm-project/vllm#26893: [Bug]: qwen3_vl.py has problem with qwen3-vl-8b model, KeyError: 'blocks.0.mlp.gate_proj.weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#26893](https://github.com/vllm-project/vllm/issues/26893) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen3_vl.py has problem with qwen3-vl-8b model, KeyError: 'blocks.0.mlp.gate_proj.weight'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Trying to finetune qwen3-vl-8b-instruct using grpo_trainer: Got error: [rank2]: File "/home/colligo/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/trainer.py", line 2325, in train [rank2]: return inner_training_loop( [rank2]: ^^^^^^^^^^^^^^^^^^^^ [rank2]: File "/home/colligo/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/trainer.py", line 2674, in _inner_training_loop [rank2]: tr_loss_step = self.training_step(model, inputs, num_items_in_batch) [rank2]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank2]: File "/home/colligo/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/trainer.py", line 4014, in training_step [rank2]: inputs = self._prepare_inputs(inputs) [rank2]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank2]: File "/home/colligo/miniconda3/envs/trl/lib/python3.11/site-packages/trl/extras/profiling.py", line 98, in wrapper [rank2]: return func(self, *args, **kwargs) [rank2]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank2]: File "/home/colligo/miniconda3/envs/trl/lib/python3.11/site-packages/trl/trainer/grpo_trainer.py", line 1076, in _prepare_inputs [rank2]: generation_batch = self._generate_an...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency Your...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: qwen3_vl.py has problem with qwen3-vl-8b model, KeyError: 'blocks.0.mlp.gate_proj.weight' bug ### Your current environment ### 🐛 Describe the bug Trying to finetune qwen3-vl-8b-instruct using grpo_trainer: Got er...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ht' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: home/colligo/miniconda3/envs/trl/lib/python3.11/site-packages/trl/extras/profiling.py", line 98, in wrapper [rank2]: return func(self, *args, **kwargs) [rank2]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank2]: File "/home/colligo/m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: el;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
