# vllm-project/vllm#24751: [Bug]: torch._inductor.exc.InductorError: AssertionError: (TensorBox(StorageBox(...)))

| 字段 | 值 |
| --- | --- |
| Issue | [#24751](https://github.com/vllm-project/vllm/issues/24751) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;moe;quantization |
| 子分类 | throughput |
| Operator 关键词 | cuda;fp8;gemm;moe;operator |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch._inductor.exc.InductorError: AssertionError: (TensorBox(StorageBox(...)))

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ` VLLM_USE_DEEP_GEMM=1 vllm bench throughput --model Qwen/Qwen3-30B-A3B-FP8 --load-format dummy --input-len 1000 --output-len 100 --trust_remote_code --enable-expert-parallel` ```bash (EngineCore_DP0 pid=2639023) File "/home/wentao/.venv/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl (EngineCore_DP0 pid=2639023) return self._call_impl(*args, **kwargs) (EngineCore_DP0 pid=2639023) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=2639023) File "/home/wentao/.venv/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl (EngineCore_DP0 pid=2639023) return forward_call(*args, **kwargs) (EngineCore_DP0 pid=2639023) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=2639023) File "/home/wentao/vllm-source/vllm/model_executor/models/qwen3_moe.py", line 682, in forward (EngineCore_DP0 pid=2639023) hidden_states = self.model(input_ids, positions, intermediate_tensors, (EngineCore_DP0 pid=2639023) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=2639023) File "/home/wentao/vllm-source/vllm/compilation/decorators.py", line 305, in __call__ (En...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ` VLLM_USE_DEEP_GEMM=1 vllm bench throughput --model Qwen/Qwen3-30B-A3B-FP8 --load-format dummy --input-len 1000 --output-len 100 --trust_remote_code --enable-expert-parallel` ```bash (EngineCore_DP0 pid=2639023) File "...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: y", line 305, in __call__ (EngineCore_DP0 pid=2639023) output = self.compiled_callable(*args, **kwargs) (EngineCore_DP0 pid=2639023) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=2639023) File "/home/wenta...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ### 🐛 Describe the bug ` VLLM_USE_DEEP_GEMM=1 vllm bench throughput --model Qwen/Qwen3-30B-A3B-FP8 --load-format dummy --input-len 1000 --output-len 100 --trust_remote_code --enable-expert-parallel` ```bash (EngineCore_...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ### Your current environment ### 🐛 Describe the bug ` VLLM_USE_DEEP_GEMM=1 vllm bench throughput --model Qwen/Qwen3-30B-A3B-FP8 --load-format dummy --input-len 1000 --output-len 100 --trust_remote_code --enable-expert-p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: nvironment ### 🐛 Describe the bug ` VLLM_USE_DEEP_GEMM=1 vllm bench throughput --model Qwen/Qwen3-30B-A3B-FP8 --load-format dummy --input-len 1000 --output-len 100 --trust_remote_code --enable-expert-parallel` ```bash (...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
