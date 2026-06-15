# vllm-project/vllm#28553: [Bug][ROCm] gpt-oss TypeError: cannot assign 'triton_kernels.tensor.Tensor' as parameter 'w13_weight' (torch.nn.Parameter or None expected)

| 字段 | 值 |
| --- | --- |
| Issue | [#28553](https://github.com/vllm-project/vllm/issues/28553) |
| 状态 | closed |
| 标签 | bug;rocm;gpt-oss |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][ROCm] gpt-oss TypeError: cannot assign 'triton_kernels.tensor.Tensor' as parameter 'w13_weight' (torch.nn.Parameter or None expected)

### Issue 正文摘录

### Your current environment I am using Triton + triton_kernels from https://github.com/vllm-project/vllm/blob/edb59a9470f5c67ef11d52e7bb25fb8ea17f120f/docker/Dockerfile.rocm_base#L2-L3 (i.e. https://github.com/ROCm/triton/tree/57c693b627fe058878ade4163a0a8df95d9fefa1), although I wish I could use upstream `pytorch-triton-rocm==3.5.0` from https://download.pytorch.org/whl/rocm6.4. I am using torch from `pip3 install torch torchvision --index-url https://download.pytorch.org/whl/rocm6.4`. ### 🐛 Describe the bug Hi, Running vllm @ 1761dea1a8567fc143b7bfbe61cb1e00cc081c7f & unning on CDNA3 GPU: ```bash vllm serve openai/gpt-oss-20b --tensor-parallel-size 1 --enforce-eager ``` you'd get: ``` (EngineCore_DP0 pid=54260) Process EngineCore_DP0: (EngineCore_DP0 pid=54260) Traceback (most recent call last): (EngineCore_DP0 pid=54260) File "/root/miniforge3/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP0 pid=54260) self.run() (EngineCore_DP0 pid=54260) File "/root/miniforge3/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_DP0 pid=54260) self._target(*self._args, **self._kwargs) (EngineCore_DP0 pid=54260) File "/shared_volume/repos...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: thub.com/vllm-project/vllm/blob/edb59a9470f5c67ef11d52e7bb25fb8ea17f120f/docker/Dockerfile.rocm_base#L2-L3 (i.e. https://github.com/ROCm/triton/tree/57c693b627fe058878ade4163a0a8df95d9fefa1), although I wish I could use...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ad_model (EngineCore_DP0 pid=54260) self.model_runner.load_model(eep_scale_up=eep_scale_up) (EngineCore_DP0 pid=54260) File "/shared_volume/repos/vllm/vllm/v1/worker/gpu_model_runner.py", line 3064, in load_model (Engin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug][ROCm] gpt-oss TypeError: cannot assign 'triton_kernels.tensor.Tensor' as parameter 'w13_weight' (torch.nn.Parameter or None expected) bug;rocm;gpt-oss ### Your current environment I am using Triton + triton_kernel...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug][ROCm] gpt-oss TypeError: cannot assign 'triton_kernels.tensor.Tensor' as parameter 'w13_weight' (torch.nn.Parameter or None expected) bug;rocm;gpt-oss ### Your current environment I am using Triton + triton_kernel...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug][ROCm] gpt-oss TypeError: cannot assign 'triton_kernels.tensor.Tensor' as parameter 'w13_weight' (torch.nn.Parameter or None expected) bug;rocm;gpt-oss ### Your current environment I am using Triton + triton_kernel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
