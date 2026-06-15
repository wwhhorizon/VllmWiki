# vllm-project/vllm#25604: [Bug]: Dynamo Unsupported due to `BasevLLMParameter.torch_function` calling disabled super()

| 字段 | 值 |
| --- | --- |
| Issue | [#25604](https://github.com/vllm-project/vllm/issues/25604) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Dynamo Unsupported due to `BasevLLMParameter.torch_function` calling disabled super()

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm bench throughput --model Qwen/Qwen3-30B-A3B-FP8 --load-format dummy --input-len 1000 --output-len 100 --trust_remote_code --enable-expert-parallel` ```bash (EngineCore_DP0 pid=2439401) self.run() (EngineCore_DP0 pid=2439401) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_DP0 pid=2439401) self._target(*self._args, **self._kwargs) (EngineCore_DP0 pid=2439401) File "/home/wentao/vllm-source/vllm/v1/engine/core.py", line 712, in run_engine_core (EngineCore_DP0 pid=2439401) raise e (EngineCore_DP0 pid=2439401) File "/home/wentao/vllm-source/vllm/v1/engine/core.py", line 695, in run_engine_core (EngineCore_DP0 pid=2439401) engine_core = DPEngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=2439401) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=2439401) File "/home/wentao/vllm-source/vllm/v1/engine/core.py", line 965, in __init__ (EngineCore_DP0 pid=2439401) super().__init__(vllm_config, local_client, handshake_address, (EngineCore_DP0 pid=2439401) File "/home/wentao/vllm-source/vllm/v1/engine/core.py", line 498, in __init__ (EngineCore_DP0 pid=2439401) super().__init__(vllm_config, exe...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: current environment ### 🐛 Describe the bug `vllm bench throughput --model Qwen/Qwen3-30B-A3B-FP8 --load-format dummy --input-len 1000 --output-len 100 --trust_remote_code --enable-expert-parallel` ```bash (EngineCore_DP...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: bug ### Your current environment ### 🐛 Describe the bug `vllm bench throughput --model Qwen/Qwen3-30B-A3B-FP8 --load-format dummy --input-len 1000 --output-len 100 --trust_remote_code --enable-expert-parallel` ```bash (...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: mat dummy --input-len 1000 --output-len 100 --trust_remote_code --enable-expert-parallel` ```bash (EngineCore_DP0 pid=2439401) self.run() (EngineCore_DP0 pid=2439401) File "/usr/lib/python3.12/multiprocessing/process.py...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ## 🐛 Describe the bug `vllm bench throughput --model Qwen/Qwen3-30B-A3B-FP8 --load-format dummy --input-len 1000 --output-len 100 --trust_remote_code --enable-expert-parallel` ```bash (EngineCore_DP0 pid=2439401) self.r...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: s/linear.py", line 236, in apply (EngineCore_DP0 pid=2439401) return dispatch_unquantized_gemm()(layer, x, layer.weight, bias) (EngineCore_DP0 pid=2439401) File "/home/wentao/vllm-source/vllm/model_executor/layers/utils...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
