# vllm-project/vllm#33099: [Bug]: vllm Requests stuck indefinitely

| 字段 | 值 |
| --- | --- |
| Issue | [#33099](https://github.com/vllm-project/vllm/issues/33099) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm Requests stuck indefinitely

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug System: GPUs: 2x NVIDIA L40S vllm version: 0.14.0 CUDA version: 12.8 Driver: 570.195.03 Python version: 3.10.12 OS: Ubuntu 22.04.05 LTS Model: unsloth/Mistral-Small-3.2-24B-Instruct-2506-FP8 vllm running via serivce: [Unit] Description=vLLM Mistral Small 3.2 Service After=network.target [Service] Type=simple User=REDACTED Group=REDACTED WorkingDirectory=/REDACTED/vllm Environment="HOME=/REDACTED/vllm" Environment="CUDA_VISIBLE_DEVICES=0,1" Environment="HF_HOME=/REDACTED/vllm/.cache/huggingface" Environment="TRANSFORMERS_CACHE=/REDACTED/vllm/.cache/huggingface/transformers" Environment="TORCH_HOME=/REDACTED/vllm/.cache/torch" Environment="XDG_CACHE_HOME=/REDACTED/vllm/.cache" Environment="XDG_CONFIG_HOME=/REDACTED/vllm/.config" Environment="XDG_STATE_HOME=/REDACTED/vllm/.state" Environment="VLLM_LOGGING_LEVEL=DEBUG" ExecStart=/bin/bash -c '\ . /REDACTED/vllm-venv/bin/activate && \ vllm serve unsloth/Mistral-Small-3.2-24B-Instruct-2506-FP8 \ --host 0.0.0.0 \ --port 8000 \ --api-key sk-REDACTED \ --tensor-parallel-size 2 \ --max-model-len 100000 \ --max-num-seqs 8 \ --max-num-batched-tokens 16384 \ --gpu-memory-utilization 0.80 \ --...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: 12.8 Driver: 570.195.03 Python version: 3.10.12 OS: Ubuntu 22.04.05 LTS Model: unsloth/Mistral-Small-3.2-24B-Instruct-2506-FP8 vllm running via serivce: [Unit] Description=vLLM Mistral Small 3.2 Service After=network.ta...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: vironment ### 🐛 Describe the bug System: GPUs: 2x NVIDIA L40S vllm version: 0.14.0 CUDA version: 12.8 Driver: 570.195.03 Python version: 3.10.12 OS: Ubuntu 22.04.05 LTS Model: unsloth/Mistral-Small-3.2-24B-Instruct-2506...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: : Ubuntu 22.04.05 LTS Model: unsloth/Mistral-Small-3.2-24B-Instruct-2506-FP8 vllm running via serivce: [Unit] Description=vLLM Mistral Small 3.2 Service After=network.target [Service] Type=simple User=REDACTED Group=RED...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: # 🐛 Describe the bug System: GPUs: 2x NVIDIA L40S vllm version: 0.14.0 CUDA version: 12.8 Driver: 570.195.03 Python version: 3.10.12 OS: Ubuntu 22.04.05 LTS Model: unsloth/Mistral-Small-3.2-24B-Instruct-2506-FP8 vllm ru...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm Requests stuck indefinitely bug ### Your current environment ### 🐛 Describe the bug System: GPUs: 2x NVIDIA L40S vllm version: 0.14.0 CUDA version: 12.8 Driver: 570.195.03 Python version: 3.10.12 OS: Ubuntu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
