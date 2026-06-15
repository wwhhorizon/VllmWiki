# vllm-project/vllm#6118: [Installation]:       ImportError: undefined symbol: __nvJitLinkAddData_12_1, version libnvJitLink.so.12

| 字段 | 值 |
| --- | --- |
| Issue | [#6118](https://github.com/vllm-project/vllm/issues/6118) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]:       ImportError: undefined symbol: __nvJitLinkAddData_12_1, version libnvJitLink.so.12

### Issue 正文摘录

### Your current environment ``` Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: CentOS Stream 9 (x86_64) GCC version: (GCC) 11.4.1 20231218 (Red Hat 11.4.1-3) Clang version: 17.0.6 (CentOS 17.0.6-5.el9) CMake version: version 3.26.5 Libc version: glibc-2.34 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.12.0-0_fbk16_zion_7661_geb00762ce6d2-x86_64-with-glibc2.34 Is CUDA available: False CUDA runtime version: 12.0.140 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA PG509-210 GPU 1: NVIDIA PG509-210 GPU 2: NVIDIA PG509-210 GPU 3: NVIDIA PG509-210 GPU 4: NVIDIA PG509-210 GPU 5: NVIDIA PG509-210 GPU 6: NVIDIA PG509-210 GPU 7: NVIDIA PG509-210 Nvidia driver version: 525.105.17 cuDNN version: Probably one of the following: /usr/lib64/libcudnn.so.8.8.0 /usr/lib64/libcudnn_adv_infer.so.8.8.0 /usr/lib64/libcudnn_adv_train.so.8.8.0 /usr/lib64/libcudnn_cnn_infer.so.8.8.0 /usr/lib64/libcudnn_cnn_train.so.8.8.0 /usr/lib64/libcudnn_ops_infer.so.8.8.0 /usr/lib64/libcudnn_ops_train.so.8.8.0 HIP...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: [Installation]: ImportError: undefined symbol: __nvJitLinkAddData_12_1, version libnvJitLink.so.12 installation ### Your current environment ``` Collecting environment information... PyTorch version: 2.3.0 Is debug
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: CentOS Stream 9 (x86_64) GCC version: (GCC) 11.4.1 20231218 (Red...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: installation ### Your current environment ``` Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: CentOS S...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req pku ospke avx512_vnni md_clear flush_l1d arch_capabilities Virtualization: VT-x...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: CentOS Stream 9 (x86_64) GCC version: (GCC) 11.4.1 20231218...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
