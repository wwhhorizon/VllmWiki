# vllm-project/vllm#26791: [Bug]: NVIDIA Thor with CUDA capability sm_110 is not compatible

| 字段 | 值 |
| --- | --- |
| Issue | [#26791](https://github.com/vllm-project/vllm/issues/26791) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NVIDIA Thor with CUDA capability sm_110 is not compatible

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash # run script vllm serve --config /home/xxx/proj/infer/vllm_config/holo-1.5-7b.yaml # core log ... (EngineCore_DP0 pid=107532) /home/xxx/miniconda3/envs/llm/lib/python3.12/site-packages/torch/cuda/__init__.py:327: UserWarning: (EngineCore_DP0 pid=107532) NVIDIA Thor with CUDA capability sm_110 is not compatible with the current PyTorch installation. (EngineCore_DP0 pid=107532) The current PyTorch install supports CUDA capabilities sm_80 sm_90 sm_100 sm_120. ... (EngineCore_DP0 pid=107532) ERROR 10-14 17:07:18 [core.py:790] File "/home/xxx/miniconda3/envs/llm/lib/python3.12/site-packages/vllm/platforms/cuda.py", line 85, in set_device (EngineCore_DP0 pid=107532) ERROR 10-14 17:07:18 [core.py:790] _ = torch.zeros(1, device=device) (EngineCore_DP0 pid=107532) ERROR 10-14 17:07:18 [core.py:790] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=107532) ERROR 10-14 17:07:18 [core.py:790] torch.AcceleratorError: CUDA error: no kernel image is available for execution on the device ... ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: r with CUDA capability sm_110 is not compatible with the current PyTorch installation. (EngineCore_DP0 pid=107532) The current PyTorch install supports CUDA capabilities sm_80 sm_90 sm_100 sm_120. ... (EngineCore_DP0 pi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: NVIDIA Thor with CUDA capability sm_110 is not compatible bug ### Your current environment ### 🐛 Describe the bug ```bash # run script vllm serve --config /home/xxx/proj/infer/vllm_config/holo-1.5-7b.yaml # core...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;crash;mismatch;na...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ronment ### 🐛 Describe the bug ```bash # run script vllm serve --config /home/xxx/proj/infer/vllm_config/holo-1.5-7b.yaml # core log ... (EngineCore_DP0 pid=107532) /home/xxx/miniconda3/envs/llm/lib/python3.12/site-pack...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;crash;mismatch;nan_inf dtype;env_dependency Yo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
