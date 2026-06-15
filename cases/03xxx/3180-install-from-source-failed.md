# vllm-project/vllm#3180: install from source failed

| 字段 | 值 |
| --- | --- |
| Issue | [#3180](https://github.com/vllm-project/vllm/issues/3180) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;moe;quantization |
| 子分类 | install |
| Operator 关键词 | attention;cuda;moe;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> install from source failed

### Issue 正文摘录

I encountered a problem when trying to compile vllm using 'pip install -e .', but I succeeded using 'pip install vllm' Here is my env configuration steps ``` conda create --name vllm python=3.9 git clone https://github.com/vllm-project/vllm.git cd vllm pip install -r requirements.txt pip install -e . ``` Env: cuda 12.1 python 3.9.18 numpy 1.26.4 ninja 1.11.1.1 Error: ``` Building editable for vllm (pyproject.toml) ... error error: subprocess-exited-with-error × Building editable for vllm (pyproject.toml) did not run successfully. │ exit code: 1 ╰─> [221 lines of output] /tmp/pip-build-env-dy69uemu/overlay/lib/python3.9/site-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at ../torch/csrc/utils/tensor_numpy.cpp:84.) device: torch.device = torch.device(torch._C._get_default_device()), # torch.device('cpu'), running editable_wheel creating /tmp/pip-wheel-nzc13jkb/.tmp-o_cwr7m0/vllm.egg-info writing /tmp/pip-wheel-nzc13jkb/.tmp-o_cwr7m0/vllm.egg-info/PKG-INFO writing dependency_links to /tmp/pip-wheel-nzc13jkb/.tmp-o_cwr7m0/vllm.egg-info/dependency_links.txt writing requirements to /tmp/pip-wheel-nzc13...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: install from source failed I encountered a problem when trying to compile vllm using 'pip install -e .', but I succeeded using 'pip install vllm' Here is my env configuration steps ``` conda create --name vllm python=3.
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: USE_CXX11_ABI=0 -gencode arch=compute_75,code=sm_75 --threads 8 -DENABLE_FP8_E5M2 -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relax...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: m.git cd vllm pip install -r requirements.txt pip install -e . ``` Env: cuda 12.1 python 3.9.18 numpy 1.26.4 ninja 1.11.1.1 Error: ``` Building editable for vllm (pyproject.toml) ... error error: subprocess-exited-with-...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: s/vllm/include/python3.9 -c -c /home/jasonj/code/llm/vllm/csrc/moe_align_block_size_kernels.cu -o /tmp/tmpucwtn8_8.build-temp/csrc/moe_align_block_size_kernels.o --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: unds defined for CUDA version {cuda_str_version}') building 'vllm._moe_C' extension creating /tmp/tmpucwtn8_8.build-temp/csrc creating /tmp/tmpucwtn8_8.build-temp/csrc/moe Emitting ninja build file /tmp/tmpucwtn8_8.buil...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
