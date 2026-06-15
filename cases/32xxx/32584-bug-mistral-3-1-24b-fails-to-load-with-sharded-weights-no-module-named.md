# vllm-project/vllm#32584: [Bug]: Mistral 3.1 24B fails to load with sharded weights - "no module named 'language_model' in LlamaForCausalLM" error

| 字段 | 值 |
| --- | --- |
| Issue | [#32584](https://github.com/vllm-project/vllm/issues/32584) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral 3.1 24B fails to load with sharded weights - "no module named 'language_model' in LlamaForCausalLM" error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When loading Mistral 3.1 24B Instruct model with sharded safetensors (no consolidated.safetensors), vLLM fails with `ValueError: There is no module or parameter named 'language_model' in LlamaForCausalLM`. The model has correct `config.json` with `"architectures": ["Mistral3ForConditionalGeneration"]` and `"model_type": "mistral3"`, and weights have the correct `language_model.model.layers.*` prefix structure. The error occurs in `pixtral.py:583` where it calls `self.language_model.load_weights()`, but then the weight loader treats it as `LlamaForCausalLM` which doesn't have the `language_model` submodule. But the model successfully loads when `consolidated.safetensors` is present. ### Regression This is a regression from `vLLM 0.11.0`. In the previous `vLLM 0.11.0` sharded weights loaded successfully by default even when `consolidated.safetensors` was present, without requiring `--load-format` or `--config-format` flags. But from `0.12.0+` model loading only works when `consolidated.safetensors` is present. ### Steps to Reproduce Get the vLLM `0.12.0` or `0.13.0` package using pip and initialize the vLLM inference engine with Mi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: 3.1 24B fails to load with sharded weights - "no module named 'language_model' in LlamaForCausalLM" error bug ### Your current environment ### 🐛 Describe the bug When loading Mistral 3.1 24B Instruct model with sharded...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: .12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: worker.py", line 273, in load_model self.model_runner.load_model(eep_scale_up=eep_scale_up) File "/opt/dynamo/venv/lib/python3.12/site-packages/vllm/v1/worker/gpu_model_runner.py", line 3484, in load_model self.model =...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: _model' in LlamaForCausalLM`. The model has correct `config.json` with `"architectures": ["Mistral3ForConditionalGeneration"]` and `"model_type": "mistral3"`, and weights have the correct `language_model.model.layers.*`...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: odel successfully loads when `consolidated.safetensors` is present. ### Regression This is a regression from `vLLM 0.11.0`. In the previous `vLLM 0.11.0` sharded weights loaded successfully by default even when `consoli...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
