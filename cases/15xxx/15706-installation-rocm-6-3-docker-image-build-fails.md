# vllm-project/vllm#15706: [Installation]: ROCm 6.3 docker image build fails

| 字段 | 值 |
| --- | --- |
| Issue | [#15706](https://github.com/vllm-project/vllm/issues/15706) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: ROCm 6.3 docker image build fails

### Issue 正文摘录

### Your current environment ```sh python collect_env.py ``` ```text Traceback (most recent call last): File "/home/marc/project/vllm/collect_env.py", line 17, in from vllm.envs import environment_variables File "/home/marc/project/vllm/vllm/__init__.py", line 9, in import torch ModuleNotFoundError: No module named 'torch' ``` Not really applicable, I am trying to build a docker image specifically because building from source does not work. ```sh rocminfo ``` ```text ROCk module version 6.10.5 is loaded ===================== HSA System Attributes ===================== Runtime Version: 1.14 Runtime Ext Version: 1.6 System Timestamp Freq.: 1000.000000MHz Sig. Max Wait Duration: 18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count) Machine Model: LARGE System Endianness: LITTLE Mwaitx: DISABLED DMAbuf Support: YES ========== HSA Agents ========== ******* Agent 1 ******* Name: AMD Ryzen 7 5800X3D 8-Core Processor Uuid: CPU-XX Marketing Name: AMD Ryzen 7 5800X3D 8-Core Processor Vendor Name: CPU Feature: None specified Profile: FULL_PROFILE Float Round Mode: NEAR Max Queue Number: 0(0x0) Queue Min Size: 0(0x0) Queue Max Size: 0(0x0) Queue Type: MULTI Node: 0 Device Type: CPU Cach...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: ROCm 6.3 docker image build fails installation ### Your current environment ```sh python collect_env.py ``` ```text Traceback (most recent call last): File "/home/marc/project/vllm/collect_env.py", lin
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: on: 18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count) Machine Model: LARGE System Endianness: LITTLE Mwaitx: DISABLED DMAbuf Support: YES ========== HSA Agents
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Installation]: ROCm 6.3 docker image build fails installation ### Your current environment ```sh python collect_env.py ``` ```text Traceback (most recent call last): File "/home/marc/project/vllm/collect_env.py", line...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: Ranges:4 Coherent Host Access: FALSE Memory Properties: Features: KERNEL_DISPATCH Fast F16 Operation: TRUE Wavefront Size: 32(0x20)
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ---------------------- N=8192,K=1536,device_name=AMD_Instinct_MI325_OAM,dtype=fp8_w8a8,block_shape=[128,128].json -> build/lib.linux-x86_64-cpython-312/vllm/model_executor/layers/quantization/utils/configs 42.86 running...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
