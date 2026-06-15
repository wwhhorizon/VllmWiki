# vllm-project/vllm#2493: Trying to build with AMD Radeon 780M GPU -> Cannot find CUDA_HOME. CUDA must be available to build the package.

| 字段 | 值 |
| --- | --- |
| Issue | [#2493](https://github.com/vllm-project/vllm/issues/2493) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;moe |
| 子分类 | install |
| Operator 关键词 | cuda;moe |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Trying to build with AMD Radeon 780M GPU -> Cannot find CUDA_HOME. CUDA must be available to build the package.

### Issue 正文摘录

Hello! I am trying to build vLLM on my Debian System (AMD Ryzen 7 7840HS / Radeon 780M). With "pip install -e ." I get: [...] error: subprocess-exited-with-error × Getting requirements to build editable did not run successfully. │ exit code: 1 ╰─> [19 lines of output] /tmp/pip-build-env-g6hyzj6x/overlay/lib/python3.9/site-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at ../torch/csrc/utils/tensor_numpy.cpp:84.) device: torch.device = torch.device(torch._C._get_default_device()), # torch.device('cpu'), Traceback (most recent call last): File "/home/stephan/miniconda3/envs/python-3_9-env/lib/python3.9/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in main() File "/home/stephan/miniconda3/envs/python-3_9-env/lib/python3.9/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main json_out['return_val'] = hook(**hook_input['kwargs']) File "/home/stephan/miniconda3/envs/python-3_9-env/lib/python3.9/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 132, in get_requires_for_build_editable return hook(config_setting...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Trying to build with AMD Radeon 780M GPU -> Cannot find CUDA_HOME. CUDA must be available to build the package. Hello! I am trying to build vLLM on my Debian System (AMD Ryzen 7 7840HS / Radeon 780M). With "pip install...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ilable to build the package. [end of output] [...] I am not a big expert for GPUs and the CUDA framework, but from what I understand so far CUDA is for Nvidia!? So is the AMD Radeon 780M GPU not supported? How to get it...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Trying to build with AMD Radeon 780M GPU -> Cannot find CUDA_HOME. CUDA must be available to build the package. Hello! I am trying to build vLLM on my Debian System (AMD Ryzen 7 7840HS / Radeon 780M). With "pip install...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .py", line 132, in get_requires_for_build_editable return hook(config_settings) File "/tmp/pip-build-env-g6hyzj6x/overlay/lib/python3.9/site-packages/setuptools/build_meta.py", line 441, in get_requires_for_build_editab...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
