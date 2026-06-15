# vllm-project/vllm#5461: [Bug]: Torch2.3 run fail

| 字段 | 值 |
| --- | --- |
| Issue | [#5461](https://github.com/vllm-project/vllm/issues/5461) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Torch2.3 run fail

### Issue 正文摘录

### Your current environment [rank0]: AttributeError: '_OpNamespace' '_C' object has no attribute 'rms_norm' ### 🐛 Describe the bug [rank0]: AttributeError: '_OpNamespace' '_C' object has no attribute 'rms_norm' k0]: File "/usr/local/lib/python3.8/dist-packages/vllm/model_executor/models/qwen2.py", line 202, in forward [rank0]: hidden_states = self.input_layernorm(hidden_states) [rank0]: File "/usr/local/lib/python3.8/dist-packages/torch/nn/modules/module.py", line 1532, in _wrapped_call_impl [rank0]: return self._call_impl(*args, **kwargs) [rank0]: File "/usr/local/lib/python3.8/dist-packages/torch/nn/modules/module.py", line 1541, in _call_impl [rank0]: return forward_call(*args, **kwargs) [rank0]: File "/usr/local/lib/python3.8/dist-packages/vllm/model_executor/custom_op.py", line 13, in forward [rank0]: return self._forward_method(*args, **kwargs) [rank0]: File "/usr/local/lib/python3.8/dist-packages/vllm/model_executor/layers/layernorm.py", line 62, in forward_cuda [rank0]: ops.rms_norm( [rank0]: File "/usr/local/lib/python3.8/dist-packages/vllm/_custom_ops.py", line 132, in rms_norm [rank0]: torch.ops._C.rms_norm(out, input, weight, epsilon) [rank0]: File "/usr/local/lib/pyt...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ute 'rms_norm' k0]: File "/usr/local/lib/python3.8/dist-packages/vllm/model_executor/models/qwen2.py", line 202, in forward [rank0]: hidden_states = self.input_layernorm(hidden_states) [rank0]: File "/usr/local/lib/pyth...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: pe "help", "copyright", "credits" or "license" for more information. >>> import torch torch>>> torch.__version__ '2.3.0'
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t-packages/vllm/model_executor/layers/layernorm.py", line 62, in forward_cuda [rank0]: ops.rms_norm( [rank0]: File "/usr/local/lib/python3.8/dist-packages/vllm/_custom_ops.py", line 132, in rms_norm [rank0]: torch.ops._...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
