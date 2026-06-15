# vllm-project/vllm#20639: [Installation]: rocm pip install -e . AssertionError: CUDA_HOME is not set

| 字段 | 值 |
| --- | --- |
| Issue | [#20639](https://github.com/vllm-project/vllm/issues/20639) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: rocm pip install -e . AssertionError: CUDA_HOME is not set

### Issue 正文摘录

### Your current environment This thread is linked with closed similar problem: https://github.com/vllm-project/vllm/issues/17445 I have same issue, but my persists. And I think that I have found cause of the problem. So during installation from sources on Ubuntu 24.04.2 LTS (Noble Numbat) and ROCm 6.4.1 (2 x Radeon 7900 XT) the message is shown: ``` /tmp/pip-build-env-hozjdhze/overlay/lib/python3.12/site-packages/torch/_subclasses/functional_tensor.py:276: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:81.) cpu = _conversion_method_template(device=torch.device("cpu")) No ROCm runtime is found, using ROCM_HOME='/opt/rocm-6.4.1' None 12.6 Traceback (most recent call last): File "/home/ai_server/.local/share/mamba/envs/vllm_env/lib/python3.12/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 389, in main() File "/home/ai_server/.local/share/mamba/envs/vllm_env/lib/python3.12/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 373, in main json_out["return_val"] = hook(**hook_input["kwargs"]) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/ai_server/.local/...

## 现有链接修复摘要

#38337 [ROCm][Build] Fix pip install detection when build isolation installs CUDA PyTorch

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: [Installation]: rocm pip install -e . AssertionError: CUDA_HOME is not set installation;stale ### Your current environment This thread is linked with closed similar problem: https://github.com/vllm-project/vllm/issues/17
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Installation]: rocm pip install -e . AssertionError: CUDA_HOME is not set installation;stale ### Your current environment This thread is linked with closed similar problem: https://github.com/vllm-project/vllm/issues/1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: .py", line 157, in get_requires_for_build_editable return hook(config_settings) ^^^^^^^^^^^^^^^^^^^^^ File "/tmp/pip-build-env-hozjdhze/overlay/lib/python3.12/site-packages/setuptools/build_meta.py", line 473, in get_re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: rocm pip install -e . AssertionError: CUDA_HOME is not set installation;stale ### Your current environment This thread is linked with closed similar problem: https://github.com/vllm-project/vllm/issues/17445 I have same...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: aries ============================== [pip3] numpy==1.26.4 [pip3] pytorch-triton-rocm==3.2.0+rocm6.4.1.git6da9e660 [pip3] pyzmq==27.0.0 [pip3] torch==2.6.0+rocm6.4.1.git1ded221d [pip3] torchaudio==2.6.0+rocm6.4.1.gitd883...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38337](https://github.com/vllm-project/vllm/pull/38337) | closes_keyword | 0.95 | [ROCm][Build] Fix pip install detection when build isolation installs CUDA PyTorch | Fixes #20639 ## Test plan - [ ] `pip install -e .` on a ROCm system without ROCm PyTorch — should detect ROCm via ROCM_HOME fallback - [ ] `pip install -e .` on a ROCm system with |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
