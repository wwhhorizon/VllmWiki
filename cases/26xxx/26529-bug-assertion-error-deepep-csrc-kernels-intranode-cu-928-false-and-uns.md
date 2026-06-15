# vllm-project/vllm#26529: [Bug]: Assertion error DeepEP/csrc/kernels/intranode.cu:928: 'false and "Unsupported type"'

| 字段 | 值 |
| --- | --- |
| Issue | [#26529](https://github.com/vllm-project/vllm/issues/26529) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Assertion error DeepEP/csrc/kernels/intranode.cu:928: 'false and "Unsupported type"'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm serve deepseek-ai/DeepSeek-R1 -dp 8 --enable-expert-parallel --port 9256 --max_num_seqs 128 --enforce_eager` And then ```bash curl -sS -i -H 'Content-Type: application/json' -X POST http://127.0.0.1:9256/v1/completions -d '{"model":"deepseek-ai/DeepSeek-R1","prompt":"Hello","max_tokens":10}' ``` We will meet the issue ```bash (EngineCore_DP5 pid=3148182) File "/home/wentao/vllm-source/vllm/v1/worker/gpu_model_runner.py", line 3437, in _dummy_run (EngineCore_DP5 pid=3148182) outputs = self.model( (EngineCore_DP5 pid=3148182) ^^^^^^^^^^^ (EngineCore_DP5 pid=3148182) File "/home/wentao/.venv/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl (EngineCore_DP5 pid=3148182) return self._call_impl(*args, **kwargs) (EngineCore_DP5 pid=3148182) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP5 pid=3148182) File "/home/wentao/.venv/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl (EngineCore_DP5 pid=3148182) return forward_call(*args, **kwargs) (EngineCore_DP5 pid=3148182) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP5 pid=3148182) File "/home/wentao/vllm-source/v...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: # 🐛 Describe the bug `vllm serve deepseek-ai/DeepSeek-R1 -dp 8 --enable-expert-parallel --port 9256 --max_num_seqs 128 --enforce_eager` And then ```bash curl -sS -i -H 'Content-Type: application/json' -X POST http://127...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: forward_impl (EngineCore_DP5 pid=3148182) final_hidden_states = self.quant_method.apply( (EngineCore_DP5 pid=3148182) ^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP5 pid=3148182) File "/home/wentao/vllm-source/vllm/model_execu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ce/vllm/model_executor/layers/fused_moe/layer.py", line 2051, in forward_cuda (EngineCore_DP5 pid=3148182) return self.forward_native(hidden_states, router_logits) (EngineCore_DP5 pid=3148182) ^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ;speculative_decoding cuda;fp8;kernel;moe;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
