# vllm-project/vllm#23577: [Bug]: default_weight_loader receives unexpected `weight_name` kwarg in GPT-OSS load_weights

| 字段 | 值 |
| --- | --- |
| Issue | [#23577](https://github.com/vllm-project/vllm/issues/23577) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: default_weight_loader receives unexpected `weight_name` kwarg in GPT-OSS load_weights

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using TRL's `GRPOTrainer` with `use_vllm: true` and `vllm_mode: colocate` on `openai/gpt-oss-20b`, training immediately fails with: ``` [rank2]: File "/app/scripts/trl_methods/grpo_entry.py", line 640, in main [rank2]: trainer.train() [rank2]: File "/usr/local/lib/python3.12/dist-packages/transformers/trainer.py", line 2238, in train [rank2]: return inner_training_loop( [rank2]: ^^^^^^^^^^^^^^^^^^^^ [rank2]: File "/usr/local/lib/python3.12/dist-packages/transformers/trainer.py", line 2582, in _inner_training_loop [rank2]: tr_loss_step = self.training_step(model, inputs, num_items_in_batch) [rank2]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank2]: File "/usr/local/lib/python3.12/dist-packages/transformers/trainer.py", line 3790, in training_step [rank2]: inputs = self._prepare_inputs(inputs) [rank2]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank2]: File "/usr/local/lib/python3.12/dist-packages/trl/extras/profiling.py", line 98, in wrapper [rank2]: return func(self, *args, **kwargs) [rank2]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank2]: File "/usr/local/lib/python3.12/dist-packages/trl/trainer/grpo_trainer.py", line 1279, in _prepar...

## 现有链接修复摘要

#20988 [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | #25694 [GPT-OSS] Save `extra_weight_attrs` and use at `load_weights` time for Marlin kernel

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ument 'weight_name' ``` Minimal Repro Script ```python from transformers import AutoModelForCausalLM, AutoTokenizer from trl import GRPOTrainer, GRPOConfig import torch model = AutoModelForCausalLM.from_pretrained( "ope...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: from_pretrained( "openai/gpt-oss-20b", trust_remote_code=True, torch_dtype=torch.bfloat16 ) tokenizer = AutoTokenizer.from_pretrained("openai/gpt-oss-20b", trust_remote_code=True) training_args = GRPOConfig( output_dir=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: or. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: default_weight_loader receives unexpected `weight_name` kwarg in GPT-OSS load_weights bug;stale ### Your current environment ### 🐛 Describe the bug When using TRL's `GRPOTrainer` with `use_vllm: true` and `vllm_m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ader receives unexpected `weight_name` kwarg in GPT-OSS load_weights bug;stale ### Your current environment ### 🐛 Describe the bug When using TRL's `GRPOTrainer` with `use_vllm: true` and `vllm_mode: colocate` on `opena...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20988](https://github.com/vllm-project/vllm/pull/20988) | mentioned | 0.6 | [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | [installation] 28. #23578: [Installation]:... [installation] 29. #23577: [Bug]: default_weight_loader receives unexpected `weight_nam... [bug] 30. #23575: [Feature]: Add usage in |
| [#25694](https://github.com/vllm-project/vllm/pull/25694) | mentioned | 0.6 | [GPT-OSS] Save `extra_weight_attrs` and use at `load_weights` time for Marlin kernel | lt On the latest vllm version, this will fail with the same error in #23577 . With the fixes in this PR, the script runs successfully. ### Generations before weight loading ```bas… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
