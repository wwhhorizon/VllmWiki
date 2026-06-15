# vllm-project/vllm#37847: [Installation]: Documented v0.18.0 cu128 release wheel URL returns 404

| 字段 | 值 |
| --- | --- |
| Issue | [#37847](https://github.com/vllm-project/vllm/issues/37847) |
| 状态 | open |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Documented v0.18.0 cu128 release wheel URL returns 404

### Issue 正文摘录

### Your current environment I followed the official v0.18.0 GPU installation docs for pre-built wheels. The docs say that vLLM provides binaries compiled with CUDA 12.8 / 12.9 / 13.0, and give the following URL pattern for release wheels: vllm-${VLLM_VERSION}+cu${CUDA_VERSION}-cp38-abi3-manylinux_2_35_${CPU_ARCH}.whl For v0.18.0 on x86_64 with CUDA 12.8, this resolves to: https://github.com/vllm-project/vllm/releases/download/v0.18.0/vllm-0.18.0+cu128-cp38-abi3-manylinux_2_35_x86_64.whl However, this URL returns HTTP 404. ### Command used ```bash uv pip install \ "https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cu128-cp38-abi3-manylinux_2_35_${CPU_ARCH}.whl" \ --extra-index-url https://download.pytorch.org/whl/cu128 ### How you are installing vllm uv pip install \ > "https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cu128-cp38-abi3-manylinux_2_35_${CPU_ARCH}.whl" \ > --extra-index-url https://download.pytorch.org/whl/cu128 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: Documented v0.18.0 cu128 release wheel URL returns 404 installation ### Your current environment I followed the official v0.18.0 GPU installation docs for pre-built wheels. The docs say that vLLM provide
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: re-built wheels. The docs say that vLLM provides binaries compiled with CUDA 12.8 / 12.9 / 13.0, and give the following URL pattern for release wheels: vllm-${VLLM_VERSION}+cu${CUDA_VERSION}-cp38-abi3-manylinux_2_35_${C...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
