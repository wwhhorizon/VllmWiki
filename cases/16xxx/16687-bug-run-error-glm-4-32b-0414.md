# vllm-project/vllm#16687: [Bug]: Run error GLM-4-32B-0414

| 字段 | 值 |
| --- | --- |
| Issue | [#16687](https://github.com/vllm-project/vllm/issues/16687) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Run error GLM-4-32B-0414

### Issue 正文摘录

### Your current environment ERROR 04-16 08:38:03 [core.py:387] RuntimeError: ('Worker failed with error %s, please check the stack trace above for the root cause', 'TypeError : linear(): argument \'input\' (position 1) must be Tensor, not tuple\n\nfrom user code:\n File "/home/cheng/anaconda3/envs/VLLM/lib/python3.12/site-packages/vllm/model_executor/models/llama.py", line 360, in forward\n hidden_states, residual = layer(positions, hidden_states, residual)\n File "/home/cheng/anaconda3/envs/VLLM/lib/python3.12/site-packages/vllm/model_executor/models/glm4.py", line 204, in forward\n hidden_states = self.mlp(hidden_states)\n File "/home/cheng/anaconda3/envs/VLLM/lib/python3.12/site-packages/vllm/model_executor/models/llama.py", line 92, in forward\n x, _ = self.gate_up_proj(x)\n File "/home/cheng/anaconda3/envs/VLLM/lib/python3.12/site-packages/vllm/model_executor/layers/linear.py", line 474, in forward\n output_parallel = self.quant_method.apply(self, input_, bias)\n File "/home/cheng/anaconda3/envs/VLLM/lib/python3.12/site-packages/vllm/model_executor/layers/linear.py", line 191, in apply\n return F.linear(x, layer.weight, bias)\n\nSet TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBO...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: File "/home/cheng/anaconda3/envs/VLLM/lib/python3.12/site-packages/vllm/model_executor/models/llama.py", line 360, in forward\n hidden_states, residual = layer(positions, hidden_states, residual)\n File "/home/cheng/ana...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nYou can suppress this exception and fall back to eager by setting:\n import torch._dynamo\n torch._dynamo.config.suppress_errors = True\n') ERROR 04-16 08:38:03 [core.py:387] CRITICAL 04-16 08:38:03 [core_client.py:359...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: utor/layers/linear.py", line 474, in forward\n output_parallel = self.quant_method.apply(self, input_, bias)\n File "/home/cheng/anaconda3/envs/VLLM/lib/python3.12/site-packages/vllm/model_executor/layers/linear.py", li...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 已杀死 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
