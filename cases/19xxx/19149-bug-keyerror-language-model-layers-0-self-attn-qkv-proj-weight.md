# vllm-project/vllm#19149: [Bug]: KeyError: 'language_model.layers.0.self_attn.qkv_proj.weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#19149](https://github.com/vllm-project/vllm/issues/19149) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: KeyError: 'language_model.layers.0.self_attn.qkv_proj.weight'

### Issue 正文摘录

### Your current environment ## My Environment torch 2.6.0 torchaudio 2.6.0 torchvision 0.21.0 transformers 4.52.4 transformers-stream-generator 0.0.5 vllm 0.8.5 ### 🐛 Describe the bug I use ms-swift to GRPO Qwen2.5-VL-3B model. The error message show as follow: ``` Traceback (most recent call last): File "/mdata/llh/Projects/ms-swift/swift/cli/rlhf.py", line 5, in rlhf_main() File "/mdata/llh/Projects/ms-swift/swift/llm/train/rlhf.py", line 169, in rlhf_main return SwiftRLHF(args).main() ^^^^^^^^^^^^^^^^^^^^^^ File "/mdata/llh/Projects/ms-swift/swift/llm/base.py", line 49, in main result = self.run() ^^^^^^^^^^ File "/mdata/llh/Projects/ms-swift/swift/llm/train/sft.py", line 123, in run return self.train(trainer) ^^^^^^^^^^^^^^^^^^^ File "/mdata/llh/Projects/ms-swift/swift/llm/train/sft.py", line 184, in train trainer.train(trainer.args.resume_from_checkpoint) File "/mdata/llh/Projects/ms-swift/swift/trainers/mixin.py", line 369, in train res = super().train(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/mdata/llh/miniconda3/envs/swift/lib/python3.11/site-packages/transformers/trainer.py", line 2240, in train return inner_training_loop( ^^^^^^^^^^^^^^^^^^^^ File "/mdata/l...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: KeyError: 'language_model.layers.0.self_attn.qkv_proj.weight' bug;stale ### Your current environment ## My Environment torch 2.6.0 torchaudio 2.6.0 torchvision
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: /mdata/llh/miniconda3/envs/swift/lib/python3.11/site-packages/trl/extras/profiling.py", line 96, in wrapper return func(self, *args, **kwargs)
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: KeyError: 'language_model.layers.0.self_attn.qkv_proj.weight' bug;stale ### Your current environment ## My Environment torch 2.6.0 torchaudio 2.6.0 torchvision 0.21.0 transformers

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
