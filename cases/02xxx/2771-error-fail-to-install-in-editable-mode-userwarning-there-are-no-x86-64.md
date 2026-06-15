# vllm-project/vllm#2771: ERROR: Fail to install in editable mode. "UserWarning: There are no .../x86_64-conda-linux-gnu-c++ version bounds defined for CUDA version 12.1"

| 字段 | 值 |
| --- | --- |
| Issue | [#2771](https://github.com/vllm-project/vllm/issues/2771) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> ERROR: Fail to install in editable mode. "UserWarning: There are no .../x86_64-conda-linux-gnu-c++ version bounds defined for CUDA version 12.1"

### Issue 正文摘录

I am unable to install vllm in editable mode using `pip install -e .` Please advise. I have attached the error log along with environment details. Here's the error log: ``` Building wheels for collected packages: vllm Building editable for vllm (pyproject.toml) ... error error: subprocess-exited-with-error × Building editable for vllm (pyproject.toml) did not run successfully. │ exit code: 1 ╰─> [330 lines of output] /scratch/270889/pip-build-env-uduxn033/overlay/lib/python3.9/site-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at ../torch/csrc/utils/tensor_numpy.cpp:84.) device: torch.device = torch.device(torch._C._get_default_device()), # torch.device('cpu'), running editable_wheel creating /scratch/270889/pip-wheel-t8xj16th/.tmp-47xs7i65/vllm.egg-info writing /scratch/270889/pip-wheel-t8xj16th/.tmp-47xs7i65/vllm.egg-info/PKG-INFO writing dependency_links to /scratch/270889/pip-wheel-t8xj16th/.tmp-47xs7i65/vllm.egg-info/dependency_links.txt writing requirements to /scratch/270889/pip-wheel-t8xj16th/.tmp-47xs7i65/vllm.egg-info/requires.txt writing top-level names to /scratch/270889/pip-wheel-t8x...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: ERROR: Fail to install in editable mode. "UserWarning: There are no .../x86_64-conda-linux-gnu-c++ version bounds defined for CUDA version 12.1" I am unable to install vllm in editable mode using `pip install -e .` Plea...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' -O2 ``` Other information: ``` nvcc --version nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2023 NVIDIA Corporation Built on Mon_Apr__3_17:16:06_PDT_2023...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: src/attention creating /scratch/270889/tmpztz3hxtz.build-temp/csrc/quantization creating /scratch/270889/tmpztz3hxtz.build-temp/csrc/quantization/awq creating /scratch/270889/tmpztz3hxtz.build-temp/csrc/quantization/gpt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: : There are no .../x86_64-conda-linux-gnu-c++ version bounds defined for CUDA version 12.1" I am unable to install vllm in editable mode using `pip install -e .` Please advise. I have attached the error log along with e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 0.16.2 tqdm 4.66.1 transformers 4.37.2 triton 2.0.0 typing_extensions 4.9.0 urllib3 2.2.0 uvicorn 0.27.0.post1 uvloop 0.19.0 vllm 0.3.0 watchfiles

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
