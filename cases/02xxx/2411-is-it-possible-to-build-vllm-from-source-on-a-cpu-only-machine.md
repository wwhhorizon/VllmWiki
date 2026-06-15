# vllm-project/vllm#2411: Is it possible to build vllm from source on a CPU only machine?

| 字段 | 值 |
| --- | --- |
| Issue | [#2411](https://github.com/vllm-project/vllm/issues/2411) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;quantization |
| 子分类 | install |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> Is it possible to build vllm from source on a CPU only machine?

### Issue 正文摘录

My dockerfile look like ``` FROM nvcr.io/nvidia/pytorch:23.07-py3 RUN git clone https://github.com/vllm-project/vllm RUN cd vllm && git checkout v0.2.7 RUN cd vllm && pip install -e . ``` And I got error as below when I run the docker in a machine without GPU. Is it possible to build vllm from a machine without GPU and then run the docker image in a machine with GPU? ``` #4 401.4 × Building editable for vllm (pyproject.toml) did not run successfully. #4 401.4 │ exit code: 1 #4 401.4 ╰─> [422 lines of output] #4 401.4 /tmp/pip-build-env-zucywvvn/overlay/local/lib/python3.10/dist-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at ../torch/csrc/utils/tensor_numpy.cpp:84.) #4 401.4 device: torch.device = torch.device(torch._C._get_default_device()), # torch.device('cpu'), #4 401.4 No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda' #4 401.4 :142: UserWarning: Unsupported CUDA/ROCM architectures ({'6.0', '6.1', '5.2'}) are excluded from the `TORCH_CUDA_ARCH_LIST` env variable (5.2 6.0 6.1 7.0 7.5 8.0 8.6 9.0+PTX). Supported CUDA/ROCM architectures are: {'7.0', '9.0', '7.5', '8.6', '7.0+PTX', '7....

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: Is it possible to build vllm from source on a CPU only machine? My dockerfile look like ``` FROM nvcr.io/nvidia/pytorch:23.07-py3 RUN git clone https://github.com/vllm-project/vllm RUN cd vllm && git checkout v0.2.7 RUN...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: rch._C._get_default_device()), # torch.device('cpu'), #4 401.4 No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda' #4 401.4 :142: UserWarning: Unsupported CUDA/ROCM architectures ({'6.0', '6.1', '5.2'}) are excl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: /csrc/attention #4 401.4 creating /tmp/tmp9jpwzd7u.build-temp/csrc/quantization #4 401.4 creating /tmp/tmp9jpwzd7u.build-temp/csrc/quantization/awq #4 401.4 creating /tmp/tmp9jpwzd7u.build-temp/csrc/quantization/gptq #4...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: antization attention;cuda;quantization build_error env_dependency #4 Use FlashAttention for `multi_query_kv_attention` My dockerfile look like
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 9jpwzd7u.build-temp/csrc/quantization/squeezellm/quant_cuda_kernel.o #4 401.4 /usr/local/cuda/bin/nvcc -i/tmp/pip-build-env-zucywvvn/overlay/local/lib/python3.10/dist-package |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
