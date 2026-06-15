# vllm-project/vllm#36811: [Bug]: CUDA illegal memory access on GPTQ Marlin

| 字段 | 值 |
| --- | --- |
| Issue | [#36811](https://github.com/vllm-project/vllm/issues/36811) |
| 状态 | open |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA illegal memory access on GPTQ Marlin

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Similar to https://github.com/vllm-project/vllm/issues/32834 but observed when running a GPTQ Marlin quantized model. Image used: `vllm/vllm-openai:nightly-76c6e6da08dbe73c2ee0d92dabe01786b44845d2`. ### Server Arguments ``` --model Qwen/Qwen3.5-35B-A3B-GPTQ-Int4 --served-model-name main --max-model-len 8192 --host 0.0.0.0 --port 8080 --language-model-only --enable-auto-tool-choice --tool-call-parser qwen3_coder --reasoning-parser qwen3 --default-chat-template-kwargs {"enable_thinking": false} --max-cudagraph-capture-size 32 --gpu-memory-utilization 0.8 ``` ### Environment Variables ``` VLLM_LOGGING_LEVEL=DEBUG CUDA_LAUNCH_BLOCKING=1 TORCH_USE_CUDA_DSA=1 ``` ### Logs ``` (EngineCore_DP0 pid=121) model_output = self._model_forward( (EngineCore_DP0 pid=121) ^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=121) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_model_runner.py", line 3277, in _model_forward (EngineCore_DP0 pid=121) return self.model( (EngineCore_DP0 pid=121) ^^^^^^^^^^^ (EngineCore_DP0 pid=121) File "/usr/local/lib/python3.12/dist-packages/vllm/compilation/cuda_graph.py", line 342, in __call__ (EngineCore_DP0 p...

## 现有链接修复摘要

#36889 [WIP][Bugfix] Fix CUDA illegal memory access for GPTQ Marlin MoE with CUDA graphs

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;opera...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: m/vllm-project/vllm/issues/32834 but observed when running a GPTQ Marlin quantized model. Image used: `vllm/vllm-openai:nightly-76c6e6da08dbe73c2ee0d92dabe01786b44845d2`. ### Server Arguments ``` --model Qwen/Qwen3.5-35...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: CUDA illegal memory access on GPTQ Marlin bug ### Your current environment ### 🐛 Describe the bug Similar to https://github.com/vllm-project/vllm/issues/32834 but observed when running a GPTQ Marlin quantized mod...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: soning-parser qwen3 --default-chat-template-kwargs {"enable_thinking": false} --max-cudagraph-capture-size 32 --gpu-memory-utilization 0.8 ``` ### Environment Variables ``` VLLM_LOGGING_LEVEL=DEBUG CUDA_LAUNCH_BLOCKING=...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ject/vllm/issues/32834 but observed when running a GPTQ Marlin quantized model. Image used: `vllm/vllm-openai:nightly-76c6e6da08dbe73c2ee0d92dabe01786b44845d2`. ### Server Arguments ``` --model Qwen/Qwen3.5-35B-A3B-GPTQ...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36889](https://github.com/vllm-project/vllm/pull/36889) | closes_keyword | 0.95 | [WIP][Bugfix] Fix CUDA illegal memory access for GPTQ Marlin MoE with CUDA graphs | Close #36811 Fix CUDA illegal memory access when running GPTQ Marlin quantized MoE models (e.g., Qwen/Qwen3.5-35B-A3B-GPTQ-Int4) with CUDA graphs enabled. ### Root Cause: `c_ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
