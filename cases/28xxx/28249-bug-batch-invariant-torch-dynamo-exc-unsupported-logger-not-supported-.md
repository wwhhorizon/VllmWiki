# vllm-project/vllm#28249: [Bug]: Batch invariant `torch.dynamo.exc.Unsupported: Logger not supported for non-export cases`

| 字段 | 值 |
| --- | --- |
| Issue | [#28249](https://github.com/vllm-project/vllm/issues/28249) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Batch invariant `torch.dynamo.exc.Unsupported: Logger not supported for non-export cases`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash export VLLM_ATTENTION_BACKEND="FLASH_ATTN_MLA" export VLLM_BATCH_INVARIANT=1 vllm serve deepseek-ai/DeepSeek-V3.1 -dp 8 --enable-expert-parallel --port 9256 ``` And we will see the error ```bash (EngineCore_DP0 pid=1251450) torch._dynamo.exc.Unsupported: Logger not supported for non-export cases. To avoid graph breaks caused by logger in compile-mode, it is recommended to disable logging by adding logging methods to config.ignore_logger_methods (EngineCore_DP0 pid=1251450) (EngineCore_DP0 pid=1251450) from user code: (EngineCore_DP0 pid=1251450) File "/home/yewentao256/vllm-source/vllm/model_executor/models/deepseek_v2.py", line 1164, in forward (EngineCore_DP0 pid=1251450) hidden_states, residual = layer(positions, hidden_states, residual) (EngineCore_DP0 pid=1251450) File "/home/yewentao256/vllm-source/vllm/model_executor/models/deepseek_v2.py", line 1062, in forward (EngineCore_DP0 pid=1251450) hidden_states = self.self_attn( (EngineCore_DP0 pid=1251450) File "/home/yewentao256/vllm-source/vllm/model_executor/models/deepseek_v2.py", line 973, in forward (EngineCore_DP0 pid=1251450) return self.mla_attn(positions, hidde...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 565, in forward (EngineCore_DP0 pid=1251450) output_parallel = self.quant_method.apply(self, input_, bias) (EngineCore_DP0 pid=1251450) File "/home/yewentao256/vllm-source/vllm/model_executor/layers/quantization/fp8.py"...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: nt environment ### 🐛 Describe the bug ```bash export VLLM_ATTENTION_BACKEND="FLASH_ATTN_MLA" export VLLM_BATCH_INVARIANT=1 vllm serve deepseek-ai/DeepSeek-V3.1 -dp 8 --enable-expert-parallel --port 9256 ``` And we will...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: -mode, it is recommended to disable logging by adding logging methods to config.ignore_logger_methods (EngineCore_DP0 pid=1251450) (EngineCore_DP0 pid=1251450) from user code: (EngineCore_DP0 pid=1251450) File "/home/ye...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: upported for non-export cases. To avoid graph breaks caused by logger in compile-mode, it is recommended to disable logging by adding logging methods to config.ignore_logger_methods (EngineCore_DP0 pid=1251450) (EngineC...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
