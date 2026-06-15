# vllm-project/vllm#3564: [Usage]: Unable to get the vllm fastapi up and running in GPU enabled container in kube cluster

| 字段 | 值 |
| --- | --- |
| Issue | [#3564](https://github.com/vllm-project/vllm/issues/3564) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel;operator |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Unable to get the vllm fastapi up and running in GPU enabled container in kube cluster

### Issue 正文摘录

### Your current environment **OS:** Ubuntu: 20.04 **GPU:** NVIDIA L40S-48C **Driver Version:** 535.154.05 **CUDA Version:** 12.2 **Kubernetes node info:** Name: auto-int-k8w02 Roles: Labels: beta.kubernetes.io/arch=amd64 beta.kubernetes.io/os=linux dedicated=distilgpt2-fastapi feature.node.kubernetes.io/cpu-cpuid.ADX=true feature.node.kubernetes.io/cpu-cpuid.AESNI=true feature.node.kubernetes.io/cpu-cpuid.AMXBF16=true feature.node.kubernetes.io/cpu-cpuid.AMXINT8=true feature.node.kubernetes.io/cpu-cpuid.AMXTILE=true feature.node.kubernetes.io/cpu-cpuid.AVX=true feature.node.kubernetes.io/cpu-cpuid.AVX2=true feature.node.kubernetes.io/cpu-cpuid.AVX512BF16=true feature.node.kubernetes.io/cpu-cpuid.AVX512BITALG=true feature.node.kubernetes.io/cpu-cpuid.AVX512BW=true feature.node.kubernetes.io/cpu-cpuid.AVX512CD=true feature.node.kubernetes.io/cpu-cpuid.AVX512DQ=true feature.node.kubernetes.io/cpu-cpuid.AVX512F=true feature.node.kubernetes.io/cpu-cpuid.AVX512FP16=true feature.node.kubernetes.io/cpu-cpuid.AVX512IFMA=true feature.node.kubernetes.io/cpu-cpuid.AVX512VBMI=true feature.node.kubernetes.io/cpu-cpuid.AVX512VBMI2=true feature.node.kubernetes.io/cpu-cpuid.AVX512VL=true feature....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ent environment **OS:** Ubuntu: 20.04 **GPU:** NVIDIA L40S-48C **Driver Version:** 535.154.05 **CUDA Version:** 12.2 **Kubernetes node info:** Name: auto-int-k8w02 Roles: Labels: beta.kubernetes.io/arch=amd64 beta.kuber...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: untu: 20.04 **GPU:** NVIDIA L40S-48C **Driver Version:** 535.154.05 **CUDA Version:** 12.2 **Kubernetes node info:** Name: auto-int-k8w02 Roles: Labels: beta.kubernetes.io/arch=amd64 beta.kubernetes.io/os=linux
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: RED_CTRL=true feature.node.kubernetes.io/cpu-cpuid.LAHF=true feature.node.kubernetes.io/cpu-cpuid.MD_CLEAR=true feature.node.kubernetes.io/cpu-cpuid.MOVBE=true feature.node.kubernetes.io/cpu-cpuid.MOVDIR64B=true
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: d.AESNI=true feature.node.kubernetes.io/cpu-cpuid.AMXBF16=true feature.node.kubernetes.io/cpu-cpuid.AMXINT8=true feature.node.kubernetes.io/cpu-cpuid.AMXTILE=true feature.node.kubernetes.io/cpu-cpuid.AVX=true
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: feature.node.kubernetes.io/cpu-hardware_multithreading=false feature.node.kubernetes.io/cpu-model.family=6 feature.node.kubernetes.io/cpu-model.id=143 feature.node.kubernetes.io/cpu-model.vendor_id=Intel

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
