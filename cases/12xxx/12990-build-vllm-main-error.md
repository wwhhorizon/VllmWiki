# vllm-project/vllm#12990: build vllm main error

| 字段 | 值 |
| --- | --- |
| Issue | [#12990](https://github.com/vllm-project/vllm/issues/12990) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;quantization |
| 子分类 | install |
| Operator 关键词 | quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> build vllm main error

### Issue 正文摘录

### Your current environment Ubuntu 20.04.6 LTS GNU GCC 12.4.0 Python 3.12.9 cmake 3.31.4 vllm main Intel(R) Xeon(R) Platinum 8360H No GPU ### How you are installing vllm Build from source * pip install cmake>=3.26 wheel packaging ninja "setuptools-scm>=8" numpy * pip install -v -r requirements-cpu.txt --extra-index-url https://download.pytorch.org/whl/cpu * VLLM_TARGET_DEVICE=cpu python setup.py install kineto Currently only NVIDIA GPUs are supported. Compile log as follows ``` ....... copying vllm/model_executor/layers/quantization/utils/configs/N=7168,K=2048,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128,128].json -> build/lib.linux-x86_64-cpython-312/vllm/model_executor/layers/quantization/utils/configs copying vllm/model_executor/layers/quantization/utils/configs/N=2304,K=7168,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128,128].json -> build/lib.linux-x86_64-cpython-312/vllm/model_executor/layers/quantization/utils/configs running build_ext -- The CXX compiler identification is GNU 12.4.0 -- Detecting CXX compiler ABI info -- Detecting CXX compiler ABI info - done -- Check for working CXX compiler: /usr/local/gcc-12.4.0/bin/c++ - skipped...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: build vllm main error installation ### Your current environment Ubuntu 20.04.6 LTS GNU GCC 12.4.0 Python 3.12.9 cmake 3.31.4 vllm main Intel(R) Xeon(R) Platinum 8360H No GPU ### How you are installing vllm Build from
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: d. Compile log as follows ``` ....... copying vllm/model_executor/layers/quantization/utils/configs/N=7168,K=2048,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128,128].json -> build/lib.linux-x86_64-cpy...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cutor/layers/quantization/utils/configs/N=7168,K=2048,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128,128].json -> build/lib.linux-x86_64-cpython-312/vllm/model_executor/layers/quantization/utils/confi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: IDIA GPUs are supported. Compile log as follows ``` ....... copying vllm/model_executor/layers/quantization/utils/configs/N=7168,K=2048,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128,128].json -> buil...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s/configs/N=7168,K=2048,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128,128].json -> build/lib.linux-x86_64-cpython-312/vllm/model_executor/layers/quantization/utils/configs copying vllm/model_executor...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
