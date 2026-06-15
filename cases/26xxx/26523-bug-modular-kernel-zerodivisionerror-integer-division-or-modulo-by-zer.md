# vllm-project/vllm#26523: [Bug]: modular_kernel: ZeroDivisionError: integer division or modulo by zero

| 字段 | 值 |
| --- | --- |
| Issue | [#26523](https://github.com/vllm-project/vllm/issues/26523) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: modular_kernel: ZeroDivisionError: integer division or modulo by zero

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm serve deepseek-ai/DeepSeek-R1 -dp 8 --enable-expert-parallel --port 9256 --max_num_seqs 128 --enforce_eager` Then `curl -sS -i -H 'Content-Type: application/json' -X POST http://127.0.0.1:9256/v1/completions -d '{"model":"deepseek-ai/DeepSeek-R1","prompt":"Hello","max_tokens":10}'` Will trigger ```bash (EngineCore_DP5 pid=2911124) File "/home/wentao/vllm-source/vllm/model_executor/layers/quantization/fp8.py", line 1216, in apply (EngineCore_DP6 pid=2911125) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP5 pid=2911124) result = self.fused_experts( (EngineCore_DP6 pid=2911125) File "/home/wentao/vllm-source/vllm/model_executor/layers/fused_moe/layer.py", line 2051, in forward_cuda (EngineCore_DP5 pid=2911124) ^^^^^^^^^^^^^^^^^^^ (EngineCore_DP6 pid=2911125) return self.forward_native(hidden_states, router_logits) (EngineCore_DP5 pid=2911124) File "/home/wentao/.venv/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl (EngineCore_DP6 pid=2911125) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP5 pid=2911124) return self._call_impl(*args, **kwargs) (EngineCore_DP6 pid=...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: # 🐛 Describe the bug `vllm serve deepseek-ai/DeepSeek-R1 -dp 8 --enable-expert-parallel --port 9256 --max_num_seqs 128 --enforce_eager` Then `curl -sS -i -H 'Content-Type: application/json' -X POST http://127.0.0.1:9256...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: pid=2911124) File "/home/wentao/vllm-source/vllm/model_executor/layers/quantization/fp8.py", line 1216, in apply (EngineCore_DP6 pid=2911125) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP5 pid=2911124) result = s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ce/vllm/model_executor/layers/fused_moe/layer.py", line 2051, in forward_cuda (EngineCore_DP5 pid=2911124) ^^^^^^^^^^^^^^^^^^^ (EngineCore_DP6 pid=2911125) return self.forward_native(hidden_states, router_logits) (Engin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: pe: application/json' -X POST http://127.0.0.1:9256/v1/completions -d '{"model":"deepseek-ai/DeepSeek-R1","prompt":"Hello","max_tokens":10}'` Will trigger ```bash (EngineCore_DP5 pid=2911124) File "/home/wentao/vllm-sou...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
